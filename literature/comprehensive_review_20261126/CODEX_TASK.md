# Codex 执行任务：系统性文献搜索、合法获取与入库

## 范围与边界
研究主题：竞争风险数据下基于分位数准则的两阶段个体化治疗规则。现行研究对象是基线协变量下两准则顺序优化，不等于两次临床治疗。研究背景包括条件CIF分位数、总体首次事件时间、重点事件、有限随访截断；不据此决定论文新理论、估计器或模拟参数。
输入：literature_catalog.csv（141条种子，55条已有入口，86条待搜索，其中包含专题搜索词，不代表141篇论文）；读取原有 literature/quantile_treatment_rules/ 和 literature/decision_theory_review_20261126/ 只读去重。
优先级P0=26，P1=100，P2=15；仅用于获取顺序，不表示学术结论。
本仓库为公开仓库。仅同步有明确再分发许可的开放全文及其许可证明；开放阅读不等于允许再分发。其他合法获得的文件存放本地非跟踪目录，不提交。不要绕过付费墙、登录、CAPTCHA或反爬限制；不得上传患者级数据、访问凭据、受限PDF、学校授权文件。

## 一、书目解析与扩展搜索
1. 对每一条种子核对 Crossref / PubMed / Europe PMC / OpenAlex / 出版社 / arXiv / 作者机构页面。按题名、作者、年份交叉核实；记录 online year 和 issue year 分开，DOI小写归一化。特别区分 Yu Zhou 2023、Jie Zhou 2021、Christina Zhou 2024。
2. 搜索线索与真实论文分表保存，不虚构DOI、作者、年份、期刊、PDF入口。多篇候选均保留候选证据，待人工确认；搜索型记录可解析为多篇。
3. 使用核心P0文献、综述（Peng 2021；Competing Risks: Concepts, Methods, and Software；Optimal Treatment Regimes: A Review and Empirical Comparison）进行两向引文追踪：参考文献和 citing works；在首次筛选后对新增直接近邻再追踪一轮，记录来源seed和扩展深度。不限于预列作者或期刊。
4. 经典文献不限年份；现代专题搜索截至2026-11-26。2024–2026独立增量检索，检查预印本是否已正式发表、更正或撤回。
5. 数据库：PubMed/Europe PMC、Crossref、OpenAlex、arXiv、JASA/JRSSB/Biometrika/Biometrics/Biostatistics/AoS/Statistics in Medicine/Lifetime Data Analysis/JMLR、作者主页。Google Scholar、Web of Science/Scopus在可合法访问时辅助使用；不能访问须记录。
6. 检索组合（适配各数据库语法，保存原始查询与日期）：
   - ("competing risks" OR "competing events" OR "subdistribution") AND ("optimal treatment regime" OR "individualized treatment rule" OR "policy learning" OR "optimal decision")
   - ("quantile" OR "percentile" OR "distributional welfare" OR "risk-sensitive") AND ("optimal treatment" OR "individualized decision" OR "policy learning") AND (survival OR censored OR competing OR outcome)
   - ("competing risks" OR "cumulative incidence") AND ("quantile regression" OR "quantile inference" OR "conditional quantile" OR "inverse CIF")
   - ("individualized treatment" OR "treatment regime" OR "policy learning") AND ("risk constraint" OR "multiple outcomes" OR "near-optimal" OR "set-valued" OR "noninferiority" OR "lexicographic" OR "epsilon constraint" OR "prioritized outcomes")
   - ("policy learning" OR "treatment rule") AND (regret OR consistency OR "margin condition" OR "non-unique" OR "cube root" OR "value function") 
   - ("competing risks" OR censored OR survival) AND ("quantile loss" OR "proper scoring" OR "Brier score" OR "policy evaluation" OR "restricted mean time lost" OR "restricted mean survival time")
   - (quantile OR "cumulative incidence") AND (joint OR vector OR multivariate) AND (loss OR score OR regret OR decision)
   - ("acute myeloid leukemia" OR AML) AND ("conditioning intensity" OR myeloablative OR "reduced intensity") AND (relapse OR "non-relapse mortality" OR "disease risk index")
7. 纳入：直接估计/优化相关统计目标、理论证明工具、评价与因果识别、相关临床证据。排除：只有术语重合、纯算法无关医疗决策、重复版本、不可核实来源；保留筛选理由。区分预测、治疗效应、政策价值；区分个体与人群约束、条件与边际分位数、CIF与净分布。
8. 每次查询记录日期、数据库、原始query、命中数（若API给出）、检索数、纳入数和排除原因；无法获知总数就标NA。形成流程统计，不声称完成正式系统综述或穷尽全部文献。

## 二、全文与附录获取
逐条尝试：官方OA→PMC/Europe PMC→arXiv→作者/机构合法存档→官方补充材料→合法代码仓库。可利用 Unpaywall（使用真实合法配置的联系邮箱，不编造）与 Crossref links。下载须记录来源URL、最终URL、版本、日期、许可、字节数、SHA256。校验 magic bytes %PDF、pdfinfo/pdftotext、标题首页、页数；拒绝HTML/CAPTCHA伪PDF。补充材料单独保存并确认属于对应版本；官方正文、作者预印本、supplement不能互相冒充。ZIP及代码只获取来源明确的公开资源，记录版本/commit/license，不执行下载来的脚本。
无法合法取得全文或附录：标明 paywall / no_oa / captcha / broken_link / not_found / license_unclear；提供出版社、DOI、作者主页或学校图书馆人工获取路径。
OA但不允许再分发或许可证不清晰：仅提交元数据、合法下载链接和原创笔记；本地合法下载文件放 local_private/，该目录gitignore。明确允许再分发才提交PDF，保留许可证、归属、来源；不把仅有public URL当作许可。体积超限时保留链接和hash，不强行使用LFS。
不复制大量受版权保护的正文，不将全文机器翻译当作原创精读。笔记以公式编号、页码、独立解释及独立推导为主。

## 三、仓库输出（在本目录内新增，原有工作不改）
- resolved_catalog.csv：paper_id, seed_id, authors, title, journal, year_online, year_issue, doi, pmid, pmcid, arxiv, version, category, priority, source_url, abstract_url, relevance, status, duplicate_of, discovery_source
- search_log.csv：date, database, query, hits, retrieved, screened, included, notes
- screening.csv：candidate_id, decision, reason, evidence_url
- references.bib：验证过的书目，DOI去重，预印本与正式版关联
- download_manifest.csv：paper_id, artifact_type(main/supplement/code/data_dictionary), version, status, source_url, final_url, license, license_evidence, local_path, repo_path, sha256, bytes, pages, fetched_at, error
- acquisition_report.md：各类与优先级的完成情况、无法取得清单、需人工授权清单、下一轮搜索建议。
- reading_index.md：每篇原文的正文/附录/代码入口、可用性、建议精读位置（只在查看原文后填章节编号，不虚构）。
- scripts/：实际执行的检索下载代码、依赖版本、运行说明；遵守API限流，有重试和断点恢复，token不提交。
- open_access/：仅明确许可可再分发的正文与补充材料；按paper_id归档。
- local_private/：本地非跟踪文件；.gitignore确保不提交。
- notes/：后续精读逐篇独立，现阶段不替论文确定理论结论。

## 四、核验与交付
先完成P0，逐批提交P1/P2和新增候选。每批汇报准确数量、重复数、全文可用数、补充可用数、许可状态、失败原因。不得把摘要、搜索结果、仅链接或下载失败计为已取得全文。核对重复DOI、路径、hash、BibTeX和CSV可读性；用git status/diff检查无原有论文及实验修改、无敏感或受限文件。报告实际commit SHA。
需要人工取得的文章保持未完成状态；不要承诺访问失败后一定能取得。只有完成检索和筛选、说明覆盖与限制后才可报告本轮文献收集结束。本轮不是论文理论改写任务。
