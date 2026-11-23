#!/usr/bin/env python3
"""Verify bytewise frozen files before any native fit."""
from __future__ import annotations
import argparse,hashlib,json
from pathlib import Path

def main():
  a=argparse.ArgumentParser();a.add_argument('--data',type=Path,required=True);a.add_argument('--frozen',type=Path,required=True)
  v=a.parse_args();observed=json.loads((v.data/'manifest.json').read_text());target=json.loads(v.frozen.read_text())
  for k in ('seed','ntrains','nreps','mechanisms','p_grid','horizon','files'):
    if observed[k]!=target[k]:raise AssertionError(f'manifest field differs: {k}')
  if len(target['files'])!=120:raise AssertionError('wrong number of datasets')
  for name,digest in target['files'].items():
    computed=hashlib.sha256((v.data/name).read_bytes()).hexdigest()
    if computed!=digest:raise AssertionError(f'{name} hash mismatch')
  print('PASS 120 frozen training/test CSV hashes; all design keys match')
if __name__=='__main__':main()
