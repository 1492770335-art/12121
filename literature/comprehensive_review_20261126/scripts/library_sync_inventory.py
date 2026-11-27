"""Read-only inventory of literature roots, including extensionless cached PDFs."""
from library_audit import *
import zipfile,tarfile,difflib

def run():
    roots=[Path('D:/最后一版/EXP02_repo/literature'),Path('D:/最后一版/参考文献原文'),Path('D:/最后一版/刘莉文献精读_20261114')]
    paths=[]
    for root in roots:
        for p in root.rglob('*'):
            if not p.is_file():continue
            if p.suffix.lower() in ['.pdf','.tex','.xml','.zip','.gz','.tgz'] or (p.parent.name=='cache' and not p.suffix):paths.append(p)
    paths += [p for p in Path('C:/Users/asus/Desktop').glob('*.pdf') if p.name not in ['main(1).pdf','财政部全国财政电子票据查验平台.pdf']]
    hashids={}
    for f in ['download_manifest.csv','local_materials_manifest.csv','extra_manifest.csv','core_followup_manifest.csv','fulltext_library/license_audit.csv','fulltext_library/new_artifact_audit.csv']:
        if not (BASE/f).exists():continue
        for a in read(f):
            if a.get('sha256') and a.get('paper_id'):hashids.setdefault(a['sha256'],set()).add(a['paper_id'])
    for a in json.loads((WORK/'sync_base_index.json').read_text(encoding='utf-8')):
        for d in a['license_decisions']:hashids.setdefault(d['sha256'],set()).add(a['paper_id'])
    records=[];unique={};cache_skipped=0
    for p in dict.fromkeys(paths):
        with p.open('rb') as f:head=f.read(100)
        fmt='pdf' if head.startswith(b'%PDF-') else p.suffix.lower().lstrip('.')
        if not p.suffix and fmt!='pdf':cache_skipped+=1;continue
        data=p.read_bytes();h=hashlib.sha256(data).hexdigest()
        a=dict(local_path=str(p),filename=p.name,sha256=h,bytes=len(data),format=fmt,paper_ids=sorted(hashids.get(h,set())),status='duplicate_hash' if h in unique else 'not_inspected')
        if h in unique:
            a.update({k:v for k,v in unique[h].items() if k not in ['local_path','filename','status']});a['status']='duplicate_hash'
        else:
            try:
                if fmt=='pdf':
                    doc=pymupdf.open(p);t='\n'.join(doc[i].get_text() for i in range(min(2,len(doc))));a.update(pdf_pages=len(doc),first_pages=t[:1500],status='valid_pdf',has_text_layer=bool(t.strip()))
                    if not a['paper_ids']:
                        lower=t.lower()
                        ids=[pid for pid,c in CAT.items() if c.get('doi') and c['doi'].lower() in lower]
                        if not ids:
                            norm=lambda s:re.sub(r'[^a-z0-9]','',s.lower())
                            nt=norm(t)
                            ids=[pid for pid,c in CAT.items() if len(norm(c['title']))>30 and norm(c['title']) in nt]
                        a['paper_ids']=ids
                    a['license_lines']=[dict(pdf_page=i+1,text=l[:300]) for i,pg in enumerate(doc) for l in pg.get_text().splitlines() if any(s in l.lower() for s in ['creativecommons','creative commons','all rights reserved','redistribution','re-distribution'])]
                elif fmt=='xml':
                    rr=ET.fromstring(data);a.update(status='valid_xml',root_tag=rr.tag)
                elif fmt=='zip':
                    with zipfile.ZipFile(p) as z:a.update(status='valid_zip' if z.testzip() is None else 'zip_crc_error',archive_members=z.namelist())
                elif fmt in ['gz','tgz']:
                    with tarfile.open(p) as z:a.update(status='valid_tar_archive',archive_members=z.getnames())
                elif fmt=='tex':a.update(status='original_tex',utf8_readable=True);data.decode('utf-8')
                else:a['status']='not_pdf_or_supported_material'
            except Exception as e:a.update(status='inspection_failed',error=str(e)[:250])
            unique[h]=a
        records.append(a)
    dump= lambda path,obj:path.write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8')
    dump(WORK/'sync_inventory_private.json',records)
    dump(WORK/'sync_inventory_unique.json',list(unique.values()))
    stats=dict(file_instances=len(records),unique_hashes=len(unique),duplicate_instances=len(records)-len(unique),unique_formats={f:sum(a['format']==f for a in unique.values()) for f in sorted({a['format'] for a in unique.values()})},non_pdf_cache_entries_skipped=cache_skipped,roots=[str(r) for r in roots],excluded='User thesis main(1).pdf and unrelated personal PDFs excluded.')
    dump(WORK/'sync_inventory_summary.json',stats);print(json.dumps(stats,ensure_ascii=False))
    priority=['D01','D02','D03','D04','B01','B02','A01','A03','C01','C03','I03','K01','N83defe8bc4']
    for pid in priority:
        matches=[a for a in unique.values() if pid in a['paper_ids'] and a['format']=='pdf']
        print(pid,json.dumps([dict(filename=a['filename'],pages=a.get('pdf_pages'),sha256=a['sha256'],path=a['local_path']) for a in matches],ensure_ascii=False))

if __name__=='__main__':run()
