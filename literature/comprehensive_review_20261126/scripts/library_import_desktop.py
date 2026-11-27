"""Import the seven user-supplied PDFs; publish only explicitly licensed text."""
from library_build import *
import copy

BATCH='desktop_20261127'
FILES=[('2411.08315.pdf','A02'),('2204.04052v1.pdf','A03'),('nihms-1001475.pdf','B02'),('nihms915733.pdf','B01'),('10104503.pdf','B01'),('nihms970979.pdf','N83defe8bc4'),('kxz026.pdf','A01')]

def run():
    repo=BASE.parent.parent;changed=set();records=[];locators=[];private_records=[]
    index=json.loads((WORK/'import_remote_index.json').read_text(encoding='utf-8'))
    byid={r['paper_id']:r for r in index}
    def put(p,s):
        write(p,s);changed.add(p)
    def js(p,v):put(p,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
    def csvout(p,rows):
        import io
        stream=io.StringIO(newline='');w=csv.DictWriter(stream,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows);put(p,stream.getvalue())
    for name,pid in FILES:
        src=Path('C:/Users/asus/Desktop')/name;data=src.read_bytes();assert data.startswith(b'%PDF-')
        h=hashlib.sha256(data).hexdigest();r=CAT[pid];doc=pymupdf.open(src)
        public=pid=='A02';reason='cc_by_4_0_exact_arxiv_v1_content_user_supplied_pdfium_rendition' if public else 'all_rights_reserved_printed_on_page_1' if pid=='A01' else 'arxiv_nonexclusive_no_further_reuse_grant' if pid=='A03' else 'redistribution_license_not_confirmed'
        local=PRIVATE/'fulltext_library_local'/r['category']/pid/h[:12];local.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(src,local/'original.pdf');assert hashlib.sha256((local/'original.pdf').read_bytes()).hexdigest()==h
        a=dict(paper_id=pid,local_path=str(local/'original.pdf'),sha256=h)
        pages=pdf_transcript(a,local)
        # Add exact extraction line ranges to physical page map.
        for ext in ['md','txt']:
            lines=(local/f'fulltext.{ext}').read_text(encoding='utf-8').splitlines()
            pattern=r'^## PDF page (\d+)' if ext=='md' else r'^===== ORIGINAL PDF PAGE (\d+)'
            starts=[(int(m[1]),i+1) for i,line in enumerate(lines) if (m:=re.match(pattern,line))]
            assert len(starts)==len(doc)
            for j,(n,start) in enumerate(starts):pages[n-1][ext+'_start_line']=start;pages[n-1][ext+'_end_line']=starts[j+1][1]-1 if j+1<len(starts) else len(lines)
        dump(local/'page_map.json',pages)
        for p in pages:
            for anchor in p['anchors']:locators.append(dict(paper_id=pid,filename=name,sha256=h,pdf_page=p['pdf_page'],anchor=anchor,requires_formula_check=p['requires_formula_check']))
        folder=ROOT/r['category']/pid;dest=folder/'artifacts'/h[:12]
        pubpaths={}
        if public:
            dest.mkdir(parents=True,exist_ok=True)
            for f in ['original.pdf','fulltext.md','fulltext.txt','page_map.json']:
                shutil.copyfile(local/f,dest/f);changed.add(dest/f)
            pubpaths={k:(dest/v).relative_to(ROOT).as_posix() for k,v in [('pdf','original.pdf'),('markdown','fulltext.md'),('txt','fulltext.txt'),('page_map','page_map.json')]}
        evidence=dict(paper_id=pid,filename=name,sha256=h,bytes=len(data),pdf_pages=len(doc),source='user_supplied_local_file',original_url=r['source_url'],version_stamp=next((line for line in doc[0].get_text().splitlines() if 'arXiv:' in line),''),decision='public_allowed' if public else 'local_only',reason=reason,license_url='https://creativecommons.org/licenses/by/4.0/' if public else '',license_evidence_url='https://arxiv.org/abs/2411.08315v1' if public else '',checked_at=stamp(),public_paths=pubpaths,formula_flagged_pages=sum(p['requires_formula_check'] for p in pages),conversion='Unedited text-layer extraction; no mathematical reconstruction; original physical pages preserved.')
        if public:
            evidence['version_note']='User-supplied PDF metadata identifies PDFium; hash differs from canonical arXiv PDF. First-page stamp identifies 2411.08315v1, authors/title/page count match. Preserve both renditions and do not claim byte identity.'
            js(dest/'provenance_and_license.json',evidence)
        records.append(evidence)
        if not public:private_records.append(dict(paper_id=pid,artifact_type='main',sha256=h,pdf_pages=len(doc),status='private_pdf_markdown_txt',local_directory=str(local),reason=reason))
        if pid not in byid:
            entry=dict(paper_id=pid,category=r['category'],title=r['title'],authors=r['authors'],doi=r['doi'],year=r.get('year_issue') or r.get('year_online'),original_url=r['source_url'],local_fulltext=True,public_pdf=[],public_markdown=[],public_txt=[],original_tex=[],public_xml=[],supplements=[],license_decisions=[],hash_duplicate_of=[],readme=f"{r['category']}/{pid}/README.md",status='local_only')
            byid[pid]=entry;index.append(entry)
        entry=byid[pid];entry['local_fulltext']=True
        if not any(x['sha256']==h for x in entry['license_decisions']):entry['license_decisions'].append(dict(sha256=h,decision=evidence['decision'],reason=reason,license_url=evidence['license_url'],source_url=r['source_url']))
        if public:
            for field,k in [('public_pdf','pdf'),('public_markdown','markdown'),('public_txt','txt')]:
                if pubpaths[k] not in entry[field]:entry[field].append(pubpaths[k])
        entry['status']='public_fulltext' if entry['public_pdf'] or entry['public_xml'] else 'local_only'
    index.sort(key=lambda x:x['paper_id'])
    js(ROOT/'index.json',index)
    csvout(ROOT/'index.csv',[{k:(';'.join(v) if isinstance(v,list) and (not v or isinstance(v[0],str)) else json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v) for k,v in r.items()} for r in index])
    for pid in set(pid for _,pid in FILES):
        e=byid[pid];folder=ROOT/e['category']/pid;js(folder/'metadata.json',e)
        lines=[f"# {pid} — {e['title']}",'',e['authors'],'',f"DOI: {e['doi']}",f"Original: {e['original_url']}",f"Availability: **{e['status']}**",'']
        for field in ['public_pdf','public_markdown','public_txt','original_tex','public_xml']:
            for path in e[field]:lines.append(f"- {field}: [{Path(path).name}]({os.path.relpath(ROOT/path,folder).replace(os.sep,'/')})")
        lines+=['','User-supplied PDFs have been converted locally. Restricted PDF/Markdown/TXT are not published. See [batch audit](../../local_imports/'+BATCH+'/manifest.json) and [reading note](reading_note.md).']
        put(folder/'README.md','\n'.join(lines)+'\n')
        lines=[f"# {pid}：本地文件核对与精读定位",'',f"题名：{e['title']}。作者：{e['authors']}。原文：{e['original_url']}。",'','2026-11-27：用户提供文件已通过PDF签名、首页身份、页数与SHA256核对，已生成逐页Markdown/TXT。未完成逐式人工审校。']
        for a in records:
            if a['paper_id']==pid:lines+=['',f"版本文件：{a['filename']}；{a['pdf_pages']}页；SHA256 `{a['sha256']}`；{a['decision']}；{a['reason']}。"]
        lines+=['','实际提取到的定位标签（PDF物理页码）：']
        lines += [f"- {a['filename']}，第{a['pdf_page']}页：{a['anchor']}。" for a in locators if a['paper_id']==pid]
        lines+=['','精读时分别核对统计目标、识别条件、估计条件、定理依赖与附录。上述标签来自实际文本扫描，不代表已完成证明审核；公式以原始PDF或作者TeX为准。']
        put(folder/'reading_note.md','\n'.join(lines)+'\n')
    batch=ROOT/'local_imports'/BATCH
    js(batch/'manifest.json',records);csvout(batch/'theorem_proof_locator.csv',locators)
    csvout(batch/'manifest.csv',[{k:(json.dumps(v,ensure_ascii=False) if isinstance(v,dict) else v) for k,v in a.items()} for a in records])
    summary=dict(files_converted=7,distinct_papers=6,physical_pdf_pages=sum(a['pdf_pages'] for a in records),public_pdf=1,public_markdown=1,public_txt=1,local_only_pdf=6,newly_available_core_papers=['A01','B01'],new_library_entry='N83defe8bc4',independent_supplements_added=0)
    js(batch/'summary.json',summary)
    report=['# 用户本地PDF导入结果','',json.dumps(summary,ensure_ascii=False,indent=2),'','7份PDF全部保持字节不变并完成逐页Markdown/TXT转换，公式未猜测性重构。Wang 2018的29页与34页稿分开保存；34页稿PDF第29页起为技术证明附录，29页稿PDF第16页起也有技术证明附录。这些不是独立下载的补充材料。','', 'Christina Zhou 2024的用户PDF为PDFium表示，和已有官方PDF哈希不同，保留两个表示，不覆盖原始官方版本。该arXiv v1的CC BY 4.0证据见 https://arxiv.org/abs/2411.08315v1 。','', '其余6份文件没有确认全文再分发授权，PDF、Markdown和TXT保存在local_private/fulltext_library_local/。许可状态及页码定位公开，正文不公开。','', '本轮新增可用核心正文A01、B01；此前13篇核心中的未取得正文由10篇减为8篇。Choi等2018使用已存在的书目paper_id N83defe8bc4新增全文入口。','', '本报告是文件整理及定位记录，不修改现有论文、理论、估计或模拟。']
    put(batch/'README.md','\n'.join(report)+'\n')
    # Update current remote snapshots, preserving unrelated newer work.
    core=list(csv.DictReader((WORK/'import_remote_core_status.csv').open(encoding='utf-8-sig')))
    for c in core:
        if c['paper_id'] in ['A01','B01']:c.update(fulltext_status='local_only',downloaded_main='1',reason='user_supplied_local_pdf_verified; redistribution_license_not_confirmed')
    csvout(ROOT/'core_status.csv',core)
    stats=json.loads((WORK/'import_remote_summary.json').read_text(encoding='utf-8'))
    stats.update(entries=len(index),public_entries=sum(e['status']=='public_fulltext' for e in index),local_only_entries=sum(e['status']=='local_only' for e in index),not_acquired_entries=sum(e['status']=='not_acquired' for e in index),public_unique_artifacts=stats['public_unique_artifacts']+1,public_original_pdf=stats['public_original_pdf']+1,public_markdown=stats['public_markdown']+1,public_txt=stats['public_txt']+1,reading_notes=len(index),formula_flagged_pages=stats['formula_flagged_pages']+records[0]['formula_flagged_pages'],core_new_fulltexts=stats['core_new_fulltexts']+2,last_import_batch=BATCH,last_import_at=stamp())
    oldhash={a['sha256'] for f in ['license_audit.csv','new_artifact_audit.csv','public_pdf_audit.csv'] if (ROOT/f).exists() for a in read('fulltext_library/'+f)}
    stats['all_audited_artifact_records']+=len({(a['paper_id'],a['sha256']) for a in records if a['sha256'] not in oldhash});stats['unique_audited_hashes']+=len({a['sha256'] for a in records}-oldhash)
    js(ROOT/'summary.json',stats)
    for f in ['README.md','REPORT.md']:
        s=(WORK/('import_remote_'+f)).read_text(encoding='utf-8');put(ROOT/f,'> 2026-11-27 本地文件导入更新：7份PDF已转换；A01/B01全文补齐；当前222条入口，79条有公开全文，135条仅本地，8条未取得。公开原始PDF75份，XML7份，Markdown/TXT各82份。此前正文统计为历史快照。详见[本轮记录](local_imports/'+BATCH+'/README.md)及[最新统一索引](index.csv)。\n\n'+s)
    old=list(csv.DictReader((WORK/'import_remote_local_conversion_manifest.csv').open(encoding='utf-8-sig')));seen={a['sha256'] for a in old}
    csvout(ROOT/'local_conversion_manifest.csv',old+[a for a in private_records if a['sha256'] not in seen])
    artifacts=list(csv.DictReader((WORK/'import_remote_artifact_index.csv').open(encoding='utf-8-sig')));a=records[0];p=a['public_paths']
    artifacts.append(dict(paper_id='A02',sha256=a['sha256'],artifact_type='main',original=p['pdf'],markdown=p['markdown'],txt=p['txt'],latex='',license_url=a['license_url'],source_url='https://arxiv.org/abs/2411.08315v1',pdf_pages=47,pagination='original_pdf_physical_pages'))
    csvout(ROOT/'artifact_index.csv',artifacts)
    changed.add(Path(__file__))
    # Validate every supplied byte stream and every physical page delimiter.
    for a in records:
        p=PRIVATE/'fulltext_library_local'/CAT[a['paper_id']]['category']/a['paper_id']/a['sha256'][:12]
        assert hashlib.sha256((p/'original.pdf').read_bytes()).hexdigest()==a['sha256']
        assert len(json.loads((p/'page_map.json').read_text(encoding='utf-8')))==a['pdf_pages']
    js(batch/'validation.json',dict(errors=[],files=7,pages=summary['physical_pdf_pages'],original_hashes_verified=True,all_page_maps_verified=True,restricted_fulltexts_in_publication_allowlist=0))
    allow=[]
    for p in sorted(changed):
        assert 'local_private' not in p.parts
        data=p.read_bytes();allow.append(dict(path=p.relative_to(repo).as_posix(),size=len(data),git_sha=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest(),kind='binary' if p.suffix=='.pdf' else 'text'))
    dump(WORK/'desktop_publish_manifest.json',allow)
    print(json.dumps(dict(summary=summary,publication_files=len(allow),stats=stats),ensure_ascii=False))

if __name__=='__main__':run()
