import json, os, sys, types, importlib.util
def fp(v, n):
    for p in v or []:
        if isinstance(p, dict) and p.get('Name') == n: return p
    return None
def get(r, k):
    p = fp(r['Value'], k)
    if not p: return None
    v = p.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name')=='RowName':
                return it.get('Value','')
    return v
def get_intvec(prop):
    v = prop.get('Value') if prop else None
    if isinstance(v, list) and v:
        inner = v[0]
        if isinstance(inner, dict) and isinstance(inner.get('Value'), dict):
            d = inner['Value']
            return (d.get('X'), d.get('Y'), d.get('Z'))
    return (None, None, None)
def zoneset(r):
    p = fp(r.get('Value', []), 'ZoneSet')
    return str(p.get('Value','')).split('::')[-1] if p else None
def zstate(r):
    p = fp(r.get('Value', []), 'EnabledState')
    return str(p.get('Value','')).split('::')[-1] if p else None

z = json.load(open('DT_Moria_Zones.json', encoding='utf-8'))
ch = json.load(open('DT_Moria_Chapters.json', encoding='utf-8'))
lc = json.load(open('DT_Moria_LayoutConnections.json', encoding='utf-8'))

def differs(stem):
    cur = stem + '.json'
    orig = stem + '.original.json'
    if not os.path.exists(orig): return None
    a = json.dumps(json.load(open(cur, encoding='utf-8')), sort_keys=True)
    b = json.dumps(json.load(open(orig, encoding='utf-8')), sort_keys=True)
    return a != b

print('=== Files that will bundle into the next pak ===')
for stem in ['DT_Moria_Zones','DT_Moria_Chapters','DT_Moria_Biomes','DT_Moria_Landmarks',
             'DT_Moria_ZoneDeck','DT_Moria_ZoneBubbleFilters','World',
             'DT_Moria_LayoutConnections','DT_Moria_ZoneTemplates']:
    d = differs(stem)
    flag = '[BUNDLES]' if d is True else '[skip]' if d is False else '[?]'
    print('  ' + flag + ' ' + stem)

print()
print('=== DestroyedCity_A_Desolation ===')
for r in z['Exports'][0]['Table']['Data']:
    if r['Name'] != 'Sandbox_Small_DestroyedCity_A_Desolation': continue
    print('  Chapter      = ' + str(get(r,'Chapter')))
    print('  Position     = ' + str(get_intvec(fp(r['Value'],'Position'))))
    print('  TargetSize   = ' + str(get_intvec(fp(r['Value'],'TargetSize'))))
    print('  EnabledState = ' + str(zstate(r)))
    print('  BubbleDeck   = ' + str(get(r,'BubbleDeck')))
    print('  PassageDeck  = ' + str(get(r,'PassageDeck')))
    print('  bPositionFromLandmarks = ' + str(fp(r['Value'],'bPositionFromLandmarks').get('Value')))
    print('  bExtendFootprint       = ' + str(fp(r['Value'],'bExtendFootprint').get('Value')))
    lh = fp(r['Value'], 'LandmarkHandles')
    n = len(lh.get('Value') or []) if lh else 0
    print('  LandmarkHandles count  = ' + str(n))
    if n > 0:
        for e in (lh.get('Value') or []):
            if not isinstance(e, dict): continue
            inner = e.get('Value', [])
            for sub in inner:
                if isinstance(sub, dict) and sub.get('Name') == 'Landmark':
                    lv = sub.get('Value')
                    if isinstance(lv, list):
                        for it in lv:
                            if isinstance(it, dict) and it.get('Name')=='RowName':
                                print('    -> ' + str(it.get('Value')))

print()
print('=== Live SS zones in chap-7 (Lv-7) ===')
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r)=='Disabled': continue
    if get(r,'Chapter') == 'SandboxSmall-chapter-7':
        print('  ' + r['Name'] + '  Pos=' + str(get_intvec(fp(r['Value'],'Position'))) + '  Size=' + str(get_intvec(fp(r['Value'],'TargetSize'))))

print()
print('=== Live SS zones in chap-6 (Lv-6) ===')
for r in z['Exports'][0]['Table']['Data']:
    if zoneset(r) != 'SandboxSmall' or zstate(r)=='Disabled': continue
    if get(r,'Chapter') == 'SandboxSmall-chapter-6':
        print('  ' + r['Name'] + '  Pos=' + str(get_intvec(fp(r['Value'],'Position'))) + '  Size=' + str(get_intvec(fp(r['Value'],'TargetSize'))))

print()
print('=== Sandbox_Small_21stHallToBridge connection ===')
for r in lc['Exports'][0]['Table']['Data']:
    if r['Name'] != 'Sandbox_Small_21stHallToBridge': continue
    print('  EnabledState = ' + str(zstate(r)))
    print('  ZoneRule     = ' + str(fp(r['Value'],'ZoneRule').get('Value')))
    print('  bRequired    = ' + str(fp(r['Value'],'bRequired').get('Value')))
    print('  bExclusive   = ' + str(fp(r['Value'],'bExclusive').get('Value')))

# Validator
for mod in ['tkinter','tkinter.ttk','tkinter.filedialog','tkinter.messagebox','tkinter.simpledialog','tkinter.scrolledtext','tkinter.font']:
    if mod not in sys.modules: sys.modules[mod] = types.ModuleType(mod)
class _Stub:
    def __init__(self, *a, **k): pass
    def __getattr__(self, n): return _Stub()
    def __call__(self, *a, **k): return _Stub()
for nm in list(sys.modules):
    if nm.startswith('tkinter'):
        m = sys.modules[nm]
        for attr in ('Tk','Toplevel','Frame','Label','Button','Entry','Text','Listbox','StringVar','IntVar','BooleanVar','Menu','Canvas','PhotoImage','Treeview','Scrollbar','PanedWindow','Notebook','Combobox','Style','OptionMenu','Spinbox','Radiobutton','Checkbutton','LabelFrame','Separator','Progressbar','TclError','TkVersion','END','BOTH','LEFT','RIGHT','TOP','BOTTOM','X','Y','HORIZONTAL','VERTICAL','NSEW','EW','NS','N','S','E','W','CENTER','NORMAL','DISABLED'):
            if not hasattr(m, attr): setattr(m, attr, _Stub())

spec = importlib.util.spec_from_file_location('sze', '../../scripts/SandboxZoneEditor.py')
mod = importlib.util.module_from_spec(spec)
mod.__file__ = '../../scripts/SandboxZoneEditor.py'
try: spec.loader.exec_module(mod)
except: pass

class DocLite:
    def __init__(self,k,l,p): self.key=k; self.label=l; self.json_path=p; self.data=json.loads(open(p, encoding='utf-8').read())
    @property
    def rows(self):
        try: return self.data['Exports'][0]['Table']['Data']
        except: return []
    def reconcile_namemap(self): pass

docs = {
    'zones': DocLite('zones','Zones', 'DT_Moria_Zones.json'),
    'chapters': DocLite('chapters','Chapters', 'DT_Moria_Chapters.json'),
    'landmarks': DocLite('landmarks','Landmarks', 'DT_Moria_Landmarks.json'),
    'decks': DocLite('decks','ZoneDeck', 'DT_Moria_ZoneDeck.json'),
    'connections': DocLite('connections','LayoutConnections', 'DT_Moria_LayoutConnections.json'),
}
issues = mod.BuildValidator(docs).run()
print()
print('=== BuildValidator: ' + str(len([i for i in issues if i.severity=='error'])) + ' errors, ' + str(len([i for i in issues if i.severity=='warning'])) + ' warnings ===')
for it in issues:
    print('  [' + it.severity + '] ' + it.check + ': ' + it.detail[:180])
