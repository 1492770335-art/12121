# Gate P | 风险概率水平与时间容忍量的科学依据：文献证据审查

**检索日期**：2026-11-23  
**对应研究**：竞争风险下基于条件截断分位数的两层个体化治疗选择；Oracle EXP-01 / EXP-02；既有硕士论文第 2、5、6 章。  
**证据性质**：经公开原文/摘要/正式 DOI 核查的**定向证据综述**，而非穷尽性系统评价；临床阈值的“没有发现证据”仅表示**本轮检索范围内未获得直接验证**，不等于不存在任何相关研究。  
**原始项目**：[\`experiments/EXP-02/REPORT.md\`](../../experiments/EXP-02/REPORT.md)。  
**写作纪律**：严格区分统计定义、既有临床结局、患者偏好证据和特定阈值的实证认可。不可将一项临床研究中的“数月生存获益”反向当成“可以承受数月生存损失”的证据。

## 0. 结论摘要：四类需要不同证据的命题

| 需要辩护的主张 | 本轮证据级别 | 允许的结论 | 不允许的跳跃 |
|---|---|---|---|
| “原因别 CIF 达到概率水平 p 的首次时间”是合法统计对象 | **A：直接方法学支持**，Peng & Fine (2007, 2009)、Peng 生存分位数综述 | 可以将 Q1(p) 严格定义为**在竞争事件存在时**目标事件首次累计发生概率达到 p 的时间 | 不等于病人实际事件时间的条件均值或“有 p 比例患者必定在此时发生事件” |
| p_all=0.50 | **A：50% 有中位首次事件时间的统计解释；C：无移植共识支持该固定数值为最佳保护阈值** | 在窗口可达时，Q_all(.50) 是条件中位首次事件时间；作为一个可解释的预设偏好场景 | 不等于“临床规定必须保护 50%”或由某个研究中的 50% 治愈概率验证 |
| p_1=0.10 | **B：较早/较低分位点有统计价值；C：本轮未找到 AML/NRM 的 10% 事件 CIF 时间阈值作为标准患者偏好** | 研究病人如何关注“NRM 发生概率何时首次达到 10%”，但应声明为假设性偏好情景 | 把 DCA 中的“10% 患病概率启动治疗”直接等同于“NRM CIF 达到 10% 的时间” |
| δ_Q=3 个月 | **B：不同疾病可有数月生存获益判断；C：未验证可牺牲 3 个月的条件总体首次事件中位时间为临床通用安全预算** | 作为预先固定的、易沟通的**数学时间容忍参数**；保留既有 0/1/3/6 月路径以说明预算与结果关系 | 把 ASCO 提及的“3 个月生存获益有意义”引用成“患者允许 3 个月总体无事件时间损失” |
| 数据内共同 t0 校准 p_all、p1 | **A：定义透明、可作为跨治疗共同概率标尺；C：不是外部验证的临床偏好阈值** | 在先验参考时间 t0 下，用目标人群与可行治疗的平均 CIF 确定比较水平；估计对象随人群/治疗集合变动 | 说固定 p=.50/.10 与真实数据共同校准 p 是完全相同的临床偏好 |

**总体评定**：可以继续以 Q_all–Q1 为**明确定义的、风险阈值时间偏好驱动的研究目标**，但不能声称 50%、10% 和 3 个月已经由临床文献单独验证，更不能声称具普遍临床净获益或天然优于 RMET。

## 1. 统计学最直接的先行研究：CIF 分位数为什么是有意义的量

### 1.1 Peng & Fine (2007) —— CIF quantile 本身已是正式统计学研究对象

- **L. Peng & J. P. Fine (2007)**, “Nonparametric quantile inference with competing–risks data”, *Biometrika* 94(3):735–744. DOI: https://doi.org/10.1093/biomet/asm059
- 研究明确使用原因别累计发生函数定义分位数，建立一致性、弱收敛以及一、两样本比较推断；期刊摘要直接评价这一分位数具有竞争风险下的直观含义。
- 对本论文的**直接支持**：定义 \`F_j^a(t|z)=Pr(T^a≤t,J^a=j|Z=z)\`、\`Q_j(p|z,a)=inf{t:F_j^a(t|z)≥p}\` 有明确文献传统。
- **没有支持**：p=.10 为临床验证阈值，或者“优化 CIF 10% 达到时间”本身必然改善患者结局。

### 1.2 Peng & Fine (2009) 及生存分位数综述 —— 明确“首次达到某一原因 CIF 水平的时间”

- **L. Peng & J. P. Fine (2009)**, “Competing Risks Quantile Regression”, *JASA*. DOI: https://doi.org/10.1198/jasa.2009.tm08228
- **L. Peng**, “Quantile Regression for Survival Data”, *Annual Review of Statistics and Its Application*，doi: https://doi.org/10.1146/annurev-statistics-042720-020233；全文 https://pmc.ncbi.nlm.nih.gov/articles/PMC7978418/
- 该综述 §3.2.1 精确定义原因 CIF 条件分位数，并将其解释为在给定协变量情况下、存在其他竞争失败原因时，原因 k 的累计发生概率首次超过 τ 的时间；同时区分 CIF 的 **crude/cumulative incidence** 与潜在事件时间的 **net/latent** 目标。
- 对本论文的直接支持是 **estimand 的定义**，而非 0.10 的数值或任一治疗规则本身的临床效用。
- **必须强调**：如果提高竞争事件风险导致 F1 下降，Q1 也可能推迟；这不等于竞争原因被消除后目标事件的潜在发生时间真的变长。必须列出 F1、F2、RMET 及无法达到指定水平的比例。

### 1.3 为什么 50% 特别容易解释，但没有“最优性”

- 一般生存分析中 \`Q_all(.50)\` 是首次事件时间的**中位数**，前提是条件总体 CIF 在窗口内能达到 50%；若 F_all(36)<.5，本文将 Q 截成 36 月，只是决策分数，并非已观察中位生存。
- 来源：Cancer Research UK, “What do clinical trial results mean” (median event-free survival) https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/clinical-trial-results/what-do-clinical-trial-results-mean-0
- 另见 “Which Metrics Are Appropriate to Describe the Value of New Cancer Therapies?” https://pmc.ncbi.nlm.nih.gov/articles/PMC4486603/：中位 OS 常用但仅刻画分布的一个位置，不刻画所有长期生存者。
- **允许写**：“50% 使总体第一层有中位无首次事件时间的直观解释”；**不能写**：“50% 是医学上优于其他水平的保护阈值”。

## 2. 10% 是否有临床文献直接支持？

### 2.1 本轮没有找到“AML 移植 NRM CIF 时间到 10% 是公认目标”

确有大量临床论文报告移植后 1/2/3 年非复发死亡 (NRM) 或复发 CIF，但这些**按固定时间报告风险概率**的数值，通常不是规定一个患者应优化的 \`Q_NRM(0.10)\`。某项研究出现“10% NRM”也不能自动解释为所有患者认可 \`Q_NRM(.10)\` 的临床阈值。

- 国际移植统计报告综述： “Summary of Scientific and Statistical Methods, Study Endpoints and Definitions for Observational and Registry-Based Studies in Hematopoietic Cell Transplantation” https://pmc.ncbi.nlm.nih.gov/articles/PMC8432337/ 。提供 NRM、复发等竞争事件定义和使用 CIF 的统计依据；不提供 10% 到达时间的标准化偏好。
- 移植竞争风险指南：“A Practical Guide to Competing Risk Analysis for Transplant and Cell Therapy Research” https://pmc.ncbi.nlm.nih.gov/articles/PMC12818700/ 。说明 NRM 与复发互为竞争事件；不等于指定 p=.10。
- European LeukemiaNet (2022) AML 推荐： https://ashpublications.org/blood/article/140/12/1345/485985 。强调移植决策需要权衡 NRM 与复发风险、患者和供者特征；未在本轮核对文本中得到 \`p_NRM=.10\` 的通用达到时间偏好。

### 2.2 “临床风险阈值”先行研究支持**根据偏好选阈值**，不是 10% 有唯一正确值

- **Vickers & Elkin (2006)**, “Decision curve analysis: a novel method for evaluating prediction models”, *Medical Decision Making*, DOI https://doi.org/10.1177/0272989X06295361 。用决策阈值概率编码风险/收益的取舍，是偏好敏感型决策的正式依据。
- **Wynants et al. (2019)**, “Three myths about risk thresholds for prediction models”, *BMC Medicine* 17:192, DOI https://doi.org/10.1186/s12916-019-1425-3 。指出风险阈值常被任意设置，通常不存在普适的最佳阈值，应按临床情景解释并展示合理范围。
- **Vickers et al. (2019)**, “A simple, step-by-step guide to interpreting decision curve analysis”, DOI https://doi.org/10.1186/s41512-019-0064-7 。如果方案优劣依赖偏好阈值，可得结论是仅适用于某些合理偏好范围，不能说全面有效。
- **重要的概念区别**：DCA 的 \`r\` 往往是“在固定随访时点预测事件风险高于 r 即考虑治疗”的**治疗行动阈值**；本论文的 \`p=.10\` 是固定事件累计概率的**时间反演水平**。两种阈值不等同，不能用 DCA 证明具体 \`Q_NRM(.10)\` 的临床最优性。DCA 只能支持“把偏好参数显式化、结合临床权衡选择、不可任意称为最佳”的逻辑。

## 3. 3 个月的时间容忍预算：能找到什么，不能找到什么？

### 3.1 有“数月生存获益可以有意义”的肿瘤学文献

- **Ellis et al. / ASCO (2014)**, “American Society of Clinical Oncology Perspective: Raising the Bar for Clinical Trials by Defining Clinically Meaningful Outcomes”, *JCO*, DOI https://doi.org/10.1200/JCO.2013.53.8009 ；后续 ASCO 治疗价值框架提到依癌种不同的 2.5–6 个月中位 OS 获益基准：https://doi.org/10.1200/JCO.2015.61.6706 。
- **此证据只能说明**：在某些具体肿瘤与基线预后环境中，某些**中位总体生存获益**大小被工作组视为有意义。
- **严格不能推出**：急性髓系白血病移植患者愿意用 \`Q_all(.50)\` 或 DFS 首次失败时间**减少 3 个月**换取某个 NRM \`Q1(.10)\` 的增长。OS 与 DFS/总体首次事件不同；获益与可接受损失方向相反；接受何种代价还取决于复发风险与死亡严重程度。

### 3.2 直接的移植患者偏好研究更支持“不同患者权衡不同”

- “Patient preferences for allogeneic haematopoietic stem cell transplantation: how much benefit is worthwhile from the patient’s perspective?” *Supportive Care in Cancer* (2021), DOI https://doi.org/10.1007/s00520-020-05816-z 。184 名经历过移植患者的偏好调查，多数认为很长期的生存益处才足以证明移植值得；年龄与可接受收益存在关系。研究中提到的“50% cure rate”是患者认为值得的**治愈率**，不是 \`Q_all(.50)\` 的中位首次失败时间；**严禁混同**。该调查存在移植后生存者选择偏差，不能外推为所有拟移植患者的固定容忍量。
- “Patient and Physician Preferences for Acute Myeloid Leukemia Maintenance Treatments Following Hematopoietic Stem Cell Transplantation”, *Patient Preference and Adherence* (2023), DOI https://doi.org/10.2147/PPA.S421871 。AML 移植后维持治疗的离散选择实验表明患者与医生会在疗效、住院、严重感染等多属性间作取舍；**非 MAC/RIC 预处理决策**，不产生本论文 3 个月总体风险时间预算。
- “Developing an instrument to assess patient preferences for benefits and risks of treating acute myeloid leukemia to promote patient-focused drug development” (2018), DOI https://doi.org/10.1080/03007995.2018.1456414 。正式利用患者偏好实验/问卷量化收益风险，可支持将容忍量视作患者偏好参数；未给出统一 \`δ_Q=3月\`。
- “Using the Threshold Technique to Elicit Patient Preferences” (2019/2020), DOI https://doi.org/10.1007/s40258-019-00521-3 。介绍通过阈值法询问最小可接受获益、最大可接受风险等的方法，为将 \`δ_Q\` 在将来的独立偏好研究中实证化提供路线；并没有直接校准本论文的时间预算。

**判断**：δ=3 月目前仍是**预先指定的统计决策容忍量**。已有 0、1、3、6 月的容忍路径足以说明“允许的总体时间损失变化如何改变可行集、处方与潜在结局”，不应补造临床公认阈值。不能把 EXP-02 中 Q–Q 自身保护预算零违反解释为“3 个月医学安全”。

## 4. 为什么 AML/HCT 的「存在取舍」有直接临床证据

- “Dose intensity for conditioning in allogeneic hematopoietic cell transplantation: can we recommend ‘when and for whom’ in 2021?”, *Haematologica* (2021), DOI https://doi.org/10.3324/haematol.2020.268839 。临床综述明确指出：更高强度预处理通常意味着较高 NRM 与较低复发，选择需要按 MRD、疾病风险与患者风险因素权衡；该文举例 MRD 阳性人群 3 年复发 67% vs 19%，NRM 27% vs 9%（来自具体研究、不可视作当前 LK 的数值）。
- NCI AML PDQ（医疗专业人员版） https://www.cancer.gov/types/leukemia/hp/adult-aml-treatment-pdq 。同种异体移植对复发控制的益处可能被 GVHD、感染等发病和死亡风险抵消，支持研究多结局决策而非单独优化一种失败原因。
- 临床真实意义是治疗收益/毒性/复发间存在取舍，**不是**证明阈值 50%、10%、3 个月由移植医学规定。

## 5. 关键新增结论：EXP-02 固定 p 与论文真实数据共同 t0 校准并非同一个 estimand

### 5.1 先抄准论文真实定义

根据用户存档最新 **2026-11-18 硕士论文第 2.2.1 节式 (2.3)**，对于目标协变量分布 \`P_Z\` 与患者可行治疗集合 \`ψ(z)\`：

\[
\tau_0 =
E_Z\left\{\frac{1}{|\psi(Z)|}\sum_{a\in\psi(Z)}
F_{\mathrm{all}}^{(a)}(t_0\mid Z)\right\},\quad
\eta_0 =
E_Z\left\{\frac{1}{|\psi(Z)|}\sum_{a\in\psi(Z)}
F_1^{(a)}(t_0\mid Z)\right\}.
\]

论文明确规定这是在给定参考时间 \`t0\`，**按可行治疗等权并对目标人群平均**。该定义不依赖观测治疗的分配频率；不同目标人群、治疗集合、参考时点、结局模型会改变 \`(\tau_0,\eta_0)\`；校准是共同参考**统计构造**，而不是患者通过偏好调查认可这一风险水平。

对应个人和治疗的 \`Q_{\mathrm{all},\tau_0,L}^{(a)}(z)\` 与 \`Q_{1,\eta_0,L}^{(a)}(z)\` 使用相同的群体校准水平反演，但通常**不等于 t0**，因为群体平均后的分位数反演与逐个患者的条件 CIF 反演不可交换。

### 5.2 比较表：原 Oracle EXP-02、论文真实数据

| 场景 | t0 | L | 时间预算 | 总体 p | 重点 p | p 的来源 |
|---|---|---|---|---|---|---|
| Oracle EXP-02 | 未用共同 t0 决定概率水平（可另在 t=12 月报告 CIF） | 36 月 | 3 月 | **0.5000** | **0.1000** | **固定外生阈值** |
| LK16-02（11 月 17 日工作稿指定留出、共享 Cox） | 12 月 | 36 月 | 3 月 | **约 0.4079** | **约 0.1379** | **训练群体共同 t0 校准** |
| IST（同一工作稿指定留出、共享 Cox） | **5 天** | **14 天** | **1 天** | **约 0.0716** | **约 0.0214** | **训练群体共同 t0 校准** |
| BIG 1-98（同一工作稿指定留出、共享 Cox） | **1 年** | **4 年** | **0.25 年** | **约 0.0156** | **约 0.0067** | **训练群体共同 t0 校准** |

**出处与版本限定**：真实数据参考时间、评价窗与预算取自 2026-11-18 论文第 6 章/附录 C 的分析设置；上表近似概率值取自**2026-11-17 工作稿附录表 C.12「指定留出中的预测误差与训练共同水平」**所列**共享 Cox**列，**不能将其误写为所有 20 次五折的固定共同水平、总体真实概率或临床指导阈值**。11 月 18 日稿第 2 章仍保留共同校准定义。最终投稿前应重新从最终版本脚本和对应分折输出核对这些估计值。

注意 LK 中 0.4079/0.1379 与模拟的 0.50/0.10 看似相近，但它们来源不同；IST 和 BIG 的时间尺度与目标风险水平完全不同，不能声称三个真实应用均在“50% 与 10% 风险偏好”下获得相同临床意义。即使同为 3 个月、36 个月的 LK，与固定 p Oracle 的 estimand 也不完全相同。

### 5.3 数学上为什么 t0 校准不等于“个体事件将在 t0 达到风险阈值”

由于 \`τ_0=E_{Z,a}F_all^a(t0|Z)\`，它只是群体平均意义下 t0 的一个概率。对于给定个体 z 与治疗 a，\`F_all^a(t0|z)\` 可高于也可低于 τ0，于是通常有

\[
Q^{(a)}_{\mathrm{all}}(\tau_0\mid z)\ne t_0,\qquad
Q^{(a)}_1(\eta_0\mid z)\ne t_0.
\]

因此不要写“共同 t0 使所有治疗的比较分位数发生在 t0 左右”，也不要把 “F(t0) 固定时点风险”当作 “Q(p) 达到时间”；群体校准是一个合理的**共享尺度与目标人口对齐策略**，不是临床偏好 elicitation。

### 5.4 要让固定 p 与共同校准 p 在一个文章里共存，建议明确分成两类情景

**情景 A（固定概率水平/偏好设定）**：\`p_all=.50,p1=.10,δ=3月,L=36月\`。用途是研究给定“中位总体失效时间保护＋重点原因 10% 风险到达时间目标”的政策，在什么结构和人群中与 RMET/CIF 政策不同；其数值是说明机制的**情景参数**，非移植临床标准。

**情景 B（共同 t0 参照水平）**：在真实数据与论文原有模拟中，预先选择具有该临床结局时间尺度含义的 t0，然后在训练资料内估计 τ0,η0，冻结后用于评价。用途是避免对两个终点随意指定同一个固定 p，并在可行治疗下保证共同风险量尺；但仍需从患者偏好角度说明为什么该 t0 值值得关心。

**不能**把 A 的数值支持直接当作 B 的临床外推；能跨场景外推的是算法构造、识别条件、理论界和“风险时间偏好可能改变推荐”的概念性机制，而非具体的改判率或获益值。

## 6. Gate P 可以据此确定的论文表述（建议置于第 2 章和第五章实验设计前）

> 在竞争风险下，原因别 CIF 分位数刻画目标事件作为首次事件的累积发生概率首次达到预定水平所需时间。已有分位数推断研究为该指标提供了明确的统计定义与估计理论，但风险概率水平本身具有偏好依赖性，不存在适用于所有临床情景的统一最优取值。本文将总体首次事件的 50% 分位数、重点事件 10% CIF 分位数和 3 个月总体时间容忍量作为 Oracle 模拟中事先固定的决策情景，用于分析在不同治疗风险结构下两类时间泛函的权衡，而不将这些值解释为已有临床指南认可的阈值。
>
> 真实数据研究则依据事先设定的参考时间 t0，通过目标协变量分布和可行治疗等权平均确定两类结局的共同概率水平。该设计提供跨治疗一致的风险标尺，但并不等同于经过患者偏好研究确认的风险阈值。无论固定概率情景还是时间校准情景，均需分别报告重点与竞争事件 CIF、总体首次事件结局及分位数不可达情况；模型预测的重点分位数增量亦不自动代表临床净获益。

可考虑在结论中再加一句：

> 当前分析的创新主张限定为一种**患者条件的、指定风险达到时间的受约束治疗决策对象及其估计稳定性问题**；不以某组参数下不同治疗推荐或有利于自身目标的结果宣称疗效优越。

## 7. 后续若真要验证 p 与 δ 的临床合理性，应补什么证据？

这不是再对既有 DGP 进行大量搜索。优先从**患者偏好研究**中寻找可被估计的数据：
1. 确定具体治疗决策：AML 接受 MAC / RIC-NMA，重点原因 NRM、竞争原因为复发；明确两原因的严重程度、死亡与复发的后续含义。
2. 让医生与患者**分别**评估“在 36 个月管理窗里，目标 10% NRM CIF 达到时间增加 X 月”与“总体首次失败风险 50% 时间减少 Y 月”，理解这并非实际个体事件时间的变化。
3. 利用 time trade-off、threshold technique 或 DCE（具体设计前应经临床/伦理审查）确认受访者能够理解风险轨迹、并测量可接受的时间预算分布；如果偏好无法稳定表达，应重新检视此 estimand 的临床可沟通性。
4. 如果不开展新偏好研究，就维持 **示范/情景分析** 的诚实定位，不必再用模拟去“证实”这三个数字天生正确。

## 8. 引用清单（优先引入第 2 章、第 6 章）

**统计定义与生存终点**
- Peng, L. & Fine, J. P. (2007). Nonparametric quantile inference with competing-risks data. *Biometrika*. DOI https://doi.org/10.1093/biomet/asm059
- Peng, L. & Fine, J. P. (2009). Competing Risks Quantile Regression. *JASA*. DOI https://doi.org/10.1198/jasa.2009.tm08228
- Peng, L. Quantile Regression for Survival Data. *Annual Review of Statistics and Its Application*. DOI https://doi.org/10.1146/annurev-statistics-042720-020233
- Cancer Research UK. What do clinical trial results mean? https://www.cancerresearchuk.org/about-cancer/find-a-clinical-trial/clinical-trial-results/what-do-clinical-trial-results-mean-0

**风险阈值和偏好**
- Vickers, A. J. & Elkin, E. B. (2006). Decision curve analysis: a novel method for evaluating prediction models. *Medical Decision Making*. DOI https://doi.org/10.1177/0272989X06295361
- Wynants et al. (2019). Three myths about risk thresholds for prediction models. *BMC Medicine*. DOI https://doi.org/10.1186/s12916-019-1425-3
- Vickers et al. (2019). A simple, step-by-step guide to interpreting decision curve analysis. DOI https://doi.org/10.1186/s41512-019-0064-7
- Using the Threshold Technique to Elicit Patient Preferences (2019/2020). DOI https://doi.org/10.1007/s40258-019-00521-3

**HCT/AML 风险与偏好**
- Dose intensity for conditioning in allogeneic hematopoietic cell transplantation: can we recommend “when and for whom” in 2021? DOI https://doi.org/10.3324/haematol.2020.268839
- Patient preferences for allogeneic haematopoietic stem cell transplantation: how much benefit is worthwhile from the patient’s perspective? DOI https://doi.org/10.1007/s00520-020-05816-z
- Patient and Physician Preferences for Acute Myeloid Leukemia Maintenance Treatments Following Hematopoietic Stem Cell Transplantation. DOI https://doi.org/10.2147/PPA.S421871
- Developing an instrument to assess patient preferences for benefits and risks of treating acute myeloid leukemia. DOI https://doi.org/10.1080/03007995.2018.1456414
- Ellis et al. (2014). ASCO perspective on clinically meaningful outcomes. DOI https://doi.org/10.1200/JCO.2013.53.8009
- ASCO Statement: A Conceptual Framework to Assess the Value of Cancer Treatment Options. DOI https://doi.org/10.1200/JCO.2015.61.6706

## 9. 搜索策略与局限

检索主题组合包括 \`competing risks quantile CIF threshold\`、\`nonrelapse mortality 10% risk threshold transplantation\`、\`allogeneic hematopoietic transplantation patient preferences time trade off\`、\`clinically meaningful three months overall survival AML\`、\`decision curve risk threshold patient preference\`。优先同行评议期刊全文、统计学综述、医学会文献、PubMed/PMC/期刊 DOI；检查现有论文最新及前一版的 t0 校准定义与示例表。

**未做**：PRISMA 系统综述、完整数据库检索式复现、付费全文逐页审计、临床专家访谈或真实患者阈值估计。所有不属于相同结局/干预/估计对象的研究，只能提供方法学或解释类比，不能外推具体临床阈值。
