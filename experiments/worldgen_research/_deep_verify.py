"""Deep verification before build — every angle, no assumptions."""
import json, sys, io, importlib.util
from pathlib import Path
from collections import Counter
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

z = json.load(open('DT_Moria_Zones.json',encoding='utf-8'))
lm = json.load(open('DT_Moria_Landmarks.json',encoding='utf-8'))
ch = json.load(open('DT_Moria_Chapters.json',encoding='utf-8'))
lc = json.load(open('DT_Moria_LayoutConnections.json',encoding='utf-8'))

def fp(v,n):
    for p in v or []:
        if isinstance(p,dict) and p.get('Name')==n: return p
    return None
def gv(p):
    v=p.get('Value') if p else None
    if isinstance(v,list) and v:
        d=v[0].get('Value') if isinstance(v[0],dict) else None
        if isinstance(d,dict): return (d.get('X'),d.get('Y'),d.get('Z'))
    return None
def gf(r,k):
    p=fp(r['Value'],k); v=p.get('Value') if p else None
    if isinstance(v,list):
        for it in v:
            if isinstance(it,dict) and it.get('Name')=='RowName': return it.get('Value','')
    return v
def st(r):
    p=fp(r.get('Value',[]),'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zoneset(r):
    p=fp(r.get('Value',[]),'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None

ss_cells = set()
chap_band = {}
for r in ch['Exports'][0]['Table']['Data']:
    n = r['Name']
    if not (n.startswith('SandboxSmall-Chapter') or n.startswith('SandboxSmall-chapter')): continue
    if st(r) == 'Disabled': continue
    mn = gf(r,'MinZ'); mx = gf(r,'MaxZ'); pz = gf(r,'PrimeZ')
    chap_band[n] = (mn, mx, pz)
    if isinstance(mn,int) and isinstance(mx,int):
        for cz in range(mn, mx+1):
            ss_cells.add(cz)

print('CHECK 1 - SS Z bands:')
print('  Live SS cells:', sorted(ss_cells))
print('  Free in [0..29]:', sorted(set(range(30)) - ss_cells))

print('\nCHECK 2 - Zone Position+TS within chapter band (vanilla pattern, info only):')
out_of_band = 0
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    pos = gv(fp(r['Value'],'Position'))
    sz = gv(fp(r['Value'],'TargetSize'))
    if not pos or pos == (0,0,0): continue
    chap = gf(r,'Chapter')
    band = chap_band.get(chap)
    if not band: continue
    z0 = pos[2]; z1 = pos[2] + sz[2] - 1
    mn, mx = band[0], band[1]
    if not isinstance(mn,int): continue
    if z0 < mn or z1 > mx:
        out_of_band += 1
print('  Zones with Position outside chapter band (vanilla mismatch, OK):', out_of_band)

print('\nCHECK 3 - Zone Position.Z in some Live SS cell:')
bad = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    pos = gv(fp(r['Value'],'Position'))
    if not pos or pos == (0,0,0): continue
    if pos[2] not in ss_cells:
        bad.append((r['Name'], pos))
print('  Zones at uncovered Z:', len(bad))
for n, p in bad[:10]:
    print(' ', n, p)

print('\nCHECK 4 - Sandbox/Bridge landmark BP.Z in any SS cell:')
ss_namespaces = ('Sandbox.',)
ss_bridge_names = {'TradingPost','DurinsTower','DimrillDale','Sandbox_DurinsTower','Sandbox_TradingPost','Sandbox_DimrillDale'}
bad = []
for r in lm['Exports'][0]['Table']['Data']:
    n = r['Name']
    if not (n.startswith(ss_namespaces) or n in ss_bridge_names): continue
    if st(r) == 'Disabled': continue
    bp = gv(fp(r['Value'],'BasePosition'))
    if not bp or (bp[0]==0 and bp[1]==0): continue
    if bp[2] not in ss_cells:
        bad.append((n, bp))
print('  Sandbox landmarks outside SS cells:', len(bad))
for n, p in bad[:10]:
    print(' ', n, p)

print('\nCHECK 5 - PreferredZOverride in band:')
bad = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    p = fp(r['Value'],'PreferredZOverride')
    if not p: continue
    v = p.get('Value')
    if not isinstance(v,int) or v < 0: continue
    if v not in ss_cells:
        bad.append((r['Name'], v))
print('  PreferredZOverride at uncovered Z:', len(bad))
for n, v in bad:
    print(' ', n, '=', v)

print('\nCHECK 6 - Nested Subcell.Z in band:')
bad = []
for r in lc['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    for fld in ('OriginInterface','DestinationInterface'):
        prop = fp(r['Value'], fld)
        if not prop: continue
        for inner in (prop.get('Value') or []):
            if isinstance(inner,dict) and inner.get('Name')=='Subcell':
                sc_v = inner.get('Value')
                if isinstance(sc_v,list) and sc_v:
                    d = sc_v[0].get('Value')
                    if isinstance(d,dict):
                        z_val = d.get('Z')
                        if isinstance(z_val,int) and z_val != 0 and z_val not in ss_cells:
                            bad.append((r['Name'], fld, z_val))
print('  Nested Subcell.Z outside SS cells:', len(bad))
for n, f, z_val in bad:
    print(' ', n, f, 'Subcell.Z=', z_val)

print('\nCHECK 7 - Connection endpoint landmarks resolve:')
lm_names = {r['Name'] for r in lm['Exports'][0]['Table']['Data']}
bad = []
for r in lc['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    for fld in ('OriginLandmark','DestinationLandmark'):
        ln = gf(r, fld)
        if ln and ln != 'None' and ln not in lm_names:
            bad.append((r['Name'], fld, ln))
print('  Connection endpoints to missing landmarks:', len(bad))

print('\nCHECK 8 - Zone Chapter refs resolve:')
chap_names = {r['Name'] for r in ch['Exports'][0]['Table']['Data']}
bad = []
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or st(r) == 'Disabled': continue
    chap = gf(r,'Chapter')
    if chap and chap != 'None' and chap not in chap_names:
        bad.append((r['Name'], chap))
print('  Zones with broken Chapter ref:', len(bad))

print('\nCHECK 9 - NameMap counter sync:')
for fn in ['DT_Moria_Zones.json','DT_Moria_Chapters.json','DT_Moria_Landmarks.json','DT_Moria_LayoutConnections.json']:
    d = json.load(open(fn,encoding='utf-8'))
    nm_len = len(d.get('NameMap',[]))
    nrf = d.get('NamesReferencedFromExportDataCount')
    g = d.get('Generations') or []
    g_nc = g[0].get('NameCount') if g else None
    s = 'OK' if nrf == nm_len and (g_nc is None or g_nc == nm_len) else 'MISMATCH'
    print(' ', fn, 'NM=', nm_len, 'NRefED=', nrf, 'Gen.NameCount=', g_nc, s)

print('\nCHECK 10 - Chapter Layer uniqueness:')
layer_dist = Counter()
for r in ch['Exports'][0]['Table']['Data']:
    n = r['Name']
    if not (n.startswith('SandboxSmall-Chapter') or n.startswith('SandboxSmall-chapter')): continue
    if st(r) == 'Disabled': continue
    L = gf(r,'Layer')
    layer_dist[L] += 1
print('  Live SS Layer distribution:', dict(layer_dist))
dups = [L for L,c in layer_dist.items() if c > 1]
if dups:
    print('  WARN duplicate Layers:', dups)
else:
    print('  OK each Layer unique')

print('\nCHECK 11 - Full BuildValidator pass:')
spec = importlib.util.spec_from_file_location('sze',
    r'C:\Users\johnb\OneDrive\Documents\Projects\Moria-Replication\scripts\SandboxZoneEditor.py')
sze = importlib.util.module_from_spec(spec); sys.modules['sze']=sze
spec.loader.exec_module(sze)
specs=[('zones','DT_Moria_Zones.json'),('chapters','DT_Moria_Chapters.json'),
       ('landmarks','DT_Moria_Landmarks.json'),('connections','DT_Moria_LayoutConnections.json'),
       ('strings','World.json'),('biomes','DT_Moria_Biomes.json'),
       ('decks','DT_Moria_ZoneDeck.json'),('filters','DT_Moria_ZoneBubbleFilters.json'),
       ('templates','DT_Moria_ZoneTemplates.json')]
docs={}
for k,fn in specs:
    p=Path(fn)
    if p.exists():
        d=sze.DataTableDoc(k,p,fn[:-5],fn[:-5])
        if d.load(): docs[k]=d
results = sze.BuildValidator(docs).run()
errs=[r for r in results if r.severity=='error']
warns=[r for r in results if r.severity=='warning']
print('  Validator:', len(errs), 'errors,', len(warns), 'warnings')
for r in results:
    if r.severity == 'error':
        print(' ', '[error]', r.check, ':', r.detail[:140])
