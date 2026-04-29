import json, sys, io, shutil, os, importlib.util
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ts_dir = 'backups/before_shift_with_subcell'
os.makedirs(ts_dir, exist_ok=True)
files_to_save = ['DT_Moria_Zones.json','DT_Moria_Chapters.json','DT_Moria_Landmarks.json',
                 'DT_Moria_LayoutConnections.json','World.json']
for f in files_to_save:
    if os.path.exists(f): shutil.copy(f, f'{ts_dir}/{f}')
print('Saved current state to', ts_dir)

print('\nRestoring pure vanilla baseline...')
for src, dst in [
    ('DT_Moria_Zones.original.json',             'DT_Moria_Zones.json'),
    ('DT_Moria_Chapters.original.json',          'DT_Moria_Chapters.json'),
    ('DT_Moria_Landmarks.original.json',         'DT_Moria_Landmarks.json'),
    ('DT_Moria_LayoutConnections.original.json', 'DT_Moria_LayoutConnections.json'),
]:
    if os.path.exists(src):
        shutil.copy(src, dst)
        print('  restored', dst)

OFFSET = 7

def fp(v,n):
    for p in v or []:
        if isinstance(p,dict) and p.get('Name')==n: return p
    return None
def st(r):
    p=fp(r.get('Value',[]),'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zoneset(r):
    p=fp(r.get('Value',[]),'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None
def gf(r,k):
    p=fp(r['Value'],k); v=p.get('Value') if p else None
    if isinstance(v,list):
        for it in v:
            if isinstance(it,dict) and it.get('Name')=='RowName': return it.get('Value','')
    return v

ch = json.load(open('DT_Moria_Chapters.json',encoding='utf-8'))
chapter_fields = 0
ss_chapter_names = set()
for r in ch['Exports'][0]['Table']['Data']:
    n = r['Name']
    if not (n.startswith('SandboxSmall-Chapter') or n.startswith('SandboxSmall-chapter')):
        continue
    ss_chapter_names.add(n)
    for fld in ('MinZ','MaxZ','PrimeZ'):
        p = fp(r['Value'], fld)
        if p and isinstance(p.get('Value'), int):
            p['Value'] += OFFSET
            chapter_fields += 1
print('\nChapters: shifted', chapter_fields, 'fields across', len(ss_chapter_names), 'SS chapter rows')

z = json.load(open('DT_Moria_Zones.json',encoding='utf-8'))
zone_count = 0; zone_skipped = 0
ss_zones = set()
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall': continue
    ss_zones.add(r['Name'])
    pos_p = fp(r['Value'], 'Position')
    if pos_p:
        v = pos_p.get('Value')
        if isinstance(v, list) and v:
            d = v[0].get('Value') if isinstance(v[0], dict) else None
            if isinstance(d, dict):
                x, y, zz = d.get('X'), d.get('Y'), d.get('Z')
                if x == 0 and y == 0 and zz == 0:
                    zone_skipped += 1
                elif isinstance(zz, int):
                    d['Z'] = zz + OFFSET
                    zone_count += 1
print('Zones: shifted', zone_count, 'Position.Z values (preserved', zone_skipped, 'auto-place sentinels)')

lm = json.load(open('DT_Moria_Landmarks.json',encoding='utf-8'))
hosted_landmarks = set()
for r in z['Exports'][0]['Table']['Data']:
    if r['Name'] not in ss_zones: continue
    lh = fp(r['Value'], 'LandmarkHandles')
    for entry in (lh.get('Value') or []) if lh else []:
        if not isinstance(entry, dict): continue
        ev = entry.get('Value')
        if not isinstance(ev, list): continue
        for sub in ev:
            if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                lv = sub.get('Value')
                if isinstance(lv, list):
                    for it in lv:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            ln = it.get('Value', '')
                            if ln: hosted_landmarks.add(ln)

lm_count = 0; lm_sentinel = 0
for r in lm['Exports'][0]['Table']['Data']:
    if r['Name'] not in hosted_landmarks: continue
    bp_p = fp(r['Value'], 'BasePosition')
    if not bp_p: continue
    v = bp_p.get('Value')
    if isinstance(v, list) and v:
        d = v[0].get('Value') if isinstance(v[0], dict) else None
        if isinstance(d, dict):
            x, y, zz = d.get('X'), d.get('Y'), d.get('Z')
            if x == 0 and y == 0:
                lm_sentinel += 1
            elif isinstance(zz, int):
                d['Z'] = zz + OFFSET
                lm_count += 1
print('Landmarks: shifted', lm_count, 'BasePosition.Z values (preserved', lm_sentinel, 'sentinels)')

lc = json.load(open('DT_Moria_LayoutConnections.json',encoding='utf-8'))
subcell_count = 0; subcell_z0 = 0; subcell_skipped_zoneset = 0
for r in lc['Exports'][0]['Table']['Data']:
    zs_val = zoneset(r)
    if zs_val != 'SandboxSmall':
        subcell_skipped_zoneset += 1
        continue
    if st(r) == 'Disabled':
        continue
    sc_p = fp(r['Value'], 'Subcell')
    if not sc_p: continue
    v = sc_p.get('Value')
    if isinstance(v, list) and v:
        d = v[0].get('Value') if isinstance(v[0], dict) else None
        if isinstance(d, dict):
            zz = d.get('Z')
            if zz == 0:
                subcell_z0 += 1
            elif isinstance(zz, int):
                d['Z'] = zz + OFFSET
                subcell_count += 1
print('LayoutConnections.Subcell.Z: shifted', subcell_count, 'values (skipped', subcell_z0, 'Z=0 entries;', subcell_skipped_zoneset, 'non-SS rows)')

json.dump(ch, open('DT_Moria_Chapters.json','w',encoding='utf-8'), indent=2)
json.dump(z,  open('DT_Moria_Zones.json','w',encoding='utf-8'), indent=2)
json.dump(lm, open('DT_Moria_Landmarks.json','w',encoding='utf-8'), indent=2)
json.dump(lc, open('DT_Moria_LayoutConnections.json','w',encoding='utf-8'), indent=2)
print('\nAll 4 files saved.')

print('\n===== VERIFICATION =====')
print('Chapter Z bands (post-shift):')
ch_v = json.load(open('DT_Moria_Chapters.json',encoding='utf-8'))
rows = []
for r in ch_v['Exports'][0]['Table']['Data']:
    n = r['Name']
    if not (n.startswith('SandboxSmall-Chapter') or n.startswith('SandboxSmall-chapter')): continue
    if st(r) == 'Disabled': continue
    rows.append((gf(r,'Layer'), n, gf(r,'MinZ'), gf(r,'MaxZ'), gf(r,'PrimeZ')))
rows.sort(key=lambda x: -(x[0] if isinstance(x[0], int) else 0))
for L, n, mn, mx, pz in rows:
    print('  ', n, 'L=', L, 'MinZ=', mn, 'MaxZ=', mx, 'PrimeZ=', pz)

from collections import Counter
zdist = Counter()
lc_v = json.load(open('DT_Moria_LayoutConnections.json',encoding='utf-8'))
for r in lc_v['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall': continue
    if st(r) == 'Disabled': continue
    sc_p = fp(r['Value'], 'Subcell')
    if not sc_p: continue
    v = sc_p.get('Value')
    if isinstance(v, list) and v:
        d = v[0].get('Value') if isinstance(v[0], dict) else None
        if isinstance(d, dict):
            zdist[d.get('Z')] += 1
print('\nLayoutConnections.Subcell.Z distribution (Live SS only):')
for z_val in sorted(zdist):
    print('  Z=', z_val, ':', zdist[z_val], 'entries')

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
print('\nValidator:', len(errs), 'errors,', len(warns), 'warnings')
