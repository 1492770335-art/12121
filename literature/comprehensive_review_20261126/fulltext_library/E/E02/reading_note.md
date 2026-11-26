# E02：版本与精读准备札记

题名：Performance guarantees for policy learning。原文入口：https://doi.org/10.1214/19-aihp1034。

目录研究用途：regret、分位数Corollary 12。这项用途来自检索目录，尚未据此认定原文定理适用于本项目。

本札记记录文件身份、实际扫描到的位置和后续精读问题，不复制受限正文，也不声称已完成证明有效性审核。

在本地原始PDF中观察到以下定位（物理页码；不同SHA代表不同版本）：
- PDF第7页；文件 `b88ec4508b03`；标签：Theorem 1、proof o
- PDF第8页；文件 `b88ec4508b03`；标签：Theorem 2
- PDF第9页；文件 `b88ec4508b03`；标签：condition
- PDF第10页；文件 `b88ec4508b03`；标签：assumption o
- PDF第11页；文件 `b88ec4508b03`；标签：condition
- PDF第13页；文件 `b88ec4508b03`；标签：Theorem 1、Theorem 4
- PDF第14页；文件 `b88ec4508b03`；标签：Lemma 6
- PDF第15页；文件 `b88ec4508b03`；标签：Corollary 7
- PDF第16页；文件 `b88ec4508b03`；标签：Lemma 9
- PDF第17页；文件 `b88ec4508b03`；标签：Theorem 1、Corollary 10、Appendix B
- PDF第20页；文件 `b88ec4508b03`；标签：Corollary 14
- PDF第21页；文件 `b88ec4508b03`；标签：Lemma 6、Theorem 1

后续精读检查：先确定统计目标、数据结构与版本，再分别记录识别条件、估计条件和决策边界条件。对每个拟引用的结论，应沿正文—附录—外部引理核对依赖；比较条件分位数、边际分位数、CIF反演和净分布目标时，不预设它们相同。公式以原始PDF及作者TeX为准。
