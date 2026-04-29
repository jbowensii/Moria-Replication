"""Byte-level audit: every working *.json vs its *.original.json.

Run after any edit to confirm what state files are in.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent


def deep_equal(a, b, path=''):
    diffs = []
    if type(a) != type(b):
        diffs.append((path, f'TYPE: {type(a).__name__} vs {type(b).__name__}'))
        return diffs
    if isinstance(a, dict):
        for k in set(a) ^ set(b):
            diffs.append((f'{path}.{k}', 'KEY DIFF'))
        for k in set(a) & set(b):
            diffs.extend(deep_equal(a[k], b[k], f'{path}.{k}'))
    elif isinstance(a, list):
        if len(a) != len(b):
            return [(path, f'LEN: {len(a)} vs {len(b)}')]
        for i, (x, y) in enumerate(zip(a, b)):
            diffs.extend(deep_equal(x, y, f'{path}[{i}]'))
    else:
        if a != b:
            diffs.append((path, f'VAL: {a!r} vs {b!r}'))
    return diffs


def main():
    print(f'{"File":<42s}  {"Status":<10s}  {"Diffs":>6s}  Notes')
    print('-' * 110)
    pristine = 0
    deviates = 0
    for op in sorted(HERE.glob('*.original.json')):
        cur_path = HERE / op.name.replace('.original.json', '.json')
        if not cur_path.exists():
            print(f'  {cur_path.name:<40s}  MISSING')
            continue
        pri = json.loads(op.read_text(encoding='utf-8'))
        cur = json.loads(cur_path.read_text(encoding='utf-8'))
        diffs = deep_equal(cur, pri)
        if not diffs:
            pristine += 1
            print(f'  {cur_path.name:<40s}  PRISTINE   {0:>6d}')
        else:
            deviates += 1
            notes = '; '.join(f'{p}={m}' for p, m in diffs[:3])
            if len(diffs) > 3:
                notes += f' +{len(diffs)-3} more'
            print(f'  {cur_path.name:<40s}  DEVIATES   {len(diffs):>6d}  {notes[:70]}')

    print()
    print(f'PRISTINE: {pristine}    DEVIATES: {deviates}')

    no_baseline = []
    for f in sorted(HERE.glob('*.json')):
        if f.name.endswith('.original.json'):
            continue
        if not f.name.startswith(('DT_', 'World', 'BB_', 'BC_', 'BF_')):
            continue
        op = HERE / f.name.replace('.json', '.original.json')
        if not op.exists():
            no_baseline.append(f.name)
    if no_baseline:
        print()
        print('No pristine baseline (cannot verify):')
        for n in no_baseline:
            print(f'  {n}')


if __name__ == '__main__':
    main()
