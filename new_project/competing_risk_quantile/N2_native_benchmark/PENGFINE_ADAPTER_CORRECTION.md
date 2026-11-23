# Peng–Fine 原生预测适配器的核查与修正（冻结数据不变）

**核查对象**：`cmprskQR` v0.9.3、`predict.crrQR()` 的作者程序源码。

**源码**：https://github.com/cran/cmprskQR/blob/master/R/cmprskQR.r 。作者实际实现为：

```r
xb <- tcrossprod(object$beta.seq, x)
exb <- exp(xb)
if (rearrangement) exb <- apply(exb, 2, sort)
lhat <- cbind(exb, object$tau.seq)
```

因此返回矩阵的**前 n_new 列是不同患者在各 tau 下的条件分位数时间**，**最后一列才是 tau 网格**。原适配器把**第一列**误当作 `time`，把其他各列误当作 CIF 值。这是我们自己的输出语义错误，不能据此认定 Peng–Fine 原论文方法失败。首次运行以大于 1 的“非法 CIF”拒绝绝大多数患者，即源于此误读。

**适配器修复约束**：
1. 仍然使用冻结的 9 份 CSV、相同 DGP/种子/训练测试人群、相同 `cmprskQR::crrQR` 模型与 `tau.range=.02–.26`、`tau.step=.02`。
2. 直接根据**最后一列 tau**与**前 n_new 列 Q(p)** 插值/匹配预设诊断水平 .06/.12/.18/.24，不经过任何“拟合 CIF 再反演”步骤；这才是直接分位数估计的原生语义。
3. 使用 `rearrangement=TRUE` （首次运行已锁定）保持 p 上的预测时间单调。
4. `Qhat >L` 表示模型预测窗口内不可达，`Qhat` 在 (0,L) 内才计为窗口内有限分位数；报告真实/预测可达和合法评分覆盖。对无有限预测不得计算任意 `|L-Q|` 伪 MAE。
5. 若模型产生非有限、非正数或不合格的矩阵形状，计入拟合/预测失败；不得裁剪以获得好看的结果。
6. 版本化修订和所有运行日志必须保留。旧无效的“非法 CIF”统计**作废**，不可用作 Peng–Fine 统计表现证据。

**修复性质**：软件输出的正确解码，不是数据机制、算法或调参的事后选择。R 结果重新运行后才可参与和 CR-RSF、SurvivalBoost 的并列比较。
## 二次源代码审计：拟合时间必须对数变换（补充修复）

作者公开代码 `crrQR` 的函数头明确写有 `ftime = vector of failure/censoring times (log-transformed)`；函数内部的 `pseudo.resp` 使用 `ftime` 本身作线性分位数响应，而 `predict.crrQR` 使用 `exp(x beta(tau))` 得到原始时间。因此，在本次原始时间 CSV 上**应输入 `ftime=log(train$ftime)`**。首轮和解码修正后的第二轮原型均误将正值原始时间传给该函数，导致模型实际拟合了错误的时间尺度。

由于 6 个训练 CSV 的最小观测时间均严格大于 0，可以在不修改原始数据的情况下按需对数变换。此修复不改变实验样本、超参数和结果定义。**之前所谓 Peng–Fine 的大 MAE 和低可达率作废，不能作为该方法本身的数值表现**。

引用源码：<https://github.com/cran/cmprskQR/blob/master/R/cmprskQR.r>，`crrQR` 函数头与 `predict.crrQR` 函数体。该关键实现细节比简略的包帮助文本更明确。
