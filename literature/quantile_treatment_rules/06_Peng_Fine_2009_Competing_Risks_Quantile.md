# Peng & Fine (2009)：Competing Risks Quantile Regression——逐式推导与原文数值实验核验

> **一级来源：原刊 PDF 已在用户既有资料库中找到并核对。** Limin Peng 与 Jason P. Fine，*Journal of the American Statistical Association*, 104(488), 1440–1453，DOI: https://doi.org/10.1198/jasa.2009.tm08228 。本章给出的 Monte Carlo 数值直接来自原刊第 4.1 节 Table 1、Table 2；E1178 病例与统计检验来自第 4.2 节。之前“只能查到摘要、没有原始表”的说法已纠正。下文“推导补充”属于本项目的独立解释，不冒充论文原文。

## 1. 统计对象：不是普通生存时间分位数，而是 CIF 分位数

观测到潜在的首次失效时间 $T$、首次失效原因 $J\in\{1,2\}$ 和协变量 $Z$。$J=1$ 为关注事件，$J=2$ 为竞争事件。原因 1 的累计发生函数为

$$F_1(t\mid z)=P(T\le t,J=1\mid Z=z).$$

定义扩展随机变量 $T_1^*=T$（当 $J=1$），否则 $T_1^*=+\infty$。于是对于有限 $t$，$P(T_1^*\le t\mid z)=F_1(t\mid z)$。当 $F_1(\infty\mid z)<1$，$T_1^*$ 有正概率取无穷大，其分位数可能无穷大：

$$Q_1(\tau\mid z)=\inf\{t:F_1(t\mid z)\ge\tau\}.$$

**重点**：这是竞争风险下特定原因的 subdistribution quantile。它不是“给定最终会出现原因 1 后的 $T$ 分位数”，后者的条件分布分母包含 $P(J=1\mid Z=z)$，是另一个 estimand。也不是把 $J=2$ 当作随机删失后做 Kaplan–Meier 得到的潜在净风险分位数。

## 2. 原刊模型 (1) 与随分位点变化的协变量效应

原文为统一的变换分位数回归：

$$\boxed{Q_1(\tau\mid Z)=g\{Z^\top\beta_0(\tau)\},\quad \tau\in[\tau_L,\tau_U],}$$

其中 $g$ 是预先指定的**严格单调**连接变换，通常包含正时间的指数链接或时间尺度上的恒等链接。原文乳腺癌示例明确选择 $g$ 为 **identity**。不能误写成“原文只提出指数型分位数模型”。$Z$ 一般含截距和患者特征。

$\beta_k(\tau)$ 随 $\tau$ 变动，表示变量在不同累计发生水平上的时间效应不同。与原因别 Cox 的固定 log-hazard ratio、Fine–Gray 模型固定 log-subdistribution hazard ratio 相比，它允许某种异质性。但模型仍对 $g^{-1}Q_1$ 强加线性协变量结构，**不是完全非参数或无假设的分位数估计**。

若 $\beta_0(\tau)=(h(\tau),b_0^\top)^\top$，可退化为竞争风险 AFT 型结构；此时斜率对 $\tau$ 不变。原文强调一般变系数模型更灵活。

## 3. 原文估计方程 (3)–(5)：逐步证明 IPCW

设独立删失时间 $C$，观测 $X=\min(T,C)$，定义 $\delta=1$ 表示确实观察到原因 1 事件，$\delta=2$ 表示原因 2，$\delta=0$ 表示右删失。删失存活函数

$$G(t\mid Z)=P(C\ge t\mid Z),$$

假设 $C\perp(T,J)\mid Z$，以及在目标区间 $G(t\mid Z)>0$。

原刊第 2.1 节的核心识别恒等式为

$$\boxed{E\left[\frac{I(X\le x,\delta=1)}{G(X\mid Z)}\bigg\vert Z\right]=F_1(x\mid Z).}$$

**推导**：

$$
\begin{aligned}
E\!\left[\frac{I(X\le x,\delta=1)}{G(X\mid Z)}\Bigm| Z\right]
&=E\!\left[\frac{I(T\le x,J=1,C\ge T)}{G(T\mid Z)}\Bigm| Z\right]\\
&=E\!\left[I(T\le x,J=1)\frac{P(C\ge T\mid T,J,Z)}{G(T\mid Z)}\Bigm|Z\right]\\
&=P(T\le x,J=1\mid Z)=F_1(x\mid Z).
\end{aligned}
$$

第一个等号使用 $\delta=1\Leftrightarrow(J=1,C\ge T)$ 且该事件上 $X=T$。第二个等号使用条件期望塔式法则；第三个等号使用条件独立删失。将 $x=g(Z^\top b)$，在真参数 $b=\beta_0(\tau)$ 处有

$$ E\left[ Z\left\{\frac{I[X\le g(Z^\top\beta_0(\tau)),\delta=1]}{G(X\mid Z)}-\tau\right\}\right]=0.$$

样本版即原刊式 (4)–(5) 的形式（与原刊符号相同，$\widehat G$ 为删失模型估计）：

$$\boxed{S_n(b,\tau)=n^{-1/2}\sum_{i=1}^n Z_i\left\{\frac{I[X_i\le g(Z_i^\top b)]I(\delta_i=1)}{\widehat G(X_i\mid Z_i)}-\tau\right\};\quad S_n\{\widehat\beta(\tau),\tau\}\approx0.}$$

$S_n$ 是非连续的单调阶梯式方程，通常没有字面上的精确零根，因此原刊定义**广义解**，并将其转成 L1 型凸优化问题交给常规 quantile regression 数值算法。原文使用大罚参数 $M=10^5$。此处的“$\approx0$”表示广义零交叉，不是随意忽略估计方程的误差。

**这正是可以用于本文研究的直接竞争风险分位数估计路线**。注意：为估计 $G$，原刊明确允许使用分层非参数或 Cox 型删失模型。这并不等于直接原因别 Cox 事件模型。

## 4. 一致性与方差的直观推导（本项目推导补充）

令人口矩条件 $m(b,\tau)=E[Z\{F_1(g(Z^\top b)\mid Z)-\tau\}]$。设原因 1 条件 CIF 在目标分位点附近可微，局部密度记为 $f_1(t\mid Z)=\partial F_1(t\mid Z)/\partial t$，且 $g$ 可微，则雅可比矩阵为

$$\boxed{J_\tau=\frac{\partial m(b,\tau)}{\partial b^\top}\Big\vert_{b=\beta_0(\tau)}=E\left[ZZ^\top f_1\{g(Z^\top\beta_0(\tau))\mid Z\}g'(Z^\top\beta_0(\tau))\right].}$$

当 $J_\tau$ 非奇异，经验过程满足适当随机等连续性，则局部线性化可写作

$$\sqrt n\{\widehat\beta(\tau)-\beta_0(\tau)\}\approx-J_\tau^{-1}\sqrt n\,\widehat m\{\beta_0(\tau),\tau\}.$$

**注意两个边界问题**：

1. 上式中的 $\widehat m$ 含 $\widehat G$；它的影响函数除了观察事件贡献，还含删失模型估计造成的附加贡献。因此不能只把 $I(\delta=1)/G$ 当作固定权重，套用普通线性回归标准误。原刊发展对应协方差估计与过程推断。
2. 当 $f_1(Q_1(\tau\mid z)\mid z)\to0$（CIF 进入平台）时，$J_\tau$ 可能接近奇异，难以保证稳定反演。换为直接分位数回归不能在信息论层面消除目标不可识别性。

**若目标概率未达到**，原文只在有支持的 $[\tau_L,\tau_U]$ 进行估计。当前论文将不可达值强制记为 $L$，意味着已经改变 estimand，应单独说明这一截断决策约定及其临床解释。

## 5. 原刊第 4.1 节完整实验设计要点

- 协变量：$Z^{(1)}\sim\mathrm{Unif}(0,1)$，$Z^{(2)}\sim\mathrm{Bernoulli}(0.5)$，并含截距。
- 原因归属：$P(J=1\mid Z)=p_0I\{Z^{(2)}=0\}+p_1I\{Z^{(2)}=1\}$；给定原因后生成事件时间，涉及对数时间、位置参数 $\gamma_0$ 和分布函数 $\Phi$。
- 独立删失：$C$ 的分布是 $\mathrm{Unif}(0,c_u)$ 与 $c_u$ 的点质量混合，即 $P(C\le x)=0.8x/c_u$（$0\le x<c_u$），剩余在 $c_u$。原文报告两种配置下删失/原因1/原因2占比分别约 $(20\%,56\%,24\%)$ 和 $(10\%,64\%,26\%)$。
- 两个配置：$\gamma_0=(0,-0.5)^\top$ 与 $\gamma_0=(-1,-0.5)^\top$。
- 1000 次 Monte Carlo 重复；每次 $n=200$ 或 $400$；$\tau\in\{0.1,0.2,0.3,0.4\}$，连续区间 $[\tau_L,\tau_U]=[0.1,0.4]$；计算估计系数的 empirical bias、empirical SD、average estimated SD，并研究效应随分位点变化的假设检验。

**原刊 Table 1 逐格选取（配置 I；原表各列乘以 $10^3$，表中已换算为原量纲）**：

| $\tau$ | $n$ | $\beta^{(1)}$ Bias | $\beta^{(1)}$ EmpSD | $\beta^{(1)}$ EstSD | $\beta^{(2)}$ EmpSD | $\beta^{(2)}$ EstSD |
|---:|---:|---:|---:|---:|---:|---:|
| .10 | 200 | .008 | .298 | .327 | .479 | .530 |
| .10 | 400 | .003 | .212 | .229 | .337 | .365 |
| .20 | 200 | .007 | .261 | .303 | .424 | .486 |
| .20 | 400 | .001 | .193 | .207 | .307 | .330 |
| .30 | 200 | .007 | .273 | .303 | .437 | .494 |
| .30 | 400 | .001 | .189 | .204 | .307 | .338 |
| .40 | 200 | .004 | .302 | .343 | .499 | .575 |
| .40 | 400 | .002 | .207 | .233 | .351 | .393 |

对照 $n=200\to400$ 的 $\tau=.10$，$\beta^{(1)}$ EmpSD 由 .298 降为 .212，经验比值 $0.212/0.298\approx0.711$，接近 $\sqrt{200/400}\approx0.707$。这是有限样本波动与 $n^{-1/2}$ 尺度一致的例证，**不能仅凭该比值证明所有模型条件成立**。

**原刊 Table 2 逐格选取**：配置 II 的第 2 个效应，$n=200$ 时截断平均系数的 EmpBias=.008、EmpSD=.377、EstSD=.383；$n=400$ 时 .002、.268、.267。相应针对“该效应函数在各分位点处恒为 0”的检验拒绝率，$n=200$ 为 **0.718**，$n=400$ 为 **0.958**；检验“效应不随分位点改变”对应拒绝率约 **0.042** 与 **0.049**。应区别前者的 power 和后者的 type-I error，不可泛称它们都是显著性水平。配置 I 相应的零效应检验拒绝率约 .060/.056。

## 6. 原刊第 4.2 节 E1178 真实竞争风险分析

临床问题：高龄淋巴结阳性乳癌患者在他莫昔芬 vs 安慰剂治疗下的 **breast cancer recurrence (BCR)** 与 **nonrecurrence death (NRD)**。167 人：placebo 82 人（BCR 59、NRD 19），tamoxifen 85 人（BCR 42、NRD 23）。原刊按单调连接 $g=$identity 估计 BCR 的 $\tau\in[.10,.45]$，NRD 的 $\tau\in[.05,.15]$，考虑治疗、年龄、肿瘤大小、$\log(\text{positive nodes})$。

对 BCR 分位数的截断平均协变量效应零假设检验，原刊依次报告治疗、年龄、肿瘤大小、阳性淋巴结 log 数的 $p$ 值：**0.02、0.79、0.04、0.020**。这说明治疗及两个病情严重程度变量关联 BCR 分位数，而年龄在本模型中证据较弱。效应随 $\tau$ 恒定的检验对应 $p$ 值 **0.36、0.33、0.04、0.04**，提示肿瘤大小/淋巴结数对早期和后期累计风险阈值的作用不同。这一“分位水平异质效应”是 Cox 固定风险比模型可能掩盖的信息。

**重要解释**：研究没有据此学出一个以“总体首次事件时间保护+重点 BCR 延迟”为约束的个体化治疗决策规则；它主要做原因别的条件分位数效应估计与检验，因此是**当前论文的强候选估计器，而不是完整治疗规则的先行同构方法**。

## 7. 怎么真正放进你的两层约束规则

对每名患者 $z$、治疗 $a\in\{0,1\}$：

1. 在训练集上用 $(1,z^\top,a,a z^\top)^\top$ 作为治疗与交互协变量，用 Peng–Fine 型原因 1 回归计算 $\widehat Q_1(\tau_1\mid z,a)$；注意反事实治疗交换性及模型正确性。
2. 对总体首次事件 $T$，采用独立删失生存分位数回归或合适统一估计方法得到 $\widehat Q_{\mathrm{all}}(\tau_{\mathrm{all}}\mid z,a)$。不能把 Peng–Fine 的单一原因式套上并称它同时自动估计总体。
3. 保持决策函数不变：$\widehat{\mathcal A}_\delta(z)=\{a:\widehat Q_{\mathrm{all}}(z,a)\ge\max_b\widehat Q_{\mathrm{all}}(z,b)-\delta\}$，在该集合中最大化 $\widehat Q_1(z,a)$。和 Cox/灵活 Cox 使用**相同**训练对象、目标概率、删失假设、截断规则和评价样本。
4. 不可达点要额外建模或报告：$F_1(L\mid z,a)<\tau_1$ 时将截断分位数设为 $L$，并不意味着能用 Peng–Fine 模型输出该点的可靠有限时间。
5. 单独检查以延后 BCR CIF 分位数为目标的治疗是否提高 NRD 等竞争事件的风险；否则可能出现有害的“推迟”，不一定等于真正减轻患者负担。

## 8. 证据范围

本章核对的原文正文及 Table 1、Table 2、Figure 1–4 来自用户资料库保存的原刊 PDF《Competing Risks Quantile Regression》（2009，JASA 104(488)）。这里给的是**原文阅读整理和独立公式推导**；表中数据并非我们复现得到。复现必须另外取得原作者模拟代码或严格依据论文 DGP 编写、通过数值校准核验。