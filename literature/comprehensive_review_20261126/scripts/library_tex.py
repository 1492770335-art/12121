"""Fetch licensed, version-pinned arXiv TeX. Never compile or execute sources."""
from library_audit import *
import gzip

def run():
    audit=read('fulltext_library/license_audit.csv');todo={r['arxiv_id']:r for r in audit if r['decision']=='public_allowed' and r['arxiv_id']};out=[]
    previous={r['arxiv_id']:r for r in read('fulltext_library/latex_acquisition.csv')} if (ROOT/'latex_acquisition.csv').exists() else {}
    for aid,r in todo.items():
        if aid in previous:
            out.append(previous[aid]);continue
        row=dict(arxiv_id=aid,paper_id=r['paper_id'],source_url='https://arxiv.org/src/'+aid,status='',license_url=r['license_url'],license_evidence_url=r['license_evidence_url'],archive_sha256='',local_archive='',tex_files=0,error='',fetched_at=stamp())
        try:
            # Source endpoint appears on the official abstract page; pin the PDF's version.
            d,final=get(row['source_url']);row['final_url']=final
            archive=WORK/('arxiv_'+aid+'.source');archive.write_bytes(d);row.update(archive_sha256=hashlib.sha256(d).hexdigest(),local_archive=str(archive))
            dest=WORK/'tex'/aid;dest.mkdir(parents=True,exist_ok=True);files=[]
            def put(name,data):
                rel=Path(name)
                if rel.is_absolute() or '..' in rel.parts or ':' in name or '\\' in name:raise ValueError('unsafe source member path')
                if rel.suffix.lower()!='.tex':return
                target=dest/rel;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
                files.append(dict(path=rel.as_posix(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
            if d.startswith(b'%PDF-'):raise ValueError('source_is_pdf_no_tex')
            raw=d
            if d.startswith(b'\x1f\x8b'):
                raw=gzip.GzipFile(fileobj=io.BytesIO(d)).read(40*1024*1024)
                if len(raw)>=40*1024*1024:raise ValueError('decompressed_source_too_large')
            try:
                with tarfile.open(fileobj=io.BytesIO(raw)) as tf:
                    for member in tf.getmembers():
                        if member.isfile() and member.name.lower().endswith('.tex'):
                            if member.size>8*1024*1024:raise ValueError('tex_member_too_large')
                            put(member.name,tf.extractfile(member).read())
            except tarfile.ReadError:
                if b'\\documentclass' in raw or b'\\begin{document}' in raw:put('source.tex',raw)
                else:raise ValueError('not_tex_or_source_archive')
            row.update(status='downloaded_original_tex' if files else 'no_tex_members',tex_files=len(files))
            (dest/'source_manifest.json').write_text(json.dumps(dict(arxiv_id=aid,license=r['license_url'],source_url=row['source_url'],archive_sha256=row['archive_sha256'],files=files,notes='Original .tex bytes only; no compilation, no formula rewriting. Third-party styles, figures and data omitted from public source subset.'),ensure_ascii=False,indent=2),encoding='utf-8')
        except Exception as e:row.update(status='not_acquired',error=str(e))
        out.append(row);csvwrite('fulltext_library/latex_acquisition.csv',out);print('tex',aid,row['status'],row['tex_files'],flush=True)
        time.sleep(1)
if __name__=='__main__':run()
