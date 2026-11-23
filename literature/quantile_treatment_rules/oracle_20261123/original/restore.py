"""Restore original Oracle simulation ZIP from byte-exact Git blobs."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parent
NAME = 'Oracle_竞争风险决策_20261123_结果包.zip'
PART_SIZE = 524288
EXPECTED_SIZE = 3875284
EXPECTED_SHA256 = '4700ea52b9a50c0d96786965ad4fe13e30b0b40952292bc396700699c34a06b7'

parts = [ROOT / f'oracle-result.part{i:02d}' for i in range(1, 9)]
if not all(p.is_file() for p in parts):
    raise SystemExit('Missing one or more oracle-result.partNN files')
sha = hashlib.sha256()
total = 0
output = ROOT / NAME
with output.open('wb') as f:
    for n, path in enumerate(parts, 1):
        data = path.read_bytes()
        expected = PART_SIZE if n < 8 else EXPECTED_SIZE - 7 * PART_SIZE
        if len(data) != expected:
            raise ValueError(f'{path.name}: expected {expected} bytes; got {len(data)}')
        f.write(data)
        sha.update(data)
        total += len(data)
if total != EXPECTED_SIZE or sha.hexdigest() != EXPECTED_SHA256:
    output.unlink(missing_ok=True)
    raise ValueError('Size or SHA256 mismatch; restored ZIP removed')
print(f'PASS {output} ({total} bytes, SHA256={sha.hexdigest()})')
