import json, os

ROOT = r"C:/Users/johnb/OneDrive/Documents/Projects/Moria-Replication/experiments/worldgen_research"
CH = os.path.join(ROOT, "DT_Moria_Chapters.json")

with open(CH, "r", encoding="utf-8") as f:
    j = json.load(f)

ex = [e for e in j["Exports"] if e.get("$type","").startswith("UAssetAPI.ExportTypes.DataTableExport")][0]
data = ex["Table"]["Data"]
rows = {r["Name"]: r for r in data}

def gp(r, n):
    for p in r["Value"]:
        if p.get("Name") == n: return p.get("Value")
    return None

def _is_level_row(name):
    if not name.startswith("SandboxSmall-Chapter"): return False
    if "." not in name: return False
    suffix = name.split(".", 1)[1]
    return suffix.startswith("Level") or suffix.startswith("Deep")

level_rows = []
for name, r in rows.items():
    if _is_level_row(name):
        level_rows.append(name)

print(f"Total level rows: {len(level_rows)} (expected 14)")

expected = [
    "SandboxSmall-Chapter01.Level1","SandboxSmall-Chapter02.Level2","SandboxSmall-Chapter03.Level3",
    "SandboxSmall-Chapter04.Level4","SandboxSmall-Chapter05.Level5","SandboxSmall-Chapter06.Level6",
    "SandboxSmall-Chapter07.Level7",
    "SandboxSmall-Chapter14.Deep1","SandboxSmall-Chapter13.Deep2","SandboxSmall-Chapter12.Deep3",
    "SandboxSmall-Chapter11.Deep4","SandboxSmall-Chapter10.Deep5","SandboxSmall-Chapter09.Deep6",
    "SandboxSmall-Chapter08.Deep7",
]
missing = [n for n in expected if n not in rows]
print("Missing from expected:", missing)

# Sorted by Layer descending
print(f"\n{'Layer':>5}  {'Name':<40} {'ChapID':>6} {'MinZ':>5} {'MaxZ':>5} {'PrimeZ':>6} {'ESL':>4}  Disp")
table = []
for n in expected:
    if n not in rows: continue
    r = rows[n]
    table.append((gp(r,"Layer"), n, gp(r,"ChapterID"), gp(r,"MinZ"), gp(r,"MaxZ"), gp(r,"PrimeZ"), gp(r,"EnemyScalingLevel"), gp(r,"DisplayName")))

for row in sorted(table, key=lambda x: -x[0]):
    L,n,c,mn,mx,pz,esl,dn = row
    print(f"{L:>+5}  {n:<40} {c:>6} {mn:>5} {mx:>5} {pz:>6} {esl:>4}  {dn}")

# NameMap check
nm = set(j["NameMap"])
new_names = ["SandboxSmall-Chapter04.Level4","SandboxSmall-Chapter05.Level5","SandboxSmall-Chapter06.Level6","SandboxSmall-Chapter07.Level7","SandboxSmall-Chapter14.Deep1","SandboxSmall-Chapter11.Deep4","SandboxSmall-Chapter10.Deep5","SandboxSmall-Chapter09.Deep6"]
print("\nNameMap len:", len(j["NameMap"]))
print("NamesReferencedFromExportDataCount:", j.get("NamesReferencedFromExportDataCount"))
print("Generations[0].NameCount:", j["Generations"][0]["NameCount"])
for n in new_names:
    print(f"  NameMap has {n}: {n in nm}")

# _is_level_row filter check
print("\n_is_level_row filter:")
for n in expected:
    print(f"  {n}: {_is_level_row(n)}")
