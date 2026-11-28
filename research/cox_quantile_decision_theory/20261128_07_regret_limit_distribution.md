# 一般正则约束边界下决策遗憾的极限分布（2026-11-28）

承接 05 核心定理、06 PH 子模型与局部 minimax。本文仍使用原始原因别 Cox 插入式两阶段规则，不引入线性参数化决策或新的实验指标。以下为附加正则条件下的极限定理，不是对任意截断机制、离散协变量或任意 Cox 错设情形的无条件结论。

## 1. 定义及附加假设

A={0,1}，q0,q1∈[0,L]；b(z) 为总体分位数最优治疗，w=1-b。D=|q0(z,1)-q0(z,0)|，G=q1(z,w)-q1(z,b)，D1=q1(z,1)-q1(z,0)。固定 0<delta<L、K>L。v_delta=q1-K I(c>delta)，V_delta=E_Z v_delta；R=V_delta(d*)-V_delta(hat d)≥0。d* 可在双可行且 G=0 时选 b；理论 regret 不依赖真实并列代表。hat d 使用原两阶段逐点优化，任意可测并列处理。目标期望对独立 Z，条件于训练样本。记 epsilon_n=n^-1/2。

假设：
(1) e_j=max_a sup_z|hat q_j-q_j|=O_p(epsilon_n)，重点 margin P(0<|D1|<=t)<=C t^alpha，alpha>0（实际上仅需该概率→0，即可令排序遗憾 o_p(epsilon_n)）。
(2) Z 在真实阈值曲面 S={D=delta} 的固定邻域具有连续有界密度 f；支持紧，D 连续。S 是支持内部的紧致 C^2 正则超曲面，D 在其邻域 C^2，inf_S||grad D||>0。可由隐函数定理的有限局部坐标覆盖或 D 的梯度流建立统一管状坐标 z=Phi(s,t)，D(Phi(s,t))=delta+t，Phi(s,0)=s。雅可比 J(s,0)=1/||grad D(s)||。S 外无任意接近阈值而未被邻域覆盖的点（紧支持和连续性确保）。一维情形用计数测度。G 在该邻域连续（b 方向局部稳定），sigma({s∈S:G(s)=0})=0。可将条件放宽为以 f/||grad D|| 加权的零曲面质量；若存在稳定截断并列，需另外处理，见第6节。
(3) H_n(z)=sqrt(n)(hat D-D) ⇒ H(z) 于 l∞(U)，U 为上述曲面的一个固定紧邻域，H 有连续路径。允许 H 非高斯；在光滑反演条件下为联合 Cox 高斯过程的线性变换。由此可使用随机一致有界性及渐近等度连续性。不可仅凭每点 CLT 替代此条件。

## 2. 核心极限定理

令 S0={s∈S:G(s)>0}，w_S(s)=f(s)/||grad D(s)||，dσ 为 (p-1) 维曲面测度。则
$$\sqrt n R\Rightarrow \mathcal L_\delta=\int_{S_0}\{G(s)H(s)_++[K-G(s)](-H(s))_+\}w_S(s)d\sigma(s).$$
其中 x_+=max(x,0)。该极限一般为非线性高斯过程泛函，不是正态。若活跃边界具有正加权面积且 H 在其正测度子集上方差为正，则在中心高斯情形 E L>0（若可积），故极限非恒零，结合高斯连续过程小球性质可得非退化。若无活跃边界或边界 H 恒为零，一阶极限可退化，不能断言精确根 n 阶。

### 完整决策层证明

取 epsilon=epsilon_n。由 e0=O_p(epsilon)，真实/估计可行集合不同仅可能发生于 |D-delta|<=2e0；由于 delta>0，在此薄带内 b 和估计总体最优治疗相同（高概率）。可行集合相同时，正遗憾至多 2e1 I(0<|D1|<=2e1)，积分后为 O_p(epsilon^(1+alpha))=o_p(epsilon)，即排序误判不贡献根 n 尺度的 regret。

对曲面点 s 及 t=epsilon u，设 z=Phi(s,epsilon u)。在 H_n 一致有界事件上，跨越可行状态的 u 落在某固定 [-M,M]，M 可随尾部概率要求取大。真实可行状态为 u<=0；估计状态为 u+H_n(Phi(s,epsilon u))<=0。利用渐近等度连续性，sup_{s,|u|<=M}|H_n(Phi(s,epsilon u))-H_n(s)|=o_p(1)。

固定 eta>0。先限制 |G(s)|>eta，G 连续且 e1→0，故在该薄带真实与估计重点排序均保持符号。G(s)<-eta 时，b 被两种规则推荐，不产生遗憾；G(s)>eta 时：
- u<=0 且 u+H_n(z)>0：错误排除真正可行治疗 w，损失 G(z)；
- u>0 且 u+H_n(z)<=0：错误纳入不可行治疗 w，损失 K-G(z)。
其余不产生该部分遗憾。

坐标变换 dz=J(s,t)dσ(s)dt，令 t=epsilon u。f(Phi)J(s,epsilon u)→w_S(s)，G(Phi)→G(s)，均一致。替换 H_n(z) 为 H_n(s) 产生的指标误差只在 |u+H_n(s)|<=o_p(1) 的区间，积分长度 o_p(1)，故归一化误差 o_p(1)。在 M 足以容纳 H_n 的事件上，
int_{u<=0} I(u+H_n(s)>0)du=(H_n(s))_+；
int_{u>0} I(u+H_n(s)<=0)du=(-H_n(s))_+。
因而 epsilon^-1 R 的截断曲面部分等于将 H_n(s) 代入目标积分（限 G>eta）加 o_p(1)。

被排除的 |G(s)|<=eta 曲面薄带贡献，除已控制的排序误判外，归一化遗憾绝对值至多常数乘 M∫_{|G|<=eta} w_S dσ+o_p(1)，因 G=0 的曲面测度为零，令 eta↓0 后可任意小。控制 H_n 尾部事件后得
$$\sqrt n R=\Phi_\delta(H_n|_S)+o_p(1),$$
其中 Phi_delta 为定理右侧积分映射。由于正部函数 1-Lipschitz、权重有界可积，Phi_delta 在 sup 范数下 Lipschitz。连续映射定理完成证明。该证明是在固定真值及相应规则学习器下的条件性极限，不是任意 DGP 的全局一致极限。

## 3. 两个有统计意义的联合推论

同一证明给出三维联合弱收敛：
$$\sqrt n (R, P_v, V(d^*)-V(\hat d))\Rightarrow (\Phi_\delta(H),\Psi(H),\Xi(H)),$$
其中 P_v=P_Z(c(Z,hat d)>delta)，V(d)=E_Z q1(Z,d(Z))；
$$\Psi(H)=\int_{S_0}(-H)_+ w_Sd\sigma,\qquad \Xi(H)=\int_{S_0}G H w_Sd\sigma.$$
因为 V(d*)-V(hat d)=R-KP_v，Xi=Phi_delta-K Psi。违规只来自 u>0 侧的错误纳入；第二阶段排序误判在真实可行集合内不违规。若 H 为中心高斯过程，Xi 是线性高斯泛函（可能退化），但 regret 非负且非线性。这里讨论真实人群价值的训练样本随机性，不是估计该人群价值的置信区间，也不是固定规则估计量的 CLT。

若希望进一步证明联合 V_Q 的根 n 极限，不能直接用以上推论：重点排序误判虽只有 n^-1 regret，却可能改变 O(1) 的总体分位数，故对 E q0 的贡献可能为 n^-1/2；大量最优并列亦可能破坏联合价值一致性。必须增加第二条正则曲面及并列约定条件。R_Q 和 QNB 不改变本理论目标。

## 4. 原因别 Cox 如何给出 H

假定独立样本、固定维有界设计、正确 PH、独立删失、风险集正下界、非退化信息矩阵及连续基线累计危险等。标准联合 Cox–Breslow FCLT（Andersen & Gill 1982，AOS）给
sqrt(n)(hat theta_k-theta_k,hat Lambda_k-Lambda_k)⇒(B_k,U_k)，连续高斯极限；各原因使用同一联合过程，不假定估计误差独立。
令 H_k(t,z,a)=Lambda_k(t)exp(theta_k^T x(z,a))，则其极限扰动
$$\mathbb U_k(t,z,a)=e^{\theta_k^Tx(z,a)}[U_k(t)+\Lambda_k(t)x(z,a)^TB_k].$$
F0=1-exp(-sum H_k)，故
$$\mathbb F_0(t,z,a)=S(t,z,a)\sum_k\mathbb U_k(t,z,a).$$
若总体分位数在曲面邻域统一为内点、f0=partial_t F0 连续并严格正，统一反演给
$$\mathbb Q_0(z,a)=-\mathbb F_0(q_0(z,a),z,a)/f_0(q_0(z,a),z,a)
=-\frac{\sum_k\mathbb U_k(q_0,z,a)}{\sum_k\lambda_k(q_0|z,a)}.$$
证明：在根 n 统一误差下，Taylor 展开 F0(hat q)-F0(q)，并以 FCLT 渐近等度连续性替换扰动过程的时间参数。估计 CIF 的跨越超调须为 o_p(n^-1/2)；连续事件时间、无失效并列、风险集规模下界 cn 时，Breslow 最大跳量 O_p(1/n)，满足要求。更一般需显式假定最大跳量为 o_p(n^-1/2)。不应将 05 中足够用于 O_p 收敛率的 O_p(n^-1/2) 跳量界直接用作 CLT 余项。
因 D≥delta/2 的局部 b 方向稳定，
$$\mathbb H(z)=\mathbb Q_0(z,b(z))-\mathbb Q_0(z,w(z)).$$
q1 只需统一 O_p 根 n 估计和局部符号稳定；不需其高斯极限。CIF 的指数递推保持 F0=1-S，故本极限不需重复推导重点 CIF 的影响函数。若某总体分位数严格截断且 F0(L)<p0 有统一正间隔，则其扰动为 0，可以在不发生截断切换的局部曲面片应用上述论证。

## 5. 与前一 PH 子模型核对

一维 zc 曲面，D'(zc)=9，f(zc)=1/(2h)，H(zc)=9W。代入得 L=[G_c W_++(K-G_c)(-W)_+]/(2h)，恰与 06 文件一致，验证符号及雅可比。

若 H 为中心高斯且标准差 s(z)，E H_+=E(-H)_+=s(z)/sqrt(2pi)，故
$$E\mathcal L_\delta=\frac{K}{\sqrt{2\pi}}\int_{S_0}s(z)w_S(z)d\sigma(z).$$
这是极限随机变量的期望；除非证明 sqrt(n) R 的一致可积性，不可声称 sqrt(n) E R 收敛至该量。

## 6. 必须保留的限制与例外

- 总体分位数恰在 L 且 F0(L)=p0 时，点态方向导数为 min(0,-F扰动(L)/f0(L))，但跨越截断切换的统一过程未必存在连续极限。不能只用点态公式便宣称 A6。可限制在无切换的曲面局部邻域，或另证切换交集曲面测度为零及薄带忽略性。
- 若 G=0 在 S 上有正曲面测度，估计排序和约束误判可能同时贡献一阶惩罚，公式不可直接套用。特别是两重点分位数均截断为 L 的稳定并列，若真实和估计两者均严格截断且估计并列选择总体较优治疗 b，则该片无误纳遗憾；如果采用固定治疗标签的并列规则，则可能有惩罚遗憾贡献。需核实实际并列约定，不能未经用户授权改变原算法。
- 若 Z 全离散且无 D=delta 原子，第一阶段可能最终完全无误，root-n 极限退化；若阈值处有原子且 G>0、估计扰动符号非退化，原始 plug-in 甚至可能不一致。混合协变量可按有限离散层加权曲面积分，须逐层满足条件。
- 真实 Cox 错设（time_cross 等）不受此理论覆盖。中心相关样本需相应集群渐近理论。
- 该 theorem 刻画真实 oracle regret 的抽样分布，非可直接计算的统计量。普通正态/Wald 或对非光滑泛函简单中心化 n-out-of-n bootstrap 未必有效。可考虑估计方向导数并乘子模拟（Fang–Santos 2019）或 subsampling，但必须解决未知真值、曲面和权重估计；本记录未证明可实施 CI 的覆盖率。
- 不建议用主定理替代实际 QNB、R_Q 评估，也不宣称文献中未有人研究类似问题；原创性查重待继续。

## 7. 参考文献（支持方法，不声称给出本文公式）

Andersen & Gill (1982), Cox's Regression Model for Counting Processes: A Large Sample Study, Annals of Statistics. https://doi.org/10.1214/aos/1176345976
Ozenne et al. (2017), riskRegression: Predicting the Risk of an Event using Cox Regression Models, R Journal 9(2), 440–460. https://journal.r-project.org/articles/RJ-2017-062/
Fang & Santos (2019), Inference on Directionally Differentiable Functions, Review of Economic Studies 86(1), 377–412. https://academic.oup.com/restud/article/86/1/377/5094886
Samworth (2012), Optimal weighted nearest neighbour classifiers, Annals of Statistics 40(5), 2733–2763. https://doi.org/10.1214/12-AOS1049 （仅作为分类遗憾边界积分思想的相关参考，本文采用不同硬约束损失。）

建议主文保留 05 的广泛适用收敛率定理；本极限定理在验证实际模型的光滑边界、截断及并列条件之后再决定进入正文还是附录。
