"""Build a rights-filtered local/remote access audit from fresh inventory snapshots."""
from library_build import *
from bs4 import BeautifulSoup
import io,copy

OUT=ROOT/'local_sync_20261127'
def run():
    changed=set();repo=BASE.parent.parent
    def put(p,s):write(p,s);changed.add(p)
    def js(p,v):put(p,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
    def csvout(p,rows,fields=None):
        fields=fields or list(dict.fromkeys(k for r in rows for k in r));s=io.StringIO(newline='');w=csv.DictWriter(s,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(rows);put(p,s.getvalue())
    inventory=json.loads((WORK/'sync_inventory_unique.json').read_text(encoding='utf-8'))
    scan=json.loads((WORK/'sync_inventory_summary.json').read_text(encoding='utf-8'))
    attempts=json.loads((WORK/'sync_acquisition_private.json').read_text(encoding='utf-8'))
    index=json.loads((WORK/'sync_base_index.json').read_text(encoding='utf-8'));byid={r['paper_id']:r for r in index}
    kinds={};versions={};source={}
    for f in ['download_manifest.csv','local_materials_manifest.csv','extra_manifest.csv','core_followup_manifest.csv','fulltext_library/license_audit.csv','fulltext_library/new_artifact_audit.csv']:
        if not (BASE/f).exists():continue
        for a in read(f):
            if not a.get('sha256') or not a.get('paper_id'):continue
            key=(a['paper_id'],a['sha256']);kinds[key]=a.get('artifact_type') or 'main';versions[key]=a.get('version') or a.get('original_version') or 'existing local file';source[key]=a.get('source_url','')
    for a in attempts:
        if a['status']=='downloaded_pdf':inventory.append(dict(format='pdf',paper_ids=[a['paper_id']],local_path=a['local_path'],filename=Path(a['local_path']).name,sha256=a['sha256'],bytes=a['bytes'],pdf_pages=a['pdf_pages'],status='valid_pdf',license_lines=[]));source[(a['paper_id'],a['sha256'])]=a['source_url']
    htmls=[a for a in attempts if a['status']=='downloaded_article_html_pdf_not_acquired']
    local=[];allanchors=[];converted=0;reused=0;public_count=0
    for a in inventory:
        if a['format']!='pdf' or a['status'] not in ['valid_pdf','duplicate_hash']:continue
        for pid in a['paper_ids']:
            if pid not in byid:continue # Package manuals, out-of-scope and unreviewed versions remain inventory-only.
            h=a['sha256'];e=byid[pid];key=(pid,h);kind=kinds.get(key,'supplement' if 'supp' in a['filename'].lower() else 'main')
            pub=next((x for x in e['license_decisions'] if x['sha256']==h and x['decision']=='public_allowed'),None)
            if pub:
                path=next((p for p in e['public_pdf']+e['supplements'] if h[:12] in p and p.endswith('.pdf')),None)
                if not path:
                    candidates=list(ROOT.rglob(h[:12]+'/original.pdf'));path=candidates[0].relative_to(ROOT).as_posix() if candidates else ''
                dest=(ROOT/path).parent if path else None;public_count+=1
            else:
                dest=PRIVATE/'fulltext_library_local'/e['category']/pid/h[:12];dest.mkdir(parents=True,exist_ok=True)
                target=dest/'original.pdf'
                if not target.exists():shutil.copyfile(a['local_path'],target)
                assert hashlib.sha256(target.read_bytes()).hexdigest()==h
            if dest is None:continue
            maps=dest/'page_map.json'
            if not maps.exists():
                pages=pdf_transcript(dict(paper_id=pid,local_path=a['local_path'],sha256=h),dest);converted+=1
            else:pages=json.loads(maps.read_text(encoding='utf-8'));reused+=1
            assert len(pages)==a['pdf_pages']
            d=pymupdf.open(a['local_path']);loc=[]
            for i,p in enumerate(pages):
                if pid=='D03':p['printed_page_verified']=str(i+1439) if i>=1 else '';p['page_role']='publisher_download_cover' if i==0 else 'journal_page'
                for label in p['anchors']:
                    loc.append(dict(paper_id=pid,sha256=h,pdf_page=i+1,printed_page=p.get('printed_page_verified') or p.get('pdf_page_label',''),observed_label=label,formula_check_required=p['requires_formula_check']))
            if not pub:
                dump(maps,pages)
                for ext,pattern in [('md',r'^## PDF page (\d+)'),('txt',r'^===== ORIGINAL PDF PAGE (\d+)')]:
                    lines=(dest/f'fulltext.{ext}').read_text(encoding='utf-8').splitlines();starts=[(int(m[1]),i+1) for i,s in enumerate(lines) if (m:=re.match(pattern,s))]
                    assert len(starts)==len(pages)
                    for j,(n,start) in enumerate(starts):pages[n-1][ext+'_start_line']=start;pages[n-1][ext+'_end_line']=starts[j+1][1]-1 if j+1<len(starts) else len(lines)
                dump(maps,pages)
                # Source text is private; only original locator labels are published.
                local.append(dict(paper_id=pid,artifact_type=kind,format='pdf',version=versions.get(key,'local PDF; exact version stamp in original'),sha256=h,bytes=a['bytes'],pdf_pages=len(pages),local_path=str(dest/'original.pdf'),markdown=str(dest/'fulltext.md'),page_map=str(maps),source_url=source.get(key,e['original_url']),license='not_confirmed_for_third_party_sharing',status='local_only'))
            else:
                csvout(dest/'theorem_proof_locator.csv',loc,fields=['paper_id','sha256','pdf_page','printed_page','observed_label','formula_check_required'])
            allanchors+=loc
    # HTML is explicitly unpaginated and is never counted as a PDF.
    for a in htmls:
        pid=a['paper_id'];r=CAT[pid]
        if pid not in byid:
            e=dict(paper_id=pid,category=r['category'],title=r['title'],authors=r['authors'],doi=r['doi'],year=r.get('year_issue') or r.get('year_online'),original_url=r['source_url'],local_fulltext=True,public_pdf=[],public_markdown=[],public_txt=[],original_tex=[],public_xml=[],supplements=[],license_decisions=[],hash_duplicate_of=[],readme=f"{r['category']}/{pid}/README.md",status='local_only');index.append(e);byid[pid]=e
        e=byid[pid];h=a['sha256'];dest=PRIVATE/'fulltext_library_local'/r['category']/pid/h[:12];dest.mkdir(parents=True,exist_ok=True);data=Path(a['local_path']).read_bytes();assert hashlib.sha256(data).hexdigest()==h;write(dest/'original.html',data.decode('utf-8'))
        soup=BeautifulSoup(data,'html.parser');article=soup.find('article');assert article and len(article.get_text())>10000
        formula=[];images=[]
        for node in article.find_all(['math']):formula.append(str(node));node.replace_with('\n[ORIGINAL MATHML — see original_math_markup.json]\n')
        for node in article.find_all('img'):
            alt=node.get('alt','');src=node.get('src','');images.append(dict(alt=alt,src=src));node.replace_with('\n[ORIGINAL IMAGE / POSSIBLE FORMULA: '+alt+'; '+src+'; NOT TRANSCRIBED]\n')
        for node in article.find_all(['script','style']):node.decompose()
        text=article.get_text('\n',strip=True)
        intro=f"# {r['title']}\n\nUNPAGINATED OFFICIAL HTML. Not a PDF. No physical or printed pages invented. Original MathML and image references are preserved separately; image formulae are not transcribed or reconstructed.\n\nSource: {a['source_url']}\n\n"
        write(dest/'fulltext.md',intro+'````text\n'+text+'\n````\n');write(dest/'fulltext.txt',intro+text);dump(dest/'original_math_markup.json',formula);dump(dest/'image_formula_gaps.json',images)
        local.append(dict(paper_id=pid,artifact_type='main',format='html',version='PMC official full article HTML; PDF not acquired',sha256=h,bytes=len(data),pdf_pages='',local_path=str(dest/'original.html'),markdown=str(dest/'fulltext.md'),page_map='',source_url=a['source_url'],license='not_confirmed_for_third_party_sharing',status='local_only_html_formula_images_may_be_missing'))
        e['local_fulltext']=True;e['status']='local_only' if not e['public_markdown'] else 'public_fulltext';e['local_formats']=list(dict.fromkeys(e.get('local_formats',[])+['html']))
        if not any(q['sha256']==h for q in e['license_decisions']):e['license_decisions'].append(dict(sha256=h,decision='local_only',reason='official_full_article_html; no redistribution_grant_confirmed; formula_images_not_transcribed',source_url=a['source_url'],license_url=''))
    # Inventory is evidence of files, not evidence that a cached manual is a research article.
    public_inventory=[]
    for a in inventory:
        ids=[p for p in a['paper_ids'] if p in byid]
        public_inventory.append(dict(filename=a['filename'] if len(a['filename'])<100 else a['filename'][:100],sha256=a['sha256'],bytes=a['bytes'],format=a['format'],pdf_pages=a.get('pdf_pages',''),paper_ids=';'.join(ids),inspection_status=a['status'],catalog_match_status='matched_library_entry' if ids else 'inventory_only_manual_out_of_scope_or_version_pending',sharing_status='public_existing' if any(q['sha256']==a['sha256'] and q['decision']=='public_allowed' for p in ids for q in byid[p]['license_decisions']) else 'not_approved_for_upload'))
    csvout(OUT/'local_inventory.csv',public_inventory);js(OUT/'inventory_summary.json',scan)
    csvout(OUT/'local_conversion_manifest.csv',local);csvout(OUT/'theorem_proof_locator.csv',allanchors)
    csvout(OUT/'acquisition_log.csv',[{k:(json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v) for k,v in a.items() if k not in ['local_path','first_page']} for a in attempts])
    js(OUT/'acquisition_summary.json',dict(attempts=len(attempts),new_pdf_files=sum(a['status']=='downloaded_pdf' for a in attempts),article_html_files=len(htmls),new_independent_supplements=0,google_scholar='Verification page; all versions unavailable; not treated as zero search hits'))
    priority=['D01','D02','D03','D04','D05','B01','B02','A01','A03','C01','I03','C03','N83defe8bc4','N95df3c95c9','K01']
    gaps={
      'D01':'Original 2007 main/proof still absent; publisher403; author page404; Scholar verification.',
      'D02':'2008 note original absent; DOI/publisher403.',
      'D03':'Main and embedded asymptotic appendix available locally. PDF12-14 = printed1450-1452. Cover explicitly forbids redistribution; no private-host permission confirmed.',
      'D04':'2016 main/proof absent; publisher403; Pusan repository timed out; Scholar verification.',
      'D05':'Full official review HTML acquired, including literature cited; PDF not acquired. Formula-image gaps remain explicit.',
      'B01':'29/34-page manuscripts available; embedded technical proofs present. Independent online supplement still absent.',
      'B02':'2019 NIH main and 2016 36-page preprint with Appendix A/B available. Early A1-A8 are not final C1-C8; final separate supplement absent.',
      'A01':'2021 main PDF available. Official supplement ZIP endpoint returned verification/PoW HTML, not an archive.',
      'A03':'Formal main14 pages and independent supplement17 pages present locally; 53-page preprint also retained.',
      'C01':'Author PDF36 pages and full article HTML retained, with embedded proof/algorithm appendices. No separate supplement found in correct PMC record.',
      'I03':'Complete article HTML acquired; PDF and independent supplement blocked; image/formula gaps explicitly retained.',
      'C03':'43-page arXiv draft includes generalization/enumeration and diagnostics appendices. Formal independent Web Appendix not acquired; versions not interchangeable.',
      'N83defe8bc4':'23-page NIH main PDF available; final independent supplement remains absent.',
      'N95df3c95c9':'Full article HTML includes technical appendix; PDF and supplementary-data PDF blocked. Formula images not reconstructed.',
      'K01':'Full clinical article HTML obtained; original PDF and independent supplement not acquired. Tables need original-PDF visual review.'}
    status=[]
    for pid in priority:
        e=byid.get(pid);ls=[a for a in local if a['paper_id']==pid]
        status.append(dict(paper_id=pid,doi=CAT[pid]['doi'],main_status=e['status'] if e else 'not_acquired',local_pdf_versions=sum(a['format']=='pdf' and a['artifact_type']!='supplement' for a in ls),local_html_versions=sum(a['format']=='html' for a in ls),independent_supplement_versions=sum(a['artifact_type']=='supplement' for a in ls),unresolved=gaps[pid]))
    csvout(OUT/'priority_gaps.csv',status)
    index.sort(key=lambda e:e['paper_id']);js(ROOT/'index.json',index)
    csvout(ROOT/'index.csv',[{k:(';'.join(v) if isinstance(v,list) and (not v or isinstance(v[0],str)) else json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v) for k,v in e.items()} for e in index])
    for pid in ['D05','I03','K01','N95df3c95c9']:
        e=byid[pid];folder=ROOT/e['category']/pid;js(folder/'metadata.json',e)
        put(folder/'README.md',f"# {pid} — {e['title']}\n\n{e['authors']}\n\nDOI: {e['doi']}\n\nOriginal: {e['original_url']}\n\nStatus: local_only. Full official article HTML is stored locally; original PDF not acquired. Formula images are not transcribed.\n\n[Reading-location note](reading_note.md). [Current access audit](../../remote_access_manifest.csv).\n")
        put(folder/'reading_note.md',f"# {pid}：获取与版本核对\n\n2026-11-27已取得完整官方文章HTML，包含正文与文末部分。没有把HTML标作PDF，也没有编造分页。原生MathML、公式图片引用及未转换处单列保存在本地。\n\n来源：{e['original_url']}。\n\n当前缺口：{gaps[pid]}\n\n这是一份获取和定位札记，不能据此标记全部证明、图表或临床证据已核验。\n")
    # Source availability and proof-review status are deliberately separate.
    queue=list(csv.DictReader((WORK/'sync_base_reading_queue.csv').open(encoding='utf-8-sig')))
    for q in queue:
        pid=q['paper_id']
        if pid in byid:q['source_status']=byid[pid]['status']
        if pid=='D03':q['review_status']='local_original_main_and_embedded_proofs_located_remote_fulltext_restricted'
    csvout(BASE/'theoretical_studies'/'reading_queue.csv',queue)
    rows=[]
    for e in index:
        pid=e['paper_id'];ls=[a for a in local if a['paper_id']==pid]
        rows.append(dict(paper_id=pid,doi=e['doi'],version_summary=';'.join(dict.fromkeys(a['version'] for a in ls)),main_status=e['status'],supplement_status='local_independent_available' if any(a['artifact_type']=='supplement' for a in ls) else 'public_available' if e['supplements'] else 'not_acquired_or_not_confirmed',permission='per_artifact_license' if e['status']=='public_fulltext' else 'local_only_no_controlled_grant_confirmed' if e['status']=='local_only' else 'not_acquired',remote_pdf=';'.join(e['public_pdf']),remote_markdown=';'.join(e['public_markdown']),remote_latex=';'.join(e['original_tex']),remote_supplement=';'.join(e['supplements']),local_hashes=';'.join(a['sha256'] for a in ls),local_paths=';'.join(a['local_path'] for a in ls),remote_read_verification='pending_current_round_connector_read' if e['status']=='public_fulltext' else 'public_metadata_only_fulltext_not_remote',unresolved_reason=gaps.get(pid,'License/version restrictions; see per-artifact audit.' if e['status']=='local_only' else 'Main not acquired.' if e['status']=='not_acquired' else 'Formula extraction requires original PDF/TeX comparison.'),priority_gap=pid in priority))
    csvout(ROOT/'remote_access_manifest.csv',rows)
    js(OUT/'current_counts.json',dict(entries=len(index),public_readable=sum(e['status']=='public_fulltext' for e in index),controlled_sharing_approved=0,local_only=sum(e['status']=='local_only' for e in index),not_acquired=sum(e['status']=='not_acquired' for e in index),local_pdf_artifact_records=len([a for a in local if a['format']=='pdf']),local_html_artifact_records=len(htmls),new_pdf_conversions=converted,existing_pdf_conversions_reused=reused,public_pdf_artifact_records=public_count))
    # A concrete list for lawful direct document provision; no archive/encoding workaround.
    upload=[]
    for a in local:
        if a['paper_id'] not in priority:continue
        upload.append(dict(paper_id=a['paper_id'],artifact_type=a['artifact_type'],version=a['version'],format=a['format'],local_path=a['local_path'],sha256=a['sha256'],pdf_pages=a['pdf_pages'],purpose='Original proof review in user-controlled chat; verify applicable terms before provision',public_github_upload='not_approved',private_github_eligibility='rights_confirmation_required'))
    csvout(ROOT/'CHATGPT_UPLOAD_CORE_FILES.csv',upload)
    csvout(ROOT/'CONTROLLED_SHARE_CANDIDATES.csv',[dict(paper_id=a['paper_id'],sha256=a['sha256'],local_path=a['local_path'],proposed_repository='1492770335-art/12121-literature-private',permission_status='not_established',action='do_not_upload_until_rights_confirmed_and_user_approves_repository') for a in upload])
    put(ROOT/'CONTROLLED_SHARING_PROPOSAL.md',"""# 受控研究访问的具体方案（未创建仓库）

当前确认获准向第三方私有GitHub工作区共享的受限文件：0。独立私库不是版权豁免。D03的出版商下载封面明确限制再分发；不能仅凭用户批准建库就上传它。

候选仓库：`1492770335-art/12121-literature-private`；只允许仓库所有者及用户选择的ChatGPT连接器读取。现有公开仓库保持公开。逐文件清单、路径、哈希和权利待核状态见CONTROLLED_SHARE_CANDIDATES.csv。该清单已准备好，但不是上传白名单。

执行前条件：取得适用于该精确版本、允许个人受控云研究存储/第三方处理的许可或权利人授权；用户明确批准创建或连接上述独立私有仓库及其访问范围。随后仅提交获准文件，连接器授权该仓库，逐篇读取Markdown/TeX及证明页，并记录实际验证结果。当前没有创建私库、修改公共仓库可见性或扩大连接器权限。

无需先建库的路径：本地Codex已经可以直接读取这些文件并做证明研究；用户也可在适用权利允许的情况下，将CHATGPT_UPLOAD_CORE_FILES.csv列出的核心原件直接提供给其研究聊天。该清单中的文件尚未自动上传到ChatGPT。普通ChatGPT远端聊天不能通过本地磁盘路径取得文件。

产品访问步骤参考官方文档：https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt 。GitHub仓库权限参考：https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories 。arXiv再使用条件：https://info.arxiv.org/help/license/reuse.html 。PMC权利说明：https://pmc.ncbi.nlm.nih.gov/about/copyright/ 。
""")
    # Public original note: a short proof map, not a reproduction of the restricted appendix.
    put(BASE/'theoretical_studies'/'D03_Peng_Fine_2009_local_original_proof_map.md',"""# Peng–Fine 2009：本地原始证明核对与访问纠正

题名 Competing Risks Quantile Regression；DOI 10.1198/jasa.2009.tm08228。现有期刊PDF共15个物理页，第一页为下载封面，正文为印刷页1440–1453。SHA256：0e4d84e5c69d4a3dd807d49afd4e85e2f8a0f9dc62f48fddc533dc6738db2078。此前“未取得原文证明”的远端状态已过时。

原始定位：模型(1)、IPCW估计方程(4)(5)位于PDF3/印刷1441；C1–C4及Theorems1/2位于PDF4/印刷1442；渐近理论附录、凸目标与估计方程关系、Theorem1证明起点为PDF12/印刷1450；Theorem1续证、Lemma1及Theorem2证明起点为PDF13/印刷1451；Theorem2收尾、(A.3)及协方差估计论证为PDF14/印刷1452。已渲染查看PDF14的原始数学版面，原公式没有重写。

以下为原创的证明结构说明，不替代原文。研究目标是条件CIF反演的分位数，潜在净分布的分位数需要额外识别条件。证明首先控制删失分布估计引入的扰动，再对归一化估计过程建立一致大数律；局部可识别性及单调结构把估计方程的广义解限制在真值附近。弱收敛部分另外追踪删失估计的影响，使用经验过程局部增量控制与线性化，最后通过函数类的紧性得到过程极限。协方差估计部分沿估计方程的局部逆映射构造。不能将这些回归系数结论直接视为治疗规则优化器或截断端点原子的结论。

需要继续复核：原文链接函数、缩放、矩阵与影响函数符号在各式之间的对应；Lemma1调用Alexander与Lai–Ying的外部条件；一般协变量依赖删失扩展没有在本轮重证。这里不把自动文本中的符号缺失自行补正，不宣称全部外部引理已终审。

访问限制：出版商封面限制再分发，正文与全文Markdown/TXT仅留本地；公共GitHub只提供本原创定位说明和索引。完整原始证明不在公共GitHub远端，不能把这份札记当作已实现远端全文访问。参见fulltext_library/CHATGPT_UPLOAD_CORE_FILES.csv与CONTROLLED_SHARING_PROPOSAL.md。
""")
    # Save only a path/hash allowlist; publication is performed after independent checks.
    for p in [Path(__file__),BASE/'scripts/library_sync_inventory.py',BASE/'scripts/library_sync_acquire.py']:changed.add(p)
    allow=[]
    for p in sorted(changed):
        assert 'local_private' not in p.parts and p.is_relative_to(BASE)
        d=p.read_bytes();allow.append(dict(path=p.relative_to(repo).as_posix(),size=len(d),git_sha=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest(),kind='text'))
    dump(WORK/'sync_publish_manifest.json',allow)
    print(json.dumps(dict(changed_files=len(allow),local_pdf_records=len([a for a in local if a['format']=='pdf']),new_pdf_conversions=converted,existing_conversions_reused=reused,html_articles=len(htmls),indexed_entries=len(index)),ensure_ascii=False))

if __name__=='__main__':run()
