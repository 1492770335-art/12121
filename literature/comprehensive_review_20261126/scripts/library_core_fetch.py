"""Targeted official/author/institutional retrieval; no access-control bypass."""
from library_audit import *
import collect
collect.REQUEST_TIMEOUT=12
SOURCES=[
 ('C01','https://www.columbia.edu/~yw2016/benefitriskJASA.pdf','main','author-hosted accepted author version'),
 ('G02','https://web.stanford.edu/~lutian/coursepdf/cox1972paper.pdf','main','institution-hosted journal reprint with discussion'),
 ('G08','https://ishwaran.org/papers/IGKMGL.biostatistics2014.pdf','main','author-hosted journal PDF'),
 ('K01','https://escholarship.org/content/qt16b6s7jx/qt16b6s7jx.pdf','main','institutional repository PDF'),
 ('D05','https://www.annualreviews.org/doi/pdf/10.1146/annurev-statistics-042720-020233','main','official journal PDF'),
 ('D01','https://academic.oup.com/biomet/article-pdf/94/3/735/734053/asm059.pdf','main','official journal PDF'),
 ('G01',CAT['G01']['source_url'],'main','Copenhagen institutional preprint 1977'),
 ('I03','https://onlinelibrary.wiley.com/doi/pdf/10.1111/biom.12627','main','official journal PDF'),
 ('I03','https://onlinelibrary.wiley.com/doi/suppl/10.1111/biom.12627/supinfo/biom12627-sup-0001-SuppData-S1.pdf','supplement','official journal supplementary PDF'),
 ('G08','https://ishwaran.org/papers/IGKMGL.biostatistics2014supp.pdf','supplement','author-hosted supplement linked from publications page'),
 ('D04','https://www.sciencedirect.com/science/article/abs/pii/S0167947316300287','main','official publisher landing page; PDF availability probe'),
]
def one(x):
    pid,u,kind,version=x
    a=dict(paper_id=pid,artifact_type=kind,version=version,status='',source_url=u,final_url='',license='',license_evidence='',local_path='',repo_path='',sha256='',bytes='',pages='',fetched_at=stamp(),error='')
    try:
        d,f=get(u)
        if not d.startswith(b'%PDF-'):raise ValueError('non_PDF_or_verification_page')
        doc=pymupdf.open(stream=d,filetype='pdf');t=' '.join(p.get_text() for p in list(doc)[:3])
        words=set(norm(CAT[pid]['title']).split())
        if kind=='main' and len(words & set(norm(t).split()))/max(1,len(words))<.7:raise ValueError('identity_not_confirmed_from_opening_pages')
        folder=PRIVATE/'library_new'/pid;folder.mkdir(parents=True,exist_ok=True);p=folder/(kind+'_'+hashlib.sha256(u.encode()).hexdigest()[:8]+'.pdf');p.write_bytes(d)
        a.update(status='downloaded',final_url=f,local_path=str(p),sha256=hashlib.sha256(d).hexdigest(),bytes=len(d),pages=len(doc))
    except Exception as e:a.update(status='download_failed',error=str(e))
    print('core fetch',pid,kind,a['status'],a['error'],flush=True);return a
def run():
    seen={u for _,u,_,_ in SOURCES}
    state=json.loads((PRIVATE/'state.json').read_text(encoding='utf-8'))
    for pid in CORE:
        for link in state.get('meta',{}).get(pid,{}).get('cr',{}).get('link',[]):
            u=link.get('URL','')
            if (link.get('content-type')=='application/pdf' or '.pdf' in u.lower() or '/doi/pdf/' in u.lower()) and u not in seen:
                SOURCES.append((pid,u,'main','publisher PDF link from verified Crossref record'));seen.add(u)
    rows=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        for a in ex.map(one,SOURCES):rows.append(a)
    csvwrite('fulltext_library/core_acquisition_attempts.csv',rows)
    audited=[audit_one(a) for a in rows if a['status']=='downloaded']
    csvwrite('fulltext_library/new_artifact_audit.csv',audited)
if __name__=='__main__':run()
