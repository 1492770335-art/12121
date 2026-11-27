# 自主文献精读：第一批理论审查
原始资料锁定到 d433ba9d4171abd797a4569a266c03552ae574fc。当前文献库725条核验书目、221个全文库入口、79个公开全文条目（存在重复版本），不是全部可读。研究不预设本课题定理；没有修改论文、假设、估计器或模拟。
- [A02 Zhou 2024](A02_Christina_Zhou_2024_decision_theorem.md)：Theorem1 和候选集证明逐逻辑步骤核读，曲线森林定理等仍待完成。
- [C02 Meng 2020](C02_Meng_2020_sets_and_evaluation.md)：候选集合、代理风险、评价式(12)(13)及原文定理；独立附录未取得。
- [Li et al. 2023](D_Nbbecc5ccd4_Li_2023_weighted_quantile.md)：分位数估计与部分附录核读，公式及其余证明待复核。
- [阅读队列](reading_queue.csv)：221入口状态，不等于725篇逐篇筛选完成。金融、能源、预测等标题明显偏离的条目保留待复审，不机械精读无关资料。
原文可读≠已读；摘要筛选≠精读；源码读取≠全部数学核验；独立推导≠作者定理。完整精读计数仍为0。先补齐核心原文（A03正式正文和补充、A01、B01、C01、D01/D03/D04/D05、E01/E02、I01等），再推进队列；本目录为阶段性笔记，不是最终理论选型。

## 第二阶段：Zhou 2023主线收尾及顺序精读
- [Zhou 2023主线](zhou2023_mainline/README.md)：正式正文/补充均已核读；外部条件矩阵见11，严格验收残余限制保留。根据用户允许，开始其他论文，不提前构建本课题理论。
- [Wang 2018 B01](B01_Wang_2018_Quantile_Optimal_Treatment_Regimes.md)：用户作者稿与PMC正文，静态主证明；独立补充缺失。
- [Xiao 2019 B02](B02_Xiao_2019_Conditional_quantile_and_robust_loss.md)：用户作者稿，六个理论结论、pinball风险恒等式及条件/边际分位数反例；原附录缺失。
- [Peng–Fine 2007/2009访问缺口与Sun 2012](D01_D03_Peng_Fine_access_and_Sun_2012.md)：两篇原文证明未取得；Sun正式原文主要估计方程、条件和渐近证明主干已核读，截图失败。
阅读队列保持原获取状态字段不变，另更新精读状态。Sun为本批外部新增阅读，不人为增补为原221个入口。下批优先补Wang/Xiao附录和Peng–Fine原文；并推进Jie Zhou 2021、Wang–Fu–Zeng 2018、Qian–Murphy及Gneiting等。所有笔记未修改硕士论文或实验。

## 第三阶段：课题文献充分性目标与约束/评价/分位数估计
- [总目标及八项验收](00_RESEARCH_SUFFICIENCY_GOAL.md)
- [Wang–Fu–Zeng 2018](C01_Wang_Fu_Zeng_2018_Benefit_risk.md)：总体约束解析解、Appendix A、互补松弛及比值原子反例。
- [Jie Zhou 2021](A01_Jie_Zhou_2021_Restricted_CR.md)：原文HTML可读，约束目标、估计/模拟、作者明确未解决的渐近理论；PDF公式图及独立附录待取得。
- [Gneiting 2011 与 Fissler–Ziegel 2016](I01_I06_Gneiting_Fissler_Ziegel_Scoring.md)：分位数评分、联合评分、Osband原则及勘误；独立推导评分与策略评价区别。
- [Luedtke–Chambaz 2020](E02_Luedtke_Chambaz_2020_quantile_regret.md)：补读分位数regret Cor12、Lemma11及Appendix B。
- [Peng 2021](D05_Peng_2021_Survival_quantile_review.md)：正式PDF已取得，式13/14及估计器/可达域分析。Peng–Fine 2007/2009、Lee–Han2016原证明仍未取得。
本轮新增6份文件（含总目标），更新6条阅读状态；所有原获取状态字段保留。文献充分性八关均未最终验收。理论和实验未改动。


## 第四阶段：森林一致性与多结局规则融合
- [Zhou 2024 森林理论](A02_Christina_Zhou_2024_Forest_proofs.md)：作者TeX附录D/E、四个辅助命题、独立条件化证明及原因构成振荡反例。连同原决策笔记覆盖三个定理主干。外部Cho证明与全部模拟/实现仍待核。
- [Gao–Wang–Zeng 2024](Gao_2024_Fused_ITR_agreement_and_value.md)：正文及附录B.4/B.5主证明，标签一致率、价值损失、分类校准及单侧/多结局界的区别。截图失败，外部熵及其余证明待核。
- 访问复查：Peng–Fine 2007出版社购买页，2009 Taylor & Francis 403；Laber 2014 PMC验证页。未取得全文的条目不标完成。



## 第五阶段：删失分位数评价、非唯一最优规则及异质性
- [Li–Peng 2017](I03_Li_Peng_2017_Censored_quantile_prediction.md)：正文三个定理、IPCW评分、预测R¹及嵌套模型二阶展开；独立附录链接失败。
- [Luedtke–van der Laan 2016](E03_Luedtke_vdLaan_2016_Nonunique_optimal_rules.md)：正式电子重印，Theorem1/2/8关键数学机制、独立margin证明及鞅推断分解；附录未完全核读。
- [Laber 2014](Laber_2014_Set_valued_competing_outcomes.md)：找到arXiv v2，静态双阈值集合、动态兼容集合与枚举，独立边界推论；正式版、PDF图像及多治疗扩展待核。
- [PATH 2020](PATH_2020_HTE_and_policy_disagreement.md)：异质性共识及推荐比例/改判率/价值差的独立分解；E&E和观察队列相关理论待补。
本批新增4份研究笔记，更新2条原阅读队列记录。Laber/PATH未在原221入口中找到同题名，保留独立索引而不改变原文献总数。Peng–Fine与Lee–Han搜索仍未获得完整原文；另定位Smoothed quantile regression analysis of competing risks及A kernel nonparametric quantile estimator for right-censored competing risks data作为下一轮原始研究线索，尚未精读。


## 第六阶段：直接分位数估计、截断端点及LK16-02临床证据
- [Choi–Kang–Huang 2018](Choi_2018_induced_smoothing_CR_quantiles.md)：索引文本核对式(3)(5)，独立凸目标、Jacobian及oracle局部展开。完整正文/附录访问失败，不能标为全文精读。
- [Fan–Ding–Zhang 2020](Fan_2020_kernel_CR_quantile_and_endpoint.md)：索引中Theorem2.1文字、部分条件、模拟补充；独立AJ影响函数与端点三情形推导。精确Bahadur余项及原始证明未取得。
- [Bejanyan 2021 LK16-02](K01_Bejanyan_2021_LK16_02_clinical_evidence.md)：官方研究身份、原论文索引及摘要分层HR与36月概率；全文图表和数据筛选未重新核验。
Peng–Fine原文仍缺。不得把检索片段或独立推导当作作者全部原证明。
