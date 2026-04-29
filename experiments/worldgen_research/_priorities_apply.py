"""Apply P1 (disable null-endpoint LCs) + P2 (add new BuildValidator check).

Idempotent: re-running won't double-apply.
"""
import json
import shutil
import re
from pathlib import Path

WGR = Path(__file__).resolve().parent
SCRIPTS = WGR.parent.parent / 'scripts'
LC_JSON = WGR / 'DT_Moria_LayoutConnections.json'
LC_BACKUP = WGR / 'DT_Moria_LayoutConnections.before_disable_null_lcs.json'
EDITOR = SCRIPTS / 'SandboxZoneEditor.py'

P1_TARGET_ROWS = [
    'Sandbox_DoorsOfDurinToElvenEntrance',
    'Sandbox_DoorsOfDurinToElvenQuarterA',
    'Sandbox_Small_BastionToCrossroads',
    'Sandbox_Small_ElvenQuarterToBastion',
    'Sandbox_Small_Mines_CToElvenQuarter',
    'Sandbox_Small_SuburbanDTOElevatorB',
]


def fp(value_list, name):
    for p in value_list or []:
        if isinstance(p, dict) and p.get('Name') == name:
            return p
    return None


def get_rowname(prop):
    if not prop:
        return None
    v = prop.get('Value')
    if isinstance(v, list):
        for it in v:
            if isinstance(it, dict) and it.get('Name') == 'RowName':
                return it.get('Value', '')
    return v


def is_null(rn):
    return rn is None or rn == '' or rn == 'None'


def apply_p1():
    print("== P1: Disable null-endpoint LayoutConnections ==")
    if not LC_BACKUP.exists():
        shutil.copyfile(LC_JSON, LC_BACKUP)
        print(f"  backup -> {LC_BACKUP.name}")
    else:
        print(f"  backup already exists -> {LC_BACKUP.name}")
    with open(LC_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    rows = data['Exports'][0]['Table']['Data']
    by_name = {r.get('Name'): r for r in rows if isinstance(r, dict)}
    disabled, already, skipped = [], [], []
    for name in P1_TARGET_ROWS:
        r = by_name.get(name)
        if not r:
            print(f"  MISSING {name}")
            continue
        origin = get_rowname(fp(r.get('Value', []), 'OriginLandmark'))
        dest = get_rowname(fp(r.get('Value', []), 'DestinationLandmark'))
        if not (is_null(origin) and is_null(dest)):
            print(f"  SKIP {name}: origin={origin!r} dest={dest!r}")
            skipped.append(name)
            continue
        es_p = fp(r.get('Value', []), 'EnabledState')
        if not es_p:
            print(f"  WARN {name}: no EnabledState property")
            continue
        if es_p.get('Value') == 'ERowEnabledState::Disabled':
            already.append(name)
            print(f"  already disabled: {name}")
            continue
        es_p['Value'] = 'ERowEnabledState::Disabled'
        disabled.append(name)
        print(f"  disabled: {name}")

    # Ensure ::Disabled is in NameMap
    nm = data.get('NameMap', [])
    if 'ERowEnabledState::Disabled' not in nm:
        nm.append('ERowEnabledState::Disabled')
        n = len(nm)
        data['NamesReferencedFromExportDataCount'] = n
        gens = data.get('Generations') or []
        if gens and isinstance(gens[0], dict):
            gens[0]['NameCount'] = n
        print(f"  added 'ERowEnabledState::Disabled' to NameMap (n={n})")

    with open(LC_JSON, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print(f"  wrote {LC_JSON.name}")
    print(f"  disabled now: {len(disabled)}; already-disabled: {len(already)}; "
          f"skipped: {len(skipped)}")
    return disabled, already, skipped


P2_NEW_METHOD = '''    def _check_connection_null_endpoints(self):
        """Live LayoutConnection rows with null/empty OriginLandmark or
        DestinationLandmark RowName. Engine FMorLayoutConnectionInstance::GetZone()
        null-derefs at routing time when it tries to resolve the missing
        endpoint landmark. Auto-fix: set EnabledState=Disabled so the
        runtime skips the row entirely (no GetZone() lookup occurs)."""
        out = []
        conns_doc = self.docs.get('connections')
        if not conns_doc:
            return out
        bad_rows = []
        for r in conns_doc.rows:
            if self._zstate(r) == 'Disabled':
                continue
            origin = self._get(r, 'OriginLandmark')
            dest = self._get(r, 'DestinationLandmark')
            o_null = origin in (None, '', 'None')
            d_null = dest in (None, '', 'None')
            if o_null or d_null:
                bad_rows.append((r, origin, dest, o_null, d_null))
        for r, origin, dest, o_null, d_null in bad_rows:
            row_name = r.get('Name')
            def make_fix(_row=r, _doc=conns_doc):
                def fix():
                    p = self._fp(_row.get('Value', []), 'EnabledState')
                    if p:
                        p['Value'] = 'ERowEnabledState::Disabled'
                    nm = _doc.data.get('NameMap', [])
                    if 'ERowEnabledState::Disabled' not in nm:
                        nm.append('ERowEnabledState::Disabled')
                        n = len(nm)
                        _doc.data['NamesReferencedFromExportDataCount'] = n
                        g = _doc.data.get('Generations') or []
                        if g and isinstance(g[0], dict):
                            g[0]['NameCount'] = n
                return fix
            out.append(Issue(
                'error', 'connection_null_endpoints', 'connections',
                f'LayoutConnection "{row_name}" has null/empty Origin or '
                f'Destination landmark — engine GetZone() will null-deref. '
                f'Disable the row or set valid endpoint landmarks. '
                f'(OriginLandmark={origin!r}, DestinationLandmark={dest!r})',
                fixer=make_fix(),
                fixer_label=f'Disable 1 null-endpoint connection(s)'))
        return out

'''


P2_HUMAN_TITLE = """    'connection_null_endpoints': (
        "LayoutConnection has null endpoints",
        "A connection row has no Origin and/or Destination landmark. The "
        "engine null-derefs in FMorLayoutConnectionInstance::GetZone() at "
        "routing time. Auto-fix disables the row so the router skips it."),
"""


def apply_p2():
    print()
    print("== P2: Add _check_connection_null_endpoints to BuildValidator ==")
    src = EDITOR.read_text(encoding='utf-8')
    changed = False

    # 1) Insert _HUMAN_TITLES entry (idempotent).
    if "'connection_null_endpoints'" in src:
        print("  human title already present")
    else:
        # Insert before 'connection_endpoint_disabled' entry.
        marker = "    'connection_endpoint_disabled': ("
        idx = src.index(marker)
        src = src[:idx] + P2_HUMAN_TITLE + src[idx:]
        changed = True
        print("  inserted _HUMAN_TITLES entry")

    # 2) Insert method into BuildValidator (idempotent).
    if 'def _check_connection_null_endpoints' in src:
        print("  method already present")
    else:
        # Insert directly before _check_connection_endpoints_live.
        marker = '    def _check_connection_endpoints_live(self):'
        idx = src.index(marker)
        src = src[:idx] + P2_NEW_METHOD + src[idx:]
        changed = True
        print("  inserted _check_connection_null_endpoints method")

    # 3) Register in CHECKS list (idempotent).
    if 'self._check_connection_null_endpoints,' in src:
        print("  CHECKS entry already present")
    else:
        marker = '            self._check_connection_endpoints_live,'
        replacement = ('            self._check_connection_null_endpoints,\n'
                       + marker)
        src = src.replace(marker, replacement, 1)
        changed = True
        print("  added to CHECKS list (before _check_connection_endpoints_live)")

    if changed:
        EDITOR.write_text(src, encoding='utf-8')
        print(f"  wrote {EDITOR.name}")
    else:
        print("  no changes needed (already applied)")


if __name__ == '__main__':
    apply_p1()
    apply_p2()
    print()
    print("APPLY DONE.")
