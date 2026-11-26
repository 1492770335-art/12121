from collect import *

def run():
    state=json.loads((PRIVATE/'state.json').read_text(encoding='utf-8'));rs={r['paper_id']:r for r in state['rows']};out=[]
    urls=[('G01',rs['G01']['source_url'],'institutional preprint, 1977'),('I05','https://sites.stat.washington.edu/raftery/Research/PDF/Gneiting2007jasa.pdf','author-hosted journal article'),('E09','https://discovery.ucl.ac.uk/id/eprint/1522145/1/Kitagawa_Who_should_be_treated_Working-paper_May17.pdf','author working paper May 2017'),('B08','https://web.mit.edu/14.387/www/IV_Model.pdf','author manuscript')]
    # Reuse validated acquisition handler with an explicit author/official PDF source.
    for pid,url,version in urls:
        r=rs[pid].copy();r['version']=version
        try:
            d,f=get(url)
            if d[:5]!=b'%PDF-':raise ValueError('non_PDF_response')
            doc=PdfReader(io.BytesIO(d));text=doc.pages[0].extract_text() or '';words=set(norm(r['title']).split());coverage=len(words & set(norm(text).split()))/max(1,len(words))
            if coverage<.7:raise ValueError('title mismatch')
            p=PRIVATE/pid/'extra_article.pdf';p.parent.mkdir(exist_ok=True);p.write_bytes(d)
            out.append(dict(paper_id=pid,artifact_type='main',version=version,status='downloaded',source_url=url,final_url=f,license='license_unclear',license_evidence='',local_path=str(p),repo_path='',sha256=hashlib.sha256(d).hexdigest(),bytes=len(d),pages=len(doc.pages),fetched_at=stamp(),error=''))
        except Exception as e:out.append(dict(paper_id=pid,artifact_type='main',version=version,status='download_failed',source_url=url,error=str(e)))
    # Verified primary source for an added competitor, independently found by web search.
    s=dict(id='Nmanual8117077',category='A',priority='P1',relevance='Competing risk ITR with doubly robust OWL and bi-level selection; web expansion from A01')
    csvwrite('extra_manifest.csv',out)
    try:
        hits=epsearch('EXT_ID:33994608 AND SRC:MED');ep=hits[0] if hits else {}
    except Exception as e:
        ep={'doi':'10.1016/j.csda.2021.107167','pmid':'33994608','pmcid':'PMC8117077'}
        query('Europe PMC','EXT_ID:33994608 AND SRC:MED','NA',0,str(e)+'; DOI verified separately against primary PMC page')
    if ep:
        cr=crdoi(ep['doi']);r=crrow(cr,s);r.update(pmid=ep.get('pmid',''),pmcid=ep.get('pmcid',''),seed_id='A01',discovery_source='web_primary_search; https://pmc.ncbi.nlm.nih.gov/articles/PMC8117077/')
        if not any(x.get('doi')==r['doi'] for x in state['rows']):state['rows'].append(r);state['meta'][s['id']]={'cr':cr,'ep':ep}
        out.extend(acquire_one(r,dict(cr=cr,ep=ep)))
    csvwrite('extra_manifest.csv',out);save_state(state['rows'],state['meta']);csvwrite('search_log_manual.csv',LOG)
    print('extra sources',len(out),flush=True)
if __name__=='__main__':run()
