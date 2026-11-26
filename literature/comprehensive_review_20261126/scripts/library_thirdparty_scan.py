from library_audit import *
out=[]
for r in read('fulltext_library/license_audit.csv'):
    if r['decision']!='public_allowed' or r['format']!='pdf':continue
    doc=pymupdf.open(r['local_path'])
    for i,page in enumerate(doc):
        for line in page.get_text().splitlines():
            if re.search(r'reproduced.{0,40}permission|adapted.{0,40}permission|used with permission|all rights reserved',line,re.I):
                out.append(dict(paper_id=r['paper_id'],pdf_page=i+1,statement=line,sha256=r['sha256'],review='requires_context_review'))
csvwrite('fulltext_library/third_party_flags.csv',out)
print(json.dumps(out,ensure_ascii=False),flush=True)
