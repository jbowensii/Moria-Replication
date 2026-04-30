"""Re-number SandboxSmall chapter rows to vanilla-style sequential order:
Levels 1..7 (top to bottom of upper levels), then Deeps 1..7 mapped 8..14 (D-7 -> 8 ... D-1 -> 14).

Phase 1: rename 10 colliding chapter row names to chapter-tmp-N
Phase 2: update all zone Chapter and AdditionalChapters refs old -> chapter-tmp-N
Phase 3: drop tmp prefix in both files
Phase 4: update ChapterID, DisplayName.Value, EnemyScalingLevel for each renamed chapter
Phase 5: (no-op) LayoutConnections has no chapter refs
Phase 6: NameMap sync per file
"""
import json, copy

CHAP_PATH = 'DT_Moria_Chapters.json'
Z_PATH = 'DT_Moria_Zones.json'
LM_PATH = 'DT_Moria_LayoutConnections.json'

# old -> new (sequential) mapping for chapter row names that change
RENAME_MAP = {
    'SandboxSmall-chapter-9':  'SandboxSmall-chapter-5',
    'SandboxSmall-chapter-10': 'SandboxSmall-chapter-6',
    'SandboxSmall-chapter-11': 'SandboxSmall-chapter-7',
    'SandboxSmall-chapter-14': 'SandboxSmall-chapter-8',
    'SandboxSmall-chapter-13': 'SandboxSmall-chapter-9',
    'SandboxSmall-chapter-12': 'SandboxSmall-chapter-10',
    'SandboxSmall-chapter-8':  'SandboxSmall-chapter-11',
    'SandboxSmall-chapter-7':  'SandboxSmall-chapter-12',
    'SandboxSmall-chapter-6':  'SandboxSmall-chapter-13',
    'SandboxSmall-chapter-5':  'SandboxSmall-chapter-14',
}
# tmp staging for collision-free Phase 1+2
TMP_MAP = {old: 'SandboxSmall-chapter-tmp-' + new.split('-')[-1]
           for old, new in RENAME_MAP.items()}
TMP_TO_FINAL = {tmp: RENAME_MAP[old] for old, tmp in TMP_MAP.items()}

# Phase 4 metadata: final-name -> (ChapterID, DisplayName, EnemyScalingLevel)
FINAL_META = {
    'SandboxSmall-chapter-1':  (1,  'Chapter.Sandbox.Level1.Name', 0),
    'SandboxSmall-chapter-2':  (2,  'Chapter.Sandbox.Level2.Name', 1),
    'SandboxSmall-chapter-3':  (3,  'Chapter.Sandbox.Level3.Name', 2),
    'SandboxSmall-chapter-4':  (4,  'Chapter.Sandbox.Level4.Name', 3),
    'SandboxSmall-chapter-5':  (5,  'Chapter.Sandbox.Level5.Name', 4),
    'SandboxSmall-chapter-6':  (6,  'Chapter.Sandbox.Level6.Name', 5),
    'SandboxSmall-chapter-7':  (7,  'Chapter.Sandbox.Level7.Name', 6),
    'SandboxSmall-chapter-8':  (8,  'Chapter.Sandbox.Deep7.Name',  7),
    'SandboxSmall-chapter-9':  (9,  'Chapter.Sandbox.Deep6.Name',  6),
    'SandboxSmall-chapter-10': (10, 'Chapter.Sandbox.Deep5.Name',  5),
    'SandboxSmall-chapter-11': (11, 'Chapter.Sandbox.Deep4.Name',  4),
    'SandboxSmall-chapter-12': (12, 'Chapter.Sandbox.Deep3.Name',  3),
    'SandboxSmall-chapter-13': (13, 'Chapter.Sandbox.Deep2.Name',  2),
    'SandboxSmall-chapter-14': (14, 'Chapter.Sandbox.Deep1.Name',  1),
}


def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n:
            return p
    return None


def get_rowname(prop):
    """Get RowName string from a StructProperty's nested Value list."""
    v = prop.get('Value') if prop else None
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return None


def set_rowname(prop, new):
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                it['Value'] = new
                return True
    return False


# ========== LOAD ==========
chap = json.load(open(CHAP_PATH, encoding='utf-8'))
z = json.load(open(Z_PATH, encoding='utf-8'))

# ========== PHASE 1: rename chapter rows to tmp ==========
phase1_count = 0
for cd in chap['Exports'][0]['Table']['Data']:
    if cd['Name'] in TMP_MAP:
        cd['Name'] = TMP_MAP[cd['Name']]
        phase1_count += 1
print(f'Phase 1: renamed {phase1_count} chapter rows to tmp names')

# ========== PHASE 2: update zone Chapter / AdditionalChapters refs ==========
phase2_chapter_field = 0
phase2_additional = 0
phase2_zones_touched = set()

for r in z['Exports'][0]['Table']['Data']:
    rn = r['Name']
    touched = False
    cprop = fp(r['Value'], 'Chapter')
    if cprop:
        old = get_rowname(cprop)
        if old in TMP_MAP:
            set_rowname(cprop, TMP_MAP[old])
            phase2_chapter_field += 1
            touched = True
    aprop = fp(r['Value'], 'AdditionalChapters')
    if aprop:
        for entry in (aprop.get('Value') or []):
            if isinstance(entry, dict):
                # entry is StructProperty whose Value is a list of NameProperties incl RowName
                ev = entry.get('Value')
                if isinstance(ev, list):
                    for it in ev:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            old = it.get('Value', '')
                            if old in TMP_MAP:
                                it['Value'] = TMP_MAP[old]
                                phase2_additional += 1
                                touched = True
    if touched:
        phase2_zones_touched.add(rn)

print(f'Phase 2: updated {phase2_chapter_field} Chapter refs + '
      f'{phase2_additional} AdditionalChapters refs across '
      f'{len(phase2_zones_touched)} zones')

# ========== PHASE 3: drop tmp prefix in both files ==========
phase3_chap = 0
for cd in chap['Exports'][0]['Table']['Data']:
    if cd['Name'] in TMP_TO_FINAL:
        cd['Name'] = TMP_TO_FINAL[cd['Name']]
        phase3_chap += 1

phase3_zone_chapter = 0
phase3_zone_addl = 0
for r in z['Exports'][0]['Table']['Data']:
    cprop = fp(r['Value'], 'Chapter')
    if cprop:
        old = get_rowname(cprop)
        if old in TMP_TO_FINAL:
            set_rowname(cprop, TMP_TO_FINAL[old])
            phase3_zone_chapter += 1
    aprop = fp(r['Value'], 'AdditionalChapters')
    if aprop:
        for entry in (aprop.get('Value') or []):
            if isinstance(entry, dict):
                ev = entry.get('Value')
                if isinstance(ev, list):
                    for it in ev:
                        if isinstance(it, dict) and it.get('Name') == 'RowName':
                            old = it.get('Value', '')
                            if old in TMP_TO_FINAL:
                                it['Value'] = TMP_TO_FINAL[old]
                                phase3_zone_addl += 1
print(f'Phase 3: dropped tmp prefix on {phase3_chap} chapter rows, '
      f'{phase3_zone_chapter} zone Chapter refs, {phase3_zone_addl} AdditionalChapters refs')

# ========== PHASE 4: update ChapterID, DisplayName, EnemyScalingLevel ==========
phase4_changes = []
for cd in chap['Exports'][0]['Table']['Data']:
    name = cd['Name']
    if name not in FINAL_META:
        continue
    new_cid, new_dn, new_esl = FINAL_META[name]
    cur = {}
    cprop = fp(cd['Value'], 'ChapterID')
    if cprop is not None:
        cur['ChapterID'] = cprop.get('Value')
        cprop['Value'] = new_cid
    dprop = fp(cd['Value'], 'DisplayName')
    if dprop is not None:
        cur['DisplayName'] = dprop.get('Value')
        dprop['Value'] = new_dn
    eprop = fp(cd['Value'], 'EnemyScalingLevel')
    if eprop is not None:
        cur['EnemyScalingLevel'] = eprop.get('Value')
        eprop['Value'] = new_esl
    phase4_changes.append((name, cur, (new_cid, new_dn, new_esl)))

print(f'Phase 4: updated ChapterID/DisplayName/EnemyScalingLevel on '
      f'{len(phase4_changes)} chapter rows')
for name, before, after in phase4_changes:
    print(f'  {name}: {before} -> {after}')

# ========== PHASE 5: LayoutConnections (verified no refs) ==========
print('Phase 5: LayoutConnections has no chapter row refs (no-op)')

# ========== PHASE 6: NameMap sync ==========


def reconcile_namemap(d, drop_prefix='SandboxSmall-chapter-tmp-'):
    """Strip orphan tmp entries; ensure all final chapter names present."""
    nm = d.get('NameMap', [])
    # Drop any leftover tmp entries
    nm = [n for n in nm if not (isinstance(n, str) and n.startswith(drop_prefix))]
    existing = set(nm)
    added = 0
    for final in FINAL_META.keys():
        if final not in existing:
            nm.append(final)
            existing.add(final)
            added += 1
    d['NameMap'] = nm
    if 'NamesReferencedFromExportDataCount' in d:
        d['NamesReferencedFromExportDataCount'] = len(nm)
    exp0 = d['Exports'][0]
    if 'Generations' in exp0 and exp0['Generations']:
        exp0['Generations'][0]['NameCount'] = len(nm)
    return added, len(nm)


a, n = reconcile_namemap(chap)
print(f'Phase 6: Chapters NameMap +{a} (total {n})')
a, n = reconcile_namemap(z)
print(f'Phase 6: Zones NameMap +{a} (total {n})')

# ========== SAVE ==========
json.dump(chap, open(CHAP_PATH, 'w', encoding='utf-8'), indent=2)
json.dump(z, open(Z_PATH, 'w', encoding='utf-8'), indent=2)
print('\nApplied.')
