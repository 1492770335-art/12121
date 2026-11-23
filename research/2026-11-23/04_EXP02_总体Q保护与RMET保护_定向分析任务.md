# EXP-02 | 总体分位数保护 vs RMET 保护：定向 Oracle 分析任务

**日期**：2026-11-23  
**状态**：待执行分析协议（不是结果报告）  
**数据来源**：`literature/quantile_treatment_rules/oracle_20261123/original/`；归档中含 `restore.py`、8 个 `oracle-result.partNN`，完整 SHA256 在 `original/README.md`。  
**已有审查**：`literature/quantile_treatment_rules/oracle_20261123/STATISTICAL_REVIEW.md`；`research/2026-11-23/03_Oracle实验完成后的科研判断与后续任务.md`。  
**原则**：原始文件只读；不重新运行 5 个机制的全量 Oracle；不使用任何估计器；不因结果不显著而改 DGP、\(p\) 或时间窗。

## 一、研究问题和可证伪假设

研究同一个患者在同一套 Oracle 真实原因别 CIF 下，**把第一层总体保护从\(Q_{all}\)换成 36 月 RMET**，第二层保持\(Q_1\)最大化，会产生怎样的候选集、处方和结局差异？

- H1（异质性）：不同保护标准不必然选择相同的逐人候选集合，即使「双治疗都允许」的总体比例一致。
- H2（有效信息）：差异是否在 **两治疗的目标分位数均为可达严格内点** 的群体仍然存在？是否集中于边界附近或特定协变量层？
- H3（临床方向）：选择 Q 保护的患者是否真正得到特定风险阈值时间保护？有无 RMET 或 12/36 月原因1/2 CIF 的明显代价？如果没有独特信息，应如实结论为第一层可替换。

## 二、固定配置及比较对象

使用原始实验的配置与代码重新读取，不擅自猜测风险强度/分位数反演的实现。

- 主机制：`PH_tradeoff`、`time_cross`；其他三机制此前结果作为参照，不重新全量运行。
- 主参数：\(p_{all}=0.50\)，\(p_1=0.10\)，\(L=36\) 月，\(\delta_Q=3\) 月；\(t_0=12\) 月作为固定时点结局。
- 规则 Q–Q：
  \[A_Q(z)=\{a:Q_{all,L}^a(z)\ge \max_b Q_{all,L}^b(z)-\delta_Q\},\quad d_Q(z)=\arg\max_{a\in A_Q(z)}Q_{1,L}^a(z).\]
- 规则 RMET–Q1：
  \[R^a(z)=\int_0^{36}S_{all}^a(t\mid z)dt,\quad A_R(z)=\{a:R^a(z)\ge \max_bR^b(z)-\delta_R\},\quad d_R(z)=\arg\max_{a\in A_R(z)}Q_{1,L}^a(z).\]
- \(\delta_R\) 必须来自**独立于最终评价测试记录的校准样本**：匹配 \(P(|R^1-R^0|\le\delta_R)\) 与 \(P(|Q_{all,L}^1-Q_{all,L}^0|\le3)\)。首先复用原始实验 \(results/calibration_raw.csv\) 中的校准结果；如果没有逐重复阈值，核查原始 `src/run.py` 的校准实现并从冻结配置复算，仅补缺。
- 规则平局必须统一：若两个合格处理的 \(Q_1\) 差绝对值不超过原代码定义的数值容差，按原统一平局策略；显式计数平局。不能用规则名区别对待。

## 三、首先检查归档是否有足够逐患者数据

1. 在已连接的仓库内恢复原始 zip，执行 `python literature/quantile_treatment_rules/oracle_20261123/original/restore.py`；核验 SHA256。只读解压至隔离临时目录，不修改/提交原始文件。
2. 阅读原始 `README`、`config.json`、`src/oracle.py`、`src/run.py`、`tests/test_oracle.py`。
3. 优先使用原始结果 CSV：`results/policies_summary.csv`、`results/pairs_summary.csv`、`results/flips_raw.csv`、`results/calibration_raw.csv`、`results/external_cap_summary.csv`。实际文件存在性必须检查，禁止假设记录列齐全。
4. 检查是否存在逐患者: `rep_id, z1, z2, Qall0, Qall1, Q10, Q11, RMET0, RMET1, F1_12_0/1, F2_12_0/1, F1_36_0/1, F2_36_0/1, candidates, actions, reachability`。如字段缺失，可由原始 Oracle 风险代码在**两个主机制**定向补算；尽可能复用已冻结的随机数/逐患者样本。无法恢复完全相同测试患者时，必须将其标识为“新定向 Oracle 补充”，不能假称是旧实验逐行复算。
5. 不允许依据汇总表逆推出个体结局或虚构未保存的微观数据。

## 四、主分析：逐患者候选差异与推荐差异分解

对每个机制/重复/患者计算：
- \(D_Q=Q_{all,L}^1-Q_{all,L}^0\)，\(D_R=R^1-R^0\)，\(D_1=Q_{1,L}^1-Q_{1,L}^0\)。
- 双候选指标 \(B_Q=1\{|D_Q|\le3\}\)、\(B_R=1\{|D_R|\le\delta_R\}\)。
- 候选集合精确不一致 \(M_A=1\{A_Q\neq A_R\}\)、最终处方不一致 \(M_d=1\{d_Q\neq d_R\}\)。分别报告 \(P(B_Q=1)\)、\(P(B_R=1)\)、\(P(M_A=1)\)、\(P(M_d=1)\)。
- 分类计数：两者均双候选；Q 双/R 单；Q 单/R 双；均单且单独允许的治疗相同/不同；重点 Q1 真值平局/严格排序。
- 在统一第二层和平局处理下检验 \(M_d\implies M_A\)。**规则改判必须是候选集差异的子集**。若不成立则先查代码，不能发布结果。
- 候选边界绝对距离 `abs(abs(D_Q)-3)`、`abs(abs(D_R)-delta_R)`；两规则的相对距离尺度不同，必要时除以合理的测试分布尺度，只用于描述而不作等单位强弱比较。
- 对于只占 2%～2.5% 的改判者，报告样本量（每次重复和汇总），不能只报百分比。

## 五、主分析：相同患者的真实结局差（两种规则）

对每个患者定义 **本文减 RMET–Q1**：
- \(\Delta Q_1=Q_{1,L}^{d_Q}-Q_{1,L}^{d_R}\)；
- \(\Delta Q_{all}=Q_{all,L}^{d_Q}-Q_{all,L}^{d_R}\)；
- \(\Delta RMET=R^{d_Q}-R^{d_R}\)；
- \(\Delta F_j(t)=F_j^{d_Q}(t)-F_j^{d_R}(t)\)，\(j=1,2\), \(t=12,36\)；
- \(E_Q=[\max_a Q_{all,L}^a-Q_{all,L}^{d_Q}-3]_+\)；对 RMET–Q1 同样按 **Q–Q 的总体 Q 预算**计算\(E_R\)，以便比较规则 B 对同一保护目标的违反比例与幅度；另外如实报告 RMET 预算是否满足。不能把不同约束的“超额率”直接等价比较。

每个指标必须双口径：
1. **全体测试患者**的平均差，含未改判者的 0 贡献；
2. **改判患者**的条件平均差，附该群体占比、样本数和 Monte Carlo 不确定性。

结果按 200 次重复为统计单元估计 MCSE 或重复级分位区间，不把 100 万个相关模拟患者简单当作真实临床独立样本来报极窄置信区间。已有实验的任何历史结果都应标注为原报告复述，补算结果分开列示。

## 六、分位数可达性与个体异质性

主要分类（按原数值模型精确得到 \(F_j^a(36)\)）：
1. **两治疗双终点都严格内点**：对所有 \(a\)，\(F_1^a(36)>p_1\) 且 \(F_{all}^a(36)>p_{all}\)，排除\(Q=L\)由不可达强行赋值的影响。等号/容差边界单独计数；
2. 某治疗的重点\(Q_1\)不可达；两治疗重点\(Q_1\)均不可达；
3. 总体\(Q_{all}\)不可达或紧邻\(L\)。

所有分类报告全体群体占比、改判率、\(\Delta\)结局；主文如采用“严格内点”子群必须同时披露全体结果，避免选择性报告。

异质性主分组预设：\(Z_1\) 四分位 × \(Z_2\in\{0,1\}\)，报告样本量、Q/R 推荐治疗1比例、改判率、平均\(\Delta Q_1,\Delta Q_{all},\Delta RMET\)、两原因\(\Delta CIF(36)\)。绘制二维 \((D_Q,D_R)\) 与边界标注的分组散点/密度图，以及\((\Delta Q_1,\Delta F_1(36))\) 的改判子群联合分布。

在 `time_cross`：从**现有**\(p_1\)网格与已定义患者中展示 3 个典型患者（真值翻转/不翻转/保护排除翻转），完整展示 0、1 治疗的\(F_1(t),F_2(t),F_{all}(t)\)曲线与 Q1(p) 轨迹。\(p=0.10\) 为主分析；\(p=0.15\) 仅作为预先列出的风险阈值比较，不根据图挑选对本文有利的\(p\)。

## 七、交付文件、验收和结果判断

建议新建（不要覆盖原始归档或此前综述）：
- `experiments/EXP-02/README.md`（研究假设、运行命令、输入路径、数据可用性清单）
- `experiments/EXP-02/src/analyze_existing_oracle.py`；必要时增加独立 `targeted_oracle.py`，不要改原 `src/oracle.py`。
- `experiments/EXP-02/results/table_A_candidate_sets.csv`
- `experiments/EXP-02/results/table_B_counterfactual_outcomes.csv`
- `experiments/EXP-02/results/table_C_reachability_heterogeneity.csv`
- `experiments/EXP-02/figures/...`（候选差异、改判结局、CIF与阈值轨迹）
- `experiments/EXP-02/tests/test_consistency.py`
- `experiments/EXP-02/REPORT.md`（论文风格中文统计研究报告）

关键一致性测试：`F_1+F_2=F_{all}\)；\(0\le F_j\le1\)、随时间单调；\(0\le Q,R\le36\)；每个患者候选非空；Oracle Q–Q 预算不超 3 个月；\(d_Q\ne d_R\implies A_Q\ne A_R\)；全人群差约等于改判比例×改判者差；重新汇总旧算法时与既有 `STATISTICAL_REVIEW.md` 2.511% / 2.097% 在可说明的容差内一致。任何差异必须披露及溯源，禁止改输出迎合旧数值。

**Go / No-go**：如果严格内点患者中差异稳定、能够解释特定的\(p_1\)时间偏好且竞争事件代价合理，才称之为分位数保护的额外决策信息；如果差异主要是不可达截断/原因转移或临床净收益不清晰，不能继续宣称第一层 Q 保护“优于”RMET，应把论文核心贡献收窄为不同患者风险时间偏好的适用边界。**不要以 p 值显著作为唯一通过标准，也不允许实验后调参数直到 Q–Q 获胜。**

## 八、与先前研究工作衔接

实验完成后先向 `research/2026-11-23/03_Oracle实验完成后的科研判断与后续任务.md` 添加**带提交 hash 与数据出处**的结论，再依原有路线进入 Gate E（有限样本估计器比较）。本文件只是一份可复现执行说明，**未声称 EXP-02 已经运行**。
