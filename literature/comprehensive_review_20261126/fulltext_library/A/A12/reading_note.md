# A12：版本与精读准备札记

题名：Q-learning with censored data。原文入口：https://doi.org/10.1214/12-aos968。

目录研究用途：删失动态规则。这项用途来自检索目录，尚未据此认定原文定理适用于本项目。

本札记记录文件身份、实际扫描到的位置和后续精读问题，不复制受限正文，也不声称已完成证明有效性审核。

在本地原始PDF中观察到以下定位（物理页码；不同SHA代表不同版本）：
- PDF第4页；文件 `6f96bbc733ec`；标签：supplementary m
- PDF第10页；文件 `6f96bbc733ec`；标签：Lemma 4.1
- PDF第11页；文件 `6f96bbc733ec`；标签：Proof
- PDF第13页；文件 `6f96bbc733ec`；标签：condition
- PDF第15页；文件 `6f96bbc733ec`；标签：Lemma 4.1、Theorem 6.1
- PDF第16页；文件 `6f96bbc733ec`；标签：Corollary 6.2、Proof
- PDF第17页；文件 `6f96bbc733ec`；标签：Proof o、Theorem 1
- PDF第28页；文件 `6f96bbc733ec`；标签：APPENDIX、Lemma A.1
- PDF第29页；文件 `6f96bbc733ec`；标签：Proof、Corollary A.2、Corollary A.3、Lemma A.4、Corollary A.5
- PDF第30页；文件 `6f96bbc733ec`；标签：Proof、Lemma A.6、Lemma A.1
- PDF第31页；文件 `6f96bbc733ec`；标签：SUPPLEMENTARY M

后续精读检查：先确定统计目标、数据结构与版本，再分别记录识别条件、估计条件和决策边界条件。对每个拟引用的结论，应沿正文—附录—外部引理核对依赖；比较条件分位数、边际分位数、CIF反演和净分布目标时，不预设它们相同。公式以原始PDF及作者TeX为准。
