"""Export an exact allowlist for connector-based GitHub publication."""
from library_audit import *
def run():
    validation=json.loads((ROOT/'validation.json').read_text(encoding='utf-8'))
    if validation['errors']:raise ValueError('Validation errors remain')
    paths=[p for p in ROOT.rglob('*') if p.is_file()]+list((BASE/'scripts').glob('library_*.py'))+[BASE/'README.md']
    out=[]
    for p in sorted(set(paths)):
        d=p.read_bytes();text=False
        if p.suffix.lower()!='.pdf':
            try:d.decode('utf-8');text=True
            except UnicodeDecodeError:pass
        out.append(dict(path=p.relative_to(BASE.parent.parent).as_posix(),size=len(d),sha256=hashlib.sha256(d).hexdigest(),git_sha=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest(),kind='text' if text else 'binary'))
    (WORK/'publish_manifest.json').write_text(json.dumps(out,ensure_ascii=False),encoding='utf-8')
    print(json.dumps(dict(files=len(out),bytes=sum(x['size'] for x in out),binary_files=sum(x['kind']=='binary' for x in out),largest=sorted([(x['size'],x['path']) for x in out],reverse=True)[:5]),ensure_ascii=False),flush=True)
if __name__=='__main__':run()
