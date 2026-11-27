# 本地文献库同步与远端精读访问报告

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

本地逐页转换记录142条，对应141份不同受限PDF；所有相应原件哈希和物理页分段均检查。5份HTML另生成结构化文本、原始MathML与公式图片缺口清单，不编造分页或公式。

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

验证的既有原件提交：`868cc255387c6282351d6fcb84eb5fcb49ae76a9`。367个正文/转换/源码路径的远端Git blob SHA与本地文件一致。GitHub连接器完整读取210个文件：82份Markdown、121个TeX、7份XML；返回文本长度逐项与本地相同，0个读取失败、0个长度不符、0个LFS指针。原始TeX中已有的附录/证明源码也包括在121个读取中。

另从raw.githubusercontent.com实际读回2份47页原始PDF，校验PDF签名、SHA256、页数及文本层。GitHub fetch_file的base64模式对一次PDF样本返回空正文，因此不声称连接器已直接解析全部PDF；连接器精读路径应使用已验证的Markdown/TeX/XML。当前独立公开补充文件为0，不虚报补充下载或读取成功；嵌入式附录与独立补充分开记录。

证明定位CSV为每份公开PDF原件新增；PDF原始内容、原TeX与已有全文转换没有被改写。物理页、印刷页候选和人工确认页码分开；文本中的数学字形/分式/上下标/图表不能因成功取回就视为已准确转换。全公式人工审校仍未完成。

读取明细：[remote_text_read_verification.csv](local_sync_20261127/remote_text_read_verification.csv)；哈希明细：[remote_blob_verification.csv](local_sync_20261127/remote_blob_verification.csv)；逐篇文件路径与状态：[remote_access_manifest.csv](remote_access_manifest.csv)。最终发布提交SHA在本次交付回复及GitHub提交历史中记录；随后会从新提交再次读取索引、定位与报告，结果另记publication_readback.json。

## 受限文献的实际处理

原件、全文Markdown/TXT、逐页图像或全文编码均未发布。D03下载封面明确限制再分发；arXiv默认非独占分发许可和PMC公开可读本身不构成第三方再分发授权。受控分享已准备具体仓库名、逐文件路径/哈希、权限待核清单和创建/连接步骤，见[CONTROLLED_SHARING_PROPOSAL.md](CONTROLLED_SHARING_PROPOSAL.md)与[CONTROLLED_SHARE_CANDIDATES.csv](CONTROLLED_SHARE_CANDIDATES.csv)。没有把私库当作版权豁免；当前没有已确认满足条件的受限文件，未擅自创建私库。

本地Codex已经能读取这些原件。若需要另一ChatGPT远端聊天获取原始证明，可在适用权利允许时直接向该研究聊天提供[CHATGPT_UPLOAD_CORE_FILES.csv](CHATGPT_UPLOAD_CORE_FILES.csv)列出的核心文件；这些文件本轮未自动上传到ChatGPT。不能仅给出本地路径就声称远端已能读到。

## 八项文献研究验收继续推进

本轮推进关口2：取得D03本地原始证明并纠正访问状态；推进关口1/4：定位B01/B02/C01/C03与A03已有附录及版本差异；推进关口5/7：保存I03与K01完整官方HTML。八关仍全部保持开放或部分完成，不以文件同步代替理论验收。关口2尚缺D01/D02/D04等；关口1/4/5仍有最终补充缺口；关口3外部定理、关口6因果异质性、关口7图表与数据定义、关口8全目录相关性/创新性筛查尚未闭环。下一步研究必须引用具体原件与版本，不能直接据本轮整理确定本课题新理论。
