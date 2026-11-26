from collect import *
def run():
    sources=[('E02','https://projecteuclid.org/journals/annales-de-linstitut-henri-poincare-probabilites-et-statistiques/volume-56/issue-3/Performance-guarantees-for-policy-learning/10.1214/19-AIHP1034.pdf','Performance guarantees for policy learning','journal PDF, 2020'),('E02','https://arxiv.org/pdf/1704.06431','Faster Rates for Policy Learning','2017 preprint; alternative title linked from https://alexluedtke.com/research/'),('D01','https://academic.oup.com/biomet/article-pdf/94/3/735/734053/asm059.pdf','Nonparametric quantile inference with competing risks data','journal PDF, 2007')]
    out=[]
    for pid,url,title,version in sources:
        a=dict(paper_id=pid,artifact_type='main',version=version,status='',source_url=url,final_url='',license='license_unclear',license_evidence='',local_path='',repo_path='',sha256='',bytes='',pages='',fetched_at=stamp(),error='')
        try:
            d,f=get(url)
            if d[:5]!=b'%PDF-':raise ValueError('non_PDF_response')
            doc=PdfReader(io.BytesIO(d));text=doc.pages[0].extract_text() or '';words=set(norm(title).split())
            if len(words & set(norm(text).split()))/max(1,len(words))<.7:raise ValueError('title mismatch')
            p=PRIVATE/pid/('followup_'+hashlib.sha256(url.encode()).hexdigest()[:8]+'.pdf');p.parent.mkdir(exist_ok=True);p.write_bytes(d)
            a.update(status='downloaded',final_url=f,local_path=str(p),sha256=hashlib.sha256(d).hexdigest(),bytes=len(d),pages=len(doc.pages))
        except Exception as e:a.update(status='download_failed',error=str(e))
        out.append(a)
    csvwrite('core_followup_manifest.csv',out)
if __name__=='__main__':run()
