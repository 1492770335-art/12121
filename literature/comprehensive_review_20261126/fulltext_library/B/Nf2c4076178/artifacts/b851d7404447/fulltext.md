# Stabilized Direct Learning for Efficient Estimation of Individualized Treatment Rules

Original PDF: [original.pdf](original.pdf). SHA256: `b851d740444705f4f99fab57ad112909696d7161c243b2693eb8a7821b4607ea`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

FORMULA CHECK REQUIRED: original PDF page 1.

````text
Stabilized Direct Learning for Eﬃcient Estimation of Individualized Treatment Rules
Kushal S. Shah1,∗, Haoda Fu2,∗∗, and Michael R. Kosorok1,∗∗∗
1Department of Biostatistics, University of North Carolina at Chapel Hill, NC 27599, USA
2Eli Lilly and Company, Lilly Corporate Center, Indianapolis, IN 46285, USA
*email: kushshah@live.unc.edu
**email: fu haoda@lilly.com
***email: kosorok@unc.edu
Summary:
In recent years, the ﬁeld of precision medicine has seen many advancements. Signiﬁcant focus has been placed
on creating algorithms to estimate individualized treatment rules (ITR), which map from patient covariates to the space
of available treatments with the goal of maximizing patient outcome. Direct Learning (D-Learning) is a recent one-step
method which estimates the ITR by directly modeling the treatment-covariate interaction. However, when the variance
of the outcome is heterogeneous with respect to treatment and covariates, D-Learning does not leverage this structure.
Stabilized Direct Learning (SD-Learning), proposed in this paper, utilizes potential heteroscedasticity in the error term
through a residual reweighting which models the residual variance via ﬂexible machine learning algorithms such as XGBoost
and random forests. We also develop an internal cross-validation scheme which determines the best residual model amongst
competing models. SD-Learning improves the eﬃciency of D-Learning estimates in binary and multi-arm treatment scenarios.
The method is simple to implement and an easy way to improve existing algorithms within the D-Learning family, including
original D-Learning, Angle-based D-Learning (AD-Learning), and Robust D-Learning (RD-Learning). We provide theoretical
properties and justiﬁcation of the optimality of SD-Learning. Head-to-head performance comparisons with D-Learning
methods are provided through simulations, which demonstrate improvement in terms of average prediction error (APE),
misclassiﬁcation rate, and empirical value, along with data analysis of an AIDS randomized clinical trial.
Key words:
D-Learning; Heteroscedasticity; Individualized treatment rule; Multi-arm treatments; Precision medicine;
Statistical machine learning.
1. Introduction
Precision medicine is a framework at the intersection of statis-
tics, machine learning, and causal inference, for leveraging pa-
tient heterogeneity to improve patient outcomes. Individual-
ized treatment rules (ITR), attempting to maximize expected
treatment beneﬁt across a population, may recommend per-
sonalized actions based on patient demographic information,
clinical biomarkers, or genetic data. One of the primary goals
of precision medicine has been formalized as decision support -
the estimation of optimal and near-optimal regimes (Kosorok
and Laber (2019)). In this vein, it is important to develop
algorithms which work eﬃciently with the data at hand.
In recent years, an extensive literature has been developed
in the area of estimating optimal ITRs. Traditionally, algo-
rithms have fallen into one of two categories: model-based vs.
policy-search approaches. Model-based approaches may also
be considered “regression-based” or “indirect” in that they
ﬁrst model the conditional response of interest and then invert
the relationship between patient covariates, treatment, and
outcome to estimate an optimal rule (Kosorok and Moodie
(2016)). Primary examples of model-based approaches are Q-
Learning (Qian and Murphy (2011)) and A-Learning (Murphy
(2003); Robins (2004)). Q-Learning approaches model the
outcome conditional on covariates, whereas A-Learning ap-
proaches model regret functions or contrast functions between
treatments (Schulte et al. (2014)). Policy-search approaches,
on the other hand, maximize value functions directly instead
of modeling the conditional mean. For this reason, they are
also known as “value-search” or “direct-search” (Kosorok
and Moodie (2016)). By sidestepping the modeling step and
directly searching for an optimal rule among a class of
policies, they may avoid model misspeciﬁcation (Xiao et al.
(2019)). Many policy-search approaches have reframed the
maximization of clinical outcomes as a weighted classiﬁcation
problem with the goal of minimizing weighted classiﬁcation
error, including the outcome weighted learning (OWL) family
of methods (Zhao et al. (2012); Zhou et al. (2017); Zhang
et al. (2020)) and various tree-based extensions (Cui, Zhu,
and Kosorok (2017); Kallus (2018); Zhu et al. (2017)).
A third category of algorithms to estimate ITRs also ex-
ists, consisting of methods which have attempted to combine
the advantages of model-based and policy-search approaches.
Often, these methods use the augmented inverse probability
weighted estimator (AIPWE) within the classiﬁcation frame-
work. Such approaches are “doubly robust” in the sense that
they enjoy greater protection against model misspeciﬁcation
and increased eﬃciency when both models are correctly spec-
iﬁed (Zhao et al. (2019); Zhang and Zhang (2018); Liu et al.
(2018)).
Tian et al. (2014) developed a “modiﬁed-covariate” ap-
arXiv:2112.03981v1  [stat.ME]  7 Dec 2021

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
2
proach for ITR estimation, which falls into the third cat-
egory but is unique in that it maintains the regression-
based framework to model the treatment-covariate interac-
tion eﬀect directly, without having to specify a main eﬀect
model or conditional mean outcome function. Later, Qi and
Liu (2018) coined the term “Direct Learning” (D-Learning),
which extended Tian et al. (2014)’s idea to nonlinear decision
rules and multi-arm treatment settings. Key extensions to D-
Learning are Angle-based Direct Learning (AD-Learning) (Qi
et al. (2020)), which improves D-Learning in the multi-arm
treatment case, and Robust Direct Learning (RD-Learning)
(Meng and Qiao (2021)), which achieves a double robustness
property.
We provide motivation for the ITR estimation approach of
this paper by considering data from the “AIDS Clinical Trial
Group Study 175” (ACTG175), a randomized clinical trial
(RCT) which compared the eﬀectiveness of four treatments in
increasing CD4 cell counts in HIV-1 patients (Hammer et al.
(1996)). Previous studies have suggested that the response of
CD4 cell count from this data has skewed, heteroscedastic
errors (Zhang et al. (2021)) which may be dependent on
patient age (Xiao et al. (2019)). In such a situation, when the
variance of the clinical outcome is a function of the covariates
(or treatment), the D-Learning family of estimators remains
consistent for the optimal ITR, but gives each observation
equal weight by default in model training. A reweighting
approach which utilizes this error structure to prioritize obser-
vations with smaller expected outcome variance is beneﬁcial
because it can attain greater eﬃciency when estimating an
ITR.
In this article, we propose Stabilized D-Learning (SD-
Learning), a method to increase the eﬃciency of D-Learning
estimates in situations where the variance of the error term is
non-homogeneous and a function of the treatment and covari-
ates. SD-Learning leverages this heteroscedasticity through
a residual reweighting framework where residual variance
is modeled through ﬂexible machine learning methods. We
also develop an internal cross-validation scheme allowing for
the selection of an optimal model amongst methods such as
XGBoost (Chen and Guestrin (2016)) and random forests
(Breiman (2001)). The extension of SD-Learning to scenarios
with K ⩾3 treatment arms is also included, and estimation
ﬁts within a least squares framework.
SD-Learning is simple to implement and can be stacked on
top of existing D-Learning approaches to improve eﬃciency in
a range of situations. We show that SD-Learning parameter
estimates are consistent, achieve asymptotic normality in
binary and multi-arm treatment scenarios in the presence
of heterogeneous error, and have greater eﬃciency than D-
Learning estimates. Additionally, we establish value function
convergence bounds. In our simulations, we add a resid-
ual reweighting step to D-Learning, AD-Learning, and RD-
Learning to show that SD-Learning can improve parameter
estimation across a variety of scenarios with diﬀerent error
structures.
The rest of this paper is organized as follows: In Section 2,
we introduce the methodology of SD-Learning. Speciﬁcally,
Section 2.1 reviews recent developments in D-Learning and
Section 2.2 introduces the mathematical motivation behind
SD-Learning and outlines the reweighting solution. Section
2.3 extends the reweighting solution to scenarios with multi-
arm treatments. In Section 2.4, the residual model ﬁtting
step of the method is described in greater detail, and a
stepwise implementation of the method is delineated. Section
2.5 extends the method to ITR estimation settings with
observational data. In Section 3, theoretical results for SD-
Learning including consistency, asymptotic normality, asymp-
totic eﬃciency, and value bounds are established for binary
and multi-arm settings. Head-to-head simulations comparing
SD-Learning to D-Learning, AD-Learning, and RD-Learning
based on average prediction error (APE), misclassiﬁcation
rate, and empirical value are provided in Section 4, and value
comparisons from analysis of the ACTG175 RCT data are
made in Section 5. Concluding discussions and areas for future
work are presented in Section 6.
2. Stabilized Direct Learning (SD-Learning)
Although SD-Learning can be used with observational data,
for simplicity, we ﬁrst consider an RCT setting to demonstrate
the methodology. For n patients, we observe independent real-
izations of the random triplet (X, A, R). Patient covariates are
represented by the p-dimensional vector, X ∈X ⊂Rp, which
includes an intercept. We start with the binary treatment
scenario, A ∈A = {−1, 1}. A patient’s clinical outcome is
represented by R ∈R, and it is assumed, without loss of
generality, that larger R corresponds to a better outcome.
The probability of receiving treatment a, given covariates x,
is represented by π(a, x) = Pr(A = a|X = x). An ITR,
d(X): X 7→A, is a mapping from the space of covariates
to the the space of treatments. We use 1(·) to represent
the indicator function. For a matrix Z, let Z⊤denote its
transpose. Pn (·) represents the empirical average such that
Pn(X) = n−1 Pn
i=1 xi, where x1, ..., xn are realizations of the
random variable, X. Let Vec(Z) represent vectorization of
Z, which stacks the columns (e.g. for Z =
  a b
c d

, Vec(Z) =
[a c b d]⊤).
Let Y ∗(−1) and Y ∗(1) represent the potential outcome that
would have been observed had a patient received treatment
−1 or 1, respectively. We make the usual assumptions for
this context from the potential outcomes framework of Rubin
(1974): (i) Stable unit treatment value assumption (SUTVA):
Y = Y ∗(A), (ii) No unmeasured confounding (conditional
exchangeability): A ⊥{Y ∗(−1), Y ∗(1)} | X, and (iii) Positiv-
ity: π(A, X) > c > 0, ∀A ∈A, X ∈X. Prior to outlining the
proposed SD-Learning methodology, we review key ﬁndings
from the D-Learning family of methods.
2.1 D-Learning Background
It is known from Qian and Murphy (2011) that the expected
response under an ITR, d, can be represented by the value
function:
V (d) = E {R | A = d(X)} = E
R · 1{A = d(X)}
π(A, X)

,
and we deﬁne an optimal ITR, dopt, as the decision rule
that maximizes the expected average response: dopt(·) =
argmax
d∈D
V (d), where D is a prespeciﬁed class of decision rules.

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
SD-Learning for Eﬃcient Estimation of Individualized Treatment Rules
3
2.1.1 D-Learning.
In the two-arm setting, assume that
the outcome can be expressed by:
R = m(X) + δ(X)A + η,
(1)
where m(X) represents the main eﬀect, δ(X) represents the
treatment interaction eﬀect, and η is a mean-zero random
error term. Note the following:
dopt(X) = sign {E(R|X, A = 1) −E(R|X, A = −1)}
:= sign

f opt(X)
	
,
(2)
f opt(X) = E

RA
π(A, X)
X

= 2δ(X).
(3)
Tian et al. (2014) made the connection between the optimal
ITR in (2) and formulation of the optimal decision function in
(3), which forms the basis of D-Learning, as f opt(X) can now
be directly learned through a regression method of choice.
Lemma 1 of Qi and Liu (2018) shows that an estimation
framework for f opt(X) in (3) is:
f opt(X) ∈argmin
f
E
{2RA −f(X)}2
π(A, X)

,
(4)
and considering the class of linear decision functions, F =
{f(X) = X⊤β : β ∈Rp}, the estimation problem can be
solved with ordinary least squares (OLS) with or without
regularization.
2.1.2 AD-Learning.
Qi and Liu (2018) proposed pairwise
D-Learning for the case where A ∈{1, 2, ..., K}. This was
improved with AD-Learning (Qi et al. (2020)), which uses
the angle-based approach of Zhang and Liu (2014) to project
treatment A into K simplex vertices deﬁned in RK−1. Let
treatment A be represented by the vector uA ∈RK−1:
uA =



1
√K−11K−1,
A = 1
q
K
K−1eA−1 −
1+
√
K
√
(K−1)3 1K−1,
2 ⩽A ⩽K.
(5)
Here, ei is a (K −1)-dimensional vector of zeroes with 1 in
the ith location. Let the random vector U be such that U |
(X, A)
a.s.
= uA. The working model is:
R = µ(X) +
K
X
k=1
δk(X)1(A = k) + η,
where µ(X) is the main eﬀect, δk(X) is the interaction eﬀect
between the kth treatment and covariates, and η is the mean-
zero random error. The optimal ITR can then be expressed
as:
dopt(X) = argmax
k∈{1,...,K}
E(R|X = x, A = k)
= argmax
k∈{1,...,K}
u⊤
k E

RU
π(A, X)
X

= argmax
k∈{1,...,K}
u⊤
k
K
X
k=1
δk(X)uk
:= argmax
k∈{1,...,K}
u⊤
k f opt(X)
= argmax
k∈{1,...,K}
δk(X),
(6)
where f opt(X): Rp+1 7→RK−1. As shown in Lemma 1 of
Qi et al. (2020), this leads to an estimation problem for
independent responses of the form:
f opt(X) ∈argmin
f∈RK−1E
"
{KRU −f(X)}⊤{KRU −f(X)}
π(A, X)
#
.
Importantly, this is equivalent to the following working model
and estimation framework:
K
K −1R = U ⊤f(X) + ϵ,
(7)
f opt(X) ∈argmin
f∈RK−1 E
"
1
π(A, X)

K
K −1R −U ⊤f(X)
2#
.
2.1.3 RD-Learning.
Meng and Qiao (2021) develop RD-
Learning, which replaces the outcome ri in D-Learning with
the residual ri −ˆm(xi), where ˆm(X) is an estimator for the
main eﬀect, m(X) (similarly to Zhou et al. (2017)). This
reduces the variance and leads to doubly robust estimation of
the treatment eﬀect in the sense that consistency is guaran-
teed if either the main eﬀect model or propensity score model
is correctly speciﬁed.
2.2 SD-Learning
For the binary treatment RCT setting, π(A, X) is known,
and assuming (1), the D-Learning estimation problem in (4)
induces the following working model:
2RA = f(X) + ϵ.
Assume that E(ϵ|A, X) = 0 and var(ϵ|A, X) = σ2
0(A, X).
Note that this error term is very general; it can be an arbitrary
function of the treatment and covariates. In this case, the D-
Learning estimator of the treatment eﬀect is consistent, but
due to the potential heteroscedasticity, it may lack eﬃciency
as it gives each observation equal weight. Considering decision
functions in F, we propose a modiﬁed D-Learning objective
function based on reweighting to gain eﬃciency:
ˆβS
n = argmin
β∈Rp
Pn
 (2RA −X⊤β)2
w(A, X)π(A, X)

,
(8)
where w(A, X) is an arbitrary set of weights which need
to be speciﬁed and/or estimated. The following assumptions
establish the basic conditions needed to ﬁnd optimal weights.
For all A ∈A and X ∈X almost surely:
Assumption 1:
E(XX⊤) is full rank and E ∥X∥2 < ∞.
Assumption 2:
0 < c1 ⩽σ2
0(A, X) ⩽c2 < ∞.
Assumption 1 imposes a ﬁnite second moment restriction
and assumes nonsingularity of the covariates. Assumption 2
ensures that the true residual variance function is ﬁnite and
nonzero (bounded above and below).
Proposition 1:
Under Assumptions 1 and 2, setting
w(A, X) =
σ2
0(A,X)
π(A,X) minimizes the estimator of the asymptotic
variance of (8).

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
4
Proposition 1 oﬀers a simple way to perform the reweight-
ing. Let ˆβD
n be a consistent estimate of β0, which can be
obtained by ﬁtting a traditional D-Learning model (Qi and
Liu (2018)). Since ϵ = 2AR −X⊤β, σ2
0(A, X) can be esti-
mated by regressing

2AR −X⊤ˆβD
n
2
on (A, X) through a
parametric or nonparametric model. The resulting prediction
function can be denoted as ˆσ2
n(A, X). This procedure breaks
down into the following implementation steps:
(1) Obtain a D-Learning estimator:
ˆβD
n = argmin
β∈Rp
1
n
n
X
i=1
 2riai −x⊤
i β
2
π(ai, xi)
.
(2) Regress
the
squared
residuals
from
Step
1,

2AR −X⊤ˆβD
n
2
, on the treatment and covariates,
(A, X), to obtain prediction function ˆσ2
n(A, X).
(3) Find ˆβS
n using:
ˆβS
n = argmin
β∈Rp
1
n
n
X
i=1
π (ai, xi)
 2riai −x⊤
i β
2
ˆσ2n (ai, xi) π (ai, xi)
= argmin
β∈Rp
1
n
n
X
i=1
 2riai −x⊤
i β
2
ˆσ2n (ai, xi)
.
(9)
Thus, the SD-Learning estimator for the binary treatment
case is formulated as a least squares problem, reweighted by
the inverse of the estimated residual variance. A procedure
for obtaining an improved estimate of the parameters has
therefore been provided for binary D-Learning in the case of
heteroscedasticity. The same reweighting framework can be
used in the case of RD-Learning, where the only diﬀerences
are that a model for the main eﬀect, m(X), must be esti-
mated, and the augmented outcome becomes R∗= R−ˆm(X).
2.3 Extension of SD-Learning to Multiple Treatments
Now, we expand the treatment space to K treatments, in-
dexed as A ∈{1, 2, ..., K}. Let uA ∈RK−1 be deﬁned as
per (5). We use the working model in (7) under the same
scenario as Section 2.2: E(ϵ|A, X) = 0 and var(ϵ|A, X) =
σ2
0(A, X). The class of linear decision functions is deﬁned as
F = {f(X) = B⊤X : B ∈Rp×(K−1)}.
Adding an arbitrary weight term, w(A, X), in the denom-
inator, similarly to the binary case, we propose the SD-
Learning objective function as a modiﬁed version of AD-
Learning:
ˆBS
n =
argmin
B∈Rp×(K−1)Pn

1
w(A, X)π(A, X)
×

K
K −1R −U ⊤B⊤X
2 
.
(10)
Again, w(A, X) must be optimally chosen. We can reframe
this objective function so that it is easier to optimize. Using
the identity Vec (ABC) =
 C⊤⊗A

Vec(B) and the fact that
U ⊤B⊤X is a scalar,
U ⊤B⊤X = Vec

U ⊤B⊤X

=

X⊤⊗U ⊤
Vec

B⊤
= X⊤
∗B∗,
where X∗=
 X⊤⊗U ⊤⊤, B∗= Vec
 B⊤
, and ⊗denotes
the Kronecker product. This allows for an equivalent refor-
mulation of the SD-Learning estimation problem:
ˆBS
n =
argmin
B∈Rp×(K−1)Pn

1
w(A, X)π(A, X)
×

K
K −1R −X⊤
∗B∗
2 
.
(11)
Note that B∗and X∗in (11) are vectors in Rp(K−1), unlike B
and X in (10), which are a matrix in Rp×(K−1) and vector in
Rp, respectively. w(A, X) can now be optimized in a fashion
akin to the binary SD-Learning case:
Proposition 2:
Under Assumption 1 for X∗instead of X
and Assumption 2, setting w(A, X) =
σ2
0(A,X)
π(A,X) minimizes the
estimator of the asymptotic variance of (11).
Note that these are the same weights as found in Proposi-
tion 1 for the binary treatment case. Having found the optimal
weights, w(A, X), we switch back to non-vectorized notation
(using U ⊤B⊤X instead of the equivalent X⊤
∗B∗). σ2
0(A, X)
can be estimated by regressing
n
K
K−1R −u⊤  ˆBAD
n
⊤X
o2
on
(A, X) through a parametric or nonparametric model, with
the estimate denoted by ˆσ2
n(A, X). Let
ˆBAD
n
represent a
consistent estimate of B0, obtained via an AD-Learning model
(Qi et al. (2020)). The implementation of this procedure is as
follows:
(1) Obtain an AD-Learning estimator:
ˆBAD
n
=
argmin
B∈Rp×(K−1)
1
n
n
X
i=1
1
π(ai, xi)

K
K −1ri −u⊤
aiB⊤xi
2
.
(2) Regress
the
squared
residuals
from
Step
1,

K
K−1R −u⊤
ˆBAD
n
⊤
X
2
,
on
(A, X),
to
obtain
prediction function ˆσ2
n(A, X).
(3) Find ˆBS
n using:
ˆBS
n =
argmin
B∈Rp×(K−1)
1
n
n
X
i=1
1
ˆσ2n(ai, xi)

K
K −1ri −u⊤
aiB⊤xi
2
.
(12)
Thus, SD-Learning in the multi-arm scenario remains a
least squares problem, and under non-homogeneous error
structures, provides an increased-eﬃciency estimation ap-
proach through the angle-based framework (refer to Theo-
retical Results in Section 3).
As per covariate dimensionality and sparsity assumptions,
the OLS steps of the implementation (Steps 1 and 3) in the
binary or multi-arm case can be replaced with LASSO, Ridge,
Elastic Net, or other regularized least squares techniques.
Detailed proofs of Propositions 1 and 2 can be found in Web
Appendix A of the Supporting Information.
2.4 Residual Model Fitting
The residual modeling step in the implementation of SD-
Learning is important, with various parametric and nonpara-
metric options. We propose LASSO, random forest, and/or

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
SD-Learning for Eﬃcient Estimation of Individualized Treatment Rules
5
Table 1
High-level overview of the SD- and SAD-Learning algorithms.
(1)
Initial Estimate: Obtain a consistent estimate of the parameters of the decision function through D-Learning
in the binary treatment case or AD-Learning in the multi-arm treatment case (unweighted).
(2)
Hyperparameter Tuning: Obtain squared residuals from Step (1) and ﬁnd optimal LASSO, random forest,
XGBoost, and/or SuperLearner parameters for predicting squared residuals from covariates.
(3)
Internal CV: Using K-fold cross-validation, compare average test set MSEs for methods in Step (2) and pick
the method with the lowest error.
(4)
Obtaining Weights: Using optimal method from Step (3), obtain the predicted squared residual for each of n
observations.
(5)
Reweighted Estimate: Using predictions from Step (4) as weights, obtain stabilized parameter estimates
through SD-Learning as in (9) or SAD-Learning as in (12).
tree-based XGBoost for residual modeling in order to include
a diversity of approaches through parametric assumptions,
bagging, and/or boosting, respectively. Additionally, all three
methods were chosen for their speed, LASSO and XGBoost
for their ability to handle sparsity (Zhang and Huang (2008),
Fauzan and Murﬁ(2018), Chen and Guestrin (2016)), and
in the case of random forests and XGBoost, ﬂexibility. They
also have a relatively low number of hyperparameters to tune,
making their implementation easier. A SuperLearner algo-
rithm can also be used, which combines candidate parametric
and nonparametric methods to ﬁnd an optimal combination
which minimizes cross-validated risk. The SuperLearner has
been shown to perform asymptotically as well as or better
than any of the constituent candidate learners (van der Laan
et al. (2007)).
Instead of picking one residual modeling framework, we
propose comparing multiple models using an internal cross-
validation step. After residuals from the initial D-Learning
ﬁt are obtained, they are squared and regressed against the
covariates, and hyperparameters for each model are tuned.
Then, using mean squared prediction error of the squared
residuals as the evaluation metric, the models can be com-
pared using K-fold cross-validation. We describe the algo-
rithm with the high-level framework given in Table 1.
2.5 Extension to Observational Data
It was assumed in the development of the methodology that
the data stem from an RCT setting. In practice, however, it
is often the case that drug eﬃcacy is evaluated retrospec-
tively through observational data. In this case, treatment
assignment probabilities are not known. If the conditional
exchangeability assumption holds, the SD-Learning method-
ology remains intact, but π(A, X) must be estimated given
the observed covariates. As discussed in Chen, Zeng, and
Kosorok (2016), the estimate ˆπ(A, X) could be obtained by
a parametric model such as logistic regression (multinomial
regression in the multi-arm case), or a nonparametric method
such as boosting, random forests, or support vector regression
(SVR).
3. Theoretical Results
In this section, we establish the theoretical properties of SD-
Learning for settings with ﬁxed dimension, p. We establish
consistency and asymptotic normality of the SD-Learning
estimator, along with bounds for the empirical value function.
Detailed proofs for all theorems and lemmas can be found in
Web Appendix B of the Supporting Information. We state
two additional assumptions below, and will delineate which
assumptions are needed for each theorem.
Assumption 3:
ˆσ2
n(A, X)
is
uniformly
consistent
for
σ2
0(A, X). That is, ||ˆσ2
n(A, X)−σ2
0(A, X)||∞,(A,X)
P→0, where
|| · ||∞,(A,X) represents the uniform norm over (A, X), and
(A, X) is in a bounded set. In the case of observational data,
we also require ||ˆπn(A, X) −π0(A, X)||∞,(A,X)
P→0.
Assumption 4:
∀γ > 0, ∃G which is P-Donsker such that
Pr
n
Xϵ
ˆσ2n(A,X) ∈G
o
> 1 −γ, ∀n-large.
In Lemma 1, below, we propose two estimation methods for
ˆσ2
n(A, X) and provide justiﬁcation that they satisfy Assump-
tions 3 and 4. Then, in Theorem 1, we establish consistency
of the SD-Learning estimator in the binary treatment setting,
and with consistency established, asymptotic normality of the
estimator is shown in Theorem 2.
Lemma 1:
Estimating σ2
0(A, X) with (1) Linear regres-
sion with arbitrary features and (2) Random forests satisﬁes
Assumptions 3 and 4.
Theorem 1:
If Assumptions 1-3 are met, ˆβS
n
P→β0.
Theorem 2:
Let Y ∗= 2AY , E(Y ∗|X) = Xβ0, and ˆβS
n
be a consistent estimator of β0. Denote U0 = E

XX⊤
σ2
0 (A, X)

.
If Assumption 4 is additionally met, then √n
 ˆβS
n −β0

is
asymptotically normal with variance U −1
0
.
ˆβS
n achieves the lower bound of the asymptotic variance
shown in Proposition 1, and is thus the optimal estimator for
β0 among the weighted choices of (8). Thus we have achieved
consistency, convergence, and asymptotic eﬃciency.
Since Section 2.3 uniﬁes the framework between SD-
Learning in binary vs. multi-arm treatment scenarios, the
extension of Theorems 1 and 2 to multi-arm treatment are
natural. This development is outlined in Theorem 3:
Theorem 3:
Let X∗=
 X⊤⊗U ⊤⊤, B∗= Vec
 B⊤
,
Y ∗=
K
K−1R where A ∈{1, 2, ..., K}, and E (Y ∗|X∗) =

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
6
X⊤
∗B∗. Denote U0 = E
 X∗X⊤
∗
σ2
0 (A, X)

. Under Assumption
1 for X∗instead of X, Assumption 2, and Assumption 3,
ˆBS
∗
P→B∗. Moreover, if Assumption 4 is additionally met,
√n

ˆBS
∗−B∗

is asymptotically normally distributed with
variance U −1
0
.
Thus, all results established for the binary treatment case
extend to the multi-arm setting. Combining the asymptotic
normality result of Theorem 3 with Theorem 1 of Qi et al.
(2020) which shows that
V (dopt) −V ( ˆdn) ⩽2K(K −1)
1 −C(K)

E
f opt −ˆfn

2
2
1/2
,
where C(K) is a constant only depending on K, √n-
convergence of V ( ˆdn) to V (dopt) is established.
4. Numerical Results: Simulation Studies
We perform head-to-head comparisons between SD-Learning
and the D-Learning family of methods: D-Learning, AD-
Learning, and RD-Learning. In all simulations, LASSO is used
to obtain estimates of the decision function parameters (Steps
1 and 5 of Table 1), and we use internal cross-validation to
pick between LASSO, random forest, and XGBoost at the
intermediate residual modeling steps (Steps 2 and 3 of Table
1). Methods are evaluated based on three criteria:
(1) Average Prediction Error (APE): Coeﬃcient accuracy
determined by mean squared error of true vs. pre-
dicted decision functions. For binary simulation set-
tings, APE = n−1 Pn
i=1
 x⊤
i β0 −x⊤
i ˆβn
2; for multi-
arm settings, APE = n−1 Pn
i=1

f opt(xi) −ˆf(xi)
	2 =
n−1 Pn
i=1
 PK
k=1 δk(xi)uk −PK
k=1 ˆδk(xi)uk
	2.
(2) Misclassiﬁcation Rate: % incorrect treatment assignment.
(3) Empirical Value: ˆV (d) = Pn [R · 1{A = d(X)}/π(A, X)]
Pn [1{A = d(X)}/π(A, X)]
.
Better performance corresponds to lower APE, lower misclas-
siﬁcation rate, and higher empirical value. In all simulations,
performance based on these criteria is determined on a test
data set with 10000 observations. 100 replications of each
simulation setting are performed.
We compare all binary methods with p = {30, 60, 120} and
multi-arm methods with p = {20, 40, 60}. Simulated observa-
tions are independent with continuous covariates generated
according to a U[-1,1] distribution. To allow for heteroscedas-
ticity, the outcome is generated according to the working
model in (1) for binary treatments and (7) for multi-arm
treatments, but with ϵ generated according to σ0(X) ∗Z,
where Z ∼N(0, 1) and σ0(X) > 0. Here, non-constant σ0(X)
introduces heteroscedasticity.
4.1 Binary Treatment Simulations
We compare SD-Learning and D-Learning with four simula-
tion settings where n = 200:
(1) m(X) = 1 + 2X1 + X2 + 0.5X3;
δ(X) = 0.5(0.9 −X1); σ2
0(X) = 1.
(2) m(X) = 1 + 12X1 + 6X2 + 3X3;
δ(X) = 4X1; σ2
0(X) = 0.25 + (X2 + 1)2.
(3) m(X) = 1 + 10X1 + 10X2 + 20X3 + 5X4;
δ(X) = 4(0.3 −X1 −X2); σ2
0(X) = 1 + 4X2
3.
(4) m(X) = 1 + 10X1 + 6X2
1 −6X2
2 + 10X3;
δ(X) = 2X2
2 +1.5X3+3X4; σ2
0(X) = .25+(.3−X1−X2)2.
Scenario (1) is very similar to the third linear decision bound-
ary scenario in Qi and Liu (2018), and has homoscedastic
error. In this case, an intermediate residual reweighting step
is not necessary since the optimal weights are w(X) = 1 by
design, which is the default for D-Learning. Scenarios (2)-(4)
introduce heteroscedasticity through the error term. Scenarios
(2) and (3) meet linear decision function assumptions, and in
both cases, the interaction eﬀect has variables in common with
the main eﬀect but not with the error function. Finally, (4)
is a nonlinear decision boundary scenario where SD-Learning
is misspeciﬁed. This scenario will help test the robustness of
SD-Learning.
Figure 1 shows the APE for all four scenarios, and Table 2
contains misclassiﬁcation rates and the estimated empirical
value function on the test dataset. Since Scenario (1) has
homoscedastic error, D-Learning performs “optimally” in the
sense of correctly speciﬁed weights; hence, stabilizing the D-
Learning estimates is technically not needed. However, SD-
Learning still performs similarly to D-Learning, with com-
parable APE and only slightly lower misclassiﬁcation rate
and empirical value. For scenarios (2) and (3), SD-Learning
outperforms D-Learning because of the heterogeneous error
structure. SD-Learning prioritizes observations with smaller
expected outcome variance, and therefore estimates param-
eters more eﬃciently, shown by the lower APEs in Figure
1. This results in better classiﬁcation and therefore, higher
empirical value. In Scenario (4), although the true decision
boundary is nonlinear, SD-Learning’s ﬂexible modeling of
heteroscedasticity gives it an advantage over D-Learning.
We also perform simulations to show the advantage of sta-
bilizing the estimates of RD-Learning. For these simulations,
n = 100. For the main eﬀect modeling step, LASSO was used,
but nonparametric methods may also be used as per Meng
and Qiao (2021). The simulation settings for SRD-Learning
vs. RD-Learning are as follows:
(5) m(X) = 1 + 10X1 + 10X2 + 20X3 + 20X5 + 10X1X2;
δ(X) = 1.25X3 + 2.5X4; σ2
0(X) = 1 + 0.1(1 + X2
1).
(6) m(X) = 1 + 5 cos2(X1) + 10X1X2 + 20X2 + 30X5;
δ(X) = 3X1+2X2+2X2
5; σ2
0(X) = 0.5+0.5 (1 −0.25X6)3.
Both scenarios have heterogeneous error. Scenario (5) has
a true linear decision function, whereas (6) has a nonlinear
decision function along with a nonlinear cosine term in the
main eﬀect.
Figure 1 shows the APE for both scenarios, and Table 2
contains misclassiﬁcation rates and the estimated empirical
value function on the test dataset. Although RD-Learning is
already robust in the sense that the main eﬀect is removed be-
fore model ﬁtting, the reweighing step of SRD-Learning adds
eﬃciency in situations with heteroscedasticity - even in the
presence of a misspeciﬁed decision function and nonlinearity
in the main eﬀect.

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
SD-Learning for Eﬃcient Estimation of Individualized Treatment Rules
7
Figure 1.
Average Prediction Error (APE) results of four binary simulation scenarios comparing D- to SD-Learning (n =
200), two binary simulation scenarios comparing RD- to SRD-Learning (n = 100), and two multi-arm simulation scenarios
comparing AD- to SAD-Learning (n = 200). In binary scenarios, p varies from 30 to 120, and in multi-arm scenarios, p varies
from 20 to 60.
4.2 Multi-Arm Treatment Simulations
We compare SAD-Learning and AD-Learning with two multi-
arm treatment scenarios under heteroscedasticity, setting
K = 4 and n = 200 in both:
(7) m(X) = 1 + 2X1 + 2X2;
σ2
0(X) = 0.25 + 0.2(1.5 −X2)2;
δ(X) =









.75 + 1.5X1 + 1.5X2 + 1.5X3 + 1.5X4,
A = 1
.75 + 1.5X1 −1.5X2 −1.5X3 + 1.5X4,
A = 2
.75 + 1.5X1 −1.5X2 + 1.5X3 −1.5X4,
A = 3
.75 −1.5X1 + 1.5X2 −1.5X3 + 1.5X4,
A = 4.
(8) m(X) = 1 + X5 + 3X6 + 2X1X2;
σ2
0(X) = 0.5 + 2X2 ∗1(X2 > 0);
δ(X) =









0.5 + 2X1 + X2 + X3,
A = 1
1 + X1 −X2 −X3,
A = 2
1.5 + 3X1 −X2 + X3,
A = 3
1 −X1 −X2 + X3,
A = 4.
Both Scenarios (7) and (8) meet linear assumptions for the
treatment-covariate interaction eﬀects. In Scenario (7), the
heterogeneous error function is a quadratic function of the
covariate X2, but in Scenario (8) it is a spline function of X2
where the variance is constant for X2 ⩽0 and increases there-
after. Figure 1 reports the APE for both scenarios, and Table
3 displays misclassiﬁcation and value results. As observed in
the binary cases, reweighting in the multi-arm scenario under
heteroscedasticity also improves eﬃciency, resulting in lower
APEs, lower misclassiﬁcation rates, and higher empirical val-
ues. SAD-Learning improves the performance of AD-Learning
when an error structure can be learned and utilized to obtain
decision rules built by favoring observations which are more
likely to represent signal than noise.
5. Data Analysis: AIDS Clinical Trial
We apply SD-Learning approaches with a linear decision func-
tion to ACTG175 data, which may beneﬁt from a reweight-

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
8
Table 2
Mean empirical value and misclassiﬁcation rate, along with standard error of the mean (SEM), for four binary D- vs.
SD-Learning simulations and two binary RD- vs. SRD-Learning simulations for 30, 60, and 120 covariates. The
best-performing method for each category is bolded.
p = 30
p = 60
p = 120
Value
Misclass.
Value
Misclass.
Value
Misclass.
Scenario 1
D-Learning
1.43 (0.01)
0.07 (0.01)
1.43 (0.01)
0.07 (0.01)
1.44 (0.01)
0.08 (0.01)
SD-Learning
1.42 (0.01)
0.08 (0.01)
1.42 (0.01)
0.09 (0.01)
1.43 (0.01)
0.09 (0.01)
Scenario 2
D-Learning
2.27 (0.06)
0.22 (0.01)
2.35 (0.07)
0.21 (0.02)
2.30 (0.06)
0.25 (0.02)
SD-Learning
2.46 (0.05)
0.17 (0.01)
2.48 (0.06)
0.18 (0.02)
2.50 (0.06)
0.21 (0.01)
Scenario 3
D-Learning
2.64 (0.09)
0.29 (0.01)
2.40 (0.09)
0.32 (0.01)
2.16 (0.08)
0.36 (0.01)
SD-Learning
2.82 (0.08)
0.26 (0.01)
2.56 (0.09)
0.30 (0.01)
2.21 (0.08)
0.35 (0.01)
Scenario 4
D-Learning
1.81 (0.05)
0.31 (0.01)
1.91 (0.05)
0.32 (0.01)
1.90 (0.04)
0.33 (0.01)
SD-Learning
2.08 (0.03)
0.24 (0.01)
2.02 (0.05)
0.29 (0.01)
1.99 (0.04)
0.31 (0.01)
Scenario 5
RD-Learning
1.94 (0.03)
0.20 (0.01)
1.91 (0.05)
0.27 (0.01)
1.43 (0.05)
0.30 (0.01)
SRD-Learning
1.98 (0.03)
0.18 (0.01)
2.02 (0.04)
0.24 (0.01)
1.55 (0.05)
0.27 (0.01)
Scenario 6
RD-Learning
6.16 (0.04)
0.21 (0.01)
5.94 (0.04)
0.23 (0.01)
5.65 (0.05)
0.25 (0.02)
SRD-Learning
6.24 (0.04)
0.19 (0.01)
5.97 (0.04)
0.23 (0.01)
5.70 (0.05)
0.24 (0.01)
Table 3
Mean empirical value and misclassiﬁcation rate, along with standard error of the mean (SEM), for two multi-arm scenarios
comparing AD-Learning to SAD-Learning. All simulations are repeated with 20, 40, and 60 covariates. The best-performing
method for each category is bolded.
p = 20
p = 40
p = 60
Value
Misclass.
Value
Misclass.
Value
Misclass.
Scenario 7
AD-Learning
3.39 (0.02)
0.34 (0.01)
3.23 (0.03)
0.39 (0.01)
3.19 (0.03)
0.42 (0.01)
SAD-Learning
3.49 (0.01)
0.30 (0.01)
3.39 (0.02)
0.33 (0.01)
3.39 (0.02)
0.35 (0.01)
Scenario 8
AD-Learning
2.82 (0.04)
0.46 (0.01)
2.81 (0.03)
0.47 (0.01)
2.79 (0.04)
0.50 (0.01)
SAD-Learning
3.02 (0.02)
0.38 (0.01)
3.02 (0.02)
0.39 (0.01)
2.95 (0.03)
0.43 (0.01)
ing approach, as motivated in Section 1. The ACTG175
dataset is publicly available via the R package speﬀ2trial. This
double-blinded study evaluated monotherapy vs. combination
therapy approaches to increasing CD4 cell counts in HIV-
1-infected patients with initial cell counts of between 200
and 500 cells/mm3 (Hammer et al. (1996)). AIDS-deﬁning
illnesses have been shown to decrease as CD4 cell count
increases (Mocroft et al. (2013)), so larger increases in CD4
cell count are preferable.
Patients were randomly assigned to one of four daily regi-
mens with equal probability:
(1) 600 mg zidovudine (Z)
(2) 600 mg zidovudine + 400 mg didanosine (ZD)
(3) 600 mg zidovudine + 2.25 mg zalcitabine (ZZ)
(4) 400 mg didanosine (D)
The outcome we use for this analysis is the change in
CD4 cell count from baseline to 20 weeks, as done in Qi
and Liu (2018) and Qi et al. (2020). 12 covariates are se-
lected as per (Fan et al. (2017)); ﬁve continuous: weight
(kg), age (years), Karnofsky score (0-100), baseline CD4
count (cells/mm3), baseline CD8 count (cells/mm3); and
seven binary: hemophilia (1=yes, 2=no), homosexual activ-
ity (1=yes, 0=no), history of intravenous drug use (1=yes,
0=no), race (1=non-white, 0=white), gender (1=male, 0=fe-
male), antiretroviral history (1=experienced, 0=naive), and
symptomatic status (1=symptomatic, 0=asymptomatic). For
all comparisons, LASSO is used to obtain estimates of the
decision function parameters. LASSO, random forest, and
XGBoost are tuned and used for the residual modeling step
of SD- and SAD-Learning, with the optimal method picked
by internal cross-validation.

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
SD-Learning for Eﬃcient Estimation of Individualized Treatment Rules
9
Table 4
Empirical value estimates for binary AIDS data scenarios comparing performance of D- and SD-Learning on each pairwise
set of treatments (Z, ZD, ZZ, D) at varying sample sizes of training data (n = 100, 200, 400, 800). At each sample size, results
are averaged from 1000 replications, and corresponding standard error of the mean (SEM) is shown. The best-performing
method at each level of sample size is bolded. When both methods converge upon recommending a single treatment (in over
99% of patients across all replications), the treatment is speciﬁed instead of the (nearly identical) value estimates.
D-Learning
SD-Learning
D-Learning
SD-Learning
ZD vs. ZZ
n = 100
49.12 (0.31)
49.24 (0.30)
Z vs. ZD
n = 100
51.75 (0.21)
52.18 (0.20)
n = 200
51.76 (0.21)
52.12 (0.20)
n = 200
52.92 (0.15)
53.43 (0.14)
n = 400
52.74 (0.18)
53.15 (0.17)
n = 400
53.48 (0.16)
53.90 (0.16)
n = 800
53.16 (0.35)
53.55 (0.36)
n = 800
53.84 (0.35)
54.30 (0.35)
ZD vs. D
n = 100
48.67 (0.29)
48.92 (0.28)
Z vs. ZZ
n = 100
15.62 (0.27)
15.62 (0.27)
n = 200
50.59 (0.23)
51.02 (0.23)
n = 200
17.96 (0.14)
18.10 (0.15)
n = 400
52.88 (0.19)
53.28 (0.19)
n = 400
ZZ for over 99% of patients.
n = 800
55.99 (0.33)
56.42 (0.33)
n = 800
ZZ for over 99% of patients.
ZZ vs. D
n = 100
23.57 (0.13)
23.64 (0.13)
Z vs. D
n = 100
24.57 (0.19)
24.55 (0.19)
n = 200
23.89 (0.13)
23.88 (0.14)
n = 200
D for over 99% of patients.
n = 400
24.52 (0.15)
24.57 (0.15)
n = 400
D for over 99% of patients.
n = 800
25.55 (0.25)
25.48 (0.25)
n = 800
D for over 99% of patients.
Table 5
Empirical value estimates for multi-arm AIDS data scenarios comparing the performance of AD- and SAD-Learning in
selecting amongst four treatments simultaneously. Varying sample sizes of the training data were chosen to be n = 100, 200,
400, 800, and 1200. At each sample size, results are averaged from 1000 replications, and the corresponding standard error of
the mean (SEM) is shown. The best-performing method at each level of sample size is bolded.
AD-Learning
SAD-Learning
n = 100
43.27 (0.43)
43.98 (0.43)
n = 200
47.19 (0.37)
48.29 (0.35)
n = 400
50.57 (0.25)
51.74 (0.22)
n = 800
53.35 (0.18)
54.25 (0.17)
n = 1200
54.27 (0.23)
55.24 (0.23)
5.1 Binary Scenario
We compare the performance of D-Learning and its corre-
sponding stabilized version, SD-Learning, for each pairwise
set of treatments from the four choices. We randomly split
the data into a training set of n observations, using the rest
of the observations as testing data. n is selected to be 100,
200, 400, and 800. For generating empirical value estimates,
ˆV (d), we perform Monte Carlo Cross-Validation (repeated
random subsampling) with 1000 iterations at each n. The
corresponding binary treatment results are shown in Table 4.
In terms of empirical value, SD-Learning improves upon
the performance of D-Learning in most scenarios, especially
for comparisons involving treatment ZD. SD- and D-Learning
perform approximately equally well for ZZ vs. D, with empir-
ical values diﬀering by less than 0.10 in all cases. For pairwise
comparisons of Z vs. ZZ and Z vs. D, both methods eventually
converge upon recommending a single treatment to over 99%
of patients and therefore have very similar value estimates.
Overall, SD-Learning either outperforms D-Learning (ZD vs.
ZZ, ZD vs. D, and Z vs. ZD) or performs equally as well (ZZ
vs. D, Z vs. ZZ, Z vs. D).
5.2 Multi-Arm Treatment Scenario
We now compare the performance of AD- and SAD-Learning
at varying sample sizes while considering all four treatments
simultaneously. We randomly split the data into training sets
of n = 100, 200, 400, 800, and 1200 observations, using the rest
of the observations as testing data. The procedure is repeated
1000 times for each value of n. All results are shown in Table
5.
We can see that SAD-Learning has a distinct advantage
over AD-Learning at all observed training data sample sizes.
The stabilization step weighs patients diﬀerentially based on
predicted squared residual from the initial AD-Learning step.
This results in more eﬃciently estimated treatment rules and
therefore higher values, even in scenarios with very low sample
sizes.
6. Discussion
In this article, we propose SD-Learning, which boosts the
eﬃciency of D-Learning in a wide range of scenarios with
more general error functions, thus enhancing the utility of D-
Learning on datasets which may be encountered in practice.
The performance of SD-Learning relies on suﬃciently mod-
eling residuals from an initial D-Learning ﬁt, which can be
achieved through a variety of parametric or nonparametric
methods.
From another perspective, SD-Learning may be considered
an extension of feasible weighted least squares (FWLS) (Olive

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
10
(2017)) to the precision medicine setting where optimal ITR
estimation with two or more treatments is of interest. Sim-
ilarly to FWLS, SD-Learning is motivated by eﬃcient esti-
mation and controls on variance (Miller and Startz (2018)).
Our results suggest that SD-Learning pays a minor eﬃciency
price under homogeneous error, but can oﬀer substantial eﬃ-
ciency gains in the case of heterogeneous error. Additionally,
SD-Learning parameter estimates are asymptotically normal
when OLS is used for the estimation steps, allowing post-
modeling inference even in the multi-arm treatment scenario.
The implementation beneﬁts of SD-, SRD-, and SAD-
Learning lie in the fact that they are straightforward to
use and can simply be stacked on top of D-, RD-, and
AD-Learning which have been shown to perform well in a
multitude of settings. Additionally, our methodology even
in the multi-arm treatment setting (SAD-Learning) remains
estimable with a least squares framework and closed-form
solution, not requiring the use of optimization algorithms.
For practical use, we suggest considering a variety of non-
parametric prediction algorithms for the residual modeling
step in order to gain an understanding of the heteroscedastic-
ity structure of the dataset at hand. Random forest appeared
to work well under a wide variety of scenarios, with the
number of trees as the most important tuning parameter.
Although RCT settings were considered in this article, for
observational data, we recommend using SRD-Learning, since
Meng and Qiao (2021) showed that incorporation of the
mean outcome model results in protection against incorrect
speciﬁcation of the propensity score model.
Several future extensions of this work are possible. Theo-
retical results in Section 3, including Lemma 1 for random
forests, can be extended to the case where covariate dimen-
sion, p, increases with n. A natural methodological extension
is to allow for SD-Learning to estimate nonlinear decision
rules using Reproducing Kernel Hilbert Space (RKHS) tech-
niques. Additionally, SD-Learning may be broadened to work
for binary and survival outcomes under heteroscedasticity. As
proposed in this paper, SD-Learning assumes independence
(but not identically distributed errors) between observations.
It would also be valuable to use SD-Learning in scenarios
with correlation between observations. This would be akin to
feasible generalized least squares (FGLS) (Olive (2017)) for
ITR estimation.
Acknowledgements
The authors thank Marissa Ashner and Kyle Grosser for
taking time to review the manuscript and providing very
helpful feedback.
References
Breiman, L. (2001). Random Forests. Machine Learning 45,
5–32.
Chen, G., Zeng, D., and Kosorok, M. R. (2016). Personalized
Dose Finding Using Outcome Weighted Learning. Jour-
nal of the American Statistical Association 111, 1509–
1521.
Chen, T. and Guestrin, C. (2016).
XGBoost: A Scalable
Tree Boosting System. In Proceedings of the 22nd ACM
SIGKDD International Conference on Knowledge Dis-
covery and Data Mining, KDD ’16, pages 785–794, New
York, NY, USA. Association for Computing Machinery.
Cui, Y., Zhu, R., and Kosorok, M. (2017).
Tree based
weighted learning for estimating individualized treat-
ment rules with censored data.
Electronic Journal of
Statistics 11, 3927–3953.
Fan, C., Lu, W., Song, R., and Zhou, Y. (2017). Concordance-
Assisted Learning for Estimating Optimal Individualized
Treatment Regimes.
Journal of the Royal Statistical
Society. Series B, Statistical methodology 79, 1565–1582.
Fauzan, M. A. and Murﬁ, H. (2018). The Accuracy of XG-
Boost for Insurance Claim Prediction. Int. J. Advance
Soft Compu 10, 13.
Hammer, S. M., Katzenstein, D. A., Hughes, M. D., Gun-
dacker, H., Schooley, R. T., Haubrich, R. H., Henry,
W. K., Lederman, M. M., Phair, J. P., Niu, M., Hirsch,
M. S., and Merigan, T. C. (1996). A Trial Comparing
Nucleoside Monotherapy with Combination Therapy in
HIV-Infected Adults with CD4 Cell Counts from 200
to 500 per Cubic Millimeter. New England Journal of
Medicine 335, 1081–1090.
Kallus, N. (2018). Balanced Policy Evaluation and Learning.
Advances in neural information processing systems 31,.
Kosorok, M. R. and Laber, E. B. (2019). Precision Medicine.
Annual review of statistics and its application 6, 263–
286.
Kosorok, M. R. and Moodie, E. E. M. (2016). Adaptive treat-
ment strategies in practice: planning trials and analyzing
data for personalized medicine. ASA-SIAM statistics and
applied probability. Society for Industrial and Applied
Mathematics, Philadelphia.
Liu, Y., Wang, Y., Kosorok, M. R., Zhao, Y., and Zeng, D.
(2018). Augmented outcome-weighted learning for esti-
mating optimal dynamic treatment regimens. Statistics
in Medicine 37, 3776–3788.
Meng, H. and Qiao, X. (2021).
Doubly Robust Direct
Learning for Estimating Conditional Average Treatment
Eﬀect. arXiv:2004.10108 [stat] .
Miller, S. and Startz, R. (2018). Feasible Generalized Least
Squares Using Machine Learning. SSRN Scholarly Paper
ID 2966194, Social Science Research Network, Rochester,
NY.
Mocroft, A., Furrer, H. J., Miro, J. M., Reiss, P., Mussini, C.,
Kirk, O., Abgrall, S., Ayayi, S., Bartmeyer, B., Braun,
D., Castagna, A., d’Arminio Monforte, A., Gazzard, B.,
Gutierrez, F., Hurtado, I., Jansen, K., Meyer, L., Mu˜noz,
P., Obel, N., Soler-Palacin, P., Papadopoulos, A., Raﬃ,
F., Ramos, J. T., Rockstroh, J. K., Salmon, D., Torti, C.,
Warszawski, J., de Wit, S., Zangerle, R., Fabre-Colin, C.,
Kjaer, J., Chene, G., Grarup, J., and Lundgren, J. D.
(2013). The Incidence of AIDS-Deﬁning Illnesses at a
Current CD4 Count greater than 200 Cells/microliter
in the Post-Combination Antiretroviral Therapy Era.
Clinical Infectious Diseases 57, 1038–1047.
Murphy, S. A. (2003). Optimal dynamic treatment regimes.
Journal of the Royal Statistical Society: Series B (Sta-
tistical Methodology) 65, 331–355.

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
SD-Learning for Eﬃcient Estimation of Individualized Treatment Rules
11
Olive, D. J. (2017). WLS and Generalized Least Squares. In
Linear Regression, pages 163–173. Springer International
Publishing, Cham.
Qi, Z., Liu, D., Fu, H., and Liu, Y. (2020).
Multi-Armed
Angle-Based Direct Learning for Estimating Optimal
Individualized Treatment Rules With Various Outcomes.
Journal of the American Statistical Association 115,
678–691.
Qi, Z. and Liu, Y. (2018). D-learning to estimate optimal in-
dividual treatment rules. Electronic Journal of Statistics
12, 3601–3638.
Qian, M. and Murphy, S. A. (2011). Performance Guarantees
For Individualized Treatment Rules. Annals of Statistics
39, 1180–1210.
Robins, J. M. (2004).
Optimal Structural Nested Models
for Optimal Sequential Decisions.
In Lin, D. Y. and
Heagerty, P. J., editors, Proceedings of the Second Seattle
Symposium in Biostatistics: Analysis of Correlated Data,
Lecture Notes in Statistics, pages 189–326. Springer,
New York, NY.
Rubin, D. B. (1974). Estimating causal eﬀects of treatments
in randomized and nonrandomized studies. Journal of
Educational Psychology 66, 688–701.
Schulte, P. J., Tsiatis, A. A., Laber, E. B., and Davidian, M.
(2014). Q- and A-learning Methods for Estimating Op-
timal Dynamic Treatment Regimes. Statistical Science
29, 640–661.
Tian, L., Alizadeh, A. A., Gentles, A. J., and Tibshirani, R.
(2014).
A Simple Method for Estimating Interactions
Between a Treatment and a Large Number of Covariates.
Journal of the American Statistical Association 109,
1517–1532.
van der Laan, M. J., Polley, E. C., and Hubbard, A. E. (2007).
Super Learner. Statistical Applications in Genetics and
Molecular Biology 6,.
Xiao, W., Zhang, H. H., and Lu, W. (2019).
Robust Re-
gression for Optimal Individualized Treatment Rules.
Statistics in Medicine 38, 2059–2073.
Zhang, B. and Zhang, M. (2018). C-learning: A new classiﬁca-
tion framework to estimate optimal dynamic treatment
regimes. Biometrics 74, 891–899.
Zhang, C., Chen, J., Fu, H., He, X., Zhao, Y.-Q., and Liu, Y.
(2020). Multicategory Outcome Weighted Margin-based
Learning for Estimating Individualized Treatment Rules.
Statistica Sinica 30, 1857–1879.
Zhang, C. and Liu, Y. (2014).
Multicategory angle-based
large-margin classiﬁcation. Biometrika 101, 625–640.
Zhang, C.-H. and Huang, J. (2008). The sparsity and bias of
the Lasso selection in high-dimensional linear regression.
The Annals of Statistics 36, 1567–1594.
Zhang, J., Troxel, A. B., and Petkova, E. (2021).
Robust
index of conﬁdence weighted learning for optimal indi-
vidualized treatment rule estimation. Stat 10, e374.
Zhao, Y., Laber, E. B., Ning, Y., Saha, S., and Sands, B. E.
(2019). Eﬃcient augmentation and relaxation learning
for individualized treatment rules using observational
data. Journal of Machine Learning Research 20, 48.
Zhao, Y., Zeng, D., Rush, A. J., and Kosorok, M. R. (2012).
Estimating Individualized Treatment Rules Using Out-
come Weighted Learning.
Journal of the American
Statistical Association 107, 1106–1118.
Zhou, X., Mayer-Hamblett, N., Khan, U., and Kosorok, M. R.
(2017). Residual Weighted Learning for Estimating In-
dividualized Treatment Rules. Journal of the American
Statistical Association 112, 169–187.
Zhu, R., Zhao, Y.-Q., Chen, G., Ma, S., and Zhao, H. (2017).
Greedy outcome weighted tree learning of optimal per-
sonalized treatment rules. Biometrics 73, 391–400.

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
Supporting Information for “Stabilized Direct Learning for Efficient Estimation
of Individualized Treatment Rules”
Kushal S. Shah1,∗, Haoda Fu2,∗∗, and Michael R. Kosorok1,∗∗∗
1Department of Biostatistics, University of North Carolina at Chapel Hill, NC 27599, USA
2Eli Lilly and Company, Lilly Corporate Center, Indianapolis, IN 46285, USA
*email: kushshah@live.unc.edu
**email: fu haoda@lilly.com
***email: kosorok@unc.edu

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
Supporting Information for “SD-Learning for Efficient Estimation of Individualized Treatment Rules”
1
Web Appendix A
This section includes proofs of Propositions 1 and 2.
[Proof of Proposition 1] Let ln(β) = Pn
 (2RA −X⊤β)2
w(A, X)π(A, X)

, and define the first and
second derivatives of ln:
∂ln(β)
∂β
= −2Pn
(2RA −X⊤β)X
w(A, X)π(A, X)

(1)
∂2ln(β)
∂β2
= 2Pn

XX⊤
w(A, X)π(A, X)

(2)
Assume that ˆβ
P→β. Using Taylor Series approximations:
0 = ∂ln(ˆβ)
∂β
= ∂ln(β)
∂β
+
∂2ln(β)
∂β2
+ op(1)
 
ˆβ −β

.
(3)
From this, we have:
√n

ˆβ −β

= −√n
∂2ln(β)
∂β2
−1 ∂ln(β)
∂β
+ op(1)
= √n

Pn
XX⊤
w(A, X)π(A, X)
−1 
Pn
(2AR −X⊤β)X
w(A, X)π(A, X)

+ op(1)
= E

XX⊤
w(A, X)π(A, X)
−1 √nPn
ϵX
w(A, X)π(A, X)

+ op(1), and
(4)
var
n√n

ˆβ −β
o
= E

XX⊤
w(A, X)π(A, X)
−1
var

ϵX
w(A, X)π(A, X)

E

XX⊤
w(A, X)π(A, X)
−1
+ o(1)
= E

XX⊤
w(A, X)π(A, X)
−1
E
XX⊤E (ϵ2 | A, X)
w(A, X)2π(A, X)2

E

XX⊤
w(A, X)π(A, X)
−1
+ o(1)
= E

XX⊤
w(A, X)π(A, X)
−1
E

XX⊤σ2
0(A, X)
w(A, X)2π(A, X)2

E

XX⊤
w(A, X)π(A, X)
−1
+ o(1)
= A−1BA−1 + o(1),
(5)
since σ2
0(A, X) = var (ϵ | A, X) = E (ϵ2 | A, X). For ease of notation, let A = E

XX⊤
w(A, X)π(A, X)

and B = E

XX⊤σ2
0(A, X)
w(A, X)2π(A, X)2

. Letting wt(A, X) = w(A, X) + ts(A, X) be a perturbation
of the weights, we take a functional derivative and show that no matter the choice of s(A, X),
the first derivative of the variance expression is zero when w(A, X) = σ2
0(A, X)
π(A, X) (e.g. the

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
2
variance is minimized). The variance term can be written as:
var
√n(ˆβ −β)
	
= E

XX⊤
wt(A, X)π(A, X)
−1
E

XX⊤σ2
0(A, X)
wt(A, X)2π(A, X)2

E

XX⊤
wt(A, X)π(A, X)
−1
+ o(1)
= A−1
t BtA−1
t
+ o(1).
(6)
The derivatives of A−1
t
and Bt are:
∂A−1
t
∂t
= −A−1
t
∂At
∂t A−1
t
= −A−1
t E
 −XX⊤s(A, X)
wt(A, X)2π(A, X)

A−1
t
= A−1
t CtA−1
t ,
(7)
∂Bt
∂t = E
−2XX⊤σ2
0(A, X)s(A, X)
wt(A, X)3π(A, X)2

,
(8)
where Ct = E
 XX⊤s(A, X)
wt(X)2π(A, X)

. Having noted this, we can take the first derivative of the
variance expression:
∂
∂t
h
var
n√n

ˆβ −β
oi
= ∂A−1
t
∂t BtA−1
t
+ A−1
t
∂Bt
∂t A−1
t
+ A−1
t Bt
∂A−1
t
∂t
= A−1
t CtA−1
t BtA−1
t
+ A−1
t E
−2XX⊤σ2
0(A, X)s(A, X)
wt(A, X)3π(A, X)2

A−1
t
+ A−1
t BtA−1
t CtA−1
t .
(9)
Therefore:
∂
∂t
h
var
n√n

ˆβ −β
oi 
t=0
= A−1CA−1BA−1 + A−1E
−2XX⊤σ2
0(A, X)s(A, X)
w(A, X)3π(A, X)2

A−1 + A−1BA−1CA−1.
(10)
Now, letting w(A, X) = σ2
0(A,X)
π(A,X) :
E
−2XX⊤σ2
0(A, X)s(A, X)
w(A, X)3π(A, X)2

= −2C,
(11)
A−1B = E

XX⊤
σ2
0(A, X)
−1
E

XX⊤
σ2
0(A, X)

= 1.
(12)
Therefore:
∂var
n√n(ˆβ −β)
o
∂t

t=0
= A−1CA−1 −2A−1CA−1 + A−1CA−1
= 0.
(13)

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
Supporting Information for “SD-Learning for Efficient Estimation of Individualized Treatment Rules”
3
We have shown that the sandwich variance is minimized at w(A, X) = σ2
0(A, X)
π(A, X) . Thus,
the proof is complete.
[Proof of Proposition 2] Let ln(B∗) = Pn
(
1
w(A, X)π(A, X)

K
K −1R −X⊤
∗B∗
2)
,
and define the first and second derivatives of ln:
∂ln(B∗)
∂B∗
= −2Pn

1
w(A, X)π(A, X)

K
K −1R −X⊤
∗B∗

X∗

,
(14)
∂2ln(B∗)
∂B2
∗
= 2Pn

1
w(A, X)π(A, X)X∗X⊤
∗

.
(15)
Assuming that ˆ
B∗
P→B∗and using Taylor Series approximations similar to Proposition 1,
√n

ˆ
B∗−B∗

= √nE

X∗X⊤
∗
w(A, X)π(A, X)
−1 
Pn
X∗
w(A, X)π(A, X)

K
K −1R −X⊤
∗B∗

+ op(1)
= E

X∗X⊤
∗
w(A, X)π(A, X)
−1 √nPn
ϵX∗
w(A, X)π(A, X)

+ op(1), and
(16)
var
n√n

ˆ
B∗−B∗
o
= E

X∗X⊤
∗
w(A, X)π(A, X)
−1
E
 X∗X⊤
∗σ2
0(A, X)
w(A, X)2π(A, X)2

E

X∗X⊤
∗
w(A, X)π(A, X)
−1
+ o(1).
(17)
The format of (17) is now very similar to that of Proposition 1. Taking a functional
derivative, as in the proof for Proposition 1, shows that the sandwich variance is minimized
at w(A, X) = σ2
0(A, X)
π(A, X) . Thus, the proof is complete.
Web Appendix B
This section includes proofs of Lemma 1, Theorem 1, Theorem 2, and Theorem 3.
[Proof of Lemma 1] For the first case, linear regression, assume that Φ(A, X) is a finite-
dimensional collection of features in (A, X) and functions of the features. Φ(A, X) includes

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
4
main effects, and can additionally include squared and intercept terms, cubic terms, etc.
Assume that E

Φ(A, X)Φ(A, X)⊤	
is bounded and positive definite and let ˆσ2
n(A, X) be a
linear function predicting the squared residuals from the features in the set Φ(A, X). Then,
the prediction function, ˆσ2
n(A, X), is uniformly consistent for σ2
0(A, X), and moreover is a
vector process which belongs to a VC-class via Lemma 9.6 of Kosorok (2008). This implies
that it is bounded uniform integrable (belongs to a BUEI class) and therefore in a Donsker
class because of the measurability conferred by Lemma 8.12 of Kosorok (2008).
For the second case, it is known that random forest predictions can be characterized by
ˆσ2
n(A, X) = P∞
j=1 αjcjI {(a, x) ∈Rj}, where each Rj is a hyperrectangle, cj is the expected
value of Y over the region Rj, and P∞
j=1 αj = 1. The random forest prediction function,
ˆσ2
n(A, X), is therefore a convex combination of expected values over hyperrectangular regions.
Since the class of hyperrectangles of fixed dimensions is a VC-class and ˆσ2
n(A, X) is a convex
combination of them, ˆσ2
n(A, X) belongs to a convex hull class, C.
For a convex hull class, Corollary 9.5 of Kosorok (2008) applies and indicates that the
covering number of C is bounded above by K
1
ϵ
2−2/V
, where V is the VC-index of
C. Taking the square root results in ϵ−α where α ⩽1, resulting in a bounded integral
when integrated. Therefore, ˆσ2
n(A, X) belongs to a BUEI class and can also be shown to be
Pointwise Measurable (PM) (see, e.g., Section 8.2 of Kosorok (2008)).
We wish first to show that
1
ˆσ2
n(A, X) also belongs to a class that is BUEI and PM. For
g(x) = 1
x, ∂
∂xg(x) = −1
x2 ⩽−1
c2
1
since x represents the quantity ˆσ2
n(A, X). Therefore, g(x) is a
Lipschitz continuous function, and Lemma 9.17 (vi) of Kosorok (2008) shows that
1
ˆσ2
n(A, X)
is BUEI and PM using c1 ⩽∞as an envelope. Finally, using Lemma 9.17 (v),
Xϵ
ˆσ2
n(A, X)
also belongs to a class which is BUEI and PM, using E (|Xϵ|) ⩽∥X∥σ0 as an envelope.
Since
Xϵ
ˆσ2
n(A, X) belongs to a class which is BUEI and PM, by Theorem 8.19, the class is also
P-Donsker.

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
Supporting Information for “SD-Learning for Efficient Estimation of Individualized Treatment Rules”
5
[Proof of Theorem 1] Considering f opt(X) ∈F, where f opt(X) = E

RA
π(A, X)
X

=
2δ(X), let Y ∗= 2RA, and characterize the estimated variance function, ˆσ2
n(A, X), as the
matrix ˆΣn ∈Rn×n where ˆΣn = diag (ˆσ2
n (a1, x1) , ..., ˆσ2
n (an, xn)). The least squares SD-
Learning estimate for β0 can be written as:
ˆβS
n = (X⊤ˆΣ−1
n X)−1(X⊤ˆΣ−1
n Y ∗)
= β0 +
1
nX⊤ˆΣ−1
n X
−1 1
nX⊤ˆΣ−1
n ϵ

(18)
We show that the second term in this equation converges to zero. Note that since σ2
0(A, X) ⩾
c1 by Assumption 1, and ˆσ2
n(A, X) is uniformly consistent for σ2
0(A, X) by Assumption 3,
there exists N for which ˆσ2
n(A, X) ⩾c1
2 for all n ⩾N. Letting t ∈Rp be an arbitrary vector
on the unit sphere,

1
n
n
X
i=1
t⊤xix⊤
i t
ˆσ2
n(ai, xi) −1
n
n
X
i=1
t⊤xix⊤
i t
σ2
0(ai, xi)

⩽1
n
n
X
i=1
 t⊤xi
2

1
ˆσ2
n(ai, xi) −
1
σ2
0(ai, xi)

⩽1
n
n
X
i=1
∥xi∥2 · 2
c2
1
ˆσ2
n(A, X) −σ2
0(A, X)

A,X + op(1)
=
 2
c2
1
ˆσ2
n(A, X) −σ2
0(A, X)

A,X

· 1
n
n
X
i=1
∥xi∥2 + op(1)
= op(1) · Op(1) + op(1), and
(19)

1
n
n
X
i=1
Xiϵi
ˆσ2
n(ai, xi) −1
n
n
X
i=1
Xiϵi
σ2
0(ai, xi)

=

1
n
n
X
i=1
Xiϵi

1
ˆσ2
n(ai, xi) −
1
σ2
0(ai, xi)

⩽

1
n
n
X
i=1
Xiϵi
(
2 ∥ˆσ2
n(A, X) −σ2
0(X)∥A,X
c2
1
) + op(1)
=
2 ∥ˆσ2
n(A, X) −σ2
0(X)∥A,X
c2
1
·

1
n
n
X
i=1
Xiϵi
 + op(1),
(20)
where n−1 Pn
i=1 ∥xi∥2 is Op(1) because it converges to E
 XX⊤
and

1
n
Pn
i=1 Xiϵi
 converges
to |E(Xiϵi)| = 0. (19) shows that n−1X⊤ˆΣ−1
n X
P
−→n−1X⊤Σ−1
0 X, since it is true for arbitrary

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
6
t on the unit sphere, and (20) shows that n−1X⊤ˆΣ−1
n ϵ
P
−→n−1X⊤Σ−1
0 ϵ. Since inversion is
a continuous operation when the limit is a positive definite matrix,

n−1X⊤ˆΣ−1
n X
−1
P
−→
 n−1X⊤Σ−1
0 X
−1 by the Continuous Mapping Theorem. Since
 n−1X⊤Σ−1
0 X
−1 is finite and
positive definite while n−1X⊤Σ−1
0 ϵ converges to zero using the Kolmogorov Law of Large
Numbers,

n−1X⊤ˆΣ−1
n X
−1 
n−1X⊤ˆΣ−1
n ϵ

converges to zero, and ˆβS
n
P→β0.
[Proof of Theorem 2] We show that the preconditions are met for Lemma 4.4 of
Kosorok (2008). Assumptions 1 and 2 guarantee that U0 is positive definite. Additionally,
ˆβS
n
P→β0 based on Theorem 1. Pn

XX′
ˆσ2
n(A, X) −
XX′
σ2
0(A, X)

→0 was shown by (19). Now,
consider the following:

1
n
n
X
i=1

t⊤xiϵi

1
ˆσ2
n(ai, xi) −
1
σ2
0(ai, xi)
2
= 1
n
n
X
i=1
(t⊤xi)2σ2
0(ai, xi)

1
ˆσ2
n(ai, xi) −
1
σ2
0(ai, xi)
2
+ op(1)
⩽c2
n
n
X
i=1
(t⊤xi)2

1
ˆσ2
n(ai, xi) −
1
σ2
0(ai, xi)
2
⩽4c2
c4
1
· 1
n
n
X
i=1
(t⊤xi)2 ˆσ2
n(ai, xi) −σ2
0(ai, xi)
2
A,X + op(1)
⩽4c2
c4
1
ˆσ2
n(A, X) −σ2
0(A, X)
2
A,X · 1
n
n
X
i=1
∥xi∥2 + op(1)
= op(1) · Op(1) + op(1).
(21)
Therefore, Pn

Xϵ
ˆσ2
n(A, X) −
Xϵ
σ2
0(A, X)
2
P→0, and the conditions for the Lemma 4.4 of
Kosorok (2008) are met. Note the following two facts:
ˆβS
n = Pn

XX′
ˆσ2
n(A, X)
−1
Pn

XY ∗
ˆσ2
n(A, X)

=⇒√n

ˆβS
n −β0

=
"
Pn

XX′
ˆσ2
n(A, X)
−1#
· √nPn

Xϵ
ˆσ2
n(A, X)

, and
(22)
√n

Pn

Xϵ
ˆσ2
n(A, X)

−E

Xϵ
σ2
0(A, X)

→N

0, E

XX′
σ2
0(A, X)

=⇒√nPn

Xϵ
ˆσ2
n(A, X)

→N

0, E

XX′
σ2
0(A, X)

,
(23)

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Supporting Information for “SD-Learning for Efficient Estimation of Individualized Treatment Rules”
7
where E

Xϵ
σ2
0(A, X)

= 0 in (23) stems from Assumption 4. With the combination of (22)
and (23), we can establish:
√n

ˆβS
n −β0

→E

XX′
σ2
0(A, X)
−1
· N

0, E

XX′
σ2
0(A, X)

→N
"
0, E

XX′
σ2
0(A, X)
−1#
.
(24)
[Proof of Theorem 3] Since the SD-Learning framework is unified between the binary
and multi-arm case, this proof is identical to the proofs of Theorems 1 and 2, with X∗∈
Rp(K−1) instead of X ∈Rp and B∗∈Rp(K−1) instead of β0 ∈Rp.
References
Kosorok, M. R. (2008). Introduction to Empirical Processes and Semiparametric Inference.
Springer Series in Statistics. Springer New York, New York, NY.

````

