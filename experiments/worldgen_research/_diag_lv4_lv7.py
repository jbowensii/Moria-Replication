import json
def load(p): return json.load(open(p, encoding='utf-8'))
def fp(v,n):
    for p in v or []:
        if isinstance(p,dict) and p.get('Name')==n: return p
    return None
def get(r,k):
    p = fp(r['Value'], k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v,list):
        for it in v:
            if isinstance(it,dict) and it.get('Name')=='RowName':
                return it.get('Value','')
    return v
def gv(prop):
    v = prop.get('Value') if prop else None
    if isinstance(v,list) and v:
        inner = v[0]
        if isinstance(inner,dict) and isinstance(inner.get('Value'),dict):
            d = inner['Value']
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return (None,None,None)
def zoneset(r):
    p = fp(r.get('Value',[]),'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zstate(r):
    p = fp(r.get('Value',[]),'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None
def boolp(r,k):
    p = fp(r['Value'], k)
    return p.get('Value') if p else None

z = load('DT_Moria_Zones.json')
ch = load('DT_Moria_Chapters.json')
lm = load('DT_Moria_Landmarks.json')
lc = load('DT_Moria_LayoutConnections.json')
world = load('World.json')

zrows = z['Exports'][0]['Table']['Data']
crows = ch['Exports'][0]['Table']['Data']
lrows = lm['Exports'][0]['Table']['Data']
ncrows = lc['Exports'][0]['Table']['Data']

landmark_names = set(r['Name'] for r in lrows)

print("=== ALL CHAPTER ROWS for ChapID 4,5,6,7 (any zoneset) ===")
for r in crows:
    name = r['Name']
    cid = fp(r['Value'],'ChapterID')
    cid_v = cid.get('Value') if cid else None
    is_target = cid_v in (4,5,6,7)
    if not is_target:
        for n in (4,5,6,7):
            if f'hapter0{n}' in name or f'hapter-{n}' in name or f'Chapter{n}' in name:
                is_target = True; break
    if not is_target: continue
    zs = zoneset(r); st = zstate(r)
    minz = fp(r['Value'],'MinZ'); minz=minz.get('Value') if minz else None
    maxz = fp(r['Value'],'MaxZ'); maxz=maxz.get('Value') if maxz else None
    primez = fp(r['Value'],'PrimeZ'); primez=primez.get('Value') if primez else None
    layer = fp(r['Value'],'Layer'); layer=layer.get('Value') if layer else None
    dn = fp(r['Value'],'DisplayName')
    dn_key = ''
    if dn and isinstance(dn.get('Value'),list):
        for it in dn['Value']:
            if isinstance(it,dict) and it.get('Name')=='Key':
                dn_key = it.get('Value','')
    print("  %s  ZS=%s State=%s ChapID=%s MinZ=%s MaxZ=%s PrimeZ=%s Layer=%s DNKey=%s" % (name,zs,st,cid_v,minz,maxz,primez,layer,dn_key))

print()
print("=== Live SS zones in chap-4..chap-7 ===")
for cnum in (4,5,6,7):
    print("\n-- Chapter %d --" % cnum)
    pat = "SandboxSmall-Chapter0%d." % cnum
    found = 0
    for r in zrows:
        if zoneset(r)!='SandboxSmall' or zstate(r)=='Disabled': continue
        chap_ref = get(r,'Chapter') or ''
        if not chap_ref.startswith(pat): continue
        found += 1
        pos = gv(fp(r['Value'],'Position'))
        sz = gv(fp(r['Value'],'TargetSize'))
        bd = get(r,'BubbleDeck'); pd = get(r,'PassageDeck')
        ext = boolp(r,'bExtendedConnectivityLandmark')
        zext = (pos[2], pos[2] + (sz[2] or 0) - 1) if pos[2] is not None and sz[2] is not None else None
        lh = fp(r['Value'],'LandmarkHandles')
        lhandles = []
        if lh and lh.get('Value'):
            for e in lh['Value']:
                if isinstance(e,dict):
                    for sub in (e.get('Value') or []):
                        if isinstance(sub,dict) and sub.get('Name')=='Landmark':
                            lv = sub.get('Value')
                            if isinstance(lv,list):
                                for it in lv:
                                    if isinstance(it,dict) and it.get('Name')=='RowName':
                                        lhandles.append(it.get('Value'))
        miss = [h for h in lhandles if h and h not in landmark_names]
        miss_str = ("  MISSING_LM=%s" % miss) if miss else ""
        print("  %s\n    Pos=%s Size=%s Z=[%s..%s] BD=%s PD=%s ExtConn=%s LMs=%s%s" %
              (r['Name'],pos,sz,zext[0],zext[1],bd,pd,ext,lhandles or 'none',miss_str))
    if found==0:
        print("  *** NO LIVE ZONES ***")

print()
print("=== Cross-chapter overlap audit Z=22..29 ===")
cells = {}
for r in zrows:
    if zoneset(r)!='SandboxSmall' or zstate(r)=='Disabled': continue
    pos = gv(fp(r['Value'],'Position'))
    sz = gv(fp(r['Value'],'TargetSize'))
    if None in pos or None in sz: continue
    chap = get(r,'Chapter')
    for x in range(pos[0], pos[0]+sz[0]):
        for y in range(pos[1], pos[1]+sz[1]):
            for zc in range(pos[2], pos[2]+sz[2]):
                if 22 <= zc <= 29:
                    cells.setdefault((x,y,zc),[]).append((r['Name'],chap))
overlaps = {k:v for k,v in cells.items() if len(v)>1}
if overlaps:
    for k,v in sorted(overlaps.items()):
        print("  cell%s: %s" % (k,v))
else:
    print("  NONE")

print()
print("=== OOB check chap 4..7 (world 0..29) ===")
for r in zrows:
    if zoneset(r)!='SandboxSmall' or zstate(r)=='Disabled': continue
    chap = get(r,'Chapter') or ''
    if not any(("Chapter0%d."%n) in chap for n in (4,5,6,7)): continue
    pos = gv(fp(r['Value'],'Position'))
    sz = gv(fp(r['Value'],'TargetSize'))
    if None in pos or None in sz: continue
    xmax = pos[0]+sz[0]-1; ymax = pos[1]+sz[1]-1; zmax = pos[2]+sz[2]-1
    issues=[]
    if pos[0]<0 or xmax>29: issues.append("X[%d..%d]"%(pos[0],xmax))
    if pos[1]<0 or ymax>29: issues.append("Y[%d..%d]"%(pos[1],ymax))
    if pos[2]<0 or zmax>29: issues.append("Z[%d..%d]"%(pos[2],zmax))
    if issues: print("  %s OOB %s" % (r['Name'], issues))

print()
print("=== Stair zones with Z>=22 ===")
for r in zrows:
    if zoneset(r)!='SandboxSmall' or zstate(r)=='Disabled': continue
    nm = r['Name']
    pos = gv(fp(r['Value'],'Position'))
    sz = gv(fp(r['Value'],'TargetSize'))
    if None in pos or None in sz: continue
    zmax = pos[2]+sz[2]-1
    if 'levator' in nm or 'tair' in nm or (sz[2] or 0)>1:
        if zmax >= 22:
            chap = get(r,'Chapter')
            ext = boolp(r,'bExtendedConnectivityLandmark')
            print("  %s  Chap=%s Pos=%s Size=%s Z=[%d..%d] ExtConn=%s" % (nm,chap,pos,sz,pos[2],zmax,ext))

print()
print("=== Zone Pos.Z != chapter MinZ for chap 4..7 ===")
chap_minz = {}
for r in crows:
    if zoneset(r)!='SandboxSmall' or zstate(r)=='Disabled': continue
    minz = fp(r['Value'],'MinZ'); minz=minz.get('Value') if minz else None
    chap_minz[r['Name']] = minz
for r in zrows:
    if zoneset(r)!='SandboxSmall' or zstate(r)=='Disabled': continue
    chap = get(r,'Chapter') or ''
    if not any(("Chapter0%d."%n) in chap for n in (4,5,6,7)): continue
    pos = gv(fp(r['Value'],'Position'))
    sz = gv(fp(r['Value'],'TargetSize'))
    if None in pos: continue
    expect = chap_minz.get(chap)
    if expect is not None and pos[2] != expect:
        print("  %s chap=%s Pos.Z=%s chapMinZ=%s Sz.Z=%s" % (r['Name'],chap,pos[2],expect,sz[2]))

print()
print("=== DisplayName key resolution chap 4..7 ===")
text = json.dumps(world)
for r in crows:
    if zoneset(r)!='SandboxSmall': continue
    cid = fp(r['Value'],'ChapterID'); cid_v = cid.get('Value') if cid else None
    if cid_v not in (4,5,6,7): continue
    dn = fp(r['Value'],'DisplayName')
    if dn and isinstance(dn.get('Value'),list):
        key=''
        for it in dn['Value']:
            if isinstance(it,dict) and it.get('Name')=='Key': key=it.get('Value','')
        present = key in text if key else False
        print("  %s ChapID=%s key='%s' inWorld=%s" % (r['Name'],cid_v,key,present))

print()
print("=== LayoutConnections involving chap 4..7 ===")
for r in ncrows:
    if zoneset(r)!='SandboxSmall' or zstate(r)=='Disabled': continue
    nm = r['Name']
    # collect any chap refs in row
    s = json.dumps(r)
    hits = []
    for n in (4,5,6,7):
        if ("Chapter0%d."%n) in s:
            hits.append(n)
    if hits:
        # extract zone refs
        za = get(r,'ZoneA') if fp(r['Value'],'ZoneA') else None
        zb = get(r,'ZoneB') if fp(r['Value'],'ZoneB') else None
        print("  %s chaps=%s ZoneA=%s ZoneB=%s" % (nm,hits,za,zb))
