> 资料状态：基于正式文章或公开作者稿核对。数值为原文报道，不是本项目重新模拟。公式后的“推导补充”由本项目独立推导。

# Linn, Laber & Stefanski (2017) — Interactive Q-Learning for Quantiles

**发表：** *JASA*, 112(518), 638–649。  
**正式出版：** https://doi.org/10.1080/01621459.2016.1155993  
**开放全文：** https://pmc.ncbi.nlm.nih.gov/articles/PMC5586239/  
**读取范围：** 双阶段规则定义、TIQ/QIQ 动态规划、模拟和 STAR*D 真实分析。

### 4.1 主要问题与概念

研究的是**两个真正的治疗决策时点**：先依照 $H_1$ 选 $A_1$，观察中间情况构成 $H_2$ 后再选 $A_2$。与只最大化最终 $E(Y)$ 的 Q-learning 不同，希望最大化某阈值超过概率或最终结局边际 $\tau$ 分位数。

- TIQ：Threshold Interactive Q-learning。对指定门槛 $\lambda$，最大化 $P(Y>\lambda)$。
- QIQ：Quantile Interactive Q-learning。对给定 $\tau$，最大化 $Q_\tau(Y^d)$。

### 4.2 方法逻辑

首先估计最终结局条件分布/超过阈值概率 $P(Y>\lambda\mid H_2,A_2)$，为给定历史求第二时点最优 $A_2$。再把第二时点规则带来的结果按条件分布对中间病史积分，倒推第一时点决策。QIQ 需要寻找使最终策略诱导分布达到指定分位水平的门槛，从而不是单纯把传统 Q-learning 的回归损失换成 pinball 就结束。

这种问题的困难包括非线性分位数泛函、对条件分布模型的依赖、历史状态的传播和多个时点嵌套优化；论文证明对应价值的一致性。

### 4.3 数值实验和实际分析

模拟用不同真实反应机制检验 TIQ/QIQ 与常规 Q-learning、针对二元结局的 Q-learning 的治疗推荐和值函数，特别考察低分位点下、存在异方差/偏斜时是否与均值目标发生差异；常见训练样本 $n=250$，实验多次重复，利用大型测试样本计算真实策略价值。某些低分位和异质性情形 QIQ 优势明显，均值与分位数方向一致的情形提升较少。

**STAR*D 子样本（132人）报告的 TIQ 结果：**

| 方法 | 阈值超过概率的估计价值 |
| --- | ---: |
| TIQ-learning | 0.24 |
| 常规 Q-learning | 0.23 |
| Binary Q-learning | 0.19 |
| 固定策略 $(A_1,A_2)=(-1,1)$ | 0.24 |

这组实际分析也说明新规则在真实数据上可能与传统方法接近，不能以“分位数目标不同”推断必然有巨大临床改善。

### 4.4 与本课题的区别

**最需要纠正的是“两阶段”这一术语。** Linn 使用的是序贯真实治疗过程（时间点1→中间历史→时间点2）；我们使用的是单一时点对候选集合进行先保护、再择优的层级目标。若论文英文题目写成 two-stage dynamic treatment regime，会使审稿人误以为有 $A_1,A_2$ 和中间协变量。除非你的方法确实引入二次治疗，否则宜称 *two-step constrained treatment rule* 或 *lexicographic/constrained individualized treatment rule*，而非动态 DTR。

---

## 4.5 具体推导：为什么第二时点可先求“对所有阈值”共同最优

**独立推导，依照原文第 2 节符号思想整理**。假设第二时点模型写成

$$Y=m(H_2)+A_2c(H_2)+\varepsilon,$$

其中 $A_2\in\{-1,1\}$，且残差 $\varepsilon$ 的分布不因 $A_2$ 变化。令其 CDF 为 $F_\varepsilon$。给定第二时点病史 $H_2=h_2$ 和治疗 $a_2$，

$$P(Y\le\lambda\mid h_2,a_2)=F_\varepsilon\{\lambda-m(h_2)-a_2c(h_2)\}.$$

由于 $F_\varepsilon$ 单调不减，要最小化 $P(Y\le\lambda\mid h_2,a_2)$，应使 $a_2c(h_2)$ 尽可能大。因此

$$\boxed{\pi_2^*(h_2)=\mathrm{sign}\{c(h_2)\}.}$$

这种处方同时最大化**任意**阈值超过概率，从而也对所有分位点最佳。这一结论依赖“治疗只平移结局、条件误差分布不因治疗改变”的结构；若存在治疗特异方差或尾部差异，第二时点的最佳选择可能取决于 $\lambda$ 或 $\tau$，不能原样应用。

## 4.6 从第二时点倒推第一时点的积分

令 $G(u,v\mid H_1=h_1,A_1=a_1)$ 表示给定第一阶段病史和治疗后，$(m(H_2),c(H_2))$ 的条件联合分布。选第二时点最优规则之后，$Y=m(H_2)+|c(H_2)|+\varepsilon$，所以第一时点条件低于阈值概率为

$$I(\lambda;h_1,a_1)=\int F_\varepsilon\{\lambda-u-|v|\}\,dG(u,v\mid h_1,a_1).$$

因此

$$\boxed{\pi_{1,\lambda}^*(h_1)=\arg\min_{a_1}I(\lambda;h_1,a_1).}$$

TIQ 直接给定阈值 $\lambda$ 做优化；QIQ 要在候选 $\lambda$ 上搜索与目标分位水平 $\tau$ 对应的最优策略，非简单对未来 outcome 做一次条件均值 Q-learning。这一积分体现中间病史通过第一时点治疗改变，属于真实**纵向两阶段决策**。

## 4.7 为什么本文“两层准则”不能叫 dynamic Q-learning

本文没有 $H_2$、没有 $A_2$、没有第一次治疗后的再随机化，也无需 g-公式沿时间序贯积分。我们只有单次治疗 $a$ 和两条评价准则 $Q_{all}$、$Q_1$。对本文恰当的数学描述应为

$$\widehat d(z)\in\arg\max_{a:\,\widehat Q_{all}(z,a)\ge \widehat M_{all}(z)-\delta_Q}\widehat Q_1(z,a),$$

即 **two-step constrained treatment selection** 或者 **lexicographically constrained ITR**，不是 two-stage dynamic treatment regime。用 Linn 证明“分位数对于两阶段动态决策有用”作为文献脉络可以，但不能说本文已经解决 Linn 的动态 Q-learning 问题。

## 4.8 原实验结果的正确读法

STAR*D 的 $n=132$ 示例，TIQ 的目标阈值超过概率约 .24，固定策略 $(-1,1)$ 同为 .24；常规 Q-learning 约 .23，Binary Q-learning .19。说明理论丰富不一定带来真实例子中明显的实际优势。用于论文讨论时应同时写出样本量小、指标由模型/估计过程得到、并非大样本确证性治疗疗效差异。