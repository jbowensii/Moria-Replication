"""Re-run BuildValidator after the endpoint-host fix."""
import json, os, sys, types, importlib.util
ROOT = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT)

# stub tkinter
for mod in ['tkinter','tkinter.ttk','tkinter.filedialog','tkinter.messagebox','tkinter.simpledialog','tkinter.scrolledtext','tkinter.font']:
    if mod not in sys.modules: sys.modules[mod] = types.ModuleType(mod)
class _Stub:
    def __init__(self,*a,**k): pass
    def __getattr__(self,n): return _Stub()
    def __call__(self,*a,**k): return _Stub()
for nm in list(sys.modules):
    if nm.startswith('tkinter'):
        m = sys.modules[nm]
        for attr in ('Tk','Toplevel','Frame','Label','Button','Entry','Text','Listbox','StringVar','IntVar','BooleanVar','Menu','Canvas','PhotoImage','Treeview','Scrollbar','PanedWindow','Notebook','Combobox','Style','OptionMenu','Spinbox','Radiobutton','Checkbutton','LabelFrame','Separator','Progressbar','TclError','TkVersion','END','BOTH','LEFT','RIGHT','TOP','BOTTOM','X','Y','HORIZONTAL','VERTICAL','NSEW','EW','NS','N','S','E','W','CENTER','NORMAL','DISABLED'):
            if not hasattr(m, attr): setattr(m, attr, _Stub())

spec = importlib.util.spec_from_file_location('sze', '../../scripts/SandboxZoneEditor.py')
mod = importlib.util.module_from_spec(spec); mod.__file__ = '../../scripts/SandboxZoneEditor.py'
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
errs = [i for i in issues if i.severity=='error']
warns = [i for i in issues if i.severity=='warning']
print(f'=== BuildValidator: {len(errs)} errors, {len(warns)} warnings ===')
for it in issues:
    print(f'  [{it.severity}] {it.check}: {it.detail[:200]}')

# Quick sanity: count level rows
ch = json.load(open('DT_Moria_Chapters.json', encoding='utf-8'))
def fp(v,n):
    for p in v or []:
        if isinstance(p,dict) and p.get('Name')==n: return p
    return None
def get(r,k):
    p=fp(r['Value'],k);
    if not p: return None
    v=p.get('Value')
    if isinstance(v,list):
        for it in v:
            if isinstance(it,dict) and it.get('Name')=='RowName': return it.get('Value','')
    return v
levels = []
for r in ch['Exports'][0]['Table']['Data']:
    cid = get(r,'ChapterID')
    cid = '' if cid is None else str(cid)
    if cid.startswith('SandboxSmall-chapter-') or cid.startswith('SandboxSmall-deep-'):
        levels.append(r['Name'])
print(f'\nLevel/deep chapter rows present: {len(levels)}')
for n in sorted(levels): print(f'  {n}')
