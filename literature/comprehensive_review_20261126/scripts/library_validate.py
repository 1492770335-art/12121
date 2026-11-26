from library_audit import *
from collections import Counter
def run():
    index=json.loads((ROOT/'index.json').read_text(encoding='utf-8'));art=read('fulltext_library/artifact_index.csv');aud=read('fulltext_library/license_audit.csv')+read('fulltext_library/new_artifact_audit.csv')+read('fulltext_library/public_pdf_audit.csv');errors=[];allowed={a['sha256'] for a in aud if a['decision']=='public_allowed'};pages=0;texcount=0
    if len({r['paper_id'] for r in read('fulltext_library/license_audit.csv')})!=208:errors.append('baseline 208 IDs not completely audited')
    for a in art:
        p=ROOT/a['original'];data=p.read_bytes()
        if hashlib.sha256(data).hexdigest()!=a['sha256']:errors.append('original hash mismatch '+str(p))
        if a['sha256'] not in allowed:errors.append('unlicensed artifact '+str(p))
        if not cc_url(a['license_url']):errors.append('missing explicit license URL '+str(p))
        if p.suffix=='.pdf':
            doc=pymupdf.open(p);mapping=json.loads((p.parent/'page_map.json').read_text(encoding='utf-8'));md=(ROOT/a['markdown']).read_text(encoding='utf-8');txt=(ROOT/a['txt']).read_text(encoding='utf-8')
            if len(doc)!=len(mapping) or len(re.findall(r'^## PDF page \d+',md,re.M))!=len(doc) or txt.count('===== ORIGINAL PDF PAGE ')!=len(doc):errors.append('page-map mismatch '+str(p))
            if [x['pdf_page'] for x in mapping]!=list(range(1,len(doc)+1)):errors.append('page order mismatch '+str(p))
            pages+=len(doc)
        elif p.suffix=='.xml':
            ET.fromstring(data)
            if 'PAGINATION UNAVAILABLE' not in (ROOT/a['markdown']).read_text(encoding='utf-8'):errors.append('XML has no pagination warning '+str(p))
    for manifest in ROOT.rglob('latex/source_manifest.json'):
        m=json.loads(manifest.read_text(encoding='utf-8'))
        for f in m['files']:
            p=manifest.parent/f['path'];texcount+=1
            if hashlib.sha256(p.read_bytes()).hexdigest()!=f['sha256']:errors.append('original TeX modified '+str(p))
    for r in index:
        folder=(ROOT/r['readme']).parent
        if not (folder/'reading_note.md').is_file() or not (folder/'metadata.json').is_file():errors.append('entry missing note or metadata '+r['paper_id'])
        for key in ['public_pdf','public_xml','public_markdown','public_txt','original_tex','supplements']:
            for path in r[key]:
                if not (ROOT/path).is_file():errors.append('broken index path '+path)
        if r['status']=='local_only' and (r['public_pdf'] or r['public_xml'] or r['public_markdown']):errors.append('restricted full text linked as public '+r['paper_id'])
    result=dict(checked_at=stamp(),audited_baseline_paper_ids=208,public_original_files_checked=len(art),pdf_pages_checked=pages,original_tex_files_checked=texcount,index_entries_checked=len(index),errors=errors,limitations=['PDF extraction flags all detected mathematical pages; not a verified equation-to-LaTeX transcription.','XML without PDF is unpaginated.','No downloaded TeX source was compiled or executed.'])
    dumpfile=ROOT/'validation.json';dumpfile.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(result,ensure_ascii=False),flush=True)
    if errors:raise SystemExit(1)
if __name__=='__main__':run()
