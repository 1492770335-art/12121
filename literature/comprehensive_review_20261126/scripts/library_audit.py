"""Version-specific redistribution audit. No OA-to-permission inference."""
from collect import *
import pymupdf, html

WORK=PRIVATE/'fulltext_library_work';WORK.mkdir(exist_ok=True)
ROOT=BASE/'fulltext_library';ROOT.mkdir(exist_ok=True)
CORE=['A01','B01','C01','D01','D02','D04','D05','G01','G02','G04','G08','I03','K01']
def read(name):return list(csv.DictReader((BASE/name).open(encoding='utf-8-sig')))
CAT={r['paper_id']:r for r in read('resolved_catalog.csv')}

def cc_url(text):
    found=re.findall(r'https?://(?:www\.)?creativecommons\.org/(?:licenses/[a-z-]+/[\d.]+|publicdomain/(?:zero|mark)/[\d.]+)/?',html.unescape(text),re.I)
    return found[0].rstrip('/')+'/' if found else ''

def inventory():
    records={}
    for a in read('download_manifest.csv'):
        if a['status'] not in ['downloaded','existing_local_verified'] or a['artifact_type'] not in ['main','supplement']:continue
        p=Path(a['local_path'])
        if not p.is_file():continue
        key=(a['paper_id'],a['sha256'])
        if key not in records:records[key]=dict(a)
    return list(records.values())

def audit_one(a):
    pid=a['paper_id'];p=Path(a['local_path']);data=p.read_bytes();sha=hashlib.sha256(data).hexdigest()
    row=dict(paper_id=pid,category=CAT.get(pid,{}).get('category','unknown'),artifact_type=a['artifact_type'],sha256=sha,source_url=a['source_url'],original_version=a['version'],local_path=str(p),bytes=len(data),pdf_pages='',arxiv_id='',license_url='',license_evidence_url='',license_evidence_quote='',decision='local_only',reason='license_not_confirmed',checked_at=stamp(),format=p.suffix.lower().lstrip('.'))
    if sha!=a['sha256']:row.update(reason='hash_mismatch');return row
    text='';links=[]
    if data.startswith(b'%PDF-'):
        doc=pymupdf.open(p);row['pdf_pages']=len(doc)
        parts=[]
        for page in doc:
            parts.append(page.get_text())
            links.extend(l.get('uri','') for l in page.get_links() if l.get('uri'))
        text='\n'.join(parts);(WORK/(sha+'.txt')).write_text(text,encoding='utf-8')
        # Never infer identity from an arXiv citation in the reference list.
        firstpage=doc[0].get_text()
        stamp_match=re.search(r'arXiv\s*:?\s*(\d{4}\.\d{4,5})(v\d+)',firstpage,re.I)
        source_match=re.search(r'arxiv\.org/(?:pdf|abs)/(\d{4}\.\d{4,5})(v\d+)?',a['source_url'])
        if source_match:
            row['arxiv_id']=source_match[1]+(source_match[2] or '')
            if stamp_match and stamp_match[1]==source_match[1]:row['arxiv_id']=stamp_match[1]+stamp_match[2]
        elif stamp_match:row['arxiv_id']=stamp_match[1]+stamp_match[2]
        # A license printed in this very file is direct evidence. URLs may be PDF annotations.
        license_text=text+'\n'+'\n'.join(links)
        cc=cc_url(license_text)
        if cc and ('creative commons' in text.lower() or 'cc-by' in text.lower() or 'cc by' in text.lower()):
            row.update(license_url=cc,license_evidence_url=a['source_url'],license_evidence_quote='License statement and URL present in the original PDF; inspect page location in evidence file',decision='public_allowed',reason='license_printed_in_original_pdf')
            loc=[dict(pdf_page=i+1,lines='\n'.join(line for line in page.get_text().splitlines() if any(w in line.lower() for w in ['creative commons','cc-by','cc by','license:','creativecommons']))) for i,page in enumerate(doc) if any(w in page.get_text().lower() for w in ['creative commons','cc-by','cc by','creativecommons'])]
            (WORK/(sha+'.pdf_license.json')).write_text(json.dumps(loc,ensure_ascii=False,indent=2),encoding='utf-8')
    elif p.suffix.lower()=='.xml':
        try:
            root=ET.fromstring(data);per=root.find('.//article-meta/permissions')
            if per is not None:
                raw=ET.tostring(per,encoding='unicode');cc=cc_url(raw)
                if cc:row.update(license_url=cc,license_evidence_url=a['source_url'],license_evidence_quote=' '.join(per.itertext()).strip(),decision='public_allowed',reason='license_in_original_jats_permissions')
        except Exception as e:row['reason']='xml_parse_error:'+str(e)
    else:row['reason']='unsupported_format'
    # Always inspect arXiv's exact-version rights statement, even if the PDF has a license.
    if row['arxiv_id']:
        u='https://arxiv.org/abs/'+row['arxiv_id']
        try:
            raw,final=get(u);s=raw.decode('utf-8','replace')
            (WORK/(sha+'.arxiv.html')).write_text(s,encoding='utf-8')
            m=re.search(r'<div class="abs-license">(.*?)</div>',s,re.S)
            rights=m[1] if m else ''
            lic=re.search(r'href="([^"]+)"',rights)
            if lic:
                lu=html.unescape(lic[1]);cc=cc_url(lu)
                if cc:row.update(license_url=cc,license_evidence_url=u,license_evidence_quote=re.sub('<[^>]+>',' ',rights).strip()+' '+lu,decision='public_allowed',reason='arxiv_exact_version_creative_commons')
                elif 'nonexclusive-distrib' in lu and row['decision']!='public_allowed':row.update(license_url=lu,license_evidence_url=u,license_evidence_quote='arXiv perpetual non-exclusive distribution license',reason='arxiv_nonexclusive_no_further_reuse_grant')
                elif not cc and row['decision']!='public_allowed':row.update(license_url=lu,license_evidence_url=u,reason='arxiv_license_requires_review')
            elif row['decision']!='public_allowed':row.update(license_evidence_url=u,reason='arxiv_license_not_located_or_verification_page')
        except Exception as e:
            if row['decision']!='public_allowed':row.update(license_evidence_url=u,reason='arxiv_evidence_fetch_failed:'+str(e))
    print('audit',pid,row['decision'],row['license_url'],flush=True)
    return row

def run():
    inv=inventory();(WORK/'inventory.json').write_text(json.dumps(inv,ensure_ascii=False),encoding='utf-8');rows=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex:
        for future in concurrent.futures.as_completed([ex.submit(audit_one,a) for a in inv]):
            try:rows.append(future.result())
            except Exception as e:raise RuntimeError('Artifact audit failed: '+str(e))
            csvwrite('fulltext_library/license_audit.csv',rows)
    print('audited',len(rows),'public',sum(r['decision']=='public_allowed' for r in rows),flush=True)
if __name__=='__main__':run()
