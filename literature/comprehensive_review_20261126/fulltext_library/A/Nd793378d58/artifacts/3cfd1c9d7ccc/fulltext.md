# Accountable survival contrast-learning for optimal dynamic treatment regimes

Original PDF: [original.pdf](original.pdf). SHA256: `3cfd1c9d7ccc8d7eb7881c1b7bfcd30619952dd8fb5a046bc6f122049fc0db0e`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
Accountable Survival Contrast-learning for Optimal
Dynamic Treatment Regime
Taehwa Choi 
Korea University
Hyunjun Lee 
SK Inc. C&C
Sangbum Choi  (  choisang@korea.ac.kr )
Korea University
Article
Keywords:
Posted Date: March 21st, 2022
DOI: https://doi.org/10.21203/rs.3.rs-1444648/v1
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License

````

## PDF page 2

Technical extraction; compare with original PDF page 2.

````text
Accountable survival contrast-learning for optimal
dynamic treatment regime
Taehwa Choi1, Hyunjun Lee2, and Sangbum Choi1,*
1Department of Statistics, Korea University, Seoul, South Korea
2SK Inc. C&C, Seoul, South Korea
*choisang@korea.ac.kr
ABSTRACT
Dynamic treatment regime (DTR) is an emerging paradigm in recent medical studies that establishes data-driven treatment
rules for future patients, based on clinical histories of individuals. Because each patient may have different genetic and clinical
characteristics, this approach is more attractive than the standard method of allocating the same treatment to patients without
taking into account individual status. There have been many methodologies on this subject, but most focus on complete data
without censoring. However, when censorship is present, as in many longitudinal studies, standard methods are not directly
applicable with censored responses. In this paper, we propose accountable survival contrast-learning algorithms for optimal
dynamic treatment regime. To reﬂect the censorship, we adopt the pseudo-value approach that replaces survival quantities
with pseudo-observations for time-to-event outcomes. Our estimating procedure is originated from weighted classiﬁcation
scheme, which is double-robust to model misspeciﬁcation by taking more ﬂexible contrast weight function. We further use
SCAD-penalization to ﬁnd informative clinical information in a sparse model setting and present potential possibilities for
multiple treatment allocation by searching upper and lower bounds of the objective function. We demonstrate the utility of our
proposal via extensive simulations and an application to AIDS data.
Dynamic treatment regime (DTR) is an emerging paradigm for maximizing treatment efﬁcacy by providing tailored
medicine to each patient1. Many chronic diseases, such as cancer, human immunodeﬁciency virus (HIV), and depression, are
hard to be cured by a single treatment, requiring continuous disease management. Because human’s clinical information can
change over time, sequentially adjusted treatments should be provided, not only based on patients’ clinical history, but also their
prior treatment information and intermediate responses. We would like to present treatment decision rules for survival outcomes
and predict their probability distributions, even in the presence of competing risks events, as they will help in treatment planning.
In this study, we propose accountable survival contrast-learning methods to establish optimal dynamic treatment regimes. To
reﬂect the censorship or multiple competing events, we adopt the pseudo-value approach to produce pseudo survival responses
and apply a novel regularized double-robust procedure to minimize risk from model misspeciﬁcation. This approach not
only imputes the distribution of censored samples with the nonparametric Kaplan-Meier estimate but also allows us to ﬁnd
interpretable treatment allocation rules given a large volume of patients’ information. We compare our proposed method with
existing DTR-learning algorithms via simulation studies and apply to a reference survival dataset.
Since seminal work by Murphy1, extensive studies have been done to ﬁnd effective data-driven treatment rules by exploring
personal characteristics such as genetic or clinical information. Many earlier works use Q-learning and inverse probability
weighting (IPW) schemes in a single treatment setting2–5 and sequential treatment setting6–8. These approaches, however, show
some limitations, mainly due to unstable search and low accuracy from model misspeciﬁcation. To overcome forementioned
drawbacks, several double-robust (DR) estimators are studied to achieve more statistical efﬁciency and protection from model
misspeciﬁcation9–13. Zhang and Zhang12 adopted a contrast weighted tree algorithm that shows noticeable improvement for
rule identiﬁcation. Tao and wang14 studied DTR problems with multiple treatment options. More recently, there have also
been many studies with modern methodologies, such as Markov decision process or graphical models15–17. In the presence
of censorship, many algorithms were based on a classiﬁcation approach by adjusting the censorship by inverse probability
of censoring weighting18,19 or directly optimized survival or cumulative incidence rates via adjustment with nonparametric
Kaplan-Meier estimator20,21.
In this study, we propose a penalized survival contrast-learning (PSCL) algorithm to estimate patient-level tailored treatment
rules for time-to-event outcomes. It should be noted that existing DTR methods for censored data were notoriously complicated
as they directly work on nonparametric survival quantities. Jiang et al.20 and Zhou et al.21 aimed to directly optimize IPW-
adjusted nonparametric t-year survival or competing risks curves under the counterfactual framework22. Their methods, however,
are computationally unstable, requiring extra smoothing procedures. Other works18,19 mostly used double-weighting schemes

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
to facilitate censoring and received treatment. Instead, we take a jackknife-based pseudo-value approach23 to approximate
survival outcomes and adopt a regularized DR contrast-learning method via penalized linear support vector machine (SVM).
The pseudo-value approach enables us to approximate various types of complex survival measures, even in the presence of
competing risks or interval-censoring, and then apply standard machine learning algorithms with minimal loss of statistical
efﬁciency. After formulating the DTR problem from a classiﬁcation perspective, our estimation proceeds backwardly from
the last stage, and identiﬁes the optimal treatment regime at each stage by minimizing a weighted classiﬁcation loss function.
With extensive simulations and data example, we have proven that our strategy is able to uncover sequential treatment rules
effectively and can be extended to DTR problems with survival and competing risks data, and multiple treatments.
Preliminaries
We begin by brieﬂy overviewing the pseudo-value approach23. Suppose there are n random samples. Let θ = E[f(T)] be
a parameter of interest, where f is a measurable function of survival time T. For example, one might consider I(T ≥t)
and min(T,τ) for f(T), corresponding to t-year survival and mean restricted lifetime at time τ > 0. Pseudo-observations
are basically jackknife substitutes for unknown quantities. To be speciﬁc, the pseudo-observation for the ith subject can
be deﬁned as ˆθi = n ˆθ −(n −1) ˆθ −i, where ˆθ is an unbiased estimator of θ and ˆθ −i is the leave-one-out (i.e., jackknife)
estimator, based on n−1 samples, excluding the ith object. Note that the pseudo-observation ˆθi is unbiased, since E( ˆθi) =
nE( ˆθ)−(n−1)E( ˆθ −i) = nθ −(n−1)θ = θ. This property can be equivalently applied to the survival quantities. For example,
t-year survival, S(t) = P(T ≥t), can be approximated by
ˆSi(t) = n ˆS(t)−(n−1) ˆS−i(t),
(1)
where ˆS(t) and ˆS−i(t) are nonparametric Kaplan-Meier estimators, based on all n samples and n −1 samples without the
ith observation. Similar techniques can be used to approximate restricted mean lifetime or cumulative incidence rate under
competing risks. In this article, we also focus on competing risks setting as it extends general survival problems. For the ith
subject, let Di ∈{1,...,M} denote the indicator for cause of failure, where M is a known number of causes, and Ti and Ci
failure and censoring times, respectively. In the presence of censoring, we can actually observe ( ˜Ti,∆i), where ˜Ti = min(Ti,Ci)
and ∆i = I(Ti ≤Ci)Di. When the event of interest is the ﬁrst cause of failure, the primary interest may lie on modeling
t-year cumulative incidence function (CIF), deﬁned as F1(t) = P(Ti ≤t,Di = 1), which can be also approximated by pseudo-
observations. Our objective is then to construct efﬁcient and interpretable DTR rules that will produce minimal t-year CIF on
average.
Methods
Notation and assumptions
Suppose that patients are treated with K-stage sequential treatments. At the kth stage (k = 1,...,K), a patient will receive a
treatment Ak = ak ∈A k = {0,1}, given his or her covariate history Hk, which may contain both baseline and time-varying
covariates and past treatment information. More precisely, Hk = {x1,A1,x2,A2,...,xk}, where xj denotes the new covariate
information added at the jth stage. Let Rk be a reward followed by treatment Ak, for which larger value is usually preferable,
whereas smaller value is preferred when CIF is the target measure. By gathering all set of rewards, we have overall outcome
of interest denoted by Y = f(R1,...,Rk), where f(·) is a prespeciﬁed function such as summation and Y is assumed to be
bounded. When the components in Y are censored, we use the pseudo-value approach to replace them. The optimal DTR
maximizes the expectation of overall clinical results once each patient is provided the tailored treatment across all stages. Let
gk ≡gk(Hk) (k = 1,...,K) be the treatment regime at the kth stage that is the deterministic function, mapping from available
covariate and treatment history Hk to the treatment variable Ak. The DTRs, observed at the end-of-stage, are deﬁned as
g = (g1,...,gK) ∈G , where G denotes all possible set of treatment regimes including optimal treatment regime gopt
k . In the
following, we impose common assumptions to use the potential outcome framework24,25. Let denote potential pseudo-survival
outcome by Y ∗(a) that corresponds to treatment A = a. To apply the potential outcome framework, we need (i) consistency, (ii)
no unmeasured confounder and (iii) positivity assumptions, meaning that (i) the potential outcome coincides with the observed
one when a subject is actually given the treatment; (ii) potential outcome and treatment variable are independent, given covariate
and treatment history; and (iii) the propensity score πa(H) = P(A = a|H) is bounded away from 0 with probability 1.
Individualized treatment regimes
To motivate our method, we ﬁrst consider the simplest single-stage problem (i.e., K = 1). By convention, it is assumed that
the optimal treatment regime gopt ∈G should satisfy E{Y ∗(gopt)} ≥E{Y ∗(g)}, for all g ∈G . Under the consistency, the
2/11

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
potential pseudo outcome of arbitrary regime g can be expressed as Y ∗(g) = Y ∗(1)I{g(H) = 1} +Y ∗(0)I{g(H) = 0}. By
writing µa(H) = E(Y|A = a,H),
E{Y ∗(g)} = EH[µ1(H)I{g(H) = 1}+ µ0(H)I{g(H) = 0}],
where EH is expectation with respect to H. Following the classiﬁcation perspective on decision-making problems9, the optimal
treatment regime gopt can be obtained by
gopt(H) = argmin
g∈G
EH [|C(H)|{I[C(H) > 0]̸ = g(H)}],
(2)
where C(H) = µ1(H)−µ0(H) is the treatment contrast. We may use the inverse probability weighting (IPW) estimator,
ˆCIPW(H) =

A
ˆπ1(H) −
1−A
1−ˆπ1(H)

Y,
(3)
where ˆπa(H), a ∈{0,1}, is the propensity score estimated by some parametric or nonparametric methods. The IPW contrast
estimator (3) is obviously an unbiased estimator of C(H), because E[I(A = a)/P(A = a|X = x)] = 1 and the unbiased property
of pseudo-observation. However, this approach is only valid when the propensity model π1(H) is correctly posited, which
often fails to hold26,27. Alternatively, we consider the augmented inverse probability weighting (AIPW) method by combining
outcome and propensity models. Speciﬁcally, the AIPW estimator for µa takes the form
ˆµDR
a (H) = I(A = a)
ˆπa(H) Y +

1−I(A = a)
ˆπa(H)

ˆµa(H),
(4)
which is a weighted average between the observation Y and its outcome substitute ˆµa. In statistical literature, (4) is also known
as a double-robust (DR) estimator, because it still produces consistent results, when either the outcome model µa(H) (Q-model)
or propensity score model πa(H) (A-model) is correctly estimated28.
In this work, we will use (4) to obtain the DR contrast estimator
ˆCDR(H) = ˆµDR
1 (H)−ˆµDR
0 (H).
(5)
Once this contrasting factor is computed, optimal treatment regime gopt can be obtained from (2). However, the weighted
classiﬁcation error (2) is difﬁcult to optimize, requiring complex and slow generic algorithms9,10,12. Instead, we propose
to solve the classiﬁcation problem (2) via weighted linear support vector machine (SVM)29. Motivated by Song et al.7, we
adopt a penalized SVM by incorporating the contrast function ˆCDR(H) as a weight to optimize (2). Deﬁne wi = | ˆCDR
i
(Hi)| and
Zi = sign{ ˆCDR
i
(Hi)}, the equation in (2) can be approximated with a penalized hinge loss function
n−1
n
∑
i=1
wi[1−Zi f(Hi)]+ +
p
∑
j=1
Pλ(|βj|),
(6)
where (u)+ = max(0,u). For interpretability, we assume f(Hi) = HT
i β, β ∈Rp is a linear decision function. We use the
SCAD penalty function
P′
λ(|βj|) = λ

I(|β j| ≤λ)+ (γλ −|βj|)+
λ(γ −1)
I(|βj| > λ)

,
where λ > 0 is a tuning parameter and γ = 3.7 as recommended by Fan and Li30. Following local linear approximation, we
linearize the SCAD penalty as
Pλ(|β|) ≈Pλ(|β0|)+P′
λ(|β|)(|β|−|β0|), β ≈β0,
and introduce a slack variable ξi = n−1[1−Zi f(Hi)]+. Then our classiﬁcation problem in (6) can be re-expressed as
min
ξi,β +
j ,β −
j ,β +
0 ,β −
0
n
∑
i=1
wiξi +
p
∑
j=1
P′
λ(|β (0)
j
|)(β +
j +β −
j )
subject to Zi
(
β +
0 −β −
0 +
p
∑
j=1
hi j(β +
j −β −
j )
)
≥1−ξi,
ξi,β +
0 ,β −
0 ,β +
j ,β −
j ≥0, for i, j = 1,..., p,
(7)
3/11

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
where u+ ≥0 and u−≥0 are positive and negative parts of u, respectively, such that u = u+ −u−and |u| = u+ + u−. We
obtain the initial coefﬁcients β (0)
j
from standard ℓ2-type SVM. There exist many optimization packages to solve (7), such as
lp() in the R:lpSolve package. After ˆβ is obtained, the estimated treatment rule is given by ˆgopt ≡ˆgopt(H) = I( ˆf(H) > 0).
It should be noted that the above method cannot be applied to competing risks settings, since the optimal treatment will reduce
the cumulative incidence rate. In this case, we replace ˆCDR(Hi) in (6) with −ˆCDR(Hi) to minimize E[ ˆF1(t)], which is justiﬁed
from the following result.
Proposition 1 The optimal treatment rule for competing risks outcome is the minimizer of the following weighted misclassiﬁ-
cation error
gopt(H) = argmin
g∈G
EH[|C(H)|{I[C(H) ≤0]̸ = g(H)}].
Dynamic treatment regimes with survival responses
We extend the previous idea to a multi-stage problem for DTRs, g = {g1,...,gK}, where gk ≡g(Hk) ∈G k is the decision rule
at the kth stage given the corresponding covariate history Hk. Without loss of generality, we assume K = 2 in the following. To
transfer the treatment effect between adjacent stages, we deﬁne the value function at the kth stage12 as
Vk(Hk) = EH[Vk+1(Hk+1)+{µk,1(Hk)−µk,0(Hk)}{gopt
k (Hk)−Ak}|Hk],
where gopt
k
is the kth optimal treatment rule and µk,ak(Hk) = EH[Vk+1(Hk+1)|A = ak,Hk] for ak ∈{0,1}. We set V(K+1) ≡Y,
since there are no further subsequent processes. Note that µk,ak(Hk) can be interpreted as Q-function in reinforcement learning
because it represent the “quality” of action ak.
Except for the last stage, Vk(Hk) should be estimated backwardly and let denote the estimated value function by ˜Vk ≡˜Vk(Hk).
Then, the value function of the ith subject at the kth stage can be recursively estimated from
˜Vk,i = ˜V(k+1),i +{ ˆµk,1(Hk,i)−ˆµk,0(Hk,i)}{ ˆgopt(Hk,i)−Ak,i},
where we use the pseudo-observation Yi for ˜V(K+1),i. Note that ˜Vk,i is equal to ˜V(k+1),i if ˆgopt(Hki) = Ak,i, otherwise | ˆµk,1(Hk,i)−
ˆµk,0(Hk,i)| is added to ˜V(k+1),i. The second term in the above display, i.e., | ˆµk,1(Hk,i) −ˆµk,0(Hk,i)|I{ ˆgopt(Hki)̸ = Ak,i}, is
tantamount to “regret” score that we wish to remove by making optimal treatment decision. For the competing risks problem,
we shall replace µk,ak(Hk) by −µk,ak(Hk), so as to minimize cumulative incidence rates eventually, which leads to the regret
function of the kth stage is deﬁned by
EH[{µk,0(Hk)−µk,1(Hk)}{gopt
k (Hk)−Ak}|Hk].
We can use parametric or nonparametric methods, such as least squares or random forests, to estimate µk,ak(Hk,i), ak ∈{0,1}.
The optimal treatment rule at the kth stage (i.e., gopt
k ) can be determined by minimizing the expected value of weighed
misclassiﬁcation error
EH[|Ck(Hk)|{I[Ck(Hk) > 0]̸ = g(Hk)}],
(8)
and deﬁne ˆgopt
k
≡ˆgopt(Hk) = I( ˆf(Hk) > 0). This can be done by solving a similar linear programing problem as in (7). Again,
we use a DR estimator to approximate the contrast function Ck(Hk),
ˆCDR
k (Hk) =
Ak
ˆπ1(Hk)
˜V(k+1) −
Ak −ˆπ1(Hk)
ˆπ1(Hk)

ˆµk,1(Hk)−
 1−Ak
ˆπ0(Hk)
˜V(k+1) +
Ak −ˆπ1(Hk)
ˆπ0(Hk)

ˆµk,0(Hk)

,
where ˆπak(Hk) is the estimated propensity score of πak(Hk) = P(Ak = ak|Hk). This computation proceeds backwardly from
the last stage to the ﬁrst one, which will produce the desired optimal DTR, gopt = {gopt
1 ,...,gopt
K }.
Extension to DTR with multiple treatments
The forementioned approach assumes binary treatment for Ak. When there are more than two treatment options, we will
use a mixed approach of Huang et al.8 and Tao and Wang14. Deﬁne the order statistics of µak(Hk), ak = 1,...,Lk, as
µ(1)(Hk) ≤··· ≤µ(Lk)(Hk), and let νak be the order of treatment effect, so that µ(ak)(Hk) = µνak (Hk). Then the optimal
treatment regime gopt
k
among Lk treatments can be estimated by maximizing
EH
" Lk
∑
ak=1
µ(ak)(Hk)I{νak(Hk) = gk(Hk)}
#
.
(9)
4/11

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
This optimization is plausible when Lk is small or at least ﬁxed, otherwise, becomes very difﬁcult8. Instead, Tao and Wang14
focuses on the following inequalities of contrast functions for ak = 1,...,Lk −1,
0 ≤µ(Lk)(Hk)−µ(Lk−1)(Hk) ≤µ(Lk)(Hk)−µ(ak)(Hk) ≤µ(Lk)(Hk)−µ(1)(Hk).
Then, we may try to ﬁnd sub-optimal but plausible solution paths from
ˆgopt
k
= argmin
gk∈G
EH[| ˆµ(Lk)(Hk)−ˆµ(Lk−1)(Hk)|×I{νLk(Hk)̸ = gk(Hk)}],
or
ˆgopt
k
= argmin
gk∈G
EH[| ˆµ(Lk)(Hk)−ˆµ(1)(Hk)|×I{νLk(Hk)̸ = gk(Hk)}].
These equations imply that if misclassiﬁcation is inevitable, sub-optimal treatment rules may be obtained by controlling large
values of µ(Lk)(Hk)−µ(ak)(Hk). We explore both treatment selection methods in our numerical experiments with censored
observations, which reveal that they show similar performance. This is because the minimum and maximum bounds of the
objective function may converge to the same value unless the imposed models are severely misspeciﬁed.
Numerical experiments
Survival events
Cause-1 speciﬁc events
n
Censor
Method
S(3, ˆgopt)
ˆS(3, ˆgopt)
CDR1
ACDR
F1(3, ˆgopt)
ˆF1(3, ˆgopt)
CDR1
ACDR
500
15%
g = 0
0.50 (0.00)
0.39 (0.02)
0.62 (0.00)
0.62 (0.00)
0.39 (0.01)
0.43 (0.02)
0.44 (0.00)
0.50 (0.00)
g = 1
0.30 (0.00)
0.39 (0.03)
0.38 (0.00)
0.38 (0.00)
0.42 (0.01)
0.43 (0.02)
0.56 (0.00)
0.50 (0.00)
OWL
0.46 (0.05)
0.43 (0.05)
0.51 (0.09)
0.61 (0.08)
0.38 (0.04)
0.39 (0.04)
0.50 (0.09)
0.62 (0.08)
DWL
0.49 (0.05)
0.49 (0.05)
0.82 (0.08)
0.69 (0.08)
0.26 (0.02)
0.30 (0.03)
0.88 (0.05)
0.76 (0.06)
POWL
0.56 (0.02)
0.52 (0.04)
0.75 (0.07)
0.78 (0.04)
0.26 (0.01)
0.28 (0.03)
0.85 (0.05)
0.80 (0.05)
PDWL
0.59 (0.02)
0.55 (0.03)
0.88 (0.04)
0.84 (0.03)
0.25 (0.01)
0.27 (0.02)
0.90 (0.02)
0.82 (0.04)
30%
g = 0
0.50 (0.00)
0.39 (0.02)
0.62 (0.00)
0.62 (0.00)
0.41 (0.01)
0.43 (0.02)
0.44 (0.00)
0.50 (0.00)
g = 1
0.30 (0.00)
0.39 (0.03)
0.38 (0.00)
0.38 (0.00)
0.42 (0.01)
0.43 (0.02)
0.56 (0.00)
0.50 (0.00)
OWL
0.47 (0.04)
0.44 (0.05)
0.50 (0.09)
0.64 (0.07)
0.38 (0.04)
0.39 (0.04)
0.50 (0.09)
0.61 (0.07)
DWL
0.48 (0.06)
0.48 (0.05)
0.81 (0.08)
0.67 (0.08)
0.26 (0.02)
0.29 (0.03)
0.87 (0.06)
0.77 (0.06)
POWL
0.55 (0.03)
0.51 (0.04)
0.72 (0.08)
0.77 (0.05)
0.26 (0.02)
0.29 (0.03)
0.83 (0.06)
0.79 (0.05)
PDWL
0.59 (0.02)
0.54 (0.04)
0.86 (0.04)
0.83 (0.03)
0.25 (0.01)
0.27 (0.02)
0.89 (0.03)
0.82 (0.04)
1000
15%
g = 0
0.41 (0.01)
0.43 (0.01)
0.44 (0.00)
0.51 (0.00)
0.50 (0.00)
0.39 (0.01)
0.62 (0.00)
0.62 (0.00)
g = 1
0.30 (0.00)
0.39 (0.02)
0.38 (0.00)
0.38 (0.00)
0.42 (0.01)
0.43 (0.03)
0.56 (0.00)
0.50 (0.00)
OWL
0.47 (0.05)
0.45 (0.05)
0.51 (0.09)
0.65 (0.08)
0.38 (0.04)
0.40 (0.04)
0.50 (0.09)
0.58 (0.07)
DWL
0.50 (0.07)
0.51 (0.05)
0.88 (0.07)
0.73 (0.09)
0.28 (0.03)
0.31 (0.04)
0.84 (0.07)
0.73 (0.06)
POWL
0.60 (0.02)
0.55 (0.03)
0.83 (0.06)
0.85 (0.04)
0.28 (0.02)
0.31 (0.03)
0.79 (0.07)
0.73 (0.05)
PDWL
0.61 (0.01)
0.57 (0.02)
0.91 (0.02)
0.89 (0.02)
0.26 (0.01)
0.29 (0.03)
0.87 (0.03)
0.77 (0.04)
30%
g = 0
0.50 (0.00)
0.39 (0.01)
0.62 (0.00)
0.62 (0.00)
0.39 (0.01)
0.43 (0.02)
0.44 (0.00)
0.50 (0.00)
g = 1
0.30 (0.00)
0.39 (0.02)
0.38 (0.00)
0.38 (0.00)
0.42 (0.01)
0.43 (0.03)
0.56 (0.00)
0.50 (0.00)
OWL
0.48 (0.04)
0.46 (0.05)
0.50 (0.09)
0.67 (0.07)
0.39 (0.04)
0.40 (0.04)
0.50 (0.09)
0.58 (0.07)
DWL
0.49 (0.06)
0.50 (0.04)
0.87 (0.07)
0.70 (0.08)
0.28 (0.03)
0.31 (0.04)
0.83 (0.08)
0.73 (0.06)
POWL
0.59 (0.02)
0.55 (0.03)
0.80 (0.07)
0.83 (0.04)
0.29 (0.02)
0.32 (0.04)
0.76 (0.08)
0.71 (0.06)
PDWL
0.61 (0.01)
0.57 (0.03)
0.91 (0.03)
0.89 (0.02)
0.27 (0.02)
0.29 (0.03)
0.86 (0.04)
0.76 (0.04)
Table 1. Performance of several DTR algorithms. The table reports optimized t-year survival and t-year cumulative incidence
rates, correct decision rate at ﬁrst stage (CDR1), and average correct decision rate of two stages (ACDR). For each scenario, the
best model is highlighted in bold.
Scenario 1: Randomized experiment
We evaluate the performance of the proposed method for the two-stage DTR problem when responses are subject to censoring
or competing risks. Simulation results under single stage are postponed to the Table S1 and S2 in Web-appendix. We
let n = 500 or 1000 in all studies. Let xk,ji be the jth covariate value of the ith subject at the kth stage (i = 1,...,n;k =
1,2; j = 1,..., pk). At the ﬁrst stage, we generate 15 covariates x(1)
i
= (x1,1i,...,x1,15i)T, where each covariate independently
follows an Uniform[−2,2] distribution. The second stage involves a single variable x(2)
i
= (x2,i) that is generated from
Uniform[min(x1,1i),max(x1,1i)], The treatment indicator Ak,i, k = {1,2} is generated from Bernoulli(0.5). For survival outcome,
5/11

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
0.3
0.4
0.5
0.6
100
300
500
700
Sample size
S(3, g^
opt)
0.3
0.4
0.5
0.6
0.7
100
300
500
700
Sample size
S^(3, g^
opt)
0.4
0.6
0.8
1.0
100
300
500
700
Sample size
Correct decision rate
TRUE logistic
0.3
0.4
0.5
0.6
100
300
500
700
Sample size
S(3, g^
opt)
0.2
0.4
0.6
0.8
100
300
500
700
Sample size
S^(3, g^
opt)
0.4
0.6
0.8
1.0
100
300
500
700
Sample size
Correct decision rate
FALSE logistic
Method
OWL
DWL
POWL
PDWL
Figure 1. Survival probabilities and average correct decision rate of two stages under optimal dynamic treatment regimes with
OWL, DWL, POWL and PDWL for different sample sizes.
we let Ti = exp{1.5+0.5x1,1i +A1,i(x1,2i −0.5)+A2,i(x2,i −0.5)+εi}, where exp(εi) ∼Exp(1). Censoring time is generated
from Ci ∼Exp(c0), where c0 is a ﬁxed constant yielding 15% or 30% censoring rates. Propensity score for each case is estimated
by the sample proportion of the treatment, i.e., #(Ak = 1)/n. In this setting, the optimal rules are gopt
1
= I(0.9x1,2i ≥0.436) and
gopt
2
= I(x2,i ≥0.5) for the ﬁrst and second stage, respectively. Our objective is to ﬁnd DTRs that maximize the 3-year survival
rate, under which the maximal survival is known to be S(3,gopt
0 ) = 0.63.
We also consider competing risks data, for which we deﬁne Q-functions of cause-1 and 2 events as ψ1i(H2) = exp{1−
3x1,1i −A1(3.6x1,2i −0.8)−A2,i(0.5−1.7x2,i)} and ψ2i(H2) = exp{1+3x1,1i +A1(x1,2i +0.8)−A2,i(x2,i −0.5)}, respectively.
Following31, let P(Di = 1) = 1 −(1 −q)1/ψ1i(H2) and specify cumulative incidence rates as F1(t|Xi,Ai) = 1 −{1 −q(1 −
e−t)}ψ1i(H2), and F2(t|Xi,Ai) = 1 −exp{−tψ2i(H2)}. With the choice of q = 0.5, about 43% and 38% are cause-1 failures,
respectively, under 15% and 30% censoring rates. The optimal treatment rules are gopt
1
= I(0.97x1,2i ≤0.243) and gopt
2
=
I(1.7x2,i ≥0.5), for which the minimal 3-year cause-1 CIF is F1(3,gopt
0 ) = 0.23.
Table 1 summarizes the performance of several DTR methods, including outcome weighted learning (OWL) of4 and its
DR version (DWL), penalized OWL (POWL) and the proposed penalized DR weighted learning (PDWL), to optimize true
curves, {S(3, ˆgopt),F1(3, ˆgopt)}, and their empirical counterparts, { ˆS(3, ˆgopt), ˆF1(3, ˆgopt)}. Clearly, PDWL outperforms other
algorithms, nearly achieving the maximal survival and minimal cumulative incidence rates in all cases. Our method also best
performs in terms of correct decision rate at ﬁrst stage (CDR1) and average correct decision rate of two stage (ACDR). Note
that naive treatment with g = 0 even produces better outputs than OWL or DWL, implying that unpenalized learnings are
vulnerable to model misspeciﬁcation.
Scenario 2: Observational study
We also consider observational cases, where treatment selection depends on patients’ histories. In a similar simulation
conﬁguration for the survival and competing risks set-ups, we consider two scenarios: (i) True logistic: P(A1,i = 1|x1,i) =
6/11

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
0.2
0.3
0.4
0.5
100
300
500
700
Sample size
F(3, g^
opt)
0.0
0.2
0.4
0.6
100
300
500
700
Sample size
F^(3, g^
opt)
0.6
0.8
1.0
100
300
500
700
Sample size
Correct decision rate
TRUE logistic
0.2
0.3
0.4
0.5
100
300
500
700
Sample size
F(3, g^
opt)
0.0
0.2
0.4
0.6
100
300
500
700
Sample size
F^(3, g^
opt)
0.4
0.6
0.8
1.0
100
300
500
700
Sample size
Correct decision rate
FALSE logistic
Method
OWL
DWL
POWL
PDWL
Figure 2. Cumulative incidence rates and average correct decision rate of two stages under optimal dynamic treatment
regimes with OWL, DWL, POWL and PDWL for different sample sizes.
expit(x1,2i −0.6x1,3i) and P(A2,i = 1|x2,i) = expit(−0.5x2,i); and (ii) False logistic: P(A1,i = 1|x1,i) = expit(x1,2i −0.6x1,3i −
0.4x2
1,3i) and P(A2,i = 1|x2,i) = expit(−0.5x2,i −0.2x2
2,i). As long as we posit the standard logistic model without reﬂecting the
quadrature in (ii), propensity score fails to be well estimated.
Figure 1 and 2 summarize the simulation results for the survival and competing risks data, respectively. It is seen that
the proposed PDWL outperforms other methods even in the presence of model misspeciﬁcation, nearly touching the optimal
reference lines that represents {S(3,gopt
0 ),F1(3,gopt
0 )} and 100% performance. Overall, DR algorithms show consistently
stable results. Interestingly, POWL performs worse than OWL and DWL, which may imply that penalization would result in
inconsistent and misleading treatment rules under model misspeciﬁcation.
Scenario 3: Multiple treatments
Finally, we apply our method to the treatment recommendation problem with multiple treatments. For simplicity, suppose
there are three treatment options (L = 3) in a single stage (k = 1). We let x1,x2 and x3 follow Uniform[−2,2] independently
and π1 = exp(x2 −0.6x3), π2 = exp(x2 +0.2x3) and πs = 1+π1 +π2. Then, Ai is generated from a multinomial distribution
with probabilities where treatment 2 and 3 have probabilities π1/πs and π2/πs, respectively. Survival outcome is generated by
Ti = exp{1.5+0.5x1i +φi(x)+εi}, where φi(x) = (Ai = 1)(x1i −x2i)+(Ai = 2)(x1i +0.5x2i) and exp(εi) ∼Exp(1).
Figure 3 summarizes the results, where we use the one-versus-one SVM to optimize (9) under 30% censoring. Each color
represents three treatments and black dashed line is true decision line. Two DR methods (DR1 and DR2) perform well, clearly
separating three treatment regions. In contrast, IPW methods result in poor classiﬁcation performance, where treatment 1 is
dominated by treatments 2 and 3. This may imply that model speciﬁcation is also essential for the performance of classiﬁcation
algorithms.
7/11

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
−2
−1
0
1
2
−2
−1
0
1
2
DR1
x1
x2
−2
−1
0
1
2
−2
−1
0
1
2
DR2
x1
x2
−2
−1
0
1
2
−2
−1
0
1
2
IPW1
x1
x2
−2
−1
0
1
2
−2
−1
0
1
2
IPW2
x1
x2
Figure 3. Treatment allocations of DR and IPW estimators when there are three treatment options.
An application to ACTG175 data
Data description
This section provides a practical application of the proposed method to the AIDS Clinical Trial Group (ACTG175) study32. In
this study, each subject was randomized by four treatment arms with equal assignment probabilities: zidovudine monotherapy
(ZDV, ZDV plus didanosine (ddI), ZDV plus zalcitabine (zal) and ddI monotherapy alone, which are coded as 0, 1, 2 and 3,
respectively. Figure 4-(a) visualizes the survival curves for each treatment arms, showing three treatment arms except ZDV
alone share the common conﬁdence intervals. Previous work focused on the two treatment arms20. However, our framework is
able to allow the multiple treatments, so we analyze both binary (1 and 2) and three treatment arms (1, 2 and 3) to estimate
the optimal decision rule. The event of primary interest is the ﬁrst observed time-to-event of either having a larger than 50%
decline in the CD4 cell count or occurrence of immune deﬁciency syndrome or death. Twelve baseline covariates were gathered
in Hammer et al.32 and three of them were treated as an important risk factor: Age in year at baseline (Age), CD4 T-cell count
at baseline (CD40) and Karnofsky score (Karnof). We further include three more baseline covariates in our analysis: Gender
(Sex), weight in kilogram (Weight) and number of days of previously received antiretroviral therapy (Preanti). Under this
consideration, 79.7% of observations were right-censored and most of them happened at the end-of-study. We use the linear
regression to estimate Q-function, while the proportions of treated and untreated are used for propensity score because the data
are collected from randomized trial. Since there are lots of right-censored observations at the end-of-study, we conﬁne the
maximum timepoint as 1000 days.
Analysis results
Figure 4-(b) shows the optimized survival curves with ﬁve penalized and unpenalized weighted classiﬁcation algorithms, OWL,
POWL, DWL, PDWL, and MDWL, for which we used modiﬁed classiﬁers in MDWL to facilitate multiple treatment options.
The Kaplan-Meier (KM) curve under original treatment allocation is also included for comparison. Clearly, our proposed
contrast-learning methods can achieve higher overall survival probabilities than the naive KM estimator, although we focused on
a speciﬁc t-year survival outcome. Among the treatment rules from binary treatments, PDWL shows slightly better performance
than POWL as revealed in simulation studies, although the propensity score is well-posited from the randomized experiment.
However, OWL and DWL do not make any noticeable improvement over the KM estimator, showing that penalization is critical
in identifying effective treatment decision rules. At 500 days since treatments, the efﬁcacy of PDWL is the most noticeable than
the others, where the estimated optimal treatment regime is given by ˆgopt = I(0.562+0.583Age), coinciding 51% of original
treatments. At 1000 days since treatments, DWL, POWL and PDWL achieved about 83% survival rates, while the survival
rates under OWL and KM went below 80%, proving the clinical utility of our proposed method. By considering three treatment
arms, the MDWLs from two bounds produce equal survival rates and dominantly efﬁcient treatment efﬁcacy regarding most
timepoints than the rules from binary treatments, as it nearly reaches 85% survival rates at 1000 days.
Discussion
In this study, we propose an accountable survival contrast-learning for identifying tailored dynamic treatment regimes with
time-to-event outcomes. Existing methodologies for censored observations are mostly based on considerably burdensome
computing algorithms and not plausible when feature dimension is too high. It is because their procedures may involve
8/11

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
0.5
0.6
0.7
0.8
0.9
1.0
0
300
600
900
1200
Time (in days)
Survival probability
Treatments
ZDV
ZDV+ddI
ZDV+zal
ddI
(a)
0.6
0.7
0.8
0.9
1.0
0
300
600
900
Time (in days)
Survival probability
Methods
KM
OWL
DWL
POWL
PDWL
MDWL
(b)
Figure 4. Nonparametric Kaplan-Meier curves of ACTG175 data under (a) given treatment arms and (b) optimal treatment
rules.
nonparametric survival curve estimation at each iteration20,21. Instead, we employ an affordable pseudo-value approach by
replacing unknown survival or competing risks measures with their jackknife estimates. We then develop effective regularized
survival contrast-learning algorithms that can produce interpretable DTRs for clinical investigators. It is also noted that
many weighted classiﬁcation algorithms are based on IPW-weighting and ℓ2-penalization, which are vulnerable to model
mis-speciﬁcation and amount of censoring. We provide empirical evidence that our proposal can signiﬁcantly increase
accountability and prediction power in clinical decision-making by combining well-known regularization and double-robust
(DR) weighting schemes.
Of note, pseudo-observations require the strict independent censoring condition, which may fail to hold in practice. Our
empirical experiences, however, show that our approach still works well even in the case of covariate-dependent censoring.
One may adopt an inversely censoring weighted approach to facilitate covariate-dependent censoring33, but we expect that
its contribution is limited in our setting. Finally, although the one-versus-one pairwise SVM performs well with multiple
treatments, our method can also be implemented with a single SVM for multi-categorized items by employing the approach in
Hsu and Lin34. This idea is worth further investigation and will be pursued in a separate study.
Data availability
The pseudo-observation of survival quantities can be calculated by the R package pseudo35. The optimization of the penalized
SVM is conducted by the R package lpSolve36. One-versus-one pairwise SVM can be implemented by the R package
e107137. The ACTG175 dataset used in this study is available at the R package speff2trial38.
Acknowledgements
The results of ACTG data analysis are solely the responsibility of the authors and does not necessarily represent the ofﬁcial views
of the AIDS clinical trial group. The research of T.C. was supported by the junior fellow research grant of Korea University.
The research of S.C. was supported by grant from the National Research Foundation (NSF) of Korea (2019R1F1A1052239,
2022R1A2C1008514).
Author contributions
T.C. developed the method, conducted simulation and data analysis, and wrote the manuscript. H.L. validated the computation
and data analysis, and reviewed and edited the manuscript. S.C. conceptualized the method, and wrote, reviewed and edited the
9/11

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
manuscript. All authors reviewed the ﬁnal version of the manuscript.
Competing interests
The authors declare no competing interests.
Additional information
The corresponding author is responsible for submitting a competing interests statement on behalf of all authors of the paper.
This statement must be included in the submitted article ﬁle.
References
1. Murphy, S. A. Optimal dynamic treatment regimes. J. Royal Stat. Soc. Ser. B (Statistical Methodol. 65, 331–355 (2003).
2. Zhao, Y., Kosorok, M. R. & Zeng, D. Reinforcement learning design for cancer clinical trials. Stat. Medicine 28, 3294–3315
(2009).
3. Qian, M. & Murphy, S. A. Performance guarantees for individualized treatment rules. The Annals Stat. 39, 1180–1210
(2011).
4. Zhao, Y., Zeng, D., Rush, A. J. & Kosorok, M. R. Estimating individualized treatment rules using outcome weighted
learning. J. Am. Stat. Assoc. 107, 1106–1118 (2012).
5. Tian, L., Alizadeh, A. A., Gentles, A. J. & Tibshirani, R. A simple method for estimating interactions between a treatment
and a large number of covariates. J. Am. Stat. Assoc. 109, 1517–1532 (2014).
6. Chakraborty, B., Murphy, S. & Strecher, V. Inference for non-regular parameters in optimal dynamic treatment regimes.
Stat. Methods Med. Res. 19, 317–343 (2010).
7. Song, R. et al. On sparse representation for optimal individualized treatment selection with penalized outcome weighted
learning. Stat 4, 59–68 (2015).
8. Huang, X., Choi, S., Wang, L. & Thall, P. F. Optimization of multi-stage dynamic treatment regimes utilizing accumulated
data. Stat. Medicine 34, 3424–3443 (2015).
9. Zhang, B., Tsiatis, A. A., Davidian, M., Zhang, M. & Laber, E. Estimating optimal treatment regimes from a classiﬁcation
perspective. Stat 1, 103–114 (2012).
10. Zhang, B., Tsiatis, A. A., Laber, E. B. & Davidian, M. A robust method for estimating optimal treatment regimes.
Biometrics 68, 1010–1018 (2012).
11. Zhang, B., Tsiatis, A. A., Laber, E. B. & Davidian, M. Robust estimation of optimal dynamic treatment regimes for
sequential treatment decisions. Biometrika 100, 681–694 (2013).
12. Zhang, B. & Zhang, M. C-learning: A new classiﬁcation framework to estimate optimal dynamic treatment regimes.
Biometrics 74, 891–899 (2018).
13. Qi, Z., Liu, Y. et al. D-learning to estimate optimal individual treatment rules. Electron. J. Stat. 12, 3601–3638 (2018).
14. Tao, Y. & Wang, L. Adaptive contrast weighted learning for multi-stage multi-treatment decision-making. Biometrics 73,
145–155 (2017).
15. Lakkaraju, H. & Rudin, C. Learning cost-effective and interpretable treatment regimes. In International Conference on
Artiﬁcial Intelligence and Statistics, 166–175 (PMLR, 2017).
16. Sherman, E., Arbour, D. & Shpitser, I. General identiﬁcation of dynamic treatment regimes under interference. In
International Conference on Artiﬁcial Intelligence and Statistics, 3917–3927 (PMLR, 2020).
17. Cai, H., Lu, W. & Song, R. On validation and planning of an optimal decision rule with application in healthcare studies.
In International Conference on Machine Learning, 1262–1270 (PMLR, 2020).
18. Zhao, Y.-Q. et al. Doubly robust learning for estimating individualized treatment with censored data. Biometrika 102,
151–168 (2015).
19. Bai, X., Tsiatis, A. A., Lu, W. & Song, R. Optimal treatment regimes for survival endpoints using a locally-efﬁcient
doubly-robust estimator from a classiﬁcation perspective. Lifetime Data Analysis 23, 585–604 (2017).
20. Jiang, R., Lu, W., Song, R. & Davidian, M. On estimation of optimal treatment regimes for maximizing t-year survival
probability. J. Royal Stat. Soc. Ser. B (Statistical Methodol. 79, 1165–1185 (2017).
10/11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
21. Zhou, J., Zhang, J., Lu, W. & Li, X. On restricted optimal treatment regime estimation for competing risks data. Biostatistics
22, 217–232 (2021).
22. Robins, J. M. Optimal structural nested models for optimal sequential decisions. In Proceedings of the Second Seattle
Symposium in Biostatistics, 189–326 (Springer, 2004).
23. Andersen, P. K. & Pohar Perme, M. Pseudo-observations in survival analysis. Stat. Methods Med. Res. 19, 71–99 (2010).
24. Robins, J. A new approach to causal inference in mortality studies with a sustained exposure period—application to control
of the healthy worker survivor effect. Math. Model. 7, 1393–1512 (1986).
25. Schulte, P. J., Tsiatis, A. A., Laber, E. B. & Davidian, M. Q- and A-learning methods for estimating optimal dynamic
treatment regimes. Stat. Sci. 29, 640–661 (2014).
26. Lee, B. K., Lessler, J. & Stuart, E. A. Improving propensity score weighting using machine learning. Stat. Medicine 29,
337–346 (2010).
27. McCaffrey, D. F. et al. A tutorial on propensity score estimation for multiple treatments using generalized boosted models.
Stat. Medicine 32, 3388–3414 (2013).
28. Tsiatis, A. Semiparametric Theory and Missing Data (Springer, 2007).
29. Cortes, C. & Vapnik, V. Support-vector networks. Mach. Learn. 20, 273–297 (1995).
30. Fan, J. & Li, R. Variable selection via nonconcave penalized likelihood and its oracle properties. J. Am. Stat. Assoc. 96,
1348–1360 (2001).
31. Fine, J. P. & Gray, R. J. A proportional hazards model for the subdistribution of a competing risk. J. Am. Stat. Assoc. 94,
496–509 (1999).
32. Hammer, S. M. et al. A trial comparing nucleoside monotherapy with combination therapy in hiv-infected adults with cd4
cell counts from 200 to 500 per cubic millimeter. New Engl. J. Medicine 335, 1081–1090 (1996).
33. Overgaard, M., Parner, E. T. & Pedersen, J. Pseudo-observations under covariate-dependent censoring. J. Stat. Plan.
Inference 202, 112–122 (2019).
34. Hsu, C.-W. & Lin, C.-J. A comparison of methods for multiclass support vector machines. IEEE transactions on Neural
Networks 13, 415–425 (2002).
35. Maja Pohar Perme & Gerster, M. pseudo: Computes Pseudo-Observations for Modeling (2017). R package version 1.4.3.
36. Berkelaar, M., Eikland, K. & Notebaert, P. lpSolve: interface to ‘Lp_solve’v. 5.5 to solve linear/integer programs (2015).
R package version 5.6.15.
37. Meyer, D., Dimitriadou, E., Hornik, K., Weingessel, A. & Leisch, F. e1071: Misc Functions of the Department of Statistics,
ProbabilityTheory Group (Formerly: E1071), TU Wien (2020). R package version 1.7-4.
38. Juraska, M. et al. speff2trial: Semiparametric efﬁcient estimation for a two-sample treatment effect (2012). R package
version 1.0.4.
11/11

````

## PDF page 13

Technical extraction; compare with original PDF page 13.

````text
Supplementary Files
This is a list of supplementary ¦les associated with this preprint. Click to download.
supplement.pdf

````

