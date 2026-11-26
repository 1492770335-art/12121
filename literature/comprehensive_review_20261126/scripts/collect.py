"""Auditable collection, no credentials, no downloaded code execution. Python 3.13 + pypdf."""
import csv, json, re, time, hashlib, urllib.request, urllib.parse, concurrent.futures, threading, difflib, io, os
from pathlib import Path
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET
import tarfile, zipfile
from pypdf import PdfReader

BASE=Path(__file__).resolve().parents[1]
PRIVATE=BASE/'local_private'; PRIVATE.mkdir(exist_ok=True)
CACHE=PRIVATE/'cache'; CACHE.mkdir(exist_ok=True)
DATE='2026-11-26'; CUTOFF='2026-11-26'
LOCK=threading.Lock(); LOG=[]; ERR=[]
REQUEST_TIMEOUT=15
def stamp(): return datetime.now(timezone(timedelta(hours=8))).isoformat()
def get(url, binary=False):
    key=hashlib.sha256(url.encode()).hexdigest(); p=CACHE/key
    metadata=CACHE/(key+'.meta.json')
    if p.exists(): return p.read_bytes(),(json.loads(metadata.read_text(encoding='utf-8')).get('final_url','') if metadata.exists() else '')
    for attempt in range(2):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'LiteratureMetadataAudit/1.0 (academic bibliography collection)','Accept':'*/*'})
            with urllib.request.urlopen(req,timeout=REQUEST_TIMEOUT) as r:
                data=r.read(40*1024*1024); final=r.url
            p.write_bytes(data)
            metadata.write_text(json.dumps({'source_url':url,'final_url':final,'fetched_at':stamp()}),encoding='utf-8')
            return data,final
        except Exception as e:
            if attempt==1 or getattr(e,'code',0) in [400,401,403,404]: raise
            time.sleep(1+attempt*2)
def js(url): return json.loads(get(url)[0])
def query(db,q,hits,retrieved,notes='',included='NA'):
    with LOCK: LOG.append(dict(date=stamp(),database=db,query=q,hits=hits,retrieved=retrieved,screened=retrieved,included=included,notes=notes))
def csvwrite(name,rows,fields=None):
    rows=list(rows)
    if not fields: fields=list(dict.fromkeys(k for row in rows for k in row)) if rows else ['status']
    destination=BASE/name
    temporary=destination.with_name(destination.name+'.'+str(os.getpid())+'.tmp')
    with temporary.open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
    temporary.replace(destination)
def norm(t): return re.sub(r'[^a-z0-9]+',' ',t.lower()).strip()
def sim(a,b):
    a,b=norm(a),norm(b)
    return max(difflib.SequenceMatcher(None,a,b).ratio(),len(set(a.split())&set(b.split()))/max(1,len(set(a.split())|set(b.split()))))
def epsearch(q,n=5):
    u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode(dict(query=q,format='json',resultType='lite' if n>5 else 'core',pageSize=n))
    j=js(u); rows=j.get('resultList',{}).get('result',[]); query('Europe PMC',q,j.get('hitCount','NA'),len(rows),'API resultType='+('lite' if n>5 else 'core')+'; bounded page'); return rows
def crdoi(doi): return js('https://api.crossref.org/works/'+urllib.parse.quote(doi,safe=''))['message']
def crsearch(title):
    q=dict(query=title,rows=5)
    j=js('https://api.crossref.org/works?'+urllib.parse.urlencode(q))['message']; rows=j['items']
    query('Crossref',title,j.get('total-results','NA'),len(rows),'top 5 candidates; title/author/year screening')
    return rows
def year(m,k):
    try:return str(m[k]['date-parts'][0][0])
    except:return ''
def crrow(m,s):
    au=' and '.join((' '.join([a.get('given',''),a.get('family','')])).strip() for a in m.get('author',[]))
    return dict(paper_id=s['id'],seed_id=s['id'],authors=au,title=(m.get('title') or [''])[0],journal=(m.get('container-title') or [''])[0],year_online=year(m,'published-online'),year_issue=year(m,'published-print'),doi=m.get('DOI','').lower(),pmid='',pmcid='',arxiv='',version='published record',category=s['category'],priority=s['priority'],source_url=m.get('URL',''),abstract_url=m.get('URL',''),relevance=s['relevance'],status='metadata_verified_crossref',duplicate_of='',discovery_source='seed:'+s['id'],verification_evidence='https://api.crossref.org/works/'+m.get('DOI',''),fulltext_status='pending',supplement_status='pending',code_status='pending')
def eprow(m,s):
    ji=m.get('journalInfo',{})
    return dict(paper_id=s['id'],seed_id=s['id'],authors=m.get('authorString',''),title=m.get('title',''),journal=ji.get('journal',{}).get('title',''),year_online=m.get('firstPublicationDate','')[:4],year_issue=str(ji.get('yearOfPublication','')),doi=m.get('doi','').lower(),pmid=m.get('pmid',''),pmcid=m.get('pmcid',''),arxiv='',version='published record',category=s['category'],priority=s['priority'],source_url='https://europepmc.org/article/MED/'+m.get('id',''),abstract_url='https://europepmc.org/article/MED/'+m.get('id',''),relevance=s['relevance'],status='metadata_verified_europepmc',duplicate_of='',discovery_source='seed:'+s['id'],verification_evidence='https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:'+m.get('id','')+'&format=json',fulltext_status='pending',supplement_status='pending',code_status='pending')

TOPIC_IDS={'A13','B11','C11','D20','E16','I16','I17','K08'}
def resolve(s):
    title=s['title_or_search_phrase']; url=s.get('source_url',''); pid=s['id']
    r=dict(paper_id=pid,seed_id=pid,authors='',title=title,journal='',year_online='',year_issue='',doi='',pmid='',pmcid='',arxiv='',version='',category=s['category'],priority=s['priority'],source_url=url,abstract_url=url,relevance=s['relevance'],status='unresolved',duplicate_of='',discovery_source='seed:'+pid)
    if pid in TOPIC_IDS: r['status']='search_lead'; return r,{},{}
    if pid=='K02':r['status']='data_source_not_paper'; return r,{},{}
    cr={};ep={}
    try:
        d=re.search(r'doi.org/(10\..+)',url)
        if d: cr=crdoi(d[1]); r=crrow(cr,s)
        if 'PMC' in url:
            pm=re.search(r'PMC\d+',url).group(); hits=epsearch('EXT_ID:'+pm+' OR PMCID:'+pm); ep=next((e for e in hits if e.get('pmcid')==pm),{})
        elif 'pubmed.ncbi' in url:
            pm=re.search(r'pubmed.ncbi.nlm.nih.gov/(\d+)',url).group(1); hits=epsearch('EXT_ID:'+pm+' AND SRC:MED'); ep=hits[0] if hits else {}
        elif not cr and 'arxiv.org' not in url:
            candidates=crsearch(title+' '+s['author_hint']); scored=sorted([(sim(title,(m.get('title') or [''])[0]),m) for m in candidates],reverse=True,key=lambda x:x[0])
            best,m=scored[0] if scored else (0,{})
            (PRIVATE/(pid+'_candidates.json')).write_text(json.dumps(scored,ensure_ascii=False),encoding='utf-8')
            if best>=.83:
                # Reject matching title with incompatible named author or explicit year.
                hint=norm(s['author_hint']).split(); names=norm(' '.join(a.get('family','') for a in m.get('author',[])))
                hy=re.search(r'\b(19\d{2}|20\d{2})\b',s['author_hint']); yrs=[year(m,k) for k in ['published','published-online','published-print']]
                author_ok=hint[0] in names or hint[0] in ['authors','author']
                year_ok=not hy or any(y and abs(int(y)-int(hy[0]))<=1 for y in yrs)
                if author_ok and year_ok: cr=m;r=crrow(cr,s)
        if ep:
            r=eprow(ep,s)
            if r['doi'] and not cr:cr=crdoi(r['doi'])
        if cr:
            er=r; r=crrow(cr,s)
            if not ep:
                hits=epsearch('DOI:"'+r['doi']+'"'); ep=next((e for e in hits if e.get('doi','').lower()==r['doi']),{})
            if ep:
                for k in ['pmid','pmcid']:r[k]=ep.get(k,'')
                r['status']='metadata_crosschecked_crossref_europepmc' if sim(r['title'],ep.get('title',''))>.8 else 'metadata_conflict_review'
                r['verification_evidence']+=' ; https://europepmc.org/article/MED/'+ep.get('id','')
        if 'arxiv.org' in url:
            ar=url.rsplit('/',1)[-1]; r['arxiv']=ar
            data,final=get('https://arxiv.org/abs/'+ar)
            text=data.decode('utf-8','replace')
            def meta(n):
                mt=re.search(r'<meta\s+name="'+n+r'"\s+content="([^"]+)"',text); return mt[1] if mt else ''
            r.update(title=meta('citation_title') or title,authors=' and '.join(re.findall(r'<meta\s+name="citation_author"\s+content="([^"]+)"',text)),year_online=meta('citation_date')[:4],version='arXiv preprint; current version at retrieval',status='metadata_verified_arxiv',verification_evidence=url)
            doi=meta('citation_doi')
            if doi:
                cr=crdoi(doi); oldar=r['arxiv'];r=crrow(cr,s);r['arxiv']=oldar
    except Exception as e:r['verification_error']=str(e)
    print(pid,r['status'],r.get('doi',''),flush=True)
    return r,cr,ep

def save_state(rows,meta):
    (PRIVATE/'state.json').write_text(json.dumps({'rows':rows,'meta':meta},ensure_ascii=False),encoding='utf-8')
    csvwrite('resolved_catalog.csv',rows)
    if LOG:
        oldpath=BASE/'search_log.csv'
        old=list(csv.DictReader(oldpath.open(encoding='utf-8-sig'))) if oldpath.exists() else []
        csvwrite('search_log.csv',old+LOG)

def seeds():
    ss=list(csv.DictReader((BASE/'literature_catalog.csv').open(encoding='utf-8-sig')))
    rows=[];meta={}
    for pri in ['P0','P1','P2']:
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
            for r,cr,ep in ex.map(resolve,[s for s in ss if s['priority']==pri]):
                rows.append(r);meta[r['paper_id']]={'cr':cr,'ep':ep}
        save_state(rows,meta)
    return rows,meta

def acquire_one(r,m):
    pid=r['paper_id']; out=[]; evidence=[]; xml=None
    def record(kind,url,status='not_found',error='',**kw):
        a=dict(paper_id=pid,artifact_type=kind,version=r.get('version',''),status=status,source_url=url,final_url='',license='',license_evidence='',local_path='',repo_path='',sha256='',bytes='',pages='',fetched_at=stamp(),error=error);a.update(kw);out.append(a);return a
    def save(data,url,final,kind,name,lic='',licurl=''):
        name=re.sub(r'[^a-zA-Z0-9._-]','_',Path(name).name)
        pdf=data[:5]==b'%PDF-'; pages='';text=''
        if name.lower().endswith('.pdf') and not pdf:raise ValueError('non_PDF_response')
        if pdf:
            doc=PdfReader(io.BytesIO(data));pages=len(doc.pages);text=doc.pages[0].extract_text() or ''
            title_words=set(norm(r['title']).split()); page_words=set(norm(text[:6000]).split())
            if kind=='main' and len(title_words & page_words)/max(1,len(title_words))<.70:raise ValueError('title_first_page_requires_review')
        # Supplements remain private until their contents have been reviewed for patient-level data.
        permit=kind=='main' and bool(re.search(r'creativecommons.org/(licenses|publicdomain)/',lic+' '+licurl,re.I))
        root=BASE/'open_access' if permit else PRIVATE
        dest=root/pid/name;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        a=record(kind,url,'downloaded',version=r.get('version',''),final_url=final,license=lic or 'license_unclear',license_evidence=licurl,local_path=str(dest),repo_path=dest.relative_to(BASE).as_posix() if permit else '',sha256=hashlib.sha256(data).hexdigest(),bytes=len(data),pages=pages)
        if pdf:
            (PRIVATE/(pid+'_'+name+'.firstpage.txt')).write_text(text,encoding='utf-8')
        return a
    if not r.get('status','').startswith('metadata'):
        for k in ['main','supplement','code']:record(k,r.get('source_url',''),'unresolved','No verified paper identity')
        return out
    ep=m.get('ep',{});cr=m.get('cr',{});pmc=r.get('pmcid','');lic='';licurl=''
    if pmc and ep.get('isOpenAccess')=='Y':
        url='https://www.ebi.ac.uk/europepmc/webservices/rest/'+pmc+'/fullTextXML'
        try:
            data,final=get(url);xml=ET.fromstring(data)
            permissions=xml.find('.//article-meta/permissions')
            if permissions is not None:
                lic=' '.join(' '.join(permissions.itertext()).split());licurl=' ; '.join(v for n in permissions.iter() for k,v in n.attrib.items() if 'href' in k)
                evidence.append(dict(paper_id=pid,source_url=url,license=lic,license_evidence=licurl))
            # JATS is a full-text version, separately counted from PDF.
            save(data,url,final,'main','fulltext.xml',lic,licurl)
            for n in xml.findall('.//supplementary-material'):
                for med in n.iter():
                    href=med.attrib.get('{http://www.w3.org/1999/xlink}href','')
                    if href:
                        u=href if href.startswith('http') else 'https://pmc.ncbi.nlm.nih.gov/articles/'+pmc+'/bin/'+href
                        try:
                            d,f=get(u)
                            if d.lstrip().startswith(b'<') and not href.endswith('.xml'):raise ValueError('HTML_or_CAPTCHA_not_attachment')
                            save(d,u,f,'supplement',href,lic,licurl)
                        except Exception as e:record('supplement',u,'download_failed',str(e))
            for n in xml.findall('.//ext-link'):
                href=n.attrib.get('{http://www.w3.org/1999/xlink}href','')
                if 'github.com/' in href:record('code',href,'located_in_fulltext','Repository license/version requires separate verification')
        except Exception as e:record('main',url,'download_failed',str(e))
    urls=[]
    for x in ep.get('fullTextUrlList',{}).get('fullTextUrl',[]):
        if x.get('documentStyle')=='pdf' and x.get('availability')=='Open access':urls.append((x['url'],'published/PMC PDF'))
    if r.get('arxiv'):urls.append(('https://arxiv.org/pdf/'+r['arxiv'],'arXiv author preprint'))
    if r['paper_id']=='A03':urls.insert(0,('https://arxiv.org/pdf/2204.04052','arXiv author preprint with appendix'))
    cr_open=any('creativecommons.org/' in x.get('URL','') for x in cr.get('license',[]))
    for link in cr.get('link',[]):
        if link.get('content-type')=='application/pdf' and cr_open:urls.append((link['URL'],'publisher PDF'))
    # OpenAlex discovers lawful repositories and records provenance, never assumes OA = redistribution.
    if r.get('doi'):
        try:
            oa=m.get('oa') or js('https://api.openalex.org/works/https://doi.org/'+r['doi']);m['oa']=oa
            for loc in oa.get('locations',[]):
                if loc.get('is_oa') and loc.get('pdf_url'):urls.append((loc['pdf_url'],loc.get('version','repository version')))
        except Exception as e:record('main','https://api.openalex.org/works/https://doi.org/'+r['doi'],'discovery_failed',str(e))
    seen=set()
    for url,ver in urls:
        if url in seen:continue
        seen.add(url)
        try:
            d,f=get(url);old=r['version'];r['version']=ver
            save(d,url,f,'main','article.pdf',lic if 'pmc' in url.lower() else '',licurl if 'pmc' in url.lower() else '')
            r['version']=old;break
        except Exception as e:record('main',url,'download_failed',str(e))
    if not any(a['artifact_type']=='main' and a['status']=='downloaded' for a in out):record('main',r['source_url'],'no_oa_or_access_failed','See attempted source errors; library/author route required')
    if not any(a['artifact_type']=='supplement' for a in out):record('supplement',r['source_url'],'not_located','No separate supplement located in retrieved metadata/fulltext; publisher manual check pending')
    if not any(a['artifact_type']=='code' for a in out):record('code',r['source_url'],'not_located','No author code link located in retrieved fulltext; manual check pending')
    if evidence:
        dest=BASE/'license_evidence'/f'{pid}.json';dest.parent.mkdir(exist_ok=True);dest.write_text(json.dumps(evidence,ensure_ascii=False,indent=2),encoding='utf-8')
    print('download',pid,len([a for a in out if a['status']=='downloaded']),flush=True)
    return out

def acquire(rows,meta):
    manifest=[]
    for pri in ['P0','P1','P2']:
        todo=[r for r in rows if r['priority']==pri and not r.get('duplicate_of')]
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
            for result in ex.map(lambda r:acquire_one(r,meta.get(r['paper_id'],{})),todo):manifest.extend(result)
        csvwrite('download_manifest.csv',manifest);save_state(rows,meta)
    return manifest

if __name__=='__main__':
    seeds()
