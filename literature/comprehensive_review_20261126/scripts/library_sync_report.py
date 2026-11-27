"""Finalize actual remote-read evidence, reports and a publication allowlist."""
from library_build import *
import io

REF='868cc255387c6282351d6fcb84eb5fcb49ae76a9'
def run():
    out=ROOT/'local_sync_20261127';repo=BASE.parent.parent
    allow=json.loads((WORK/'sync_publish_manifest.json').read_text(encoding='utf-8'));changed={repo/a['path'] for a in allow}
    def put(p,s):write(p,s);changed.add(p)
    def js(p,v):put(p,json.dumps(v,ensure_ascii=False,indent=2)+'\n')
    def csvout(p,rows):
        stream=io.StringIO(newline='');fields=list(dict.fromkeys(k for a in rows for k in a));w=csv.DictWriter(stream,fieldnames=fields);w.writeheader();w.writerows(rows);put(p,stream.getvalue())
    reads=json.loads((WORK/'sync_remote_verified_complete.json').read_text(encoding='utf-8'));blobs=json.loads((WORK/'sync_blob_verification.json').read_text(encoding='utf-8'));pdfs=json.loads((WORK/'sync_remote_pdf_samples.json').read_text(encoding='utf-8'))
    assert all(a['success'] and a['full_text_length_verified'] and not a['lfs_pointer'] for a in reads)
    assert all(a['blob_verified'] for a in blobs)
    assert all(a['success'] for a in pdfs)
    csvout(out/'remote_text_read_verification.csv',reads);csvout(out/'remote_blob_verification.csv',blobs);js(out/'remote_pdf_sample_verification.json',pdfs)
    idx=json.loads((ROOT/'index.json').read_text(encoding='utf-8'));byid={e['paper_id']:e for e in idx};lookup={a['path']:a for a in reads}
    manifest=list(csv.DictReader((ROOT/'remote_access_manifest.csv').open(encoding='utf-8-sig')))
    for a in manifest:
        e=byid[a['paper_id']]
        paths=['literature/comprehensive_review_20261126/fulltext_library/'+p for p in e['public_markdown']+e['original_tex']+e['public_xml']]
        if paths:
            assert all(p in lookup for p in paths)
            a['remote_read_verification']='full_utf8_content_and_length_verified_via_github_connector';a['verified_ref']=REF
        else:a['verified_ref']='fulltext_not_on_remote'
    csvout(ROOT/'remote_access_manifest.csv',manifest)
    core=list(csv.DictReader((WORK/'sync_base_core_status.csv').open(encoding='utf-8-sig')))
    for a in core:
        if a['paper_id'] in ['D05','I03','K01']:
            a.update(fulltext_status='local_only',downloaded_main='1',reason='Full official article HTML locally available; PDF not acquired; formula/image gaps retained')
        a['downloaded_main_format']='html_only' if a['paper_id'] in ['D05','I03','K01'] else 'pdf' if a['downloaded_main']=='1' else ''
    csvout(ROOT/'core_status.csv',core)
    counts=json.loads((out/'current_counts.json').read_text(encoding='utf-8'));stats=json.loads((WORK/'sync_base_summary.json').read_text(encoding='utf-8'))
    stats.update(entries=counts['entries'],public_entries=counts['public_readable'],local_only_entries=counts['local_only'],not_acquired_entries=counts['not_acquired'],reading_notes=counts['entries'],controlled_sharing_approved=0,local_html_only_entries=4,core_new_fulltexts=8,last_sync_scan_at=stamp(),latest_access_report='LOCAL_LIBRARY_SYNC_REPORT.md',last_verified_artifact_ref=REF)
    js(ROOT/'summary.json',stats)
    prefix='> 2026-11-27 全库访问复核更新：当前223条入口；79条有公开全文，139条本地限定（其中4条仅有HTML而无PDF），5条正文仍缺。公开367个正文/转换/源码文件哈希已核对，210个Markdown/TeX/XML已通过GitHub连接器完整读取并比对长度。最新结果见[完整同步报告](LOCAL_LIBRARY_SYNC_REPORT.md)与[逐篇访问清单](remote_access_manifest.csv)。以下旧统计保留为历史快照。\n\n'
    for f in ['README.md','REPORT.md']:put(ROOT/f,prefix+(WORK/('sync_base_'+f)).read_text(encoding='utf-8'))
    old=(WORK/'sync_base_D01_D03_note.md').read_text(encoding='utf-8')
    put(BASE/'theoretical_studies'/'D01_D03_Peng_Fine_access_and_Sun_2012.md','> 2026-11-27 更正：Peng–Fine 2009的15页原始期刊PDF和嵌入式渐近证明已在本地找到；此前“原证明未取得”的描述已过时。其PDF12–14/印刷1450–1452含主要证明。见[本地原始证明定位与复核](D03_Peng_Fine_2009_local_original_proof_map.md)。公开全文仍受限；2007原文仍未取得。以下为先前访问记录。\n\n'+old)
    local=list(csv.DictReader((out/'local_conversion_manifest.csv').open(encoding='utf-8-sig')))
    stats_private=dict(pdf_artifact_records=sum(a['format']=='pdf' for a in local),unique_pdf_files=len({a['sha256'] for a in local if a['format']=='pdf'}),html_article_files=sum(a['format']=='html' for a in local),total_pdf_pages=sum(int(a['pdf_pages']) for a in {a['sha256']:a for a in local if a['format']=='pdf'}.values()))
    scan=json.loads((out/'inventory_summary.json').read_text(encoding='utf-8'));acq=json.loads((out/'acquisition_summary.json').read_text(encoding='utf-8'))
    summary=dict(scan=scan,current_entries=counts,private_conversions=stats_private,remote_verification=dict(verified_ref=REF,asset_blob_hashes=len(blobs),complete_connector_reads=len(reads),markdown_reads=sum(a['path'].endswith('.md') for a in reads),tex_reads=sum(a['path'].endswith('.tex') for a in reads),xml_reads=sum(a['path'].endswith('.xml') for a in reads),length_mismatches=0,lfs_pointers=0,pdf_binary_http_samples=len(pdfs),github_fetch_file_binary_base64='Returned empty content for one sampled PDF; raw HTTP original-PDF bytes were independently verified. Use Markdown/TeX/XML for connector reading.',independent_public_supplement_files=0),acquisition=acq)
    js(out/'validation.json',dict(errors=[],**summary))
    report=f"""# 本地文献库同步与远端精读访问报告

日期：2026-11-27（Asia/Shanghai）。任务来源：[CODEX_LOCAL_LIBRARY_SYNC.md](../CODEX_LOCAL_LIBRARY_SYNC.md)。本轮仅处理文献、获取日志、索引与文献研究札记，没有修改论文、理论假设、估计方法或模拟实验。公开仓库保持公开；没有创建私库或扩大访问权限。

## 实际结果与计数口径

|文献入口状态|数量|
|---|---:|
|公开全文可由GitHub连接器读取|79|
|获准向独立受控仓库共享的受限条目|0|
|本地限定|139|
|正文仍未取得|5|
|总入口数|223|

139个本地限定入口包含4个仅有完整HTML、没有原始PDF的入口。它们为D05、I03、K01、N95df3c95c9；不能把这些计为PDF下载。C01同时已有作者PDF和本轮HTML。公开原始文件仍为75份PDF、7份XML，全文Markdown/TXT各82份；原始TeX仍为121个路径（内容去重为118个TeX文件）。本轮没有新增公开原始全文；新增的是逐原件证明定位、完整远端读取证据、状态纠正及本地HTML转换。

初始扫描覆盖三个文献根目录及用户提供的桌面文献PDF：967个文件实例，SHA256去重后373个文件，包括240份PDF、118个不同TeX、7份XML、8个ZIP；另1719个非PDF缓存入口未当作论文。重复实例594个。研究ZIP内包含的手册、相邻课题及自身实验包只盘点，不当作论文或共享白名单。用户论文main(1).pdf和无关私人PDF明确排除。扫描后另取得1份作者托管的B02早期预印本表示（与已有稿属于同一版本，不能新增论文计数）及5份完整文章HTML。

本地逐页转换记录{stats_private['pdf_artifact_records']}条，对应{stats_private['unique_pdf_files']}份不同受限PDF；所有相应原件哈希和物理页分段均检查。5份HTML另生成结构化文本、原始MathML与公式图片缺口清单，不编造分页或公式。

## 最关键的原始证明与缺口

- **D03 Peng–Fine 2009：已在本地找到原始期刊稿。** PDF共15页，下载封面1页；正文印刷1440–1453。PDF12–14/印刷1450–1452包含渐近附录、Theorem1、Lemma1、Theorem2及协方差估计论证。SHA256为0e4d84e5c69d4a3dd807d49afd4e85e2f8a0f9dc62f48fddc533dc6738db2078。已查看原始渲染数学页；未声称完成全部外部引理审核。完整原证明仅本地可读；见[原创证明定位札记](../theoretical_studies/D03_Peng_Fine_2009_local_original_proof_map.md)。
- **D01 Peng–Fine 2007、D02 2008 note、D04 Lee–Han 2016：仍缺原始正文/证明。** 出版社403、机构入口超时/作者旧页404，Scholar返回验证页。没有把片段、摘要或其他文献的复述标作原始证明。
- **A03 Yu Zhou：** 正式正文14页、独立补充17页和53页预印本均已在本地，未重复下载。
- **B01 Wang 2018：** 29/34页两个稿件均保留，含嵌入技术证明；独立在线补充仍未取得。
- **B02 Xiao 2019：** 正式NIH作者稿28页与早期36页预印本均可读；早期Appendix A/B含证明。其A1–A8与最终稿C1–C8需版本对照，不能把早期附录冒称为正式补充。
- **C01 Wang–Fu–Zeng：** 36页作者稿及完整HTML可读，含嵌入的证明/算法附录；未确认有另一个独立补充。
- **C03 Laber 2014：** 43页arXiv稿含一般化/枚举及诊断附录；正式独立Web Appendix仍未取得。
- **Choi 2018：** 23页NIH正文可读；独立补充仍缺。
- **Fan 2020：** 完整官方HTML包含技术附录，PDF与supplementary-data PDF仍被验证页面阻挡。公式图片未转写。
- **I03 Li–Peng 2017：** 完整官方HTML已保存；独立补充A及PDF未取得，不能标证明闭环完成。
- **K01 Bejanyan 2021：** 完整临床文章HTML已保存；原PDF和独立补充未取得，图表视觉复核仍欠。

剩余5个未取得正文入口为D01、D02、D04、G01、G04。详见[优先缺口](local_sync_20261127/priority_gaps.csv)、[获取日志](local_sync_20261127/acquisition_log.csv)。

## 实际远端验证

验证的既有原件提交：`{REF}`。367个正文/转换/源码路径的远端Git blob SHA与本地文件一致。GitHub连接器完整读取210个文件：82份Markdown、121个TeX、7份XML；返回文本长度逐项与本地相同，0个读取失败、0个长度不符、0个LFS指针。原始TeX中已有的附录/证明源码也包括在121个读取中。

另从raw.githubusercontent.com实际读回2份47页原始PDF，校验PDF签名、SHA256、页数及文本层。GitHub fetch_file的base64模式对一次PDF样本返回空正文，因此不声称连接器已直接解析全部PDF；连接器精读路径应使用已验证的Markdown/TeX/XML。当前独立公开补充文件为0，不虚报补充下载或读取成功；嵌入式附录与独立补充分开记录。

证明定位CSV为每份公开PDF原件新增；PDF原始内容、原TeX与已有全文转换没有被改写。物理页、印刷页候选和人工确认页码分开；文本中的数学字形/分式/上下标/图表不能因成功取回就视为已准确转换。全公式人工审校仍未完成。

读取明细：[remote_text_read_verification.csv](local_sync_20261127/remote_text_read_verification.csv)；哈希明细：[remote_blob_verification.csv](local_sync_20261127/remote_blob_verification.csv)；逐篇文件路径与状态：[remote_access_manifest.csv](remote_access_manifest.csv)。最终发布提交SHA在本次交付回复及GitHub提交历史中记录；随后会从新提交再次读取索引、定位与报告，结果另记publication_readback.json。

## 受限文献的实际处理

原件、全文Markdown/TXT、逐页图像或全文编码均未发布。D03下载封面明确限制再分发；arXiv默认非独占分发许可和PMC公开可读本身不构成第三方再分发授权。受控分享已准备具体仓库名、逐文件路径/哈希、权限待核清单和创建/连接步骤，见[CONTROLLED_SHARING_PROPOSAL.md](CONTROLLED_SHARING_PROPOSAL.md)与[CONTROLLED_SHARE_CANDIDATES.csv](CONTROLLED_SHARE_CANDIDATES.csv)。没有把私库当作版权豁免；当前没有已确认满足条件的受限文件，未擅自创建私库。

本地Codex已经能读取这些原件。若需要另一ChatGPT远端聊天获取原始证明，可在适用权利允许时直接向该研究聊天提供[CHATGPT_UPLOAD_CORE_FILES.csv](CHATGPT_UPLOAD_CORE_FILES.csv)列出的核心文件；这些文件本轮未自动上传到ChatGPT。不能仅给出本地路径就声称远端已能读到。

## 八项文献研究验收继续推进

本轮推进关口2：取得D03本地原始证明并纠正访问状态；推进关口1/4：定位B01/B02/C01/C03与A03已有附录及版本差异；推进关口5/7：保存I03与K01完整官方HTML。八关仍全部保持开放或部分完成，不以文件同步代替理论验收。关口2尚缺D01/D02/D04等；关口1/4/5仍有最终补充缺口；关口3外部定理、关口6因果异质性、关口7图表与数据定义、关口8全目录相关性/创新性筛查尚未闭环。下一步研究必须引用具体原件与版本，不能直接据本轮整理确定本课题新理论。
"""
    put(ROOT/'LOCAL_LIBRARY_SYNC_REPORT.md',report)
    put(BASE/'LOCAL_LIBRARY_SYNC_REPORT.md','# 本地文献库同步报告\n\n完整报告：[fulltext_library/LOCAL_LIBRARY_SYNC_REPORT.md](fulltext_library/LOCAL_LIBRARY_SYNC_REPORT.md)。逐篇访问结果：[remote_access_manifest.csv](fulltext_library/remote_access_manifest.csv)。\n')
    gates=[('1','统计目标','B01/B02早期附录与版本已定位；最终补充缺口保留'),('2','竞争风险分位数','D03原始附录本地可读；D01/D02/D04仍缺'),('3','决策理论','A03正式独立补充已在本地；外部定理核验仍开放'),('4','约束与多目标','C01嵌入附录及C03早期附录可定位；最终版本对照未完成'),('5','评价理论','I03完整HTML可读，独立补充仍缺'),('6','异质性','本轮没有新增充分的因果异质性原始证据'),('7','临床与数据','K01完整HTML可读；PDF图表、数据字典及筛选仍需复核'),('8','创新性与综合','未完成全目录相关性复审及跨论文证据闭环')]
    csvout(BASE/'theoretical_studies'/'local_sync_acceptance_20261127.csv',[dict(gate=k,topic=t,status='open_partial_not_accepted',actual_access_progress=n) for k,t,n in gates])
    changed.add(Path(__file__))
    # Recompute after all edits; reject bodies of restricted papers in the public set.
    allow=[]
    for p in sorted(changed):
        assert p.is_relative_to(BASE) and 'local_private' not in p.parts
        if p.name in ['original.pdf','original.html','fulltext.md','fulltext.txt']:raise ValueError('Unexpected new fulltext publication '+str(p))
        d=p.read_bytes();allow.append(dict(path=p.relative_to(repo).as_posix(),size=len(d),git_sha=hashlib.sha1(b'blob '+str(len(d)).encode()+b'\0'+d).hexdigest(),kind='text'))
    dump(WORK/'sync_final_publish_manifest.json',allow)
    print(json.dumps(dict(publication_files=len(allow),private_conversions=stats_private,counts=counts,verified_texts=len(reads),blob_checks=len(blobs)),ensure_ascii=False))

if __name__=='__main__':run()
