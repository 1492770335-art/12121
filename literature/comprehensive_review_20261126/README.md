# 全面文献检索与获取任务（2026-11-26）
研究主题：竞争风险数据下基于分位数准则的两阶段个体化治疗规则。

- [人类可读目录](01_literature_catalog.md)
- [CSV种子清单](literature_catalog.csv)
- [Codex执行任务](CODEX_TASK.md)
- [既有理论精读](../decision_theory_review_20261126/README.md)
- [既有分位数文献笔记](../quantile_treatment_rules/README.md)

检索截止日期为2026-11-26，执行及最终核验持续至2026-11-27（北京时间）。本轮已实际检索、下载、入库；存在获取失败与覆盖限制，详见报告，不能视为穷尽检索或正式系统综述。

初始141条种子（P0=26、P1=100、P2=15）已逐条处理。专题检索和两层引文追踪扩展后，目录共785条记录，其中新增644条；725条通过书目与范围筛选并写入BibTeX。搜索词、软件、更正、重复版本、排除项和待核验项另有状态，不冒充已纳入论文。分类A涵盖生存政策(F)，共10个文件分类。

实际全文可用208篇，其中207篇本次联网取得、1篇仅有既有本地文件。PDF涉及203篇、JATS XML涉及7篇，两者有重叠。独立补充材料本次联网下载成功0份，核验既有本地补充1份；正文内嵌附录另有索引。取得5个固定commit的代码包。公开同步的全文为1份明确CC BY许可的PDF和7份带明确许可声明的JATS XML；其余文件仅保留本地，未上传患者数据。

- [获取报告与P0失败清单](acquisition_report.md)
- [完整解析目录及逐篇状态](resolved_catalog.csv)
- [原始查询日志](search_log.csv)、[流程数量](search_flow.csv)、[分组统计](summary_counts.csv)
- [主引文边表](citation_edges.csv)、[补充引文追踪](citation_edges_supplementary.csv)
- [初筛记录](screening.csv)、[最终范围复核](screening_final.csv)
- [BibTeX数据库](references.bib)
- [下载、版本、许可与SHA256清单](download_manifest.csv)
- [缺失全文的论文清单](missing_fulltext_papers.csv)、[逐项失败](failures.csv)、[失败分类与人工入口](failure_classification.csv)
- [精读入口索引](reading_index.md)、[实际观察到的页码标题](reading_anchors.csv)、[内嵌附录索引](embedded_appendices.csv)
- [作者代码清单](code_manifest.csv)、[许可证据](license_evidence/)、[可再分发全文](open_access/)
- [运行代码与说明](scripts/RUNNING.md)、[完整性核验结果](validation.json)

原有论文、理论假设、估计方法和模拟实验没有改动。仅本目录新增/更新。local_private/被Git忽略，包含受限或许可不明的合法本地文件、原始响应缓存和页面核验图；不会公开同步。
