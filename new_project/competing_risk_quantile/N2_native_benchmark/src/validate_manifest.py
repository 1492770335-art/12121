#!/usr/bin/env python3
"""Validate SHA256 of generator outputs frozen before the native fits."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
expected=json.loads((root/'FROZEN_SHA256.json').read_text())
for name,hash_value in expected.items():
    target=root/'data'/name
    if not target.exists():raise FileNotFoundError(target)
    actual=hashlib.sha256(target.read_bytes()).hexdigest()
    if actual!=hash_value:raise ValueError(f'mismatched {name}: {actual} != {hash_value}')
print('PASS all 9 deterministic data files exactly match pre-fit SHA256 manifest')
