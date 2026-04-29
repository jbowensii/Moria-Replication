"""Re-run audit; assert Rule A all-zero-delta and Rule B all-in-range."""
from _global_bp_audit import main

result = main()
print()
print('=== VERIFICATION ===')
bad_a = [x for x in result['rule_a'] if x[3] != x[4]]  # bp != proposed (=zone pos)
bad_b = [x for x in result['rule_b'] if not x[5]]
print(f'Rule A mismatches: {len(bad_a)}')
for z, pos, lm, bp, prop, delta in bad_a:
    print(f'  FAIL {z} {lm} BP={bp} expected={prop}')
print(f'Rule B out-of-range: {len(bad_b)}')
for z, pos, ts, lm, bp, ir, prop in bad_b:
    print(f'  FAIL {z} {lm} BP={bp} pos={pos} ts={ts}')
if not bad_a and not bad_b:
    print('ALL CLEAN')
