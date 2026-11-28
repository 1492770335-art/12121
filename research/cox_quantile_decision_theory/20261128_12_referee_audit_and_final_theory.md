# 12 — 审稿式理论核验、原创性定位与最终理论章节方案（2026-11-28）

## 0. 范围

核验05–11文件已推导的结果及其适用条件，不更改原始两阶段Cox算法、p0=.50,p1=.10,L=36月、delta=3月，也不改变R_Q/QNB。以下为数学审查及定向文献复核，不是所有文献的穷尽原创性检索；本轮未新增训练模拟。

## 1. 最重要的文献定位修正

直接核对 Christina W. Zhou, Nikki L. B. Freeman, Katharine L. McGinigle, Michael R. Kosorok (2024), Optimal individualized treatment regimes for survival data with competing risks, arXiv:2411.08315v1, 2024-11-13：https://arxiv.org/html/2411.08315v1 。本轮没有确认其后续正式期刊出版，不得标作JASA论文。与 Yu Zhou, Lan Wang, Rui Song, Tuoyi Zhao (2023), Transformation-Invariant Learning of Optimal Individualized Decision Rules with Time-to-Event Outcomes, JASA 118(544),2632–2644, https://doi.org/10.1080/01621459.2022.2068420 是不同作者/论文。

Zhou 2024 第4.1节式(4)与Theorem 1直接采用二维价值向量的L2距离并证明一致性。Assumption 10要求 B(a,Z)=phi_1^0(a,Z)-(1-alpha_phi)V_1^{0*}(Z) 在0附近有连续有界密度；附录C通过规则不一致概率控制价值距离。故 R_Q 的最直接先行来源就是该文，不可宣称本文首创联合价值距离或首次研究约束边界。本文拓展点是竞争风险分位数、绝对时间容忍、两个误判机制的不同速度和具体极限、允许截断并列的条件与反例。Zhou 2024 Theorem 1是价值一致性结论，不应说其证明了本文的速率或分布，也不要把联合价值一致性与规则一致性视为等价。

Qian & Murphy (2011), Performance Guarantees for Individualized Treatment Rules, Annals of Statistics, https://doi.org/10.1214/10-AOS864 ：Section 3, margin condition (3.3) 是单目标值损失的既有理论，本文第二阶段的margin技巧不是新的。
Luedtke & Chambaz (2020), Performance Guarantees for Policy Learning, https://pubmed.ncbi.nlm.nih.gov/35321441/ ：已有策略遗憾与margin快速度研究。
Wang, Fu & Zeng (2018), Learning Optimal Personalized Treatment Rules in Consideration of Benefit and Risk, https://pmc.ncbi.nlm.nih.gov/articles/PMC6051551/ ：人群平均风险约束，与本文逐患者约束不同。
Jie Zhou et al. (2021), On restricted optimal treatment regime estimation for competing risks data, Biostatistics 22(2),217–232, https://doi.org/10.1093/biostatistics/kxz027 （期刊页面 https://academic.oup.com/biostatistics/article/22/2/217/5542990 ），竞争风险固定时点CIF目标/约束，非本文分位数准则。
Near-optimal Individualized Treatment Recommendations (JMLR, 2020), https://pmc.ncbi.nlm.nih.gov/articles/PMC8324003/ ：近优治疗集合已有研究，不应把第一阶段候选集合本身当作首创。
Fang, Chen & Liu (2026-11-12), Distribution-First Framework for Learning Risk-Sensitive Individualized Treatment Rules, arXiv:2611.16274v1, https://arxiv.org/html/2611.16274v1 ：新近预印本，Assumption 2局部Hölder稳定性、Theorem 2边界精细遗憾界。本文硬约束惩罚分数在D=delta处不连续，因此不能直接使用该Hölder条件来证明双速率；这是实质差别，不构成“全球首次”的证明。

## 2. 审查核心定理：成立及可简化之处

沿用 D=|q0(1)-q0(0)|, S=q1(1)-q1(0), b=argmax q0, w=1-b, G=q1(w)-q1(b)，q_j∈[0,L]。所有可测规则，无受限线性规则类；训练数据给定后的目标患者分布P_Z。K>L固定。d*与hat d分别逐点优化真实和估计两阶段规则。

e_j=sup_{z,a}|hat q_j-q_j|=O_p(r_j)；P(|D-delta|<=t)<=C0 t^beta, beta>0；P(D<=delta,0<|S|<=t)<=C1 t^alpha, alpha>=0。第二margin可以仅要求真双可行区域。B={|D-delta|<=2e0}。在2e0<delta时，可行集合不同必在B内。对可行集合相同区域，正遗憾<=2e1 I(D<=delta,0<|S|<=2e1)。因此
$$R_K=V_{\delta,K}(d^*)-V_{\delta,K}(\hat d)\le (K+L)C_0(2e_0)^\beta+C_1(2e_1)^{1+\alpha}.$$
所以 R_K=O_p(r0^beta+r1^(1+alpha))；统一根n时替换r_j=n^-1/2。允许重点分位数真并列；不必要求最优规则唯一。渐近最优性、约束违反概率O_p(r0^beta)和|V1(d*)-V1(hat d)|同阶直接推出。规则一致性应写对最优集合的距离，若希望针对固定代表则需额外唯一性/并列稳定。勿误写“每位患者渐近严格可行”，只能说违规概率趋零及逐点超额<=2e0。不要把收敛上界当精确阶，不能说两个随机项一定同阶或都非退化。

### 2.1 K依赖性与不依赖K的内在决策性质（本轮新增）

定义 v=P_Z(c(Z,hat d)>delta)，u(z)=q1(z,d*)-q1(z,hat d)，U=E[u_+]、O=E[(-u)_+]。注意 O 只可能出现在违规患者，因为真可行时d*逐点最大q1，故 O<=L v。精确恒等式
$$R_K=U-O+Kv,\qquad U+(K-L)v\le R_K\le U+Kv.$$
因此对任意固定K>L，R_K与非负量 U+L v 等价（常数依赖K,L）。显式：min(1,(K-L)/L)(U+Lv)<=R_K<=max(1,K/L)(U+Lv)。所有K>L有相同的一致性与Op速率；极限分布和两类遗憾占比则依赖K。U是重点价值正损失，v是违规率，不是新增跨方法评价指标；不应临床解释K=48。可将该恒等式作为对理论惩罚的说明，避免审稿质疑“任意K制造速率”。对正则活跃边界，sqrt(n)(U,O,v)联合极限分别为∫G H_+ w_D, ∫G(-H)_+ w_D, ∫(-H)_+ w_D；相同可行集合排序的U项在root-n尺度消失。由此任意固定K的regret极限立即得到，无需重做算法。

### 2.2 必须保留约束边界无原子条件：反例

沿用06指数PH子模型，改令Z恒为zc=log(4/3)，theta=0（其他参数已知，随机治疗，行政删失）。q0(0)=12,q0(1)=9, D=delta=3，G=9-log(6/5)/lambda>0。因约束用<=，oracle选1。仅估计theta，sqrt(n)hat theta⇒非退化中心正态；hat theta>0时估计总体代价超过delta，选0，否则选1（高概率排序方向保持）。故P_training(hat d≠d*)→1/2，R_K=G I(hat theta>0)（高概率），不趋于0。注意两治疗真均可行，v恒为0，失败来自错误排除有益治疗。这证明即使Cox模型正确、分位数root-n一致，若阈值有正质量也不能无条件得到决策价值一致性。该反例独立于08重点截断并列反例。不能为了离散真实数据而无条件删除A2。若可行集合阈值无原子但不满足幂margin，仍可由P(|D-delta|<=t)→0得到一致性，不能指定幂速度。

## 3. 极限定理的正式条件及证明审查

采用真实与估计可行集合是否相同的精确分区 M=I(hat A!=A)，R0=E[ell M],R1=E[ell(1-M)]，R=R0+R1。不要混淆05为证明构造的薄带分区B与M；05上界同时控制M分区。相同候选集单例无损失，双例错误排序才有损失。

额外条件：有限离散层，层内连续协变量密度有界连续，支持紧；D=delta和可行区域S=0是支持内部紧致C²正则超曲面，梯度范数有正下界（亦可有限局部片覆盖），两曲面交集在各自的加权曲面测度下为零。若简单陈述二阶定理，取分离边界这一充分条件。G连续且在D=delta上G=0的加权曲面测度为0。不存在影响R_Q的正质量不稳定并列。需要在整个相关固定邻域内有联合FCLT (H_n,J_n)=sqrt(n)(hat D-D,hat S-S)⇒(H,J)，连续极限路径；点态CLT不足。统一root-n误差仍用于薄带定位。对总体分位数严格截断片可用零扰动；恰好触及L的切换片须另证，不能把点态方向导数当成统一FCLT。

在A={D=delta,G>0}，w_D=f_Z/||grad D||；B={S=0,D<delta}，w_S=f_Z/||grad S||；曲面积分须按离散层概率加权。局部坐标 t=D-delta 或 S，epsilon=n^-1/2。约束误判长度 H_+ 或 (-H)_+，单位损失 G 或 K-G；排序误判长度|J|，单位损失 epsilon |u|。积分后联合极限：
$$ (\sqrt n R_0,nR_1)\Rightarrow \left(\int_A [G H_++(K-G)(-H)_+]w_Dd\sigma,\ \tfrac12\int_B J^2w_Sd\sigma\right).$$
同一(H,J)决定两项，不能假定独立。07、11的局部坐标证明成立于上述条件；若两曲面不分离但交集零曲面测度，可在各自薄带中先去掉另一边界eta邻域，再取极限，排序项的权重本身O(epsilon)使交集贡献o_p(epsilon²)；不能把零测度自动写成O(epsilon²)的概率界。极限可能退化，非零活跃边界和非退化扰动才能断言相应精确阶。06的局部minimax下界仅beta=1的子模型，不能宣称全模型类全局minimax最优。它与固定参数下极限是不同陈述。

## 4. R_Q理论的审查

令 Delta=V_Q(d*)-V_Q(hat d)，V_Q=(E q0,E q1)，不是边际事件时间分位数。08的确定性界成立：
$$|\Delta_0|\le L P(B_n)+\delta P(D\le\delta,0<|S|\le2e_1)+T_n,\quad
|\Delta_1|\le L P(B_n)+2e_1P(D\le\delta,0<|S|\le2e_1),$$
其中 T_n=E[D I(D<=delta,S=0,hat d!=d*)]。唯一性可令T_n=0；并列稳定或总体分位数差小亦可控制T_n。若T_n=o_p(1)，R_Q一致；若T_n=O_p(r0^beta+r1^alpha)，R_Q同阶。08正确PH反例证明不稳定截断并列可能让R_K=0而R_Q不一致；所以不能将R_Q一致性作为无条件推论。需固定oracle与估计并列规则；原始Oracle记录是重点并列先按总体保护量，再共同硬币。pilot采用剩余并列固定标签0，不是归档原程序。若原算法的数值并列容忍tau_n>0（如1e-12年），数学渐近中必须取精确比较或tau_n=o(n^-1/2)，固定正容忍不能无条件视为精确优化。有限样本小容忍可以忽略但不等于严格数学极限。若用固定时间网格反演，网格宽度也需o(n^-1/2)以保证极限；实际Breslow失效时点反演无此固定网格问题，实验目标人口固定积分网格则需核对积分误差。

在无影响联合价值的不稳定并列及上述光滑边界FCLT条件下，
$$\sqrt n\Delta\Rightarrow Z_Q=\int_A(-\delta,G)^T H w_Dd\sigma-\int_B(C,0)^T J w_Sd\sigma,$$
C=q0(1)-q0(0)。若(H,J)为中心高斯则Z_Q为中心二元正态（允许退化），nR_Q²⇒lambda1 χ1²+lambda2 χ1² (独立)。这不是可观察估计量的Wald推断。R_Q小不必推荐一致，有符号总体/重点差可能相互抵消（不同患者）。不可把距离解释为逐患者平均欧氏损失。已有Zhou 2024直接先行依据。若本论文实际数据表报告人群边际分位数，不能套用此定理。

## 5. Cox辅助引理与实现核验

05的统一截断反演充分条件可保留：对可用的左右方向p-F(q-h)>=mh及F(q+h)-p>=mh；q=L时只需左方向。允许严格截断，不允许平坦目标阈值而无统一穿越。根n统一界与FCLT的要求不同：CIF递推误差O_p(max jump)用于速率足够；FCLT需要max jump=o_p(n^-1/2)，连续失效且风险集下界时Breslow为O_p(n^-1)。07–11的联合Cox影响函数仅在模型正确、固定维设计、有界目标协变量、独立个体与删失、风险集正下界、信息正定等条件下使用；实际中心依赖需单独处理。F1的导数分部积分与余项须注明函数型delta或渐近等度连续性，不能把sup误差乘BV直接写成二阶小量。11的同一原因交叉协方差为零的依据是风险集中心化；原因间鞅正交需要无同时失效及连续补偿。基线与系数以及各治疗的协方差不得随意删减。

PH_tradeoff模型的数值核验支持但不代替所有正则条件的解析证明。time_cross错设Cox不能引用真实oracle一致性；Zhou_exp是否满足主论文共享基线与交互项形式、原始代码、LK16-02实际数据、其他删失档均未完整核验。

## 6. 正式第四章建议

保留三项主结果，不设显然的等价性定理：
T1 决策遗憾收敛速度及自然推论（覆盖允许截断并列的情形，要求A1–A3）。
T2 在额外正则条件下两阶段遗憾的联合不同尺度极限（root-n与n），明确该结论在光滑边界子类有效。
T3 联合价值距离的一般收敛界（包括T_n），正则光滑情形的联合正态极限作为附加结论；若篇幅紧可将分布部分移附录。
附录：Cox–CIF–截断反演、所有证明、局部minimax下界、两类反例、协方差及理论校准、R_Q加权卡方推论。K等价性写入定理前后说明。QNB仍为跨方法评价，不宣称该指标最大化由本文oracle保证。

目前建议暂不开展真实数据置信区间或继续叠加新定理，先完成证明整合、统一符号、原始算法核查，随后用正式模拟方案验证（原始PH机制更多重复和另一档删失）。09–11数值结果的40次重复及固定积分网格仍不足以确认完整Cox达到渐近区间，且原程序及逐次CSV尚未完整归档GitHub。本轮没有运行新模拟、没有建立可实施统计推断，也没有证明全球原创性。