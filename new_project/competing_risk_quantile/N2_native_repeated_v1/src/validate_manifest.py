#!/usr/bin/env python3
"""Validate fresh generator outputs against a SHA256 manifest frozen before fitting."""
import argparse
from pathlib import Path
import json, hashlib

p=argparse.ArgumentParser()
p.add_argument('--data',type=Path,required=True)
p.add_argument('--freeze',type=Path,required=True)
a=p.parse_args()
m=json.loads((a.data/'manifest.json').read_text())
f=json.loads(a.freeze.read_text())
assert m['seed']==f['seed'] and m['nreps']==f['nreps'] and m['p1']==f['p1'] and m['pall']==f['pall']
assert len(m['files'])==len(f['files'])==36
for fn,hexdigest in f['files'].items():
    file=a.data/fn
    observed=hashlib.sha256(file.read_bytes()).hexdigest()
    if observed!=hexdigest:raise AssertionError(f'hash mismatch in {fn}: {observed} != {hexdigest}')
print(f'PASS {len(f["files"])} frozen CSV SHA256 checks and fixed design metadata')
