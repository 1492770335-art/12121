"""Validate actual artifact identity and integrity, not just file extensions."""
from collect import *
import bibtexparser
def run():
    rows=list(csv.DictReader((BASE/'resolved_catalog.csv').open(encoding='utf-8-sig')));manifest=list(csv.DictReader((BASE/'download_manifest.csv').open(encoding='utf-8-sig')));errors=[];checked=0;public=[]
    ids={r['paper_id']:r for r in rows};dois={}
    for r in rows:
        d=r.get('doi','')
        if d and not r.get('duplicate_of'):
            if d in dois:errors.append('duplicate DOI: '+d)
            dois[d]=r['paper_id']
    for a in manifest:
        if a['status'] not in ['downloaded','existing_local_verified']:continue
        p=Path(a['local_path'])
        if not p.is_file():errors.append('missing '+str(p));continue
        data=p.read_bytes();checked+=1
        if hashlib.sha256(data).hexdigest()!=a['sha256']:errors.append('hash mismatch '+str(p))
        if len(data)!=int(a['bytes']):errors.append('size mismatch '+str(p))
        if p.suffix.lower()=='.pdf':
            if not data.startswith(b'%PDF-'):errors.append('not PDF '+str(p));continue
            doc=PdfReader(io.BytesIO(data))
            if len(doc.pages)!=int(a['pages']):errors.append('page count mismatch '+str(p))
        if a.get('repo_path'):
            rp=Path(a['repo_path'])
            if not rp.as_posix().startswith('open_access/'):errors.append('public path outside allowlist '+str(rp))
            if not re.search(r'creativecommons.org/(licenses|publicdomain)/',a.get('license_evidence','')+' '+a.get('license','')):errors.append('missing redistribution evidence '+str(rp))
            if not (BASE/rp).is_file():errors.append('missing repo file '+str(rp))
            public.append(rp.as_posix())
    bib=(BASE/'references.bib').read_text(encoding='utf-8');keys=re.findall(r'^@\w+\{([^,]+),',bib,re.M)
    parsed=bibtexparser.parse_string(bib)
    if len(parsed.entries)!=len(keys):errors.append('BibTeX parser entry count mismatch')
    if len(keys)!=len(set(keys)):errors.append('duplicate BibTeX keys')
    for k in keys:
        if k not in ids or not ids[k]['status'].startswith('metadata') or ids[k].get('duplicate_of'):errors.append('unverified BibTeX key '+k)
    result=dict(checked_at=stamp(),catalog_records=len(rows),bibtex_entries=len(keys),artifact_records_checked=checked,public_paths=sorted(set(public)),errors=errors)
    (BASE/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False),flush=True)
    if errors:raise SystemExit(1)
if __name__=='__main__':run()
