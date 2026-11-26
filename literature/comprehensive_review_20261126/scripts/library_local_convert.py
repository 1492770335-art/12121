"""Create private page-organized renditions for restricted originals; never publish text."""
from library_build import pdf_transcript
from library_audit import *
import shutil
def run():
    rows=read('fulltext_library/license_audit.csv')+read('fulltext_library/new_artifact_audit.csv');out=[];done={}
    for a in rows:
        if a['decision']!='local_only' or a['format']!='pdf':continue
        h=a['sha256'];pid=a['paper_id'];dest=PRIVATE/'fulltext_library_local'/a['category']/pid/h[:12]
        if h in done:dest=done[h]
        else:
            dest.mkdir(parents=True,exist_ok=True);original=dest/'original.pdf'
            if not original.exists():shutil.copyfile(a['local_path'],original)
            if not (dest/'page_map.json').exists():pdf_transcript(a,dest)
            done[h]=dest
        out.append(dict(paper_id=pid,artifact_type=a['artifact_type'],sha256=h,pdf_pages=a['pdf_pages'],status='private_pdf_markdown_txt',local_directory=str(dest),reason=a['reason']))
        if len(out)%20==0:print('private conversions',len(out),flush=True)
    csvwrite('fulltext_library/local_conversion_manifest.csv',out)
    print('private conversions complete',len(out),'unique files',len(done),flush=True)
if __name__=='__main__':run()
