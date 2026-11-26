# 文献获取与核验报告

统计时间：2026-11-27T00:21:19.473847+08:00；检索截止：2026-11-26。

**状态：已完成一轮有限范围的检索与获取；全面收集任务仍有未完成项，不能视为正式系统综述或穷尽检索。**

本轮仅写入 literature/comprehensive_review_20261126/；未改论文、假设、估计方法或实验。原有目录仅用于来源核对和去重。

## 实际统计

{
  "records": 785,
  "verified_unique": 725,
  "new_records": 644,
  "bib_entries": 725,
  "main_available": 208,
  "main_network_downloaded": 207,
  "standalone_supplement_available": 1,
  "code_downloaded": 5,
  "public_artifact_files": 8
}

|分组|记录数|核验去重后|新增|正文可用|本次联网正文|独立补充可用|代码可用|
|---|---:|---:|---:|---:|---:|---:|---:|
|priority:P0|26|25|0|12|11|1|4|
|priority:P1|744|686|644|192|192|0|1|
|priority:P2|15|14|0|4|4|0|0|
|category:A|65|61|52|24|24|1|2|
|category:B|78|63|66|24|24|0|2|
|category:C|36|32|23|10|10|0|1|
|category:D|124|119|104|18|17|0|0|
|category:E|123|121|107|49|49|0|0|
|category:G|100|98|82|18|18|0|0|
|category:H|46|45|33|16|16|0|0|
|category:I|102|79|85|21|21|0|0|
|category:J|12|12|2|3|3|0|0|
|category:K|99|95|90|25|25|0|0|

正文按论文 ID 去重，PDF/JATS 同文不同版本不重复计数；联网下载与既有本地文件分别计数。独立补充材料与正文内嵌附录分别管理。失败记录是尝试次数，不是失败论文数，见 failures.csv；每篇的最终可用性以 resolved_catalog.csv 为准。

## 检索与覆盖限制

- 141条种子逐条解析；搜索词和真实论文分表。Crossref匹配需题名相似、作者和年份支持；错配的软件包和预印本/期刊版不混为一条正式引文。
- 八组任务关键词进行了 Europe PMC 检索和 2024–2026 独立增量检索，并作 Crossref 增量搜索；检索日期、API命中总数和取回条数见日志。关键词结果为有界候选页，尚未穷尽所有命中。
- 引文追踪见 citation_edges.csv：OpenAlex后向参考文献和前向引用；每节点前向最多取400条，二层追踪优先取30个相关近邻。其余队列保留在边表，尚待后续继续。
- 新候选采用题名初筛与主数据库书目核验；未逐篇完成摘要/全文适用性审查，新增记录不表示方法已被认定适用于本论文。
- 部分PMC入口返回HTML验证页、Europe PMC正文接口超时/错误、部分出版商禁止自动下载。未绕过验证或付费墙；返回HTML未计作PDF。
- 无真实Unpaywall联系邮箱配置，未调用该服务。Google Scholar、Web of Science、Scopus未使用已认证会话，未计为已检索数据库。arXiv主要用于定位版本与获取作者稿，未完成全库关键词检索。
- Crossref更正/撤回关系已保留在 publication_status.csv；仅说明所取元数据是否带通知，不能替代全面撤稿库和每个出版社Crossmark人工核验。
- 全文、独立补充及作者代码仍有未取得项；not_located表示本轮来源未定位，不能断言作者没有提供。

## 许可与本地文件

只有PDF首页明确标注CC BY 4.0的JMLR文章以及后续具有明确许可证据的文件可公开同步。开放可读本身不构成上传许可。其余PDF和代码压缩包保留于被.gitignore忽略的 local_private/，下载hash、来源、版本仍公开。既有本地出版商文件未再分发。未下载患者级数据。

## 失败与后续工作

完整逐项失败、未定位附件/代码和未解析记录见 failures.csv 和 search_leads.csv。优先人工取得P0缺失正文及配套期刊补充，核对不同版本；随后处理P1/P2失败项，继续未分页引用和未追踪的二层队列。对新候选补充摘要和全文层面的纳排理由，再做第三方书目核查。

P0最终未取得正文：
- A01 On restricted optimal treatment regime estimation for competing risks data；https://doi.org/10.1093/biostatistics/kxz026；状态 metadata_crosschecked_crossref_europepmc
- B01 Quantile-Optimal Treatment Regimes；https://doi.org/10.1080/01621459.2017.1330204；状态 metadata_crosschecked_crossref_europepmc
- C01 Learning Optimal Personalized Treatment Rules in Consideration of Benefit and Risk: With an Application to Treating Type 2 Diabetes Patients With Insulin Therapies；https://doi.org/10.1080/01621459.2017.1303386；状态 metadata_crosschecked_crossref_europepmc
- D01 Nonparametric quantile inference with competing risks data；https://doi.org/10.1093/biomet/asm059；状态 metadata_verified_crossref
- D02 A note on nonparametric quantile inference for competing risks and more complex multistate models；https://doi.org/10.1093/biomet/asn044；状态 metadata_verified_crossref
- D04 Covariate-adjusted quantile inference with competing risks；https://doi.org/10.1016/j.csda.2016.02.012；状态 metadata_verified_crossref
- D05 Quantile Regression for Survival Data；https://doi.org/10.1146/annurev-statistics-042720-020233；状态 metadata_crosschecked_crossref_europepmc
- G01 An empirical transition matrix for non-homogeneous Markov chains based on censored observations；https://www.math.ku.dk/bibliotek/arkivet/preprints-fra-ims/1977/preprint_1977_-_no_6_aalen__odd__johansen__s_ren_-_an_empirical_transition_matrix_for_non-homogeneous---.pdf；状态 metadata_verified_institutional_archive
- G02 Regression Models and Life-Tables；https://doi.org/10.1111/j.2517-6161.1972.tb00899.x；状态 metadata_verified_crossref
- G04 A Proportional Hazards Model for the Subdistribution of a Competing Risk；https://doi.org/10.1080/01621459.1999.10474144；状态 metadata_verified_crossref
- G08 Random survival forests for competing risks；https://doi.org/10.1093/biostatistics/kxu010；状态 metadata_crosschecked_crossref_europepmc
- I03 Assessing Quantile Prediction with Censored Quantile Regression Models；https://doi.org/10.1111/biom.12627；状态 metadata_crosschecked_crossref_europepmc
- K01 Myeloablative Conditioning for Allogeneic Transplantation Results in Superior Disease-Free Survival for Acute Myelogenous Leukemia and Myelodysplastic Syndromes with Low/Intermediate but not High Disease Risk Index: A Center for International Blood and Marrow Transplant Research Study；https://doi.org/10.1016/j.bbmt.2020.09.026；状态 metadata_crosschecked_crossref_europepmc