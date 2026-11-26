from collect import *
from collections import Counter, defaultdict
import importlib.metadata
import pymupdf

def run():
    state=json.loads((PRIVATE/'state.json').read_text(encoding='utf-8'));rows=state['rows'];meta=state['meta']
    xp=PRIVATE/'state_expansion.json'
    if xp.exists():
        x=json.loads(xp.read_text(encoding='utf-8'))
        for r in x['rows']:
            if r['paper_id'].startswith('N'):
                rows.append(r);meta[r['paper_id']]=x['meta'][r['paper_id']]
    # Link working-paper/preprint records to a matched journal version; preserve original seed ID.
    version_links=[]
    for r in rows:
        if r['paper_id'].startswith('N') or not r['status'].startswith('metadata'):continue
        original_type=meta.get(r['paper_id'],{}).get('cr',{}).get('type','')
        if original_type not in ['report','posted-content','working-paper','dissertation']:continue
        matches=[n for n in rows if n['paper_id'].startswith('N') and norm(n['title'])==norm(r['title']) and meta.get(n['paper_id'],{}).get('cr',{}).get('type')=='journal-article']
        if matches:
            n=matches[0];common=set(norm(r.get('authors','')).split()) & set(norm(n.get('authors','')).split())
            if len(common)<2:continue
            version_links.append(dict(seed_id=r['paper_id'],preprint_doi=r.get('doi',''),journal_doi=n.get('doi',''),journal_record=n['paper_id'],evidence_url=n.get('verification_evidence','')))
            r['preprint_doi']=r.get('doi','')
            for k in ['authors','title','journal','year_online','year_issue','doi','source_url','abstract_url','version','status','verification_evidence']:r[k]=n.get(k,'')
            meta[r['paper_id']]=meta[n['paper_id']]
    csvwrite('version_links.csv',version_links)
    seen={};clean=[]
    for r in rows:
        if r['paper_id'] in {c['paper_id'] for c in clean}:continue
        key=r.get('doi') or (norm(r['title']) if r['status'].startswith('metadata') else '')
        if key and key in seen:r['duplicate_of']=seen[key];r['status']='duplicate_version'
        elif key:seen[key]=r['paper_id']
        r['record_type']=meta.get(r['paper_id'],{}).get('cr',{}).get('type','article' if r.get('pmid') else 'unknown')
        clean.append(r)
    rows=clean
    for r in rows:
        if r.get('doi','').lower()=='10.48550/arxiv.1704.06431' or (norm(r['title'])=='faster rates for policy learning' and 'luedtke' in norm(r.get('authors',''))):
            r.update(duplicate_of='E02',status='duplicate_version')
    import html
    scope_exclusions=['monetary policy','fear of floating','tariff','panama canal','load shedding','rural electrification','transit strat','social protection','smallholder','climate risks','geopolitical','electricity system','financial uncertainty','risk spillover','interval training','math course','education','carbon emission','stock market','market consistency','clean energy','tourism','supply chain','crime in south africa']
    for r in rows:
        r['title']=' '.join(html.unescape(re.sub(r'<[^>]+>','',r['title'])).split())
        m=meta.get(r['paper_id'],{})
        dates=[]
        for datekey in ['published-online','published-print','published']:
            parts=m.get('cr',{}).get(datekey,{}).get('date-parts',[[]])[0]
            if parts:
                dates.append('-'.join(str(v).zfill(4 if i==0 else 2) for i,v in enumerate((parts+[1,1])[:3])))
        if r['paper_id'].startswith('N') and dates and min(dates)>'2026-11-26':r['status']='outside_search_cutoff'
        if not m.get('cr',{}).get('author'):
            authors=m.get('ep',{}).get('authorList',{}).get('author',[])
            if authors:r['authors']=' and '.join((a.get('lastName','')+', '+a.get('firstName','')).strip(', ') if a.get('lastName') else a.get('fullName','') for a in authors)
        if r['paper_id']=='B10':r['authors']='Victor Chernozhukov and Iván Fernández-Val and Blaise Melly'
        r['year_publication']=year(m.get('cr',{}),'published') or year(m.get('cr',{}),'issued')
        if r['paper_id'].startswith('N') and any(x in norm(r['title']) for x in scope_exclusions):r['status']='excluded_scope_after_bibliographic_check'
        if r['record_type']=='dataset':r['status']='software_or_dataset_source_not_paper' if r['paper_id'].startswith('N') or r.get('doi') else 'unresolved_wrong_software_candidate'
        if r['paper_id'].startswith('N') and re.match(r'^(Correction|Corrigendum|Erratum)',r['title'],re.I):r['status']='publication_notice'
        if r['status'].startswith('metadata') and (not r.get('authors') or not (r.get('year_online') or r.get('year_issue') or r['year_publication'])):r['status']='incomplete_bibliography_author_or_year'
        if 'arxiv' in r.get('journal','').lower():r['version']='arXiv preprint; publication status unresolved'
        if 'ssrn' in r.get('journal','').lower() or r.get('doi','').startswith(('10.1920/','10.3386/')):r['version']='working paper; journal version requires separate verification'
        if r['paper_id']=='C02':
            r['authors']='Haomiao Meng and Ying-Qi Zhao and Haoda Fu and Xingye Qiao'
            meta[r['paper_id']]['cr']={'type':'journal-article','volume':'21','issue':'183','page':'1-28'}
    manifest=[]
    for name in ['download_manifest.csv','local_materials_manifest.csv','code_manifest.csv','extra_manifest.csv','core_followup_manifest.csv','data_dictionary_manifest.csv']:
        p=BASE/name
        if p.exists():manifest.extend(csv.DictReader(p.open(encoding='utf-8-sig')))
    # Retain attempt history, deduplicate identical artifact/version/hash or identical failures.
    unique={}
    for a in manifest:
        if a.get('repo_path') and a.get('artifact_type')!='main':
            original=(BASE/a['repo_path']).resolve()
            if original.is_file() and original.is_relative_to((BASE/'open_access').resolve()):
                destination=PRIVATE/a['paper_id']/original.name;destination.parent.mkdir(exist_ok=True)
                destination.write_bytes(original.read_bytes());original.unlink()
                a.update(local_path=str(destination),repo_path='',error='Supplement retained locally pending contents review for patient-level data')
        key=(a['paper_id'],a['artifact_type'],a['source_url'],a['status'],a.get('sha256',''),a.get('error',''))
        unique[key]=a
    manifest=list(unique.values())
    rowmap={r['paper_id']:r for r in rows}
    for a in manifest:
        if a.get('status') in ['downloaded','existing_local_verified'] and a['artifact_type']=='main' and not rowmap.get(a['paper_id'],{}).get('status','').startswith('metadata') and not rowmap.get(a['paper_id'],{}).get('duplicate_of'):
            a.update(status='quarantined_unresolved_identity',error='Paper identity remains unresolved; candidate download excluded from available counts')
        if a.get('fetched_at','') and a.get('final_url')==a.get('source_url') and not (CACHE/(hashlib.sha256(a['source_url'].encode()).hexdigest()+'.meta.json')).exists():
            a['final_url']='';a['error']=(a.get('error','')+'; cached original retrieval did not persist redirect URL; final URL unknown').lstrip('; ')
    good=[a for a in manifest if a['status'] in ['downloaded','existing_local_verified']]
    aliases={r['paper_id']:r.get('duplicate_of') or r['paper_id'] for r in rows}
    have=lambda pid,kind:[a for a in good if aliases.get(a['paper_id'],a['paper_id'])==aliases.get(pid,pid) and a['artifact_type']==kind]
    for r in rows:
        pid=r['paper_id']
        for k,col in [('main','fulltext_status'),('supplement','supplement_status'),('code','code_status')]:
            r[col]='available' if have(pid,k) else 'unresolved' if not r['status'].startswith('metadata') else 'not_acquired'
        r['doi_status']='verified' if r.get('doi') else 'not_assigned_journal_article' if pid=='C02' else 'not_resolved_or_not_applicable'
    csvwrite('resolved_catalog.csv',rows)
    csvwrite('screening_final.csv',[dict(candidate_id=r['paper_id'],decision='include_bibliography_scope_reviewed' if r['status'].startswith('metadata') else r['status'],reason='Primary bibliographic record and title screening only; full text applicability review pending' if r['status'].startswith('metadata') else 'See resolved_catalog status; no fabricated authors or dates',evidence_url=r.get('verification_evidence') or r.get('source_url')) for r in rows if r['paper_id'].startswith('N')])
    csvwrite('download_manifest.csv',manifest)
    csvwrite('failures.csv',[a for a in manifest if a not in good])
    classified=[]
    for a in manifest:
        if a in good:continue
        e=a.get('error','').lower();code=a.get('status','')
        if '403' in e:code='access_denied'
        elif '404' in e:code='broken_link_or_not_available'
        elif 'timed out' in e or 'timeout' in e:code='network_timeout'
        elif 'non_pdf' in e or 'html' in e:code='non_pdf_or_verification_page'
        elif 'title' in e:code='identity_review_required'
        classified.append(dict(paper_id=a['paper_id'],artifact_type=a['artifact_type'],reason_code=code,source_url=a.get('source_url',''),error=a.get('error',''),manual_route=idsource if (idsource:=next((r.get('source_url','') for r in rows if r['paper_id']==a['paper_id']),'')) else a.get('source_url','')))
    csvwrite('failure_classification.csv',classified)
    csvwrite('search_leads.csv',[r for r in rows if not r['status'].startswith('metadata') and not r.get('duplicate_of')])
    pub=[]
    for r in rows:
        m=meta.get(r['paper_id'],{}).get('cr',{})
        if m:pub.append(dict(paper_id=r['paper_id'],doi=r['doi'],update_to=json.dumps(m.get('update-to',[])),relation=json.dumps(m.get('relation',{})),status='notices_present_review' if m.get('update-to') else 'no_notice_in_retrieved_crossref_record',limitations='Not a definitive retraction database search; publisher Crossmark manual check pending'))
    csvwrite('publication_status.csv',pub)
    logs=[]
    for name in ['search_log.csv','search_log_seed_replay.csv','search_log_expansion.csv','search_log_manual.csv','search_log_trace_supplementary.csv']:
        p=BASE/name
        if p.exists():logs.extend(csv.DictReader(p.open(encoding='utf-8-sig')))
    unique={tuple(sorted(r.items())):r for r in logs};csvwrite('search_log.csv',unique.values())
    bib=[]
    for r in rows:
        if not r['status'].startswith('metadata') or r.get('duplicate_of') or not r.get('authors'):continue
        pid=r['paper_id'];m=meta.get(pid,{}).get('cr',{});kind='book' if 'book'==m.get('type') else 'article' if r.get('journal') else 'misc'
        vals={'author':r['authors'],'title':r['title'],'journal':r.get('journal',''),'year':r.get('year_issue') or r.get('year_online') or r.get('year_publication'),'doi':r.get('doi',''),'url':r.get('source_url',''),'volume':m.get('volume',''),'number':m.get('issue',''),'pages':m.get('page',''),'publisher':m.get('publisher','') if kind=='book' else ''}
        if kind=='book':vals.pop('journal',None)
        if r.get('arxiv'):vals.update(eprint=r['arxiv'],archivePrefix='arXiv',note='Preprint linked to this record; use version-specific supplement')
        def esc(x):return str(x).replace('\\','\\textbackslash{}').replace('&','\\&').replace('%','\\%').replace('_','\\_').replace('#','\\#')
        bib.append('@'+kind+'{'+pid+',\n'+',\n'.join('  '+k+' = {'+esc(v)+'}' for k,v in vals.items() if v)+'\n}\n')
    (BASE/'references.bib').write_text('\n'.join(bib),encoding='utf-8')
    index=['# 文献精读索引','',f'生成时间：{stamp()}。本文件为获取索引；不表示已逐篇精读。章节或页码仅在实际读取文件后记录。','']
    anchors=[]
    for a in good:
        p=Path(a['local_path'])
        if p.suffix.lower()!='.pdf':continue
        try:
            doc=pymupdf.open(p)
            for i,page in enumerate(doc):
                t=page.get_text() or ''
                lines=t.splitlines()[:12]
                for line in lines:
                    if re.match(r'^\s*(Supplement(ary)?( Materials?| to)?|Appendix|References|[1-9]\.?\s+(Introduction|Proof of theory|Discussion))',line,re.I) and len(line)<180:
                        anchors.append(dict(paper_id=a['paper_id'],artifact_sha256=a['sha256'],version=a['version'],pdf_page=i+1,heading=line.strip(),source_url=a['source_url']))
        except Exception:pass
    csvwrite('reading_anchors.csv',anchors)
    embedded=[a for a in anchors if re.match(r'^(Supplement|Appendix)',a['heading'],re.I)]
    csvwrite('embedded_appendices.csv',embedded)
    for r in rows:
        index.extend(['## '+r['paper_id']+' — '+r['title'],'',f"类别 {r['category']} / {r['priority']}；书目状态：{r['status']}。",'',f"原文入口：{r.get('source_url','')}。DOI：{r.get('doi') or '未解析／未分配'}。",''])
        for kind,label in [('main','正文'),('supplement','独立补充材料'),('code','作者代码')]:
            arts=have(r['paper_id'],kind)
            if arts:
                for a in arts:index.append(f"- {label}：{a['version']}；{a.get('pages') or 'NA'} 页；{a['source_url']}；"+(a['repo_path'] or '本地 local_private/，未上传'))
            else:index.append('- '+label+'：未取得；逐项来源和原因见 download_manifest.csv / failures.csv。')
        hs=[a for a in anchors if a['paper_id']==r['paper_id']]
        if hs:index.append('- 已观察到的位置：'+'；'.join(f"PDF第{a['pdf_page']}页 {a['heading']}" for a in hs[:6])+'（不同版本分别以 reading_anchors.csv 的 hash 为准）。')
        index.append('')
    (BASE/'reading_index.md').write_text('\n'.join(index),encoding='utf-8')
    stats=[]
    for group,values in [('priority',['P0','P1','P2']),('category',list('ABCDEGHIJK'))]:
        for v in values:
            rr=[r for r in rows if r[group]==v];valid=[r for r in rr if r['status'].startswith('metadata') and not r.get('duplicate_of')]
            stats.append(dict(group=group,value=v,records=len(rr),verified_unique=len(valid),new_records=sum(r['paper_id'].startswith('N') for r in rr),main_available=sum(bool(have(r['paper_id'],'main')) for r in valid),main_network_downloaded=sum(any(a['status']=='downloaded' for a in have(r['paper_id'],'main')) for r in valid),standalone_supplement_available=sum(bool(have(r['paper_id'],'supplement')) for r in valid),code_available=sum(bool(have(r['paper_id'],'code')) for r in valid)))
    csvwrite('summary_counts.csv',stats)
    summary=dict(records=len(rows),verified_unique=sum(r['status'].startswith('metadata') and not r.get('duplicate_of') for r in rows),new_records=sum(r['paper_id'].startswith('N') for r in rows),bib_entries=len(bib),main_available=len({a['paper_id'] for a in good if a['artifact_type']=='main'}),main_network_downloaded=len({a['paper_id'] for a in good if a['artifact_type']=='main' and a['status']=='downloaded'}),standalone_supplement_available=len({a['paper_id'] for a in good if a['artifact_type']=='supplement'}),code_downloaded=len({a['paper_id'] for a in good if a['artifact_type']=='code'}),public_artifact_files=len({a['repo_path'] for a in good if a.get('repo_path')}))
    summary.update(main_available=len({aliases.get(a['paper_id'],a['paper_id']) for a in good if a['artifact_type']=='main'}),main_network_downloaded=len({aliases.get(a['paper_id'],a['paper_id']) for a in good if a['artifact_type']=='main' and a['status']=='downloaded'}))
    (BASE/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
    report=['# 文献获取与核验报告','',f'统计时间：{stamp()}；检索截止：2026-11-26。','', '**状态：已完成一轮有限范围的检索与获取；全面收集任务仍有未完成项，不能视为正式系统综述或穷尽检索。**','', '本轮仅写入 literature/comprehensive_review_20261126/；未改论文、假设、估计方法或实验。原有目录仅用于来源核对和去重。','', '## 实际统计','',json.dumps(summary,ensure_ascii=False,indent=2),'', '|分组|记录数|核验去重后|新增|正文可用|本次联网正文|独立补充可用|代码可用|','|---|---:|---:|---:|---:|---:|---:|---:|']
    for s in stats:report.append('|'+s['group']+':'+s['value']+'|'+'|'.join(str(s[k]) for k in ['records','verified_unique','new_records','main_available','main_network_downloaded','standalone_supplement_available','code_available'])+'|')
    report.extend(['','正文按论文 ID 去重，PDF/JATS 同文不同版本不重复计数；联网下载与既有本地文件分别计数。独立补充材料与正文内嵌附录分别管理。失败记录是尝试次数，不是失败论文数，见 failures.csv；每篇的最终可用性以 resolved_catalog.csv 为准。','', '## 检索与覆盖限制','', '- 141条种子逐条解析；搜索词和真实论文分表。Crossref匹配需题名相似、作者和年份支持；错配的软件包和预印本/期刊版不混为一条正式引文。','- 八组任务关键词进行了 Europe PMC 检索和 2024–2026 独立增量检索，并作 Crossref 增量搜索；检索日期、API命中总数和取回条数见日志。关键词结果为有界候选页，尚未穷尽所有命中。','- 引文追踪见 citation_edges.csv：OpenAlex后向参考文献和前向引用；每节点前向最多取400条，二层追踪优先取30个相关近邻。其余队列保留在边表，尚待后续继续。','- 新候选采用题名初筛与主数据库书目核验；未逐篇完成摘要/全文适用性审查，新增记录不表示方法已被认定适用于本论文。','- 部分PMC入口返回HTML验证页、Europe PMC正文接口超时/错误、部分出版商禁止自动下载。未绕过验证或付费墙；返回HTML未计作PDF。','- 无真实Unpaywall联系邮箱配置，未调用该服务。Google Scholar、Web of Science、Scopus未使用已认证会话，未计为已检索数据库。arXiv主要用于定位版本与获取作者稿，未完成全库关键词检索。','- Crossref更正/撤回关系已保留在 publication_status.csv；仅说明所取元数据是否带通知，不能替代全面撤稿库和每个出版社Crossmark人工核验。','- 全文、独立补充及作者代码仍有未取得项；not_located表示本轮来源未定位，不能断言作者没有提供。','', '## 许可与本地文件','', '只有PDF首页明确标注CC BY 4.0的JMLR文章以及后续具有明确许可证据的文件可公开同步。开放可读本身不构成上传许可。其余PDF和代码压缩包保留于被.gitignore忽略的 local_private/，下载hash、来源、版本仍公开。既有本地出版商文件未再分发。未下载患者级数据。','', '## 失败与后续工作','', '完整逐项失败、未定位附件/代码和未解析记录见 failures.csv 和 search_leads.csv。优先人工取得P0缺失正文及配套期刊补充，核对不同版本；随后处理P1/P2失败项，继续未分页引用和未追踪的二层队列。对新候选补充摘要和全文层面的纳排理由，再做第三方书目核查。','', 'P0最终未取得正文：'])
    for r in rows:
        if r['priority']=='P0' and r['status'].startswith('metadata') and not have(r['paper_id'],'main'):report.append('- '+r['paper_id']+' '+r['title']+'；'+r.get('source_url','')+'；状态 '+r['status'])
    (BASE/'acquisition_report.md').write_text('\n'.join(report),encoding='utf-8')
    versions={p:importlib.metadata.version(p) for p in ['pypdf','fonttools','pymupdf','cryptography','bibtexparser']}
    (BASE/'scripts'/'dependency_versions.json').write_text(json.dumps(versions,indent=2),encoding='utf-8')
    print(json.dumps(summary),flush=True)

if __name__=='__main__':run()
