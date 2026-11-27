"""Targeted legal source discovery; no login, CAPTCHA or paywall bypass."""
from library_audit import *
from html.parser import HTMLParser
import urllib.parse,zipfile,io,collect
collect.REQUEST_TIMEOUT=12

SOURCES=[
('D01','main','https://academic.oup.com/biomet/article-pdf/94/3/735/734053/asm059.pdf'),
('D02','main','https://doi.org/10.1093/biomet/asn044'),
('D04','main','https://www.sciencedirect.com/science/article/pii/S0167947316300287'),
('D04','institution','https://scholar2.pusan.ac.kr/en/resources?q=Covariate-adjusted%20quantile%20inference'),
('D01','scholar_all_versions_discovery','https://scholar.google.com/scholar?q=%22Nonparametric+quantile+inference+with+competing+risks+data%22'),
('D04','scholar_all_versions_discovery','https://scholar.google.com/scholar?q=%22Covariate-adjusted+quantile+inference+with+competing+risks%22'),
('D01','author','https://web1.sph.emory.edu/users/lpeng/'),
('D03','author','https://web1.sph.emory.edu/users/lpeng/papers.htm'),
('B01','landing','https://pmc.ncbi.nlm.nih.gov/articles/PMC6223317/'),
('B02','landing','https://pmc.ncbi.nlm.nih.gov/articles/PMC6449186/'),
('B02','author','https://wxiao0421.github.io/publication/'),
('A01','landing','https://pmc.ncbi.nlm.nih.gov/articles/PMC8036005/'),
('C01','landing','https://pmc.ncbi.nlm.nih.gov/articles/PMC6051551/'),
('C03','landing','https://pmc.ncbi.nlm.nih.gov/articles/PMC3954452/'),
('I03','main','https://pmc.ncbi.nlm.nih.gov/articles/PMC5462897/pdf/nihms827798.pdf'),
('I03','supplement','https://pmc.ncbi.nlm.nih.gov/articles/instance/5462897/bin/NIHMS827798-supplement-supplement_material.pdf'),
('I03','supplement','https://onlinelibrary.wiley.com/doi/suppl/10.1111/biom.12627/supinfo/biom12627-sup-0001-SuppData-S1.pdf'),
('K01','main','https://pmc.ncbi.nlm.nih.gov/articles/PMC8015679/pdf/nihms-1645413.pdf'),
('K01','main','https://escholarship.org/content/qt16b6s7jx/qt16b6s7jx.pdf'),
('N95df3c95c9','main','https://pmc.ncbi.nlm.nih.gov/articles/PMC9038055/pdf/CJAS_47_1631267.pdf'),
('N95df3c95c9','supplement','https://pmc.ncbi.nlm.nih.gov/articles/instance/9038055/bin/CJAS_A_1631267_SM1057.pdf'),
('N83defe8bc4','landing','https://pmc.ncbi.nlm.nih.gov/articles/PMC6156950/'),
('D05','main','https://www.annualreviews.org/doi/pdf/10.1146/annurev-statistics-042720-020233'),
]

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,t,attrs):
        d=dict(attrs)
        if t=='a' and d.get('href'):self.links.append(d['href'])

def one(x):
    pid,kind,u=x;a=dict(paper_id=pid,artifact_type=kind,source_url=u,final_url='',status='',sha256='',bytes='',pdf_pages='',local_path='',error='',fetched_at=stamp(),discovered_links=[])
    try:
        data,final=get(u);a.update(final_url=final,bytes=len(data))
        h=hashlib.sha256(data).hexdigest()
        if data.startswith(b'%PDF-'):
            doc=pymupdf.open(stream=data,filetype='pdf');text='\n'.join(doc[i].get_text() for i in range(min(3,len(doc))))
            if len(text.strip())<100:raise ValueError('PDF_identity_not_confirmed')
            if pid in CAT and kind=='main':
                title=set(re.findall('[a-z]+',CAT[pid]['title'].lower()));observed=set(re.findall('[a-z]+',text.lower()))
                if len(title&observed)/len(title)<.65:raise ValueError('PDF_title_mismatch')
            if h in EXISTING:
                a.update(status='existing_local_reused',local_path=EXISTING[h],sha256=h,pdf_pages=len(doc));return a
            out=PRIVATE/'sync_acquired'/pid;out.mkdir(parents=True,exist_ok=True);p=out/(kind+'_'+h[:12]+'.pdf');p.write_bytes(data)
            a.update(status='downloaded_pdf',sha256=h,local_path=str(p),pdf_pages=len(doc),first_page=text[:800])
        elif data.startswith(b'PK\x03\x04'):
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                if z.testzip():raise ValueError('zip_crc_error')
                members=z.namelist()
            out=PRIVATE/'sync_acquired'/pid;out.mkdir(parents=True,exist_ok=True);p=out/(kind+'_'+h[:12]+'.zip');p.write_bytes(data)
            a.update(status='downloaded_zip_not_executed',sha256=h,local_path=str(p),archive_members=members)
        else:
            html=data.decode('utf-8','replace');lower=html.lower()
            if any(s in lower for s in ['recaptcha','checking your browser','verify you are human','unusual traffic','<title>verifying','pow_challenge','cloudpmc-viewer-pow']):a.update(status='captcha_or_verification_page',error='no_access_bypass_attempted')
            else:
                links=Links();links.feed(html);urls=[urllib.parse.urljoin(final or u,s) for s in links.links]
                a['discovered_links']=list(dict.fromkeys(s for s in urls if any(k in s.lower() for k in ['supp','/bin/','.pdf','.zip'])))[:30]
                a.update(status='landing_page_only' if a['discovered_links'] else 'no_fulltext_link_found',error='Not a PDF; not counted as acquired fulltext')
    except Exception as e:a.update(status='failed',error=str(e)[:300])
    print(pid,kind,a['status'],a['error'],flush=True);return a

def run():
    global EXISTING
    inv=json.loads((WORK/'sync_inventory_unique.json').read_text(encoding='utf-8'));EXISTING={a['sha256']:a['local_path'] for a in inv if a['format']=='pdf'}
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows=list(ex.map(one,SOURCES))
    seen={x[2] for x in SOURCES};extra=[]
    for a in rows:
        for u in a['discovered_links']:
            host=urllib.parse.urlparse(u).netloc
            if u in seen or not any(s in host for s in ['ncbi.nlm.nih.gov','wiley.com','wxiao0421.github.io','oup.com']):continue
            # Only actual file links. No link/query grids or downloads from unrelated references.
            if not re.search(r'\.(pdf|zip)(?:[?#]|$)',u,re.I):continue
            if 'wxiao0421.github.io' in host and 'Xiao16RobustA.pdf' not in u:continue
            kind='supplement' if any(k in u.lower() for k in ['supp','/bin/','sm.','sm_']) else 'main'
            extra.append((a['paper_id'],kind,u));seen.add(u)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:rows+=list(ex.map(one,extra))
    (WORK/'sync_acquisition_private.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(dict(attempts=len(rows),statuses=dict(__import__('collections').Counter(a['status'] for a in rows))),ensure_ascii=False))

if __name__=='__main__':run()
