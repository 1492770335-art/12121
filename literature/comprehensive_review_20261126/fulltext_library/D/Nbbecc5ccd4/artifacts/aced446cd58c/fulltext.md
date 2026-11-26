# Weighted Competing Risks Quantile Regression Models and Variable Selection

Original PDF: [original.pdf](original.pdf). SHA256: `aced446cd58c9f5018839ab78fcbcabf7e58862ae59facd9d19c3184828a7489`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
Citation: Li, E.; Pan, J.; Tang, M.; Yu,
K.; Härdle, W.K.; Dai, X.; Tian, M.
Weighted Competing Risks Quantile
Regression Models and Variable
Selection. Mathematics 2023, 11, 1295.
https://doi.org/10.3390/
math11061295
Academic Editors: Yiqiang Zhan and
Xingrong Liu
Received: 23 January 2023
Revised: 24 February 2023
Accepted: 2 March 2023
Published: 8 March 2023
Copyright:
© 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed
under
the
terms
and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
mathematics
Article
Weighted Competing Risks Quantile Regression Models and
Variable Selection
Erqian Li 1
, Jianxin Pan 2, Manlai Tang 3, Keming Yu 4, Wolfgang Karl Härdle 5
, Xiaowen Dai 6
and Maozai Tian 7,*
1
College of Science, North China University of Technology, Beijing 100144, China
2
School of Mathematics, University of Manchester, Manchester M13 9PL, UK
3
Department of Physics, Astronomy and Mathematics, School of Physics, Engineering & Computer Science,
University of Hertfordshire, Hatﬁeld AL10 9EU, UK
4
Department of Mathematics, College of Engineering, Design and Physical Sciences Brunel University,
Uxbridge UB8 3PH, UK
5
School of Business and Economics, Humboldt-Universität zu Berlin, 10117 Berlin, Germany
6
School of Statistics and Mathematics, Shanghai Lixin University of Accounting and Finance,
Shanghai 201620, China
7
Center for Applied Statistics, School of Statistics, Renmin University of China, Beijing 100872, China
*
Correspondence: mztian@ruc.edu.cn
Abstract: The proportional subdistribution hazards (PSH) model is popularly used to deal with
competing risks data. Censored quantile regression provides an important supplement as well
as variable selection methods due to large numbers of irrelevant covariates in practice. In this
paper, we study variable selection procedures based on penalized weighted quantile regression for
competing risks models, which is conveniently applied by researchers. Asymptotic properties of the
proposed estimators, including consistency and asymptotic normality of non-penalized estimator
and consistency of variable selection, are established. Monte Carlo simulation studies are conducted,
showing that the proposed methods are considerably stable and efﬁcient. Real data about bone
marrow transplant (BMT) are also analyzed to illustrate the application of the proposed procedure.
Keywords: competing risks; cumulative incidence function; bone marrow transplant; re-distribution
method
MSC: 62N02
1. Introduction
In survival analysis, sometimes events fail because of a speciﬁc cause or from some
other causes or competing risks. Consider the dataset of bone marrow transplant (BMT)
in [1] for example, which includes 177 patients who received a stem cell transplant for acute
leukemia. Whereas 56 patients in this dataset relapsed (REL), considered as the event of
interest, 75 patients died from causes related to the transplant (transplant related mortality,
TRM), which is considered a competing risk, as it hinders the occurrence of leukemia
relapse. The other 46 patients are regarded as censored due to the end of the study. In the
analysis of such a dataset, treating competing risks (TRM) as censoring cases and using
usual Cox modelling may be inaccurate, as the competing risks are probably affected by co-
variates. To deal with such competing risks data, Ref. [2] proposed a novel semiparametric
proportional hazards for the subdistribution, or PSH model, which directly analyzes the
effect of covariates on the marginal probability function or cumulative incidence function
(CIF). The competing risks data often occur in clinical trials containing large numbers of
covariates, among which only a few have signiﬁcant or essential inﬂuence on the response,
generating the variable selection issues, such as the general penalized log-partial likelihood
method proposed by [3].
Mathematics 2023, 11, 1295. https://doi.org/10.3390/math11061295
https://www.mdpi.com/journal/mathematics

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
Mathematics 2023, 11, 1295
2 of 23
Quantile regression introduced by [4] is widely known to more comprehensively
describe the conditional distribution of response on covariates. Existing work about
competing risks quantile regression includes [5], which ﬁrst transforms competing risks
quantile regression models to accelerated the failure model and uses an estimating equa-
tion procedure for estimation. In addition, Ref. [6] discussed the quantile regression for
competing risks data with missing cause of failure. Then [7,8] developed variable selection
procedures based on unbiased estimating equations with group structures and penalization
methods for competing risks quantile regression models.
In the paper, in spite of the estimating equation method, we propose developing a
more general method for competing risks quantile regression and expanding the weighted
procedures by considering the re-distribution methods [9] for the PSH model. By trans-
formed responses, we can rewrite the competing risks quantiles formulation as a general
quantile regression objective function, then apply the constructed weights. With unbiased-
ness of the subgradient of this weighted objective function at the true cumulative-incidence
function and coefﬁcient proved, consistency and asymptotic normality of the penalty-free
estimators are established under regularity conditions. To realize the variable selection,
penalization methods such as the least absolute shrinkage and selection operator (LASSO)
proposed by [10] and the adaptive LASSO (ALASSO) developed by [11] are applied to the
weighted objective function, which can be easily applied with the R package. The consis-
tency of the variable selection procedure is also established, and Monte Carlo simulation is
performed to illustrate the efﬁciency and stability of our proposed procedures. Real data
about bone marrow transplant are analyzed using our methods.
The paper is organized as follows. Our proposed weighted competing risks quantile
regression model and its penalized methods are developed in Section 2, with asymptotic
properties demonstrated in Section 3. Simulation studies as well as the application to the
BMT data are performed in Section 4 to illustrate the performance of proposed methods.
2. Models
We take the formulation of competing risks quantile regression in [5]. In the setting of
competing risks models, assume there exist K causes of failure, denoted by an observable
indicator ϵ ∈{1, . . . , K}, the same denotation as [2]. Without loss of generality, we
can set K = 2. Let T and C denote the failure and censoring time, respectively, and we
observe X = min(T, C), and censoring or risk indicator δ = I(T ≤C), where I(·) is an
indicator function. Denote a p × 1 bounded time-independent covariate vector as ˜Z and
Z = (1, ˜Z⊤)⊤. Assume that {Xi, δiϵi, Zi}, i = 1, . . . , n are independent and identically
distributed observed samples.
Ref. [2] modeled the CIF for failure from cause 1 conditionally on the covariates,
F1(t|Z) = P(T ≤t, ϵ = 1|Z). They proposed the PSH model based on the formula of
subdistribution hazard, which is deﬁned as
λ1(t|Z)
=
lim
∆t→0
1
∆t P

t < T ≤t + ∆t, ϵ = 1
(T ≥t) ∪(T ≤t ∩ϵ̸ = 1), Z
	
=
{dF1(t|Z)/dt}/{1 −F1(t|Z)}
in [12]. Analogue to the deﬁnition of quantile, we deﬁne the conditional quantile as
Qk(τ|Z) = inf{t : Fk(t|Z) ≥τ}, k = 1, . . . , K, where Fk(t|Z) = P{T ≤t, ϵ = k} is the CIF
for cause k; for more details, refer to [5]. For τ ∈[τL, τU], consider Q1(τ|Z) to be modeled
as
Q1(τ|Z) = g{Z⊤β0(τ)},
(1)
where β0(τ) is a (p + 1) × 1 coefﬁcient vector, g(·) is a known monotone increasing and
continuously differential bounded link function, 0 < τL ≤τU < 1. With the statement
in [2], if we denote T∗
1 = I(ϵ = 1) × T + {1 −I(ϵ = 1)} × ∞, then T∗
1 has a distribution
function equal to F1(t|Z) when t < ∞and a point mass P(T∗= ∞|Z) = P(T < ∞, ϵ̸ =

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
Mathematics 2023, 11, 1295
3 of 23
1) = 1 −F1(∞|Z) at t = ∞. Then, at τ < F1(∞|Z), the τ−quantile of T∗
1 equals F−1
1 (τ|Z) =
Q1(τ|Z) = g{Z⊤β0(τ)} under the formulation of (1).
Remark 1. According to the formulation of T∗
1 , we can see that when τ ≥F1(∞; Z), the
τ−quantile of T∗
1 will become ∞, which is obvious when reviewing the deﬁnition that F1(t; Z) =
P(T ≤t, ϵ = 1|Z) ≤P(T ≤∞, ϵ = 1|Z) = F1(∞; Z) and the fact that g(·) is monotone
increasing. This fact provides a thought about the choice of τU.
With reference to [13], for proper τ, β0(τ) is supposed to be the minimizer of the
following expected loss function with respect to β(τ):
β0(τ) = arg min
β(τ) Eρτ(g−1(T∗
1 ) −Z⊤β(τ)),
(2)
where E denotes the expectation, and ρτ(u) = u{τ −I(u ≤0)} is called the “check”
function.
In a sample scenario, we can obtain the estimator ˆβ(τ) of β0(τ) via minimizing the
following objective function:
min
β(τ)
n
∑
i=1
ρτ

g−1(T∗
1,i) −Z⊤
i β(τ)

.
(3)
2.1. Weighted Competing Risks Quantile Regression
Similar to [5], our paper ﬁrst considers the case in which there are no missing data
(i.e., there is no censoring). As a result, X = T and δ = 1, δϵ = ϵ. As aforementioned,
we can estimate β0(τ) via the minimization problem (3). Because T∗
1,i is not observed, we
modify (3) to
n
∑
i=1
I(ϵi = 1)ρτ(g−1(Xi) −Z⊤
i β(τ)) + I(ϵi̸ = 1)ρτ(g−1(X∞) −Z⊤
i β(τ)),
(4)
where X∞is any value sufﬁciently large to exceed all Z⊤
i β(τ). Then, it is not difﬁcult to
derive the negative subgradient of (4) with respect to β(τ).
For the censoring case, we aim to construct such a weighted quantile objective function
to estimate β0(τ) as follows:
Q(β(τ), w0)
=
n
∑
i=1
n
w0iρτ(g−1(Xi) −Z⊤
i β(τ))
+(1 −w0i)ρτ(g−1(X+∞) −Z⊤
i β(τ))
o
.
(5)
The weight function is re-constructed based on competing risks analogy to [14], as
follows:
w0i =





1,
δiϵi = 1,
0,
δiϵi̸ = 1, F1(Ci|Zi) > τ,
τ−F1(Ci|Zi)
1−F1(Ci|Zi) ,
δiϵi̸ = 1, F1(Ci|Zi) ≤τ.
(6)
Remark 2. In our case of competing risks quantile regression, each point contributes to the sub-
gradient condition only via the sign of g−1(T∗
1,i) −Z⊤
i β0(τ). For data with δiϵi = 1, we know
Xi = Ti ≤Ci, ϵi = 1, i.e., Xi = T∗
1,i, and I(g−1(T∗
1,i) −Z⊤
i β0(τ) < 0) can be observed,
thus we assign a weight of 1 for this case. For data with δiϵi̸ = 1 and F1(Ci|Zi) > τ, then
Ti > Ci, F1(Ci|Zi) > τ or Ti ≤Ci, ϵi = 2, F1(Ci|Zi) > τ; in the ﬁrst scenario, T∗
1,i ≥
Ti ≥Xi = Ci > g(Z⊤
i β0(τ)), I(g−1(T∗
1,i) −Z⊤
i β0(τ) < 0) = 0; in the second scenario,
Ti ≤Ci, ϵ = 2, I(g−1(T∗
1,i) −Z⊤
i β0(τ) < 0) = 0, where we assign a weight of 0. The

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Mathematics 2023, 11, 1295
4 of 23
ambiguous situation is δiϵi̸ = 1 and F1(Ci|Zi) < τ, i.e., Ci ≤F−1
1 (τ|Zi) = g(Z⊤
i β0(τ)).
If δi = 1, ϵi = 2, Xi = Ti < Ci < g(Z⊤
i β0(τ)), or I{g−1(Xi) −Z⊤
i β0(τ) < 0} = 1;
if δi = 0, Xi = Ci < Z⊤
i β0(τ), i.e., I{g−1(Xi) −Z⊤
i β0(τ) < 0} = 1.
However, the
I(T∗
1,i −g(Z⊤
i β0(τ)) < 0) cannot be observed.
Thus, we assign the weight wi(F0) = τ−F1(Ci|Zi)
1−F1(Ci|Zi) for this case, where given (Zi, Ci),
E
n
I(g−1(T∗
1,i) −Z⊤
i β0(τ) < 0)|δiϵi̸ = 1, Zi
o
= P

ϵi = 1, Ti < g(Z⊤
i β0(τ))|Zi
	 −P{ϵi = 1, Ti < Ci}
1 −P(Ti ≤Ci, ϵi = 1|Zi)
= τ −F1(Ci|Zi)
1 −F1(Ci|Zi) .
(7)
We can show that a subgradient of the weighted quantile objective function (5) with
respect to β(τ)
Mn(β(τ), w0) =
n
∑
i=1
Zi
n
τ −w0iI(g−1(Xi) < Z⊤
i β(τ))
o
(8)
is an unbiased estimating function of β0(τ).
E
h
w0iI{g−1(Xi) < Z⊤
i β0(τ)}|Zi
i
= E

I{δiϵi = 1}w0iI{g−1(Xi) < Z⊤
i β0(τ)}|Zi

+E

I{δiϵi̸ = 1, F1(Ci) > Z⊤
i β0(τ)}w0iI{g−1(Xi) < Z⊤
i β0(τ)}|Zi

+E

I{δiϵi̸ = 1, F1(Ci) ≤Z⊤
i β0(τ)}w0iI{g−1(Xi) < Z⊤
i β0(τ)}|Zi

= P

ϵi = 1, g−1(Ti) < Z⊤
i β0(τ)|Zi

= τ.
Although the unbiasedness of (8) is proved with F1(Ci|Zi) in w0i, the underlying
distribution F1(t|Z) or w0i is unknown in practice. Here we use the IPCW [15] estimator
proposed by [5] to estimate F1(t|Z),
ˆF1(x|Z) = 1
n
n
∑
i=1
 I(Xi ≤x, δiϵi = 1)
1 −ˆG(Xi|Zi)

,
(9)
where 1 −G(·t|Z) is the survival function of C given Z, which can be estimated semipara-
metrically or nonparametrically. Here for simplicity, as in [2], we assume the indepen-
dence of C and (T, ϵ, Z), then the Kaplan–Meier estimator in [16] could be used. Such a
computation-friendly estimator (9) has been proved to behave quite well in simulation
results, which should be well improved combined with more effective estimators of F1(t|Z).
By plugging (9) in the expression of w0i, we can get the estimated weights wi( ˆF1),
wi( ˆF1) =





1,
δiϵi = 1,
0,
δiϵi̸ = 1, ˆF1(Ci|Zi) > τ,
τ−ˆF1(Ci|Zi)
1−ˆF1(Ci|Zi) ,
δiϵi̸ = 1, ˆF1(Ci|Zi) ≤τ,
(10)
where ˆF1 is as in (9) or replaced with other consistent estimators. Then, we obtain the
weighted censoring quantile regression estimator ˆβ(τ) by minimizing the weighted objec-
tive function,

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Mathematics 2023, 11, 1295
5 of 23
Q(β(τ), ˆF1)
=
n
∑
i=1
n
wi( ˆF1)ρτ(g−1(Xi) −Z⊤
i β(τ))
+(1 −wi( ˆF1))ρτ(g−1(X+∞) −Z⊤
i β(τ))
o
.
(11)
2.2. Variable Selection Procedure
To select important variables, a penalty function is added to the weighted objective
function (11) to obtain the penalized estimator ˜β(τ):
Qp(β(τ), wi( ˆF1))
=
n
∑
i=1
n
wi( ˆF1)ρτ(g−1(Xi) −Z⊤
i β(τ))
+(1 −wi( ˆF1))ρτ(g−1(X+∞) −Z⊤
i β(τ))
o
+
p
∑
j=1
pλ(|βj(τ)|),
(12)
where pλ(·) can be LASSO, adaptive LASSO, and so on.
For LASSO and ALASSO penalty, we can easily write pλ(|βj|) = λn| ˆβj|−γ, where
| ˆβj| is the jth element of the initial consistent unpenalized estimator. We choose γ = 0 for
LASSO and γ = 1 for ALASSO. The minimization of (12) and (11) can be directly solved
with the R package quantreg without linear programming, leading our proposed methods
to conveniently applicable tools.
3. Theoretical Property
To establish the asymptotic results in this paper, we require the following assumptions:
A1
The covariate Z is bounded in probability. There exists a constant Kz such that
E∥Z∥3 ≤Kz, and E(ZZ⊤) is a positive deﬁnite (p + 1) × (p + 1) matrix.
A2
The functions F1(t|Z) and G(t) have ﬁrst derivatives with respect to t, denoted as
f1(t|Z) and g0(t), which are uniformly bounded away from inﬁnity. Additionally,
F1(t|Z) and G(t) have bounded (uniformly in t) second-order partial derivatives with
respect to Z.
A3
For β in the neighborhood of β0(τ), E(ZZ⊤g′(Z⊤β) f1(g(Z⊤β)|Z){1 −G(g(Z⊤β))})
and E(ZZ⊤g′(Z⊤β)g0(g(Z⊤β))) are positive deﬁnite.
Assumption A1 states some tail and moment conditions on the covariate Z, which
are standard for the quantile regression. Assumption A2 is needed for the local Kaplan–
Meier estimator. It allows us to obtain the local expansions of F1(t|z) and G(t) in the
neighborhood of Z⊤β0(τ) in order to obtain the uniform consistency and the linear repre-
sentation of ˆF1(t|Z). Assumption A3 ensures that the expectation of the estimating function
E{Mn(β, F1)} has a unique zero at β0(τ), and it is needed to establish the asymptotic
distribution of ˆβ(τ).
C1
There exists ν > 0 such that P(C = ν) > 0 and P(C > ν)=0.
C2
β0(τ) is Lipschitz continuous for τ ∈[τL, τU].
C3
P(ϵ = 1|Z) < 1 a.s.
Assumptions C1 and C2 are regularity conditions for competing risks quantile regres-
sions. Assumption C3 is easily satisﬁed for the situation of competing risks; otherwise, it
will turn out to be a standard Cox model.
Theorem 1. Assume that triples {Zi, Xi, δiϵi}, i = 1, · · · , n constitute an i.i.d. multivariate
random sample and that the censoring variable Ci is independent of Ti conditionally on the covariate
Zi. Under model (1) and assumptions A1–A3, C1–C3,
ˆβ(τ) →β0(τ)
(13)

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
Mathematics 2023, 11, 1295
6 of 23
in probability as n →∞.
Theorem 2. Under the assumptions of Theorem 1 and r < 1/4, we have
n1/2( ˆβ(τ) −β0(τ)) D→N(0, Γ−1VΓ−1),
(14)
where
Γ−1 = E[ZZ⊤g′(Z⊤β0(τ)){1 −G(g(Z⊤β0(τ)))} f1(g(Z⊤β0(τ))|Z)],
(15)
and
V = Cov(mi(β0, F1) + (1 −τ)φi),
(16)
with mi(β0, F1) = Zi{τ −wi(F1)I(Xi < g(Z⊤
i β0(τ)))}, φi deﬁned in Equation (A9).
Theorems 1 and 2 established the consistency and asymptotic normality of the un-
penalized estimator ˆβ(τ).
We then establish the property of consistency in variable
selection of the proposed penalized estimator ˜β(τ). Let A(τ) = {j : β0j̸ = 0} and
Ac(τ) = {j : β0j(τ) = 0}.
Theorem 3. If A1–A3, C1–C3 hold, and if n−1/2λn →0 and n(γ−1)/2λn →∞, then
P
 {j : ˜βj(τ)̸ = 0} = A(τ)
 →1
as
n →∞.
Theorem 3 states that the proposed procedure is able to select the correct model with
probability approaching one. By the remark of Theorem 2 of [14], the oracle properties are
satisﬁed by the proposed estimators.
The proofs are presented in Appendix A.
4. Numerical Studies
4.1. Monte Carlo Simulation
We conduct Monte Carlo simulations to evaluate the performance of the proposed
methods and consider the data-generating ways as in [5] with a larger dimension of
covariates.
We generate (T, ϵ) satisfying P(ϵ = 1|Z) = p0I(Z2 = 0) + p1I(Z2 = 1), P(T ≤t|ϵ =
1, Z) = Φ(log t −γ⊤
0 Z), and P(T ≤t|ϵ = 2, Z) = Φ(log t −α⊤
0 Z), where Φ(·) denotes the
standard normal distribution function, p0 = 0.8, p1 = 0.6, γ0 and α0 are true parameters in
the model above. Set γ0 = (−2, −2.5, 2, −2.4, 0, · · · , 0) while α0 = −γ0. Then
log Q1(τ|Z)
=
Φ−1
 τ
p0

+ γ(1)
0 Z1 +

γ(2)
0
+ Φ−1
 τ
p1

−Φ−1
 τ
p0

Z2
+γ(3)
0 Z3 + γ(4)
0 Z4
where Zj is the jth component of covariate Z, and γ(j)
0
is the jth component of γ0. Then the
estimated coefﬁcient in model (1) is
β0(τ) = (Φ−1
 τ
p0

, γ(1)
0 , γ(2)
0
+ Φ−1
 τ
p1

−Φ−1
 τ
p0

, γ(3)
0 , γ(4)
0 , 0, · · · , 0).
Thus the true number of non-zero coefﬁcients is 5 for τ̸ = 0.4 and 4 for τ = 0.4 due to
Φ−1
0.4
p0

= 0.
In simulations, we set the number of irrelevant predictors to be s = #{j : β0j̸ = 0} = 30,
the sample size to be n = 200. For the structure of the covariance matrix for covariates, we
consider Σ1,ij = ρ ,where ρ = 0, 0.25, 0.5, 0.75.

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
Mathematics 2023, 11, 1295
7 of 23
We generate the covariate vector Z = (Z1, Z2, Z3, · · · , Zp)⊤as follows: Z1 ∼Unif(0,1)
and Z2 ∼Bernoulli(0.5), Zj ∼N(0, Σ), j = 3, · · · , p. For each scenario, the simulation is
repeated 500 times. The censoring rate average is 36%.
We use the following criteria to evaluate the performances: the ratio of number of rele-
vant variables correctly selected to true number of relevant variables (TPr) deﬁned as TPr =
#{{j:| ˆβj(τ)|̸=0}∩{j:|β0j(τ)|̸=0}}
#{j:|β0j(τ)|̸=0}
, the ratio of number of irrelevant variables incorrectly selected
to true number of irrelevant variables (FPr) deﬁned as FPr =
#{{j: ˆβj(τ)̸=0}∩{j:|β0j|=0}}
#{j:|β0j|=0}
, the ab-
solute error P1 = ∑
p
j=1 | ˆβj(τ) −β0j(τ)|, and the squared error P2 = ∑
p
j=1 | ˆβj(τ) −β0j(τ))|2.
The closer TPr is to 1 and FPr is to 0, the better. Both TPr and FPr range from 0 to 1, thus
we present them together in Figure 1 for comparison.
0.1
0.2
0.3
0.4
0.5
0.0
0.2
0.4
0.6
0.8
1.0
TPr and FPr Value
= 0.0
0.1
0.2
0.3
0.4
0.5
0.0
0.2
0.4
0.6
0.8
1.0
TPr and FPr Value
= 0.25
0.1
0.2
0.3
0.4
0.5
0.0
0.2
0.4
0.6
0.8
1.0
TPr and FPr Value
= 0.5
0.1
0.2
0.3
0.4
0.5
0.0
0.2
0.4
0.6
0.8
1.0
TPr and FPr Value
= 0.75
TPr:cqr.l
FPr:cqr.l
TPr:wcqr0.l
FPr:wcqr0.l
TPr:wcqr1.l
FPr:wcqr1.l
TPr:wcqr2.l
FPr:wcqr2.l
TPr:cqr.a
FPr:cqr.a
TPr:wcqr0.a
FPr:wcqr0.a
TPr:wcqr1.a
FPr:wcqr1.a
TPr:wcqr2.a
FPr:wcqr2.a
Figure 1. Case n = 200, s = 30, p0 = 0.8, p1 = 0.6. Comparison of TPr and FPr for four levels of ρ. In
each subplot, the Y axis reports the TPr and FPr values at different τ. The solid line is TPr and the
dashed line is FPr. Four colors are used to represent the methods: red for wcqr, green for wcqr0, blue
for wcqr1, and purple for wcqr2. Light colors represent the LASSO penalty and dark colors are the
ALASSO penalty for all methods.
We compare our proposed weighted estimators with the estimated estimator of com-
peting risks quantile regression model proposed in [8], denoted as wcqr and cqr, respec-
tively, implying the weighting method or not. In simulation tables, we use cqr.l and cqr.a
to represent cqr estimators with LASSO and ALASSO penalty, respectively. Similarly, our
estimators, denoted as wcqri.l and wcqri.a, i = 0, 1 stands for administrative censoring

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
Mathematics 2023, 11, 1295
8 of 23
where C is known and randomly right censoring cases where X is in place of C, respectively;
wcqr2 uses a different weight:
wi(F1)
=





1
δiϵi = 1
τ−ˆF1(Ci)
1−ˆF1(Ci)−ˆF2(Ci)
δi = 0, ˆF1(Ci) < τ
0
otherwise.
As the weight above involves the estimation of F2(t|Z) = P(T ≤t, ϵ = 2|Z), which
probably is complicated in practical circumstances, we only use it for comparison in
simulations. Here in wcqr2, we apply a similar estimating method of F1 to F2.
Alhough our theoretical results are not based on these two estimators of wi, most
simulation results show that wcqr0 and wcqr1 are considerably close, as the weight is
only different at δ = 1, suggesting good estimates in large censoring rates. Research about
massive competing risks data with enormous censored observations will appear in our
future work.
Before the variable selection, we also conduct the simulation for unpenalized estima-
tors. In this case, we use γ0 = (1, −1.5, −0.5), p0 = 0.8, p1 = 0.6, and ρ = 0. We repeat this
1000 times and compare the empirical bias (EmpBias) and average coverage probabilities
based on 95% conﬁdence intervals computed with empirical variance. The results are
summarized in Table 1, where in lower quantiles, the cqr method shows extreme excellence,
whereas in high quantiles, it displays some instability. For weighted methods, though
inferior to cqr in lower quantiles, these methods still behave well in most simulations,
especially wcqr1 and wcqr2. The average coverage probabilities display similar patterns;
cqr behaves well until τ < 0.4. In relatively high quantiles such as τ = 0.5, wcqr2 behaves
the best for most coefﬁcients.
Table 1. Bias and empirical coverage; n = 300, ρ = 0, p0 = 0.8, p1 = 0.6.
τ
Method
Bias
EmpCoverage
β1
β2
β3
β4
β1
β2
β3
β4
0.1
cqr
−0.012
−0.003
0.003
0.003
0.952
0.953
0.953
0.958
wcqr1
−0.027
−0.026
0.031
0.014
0.950
0.952
0.950
0.949
wcqr2
−0.027
−0.032
0.036
0.018
0.948
0.952
0.946
0.950
0.2
cqr
0.000
−0.015
−0.007
0.008
0.946
0.950
0.943
0.952
wcqr1
−0.024
−0.061
0.042
0.032
0.948
0.944
0.949
0.943
wcqr2
−0.019
−0.081
0.055
0.040
0.949
0.940
0.952
0.940
0.3
cqr
−0.010
−0.023
0.008
0.014
0.947
0.949
0.956
0.953
wcqr1
−0.042
−0.108
0.095
0.055
0.938
0.952
0.944
0.943
wcqr2
−0.027
−0.131
0.104
0.065
0.939
0.949
0.934
0.941
0.4
cqr
0.219
−1.244
−0.069
0.316
0.999
0.999
0.999
0.999
wcqr1
−0.065
−0.203
0.168
0.121
0.947
0.943
0.931
0.937
wcqr2
0.007
−0.153
0.111
0.095
0.949
0.939
0.941
0.922
0.5
cqr
−5.878
−25.526
−12.526
10.139
0.975
0.957
0.967
0.953
wcqr1
−0.313
−0.632
0.594
0.280
0.965
0.943
0.963
0.914
wcqr2
0.144
0.034
0.041
−0.007
0.913
0.955
0.952
0.953
With moderate dimensions of covariates (s = 30), Figure 1 presents the TPr and FPr
values evaluated for n = 200 and τ ∈(0, 0.6) and four ρs for Σ1, respectively. Generally
speaking, we can observe that almost all selection performances appear to decline as τ
increases, and with higher TPr and lower FPr, ALASSO penalized methods are overall
superior to LASSO methods. Speciﬁcally, in quantiles lower than 0.4, with ALASSO penalty,
cqr and wcqr both have good performances for identiﬁcation of important variables, with
TPr close to 1. Compared to the ALASSO method, LASSO methods have higher FPr
values and tend to select much more irrelevant variables. In Figure 1, wcqr estimators

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
Mathematics 2023, 11, 1295
9 of 23
display comparable performance with cqr estimators according to high TPr and low FPr at
moderate τ ∈(0, 0.35). At higher quantiles, although a little bit inferior to cqr estimators
in TPr, wcqr estimators have very low FPr values despite a rapid increase of FPr for cqr
estimators, which means wcqr estimators have a strong ability to drop irrelevant variables
as well as select correct variables even when cqr estimators almost fail in particularly high
quantiles. We should state that in all simulations, wcqr estimators present quite stable
performances in higher quantiles and higher dimensions. The decline of performance with
increasing τ can be explained by a higher τ that is approaching the probability P(ϵ = 1|Z),
which induces larger biases. In addition, it is notable that TPr has a very small decrease
when ρ increases except for cqr.l, which has a large decrease, since when the correlation of
covariates increases, it is more difﬁcult for identiﬁcation. Even when ρ = 0.75, the wcqr
estimators with ALASSO behave quite well in simulations.
Figure 2 shows the P1 and P2 performances for the eight methods, and the two values
for cqr estimators are too large to be displayed in the plot. In contrast, wcqr estimators
stably indicate a decrease from 0.1 to about 0.27 and an increase from 0.3 to 0.6. It can
be explained that in low quantiles, few ambiguous cases are used for estimation, which
causes insufﬁcient use of information; whereas in high quantiles, where more ambiguous
observations are weighted, the accuracy of weights will affect the estimation performance.
The improvement of estimation for w0i can be an investigation in the future.
0.1
0.2
0.3
0.4
0.5
0.0
0.5
1.0
1.5
2.0
2.5
P1 and P2 Value
= 0.0
0.1
0.2
0.3
0.4
0.5
0.0
0.5
1.0
1.5
2.0
2.5
P1 and P2 Value
= 0.25
0.1
0.2
0.3
0.4
0.5
0.0
0.5
1.0
1.5
2.0
2.5
P1 and P2 Value
= 0.5
0.1
0.2
0.3
0.4
0.5
0.0
0.5
1.0
1.5
2.0
2.5
P1 and P2 Value
= 0.75
P1:cqr.l
P2:cqr.l
P1:wcqr0.l
P2:wcqr0.l
P1:wcqr1.l
P2:wcqr1.l
P1:wcqr2.l
P2:wcqr2.l
P1:cqr.a
P2:cqr.a
P1:wcqr0.a
P2:wcqr0.a
P1:wcqr1.a
P2:wcqr1.a
P1:wcqr2.a
P2:wcqr2.a
Figure 2. Case n = 200, s = 30, p0 = 0.8, p1 = 0.6. Comparison of P1 and P2 for four levels of ρ. In
each subplot, the Y axis reports the P1 and P2 values at different τ. The solid line is P1 and the dashed
line is P2. Four colors are used to represent the methods: red for cqr, green for wcqr0, blue for wcqr1,
and purple for wcqr2. Light colors represent the LASSO penalty and dark colors are the ALASSO
penalty for all methods.

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
Mathematics 2023, 11, 1295
10 of 23
We also present other simulation results in Figures S1–S11 in the supplementary
material. Figures S1 and S2 show the TPr, FPr, P1, and P2 for s = 20 and 50, respectively.
We can observe that, in Figure S1, the TPr of wcqr estimators with ALASSO are above 0.9
except for very high quantiles, indicating stability with low FPr compared to cqr estimators;
in Figure S2, the tendency remains but the selection performance is inferior, although TPr
still stays higher than 0.8 at τ = 0.4. We also conduct the case when s = 100, n = 100, which
means the number of predictors exceeds the sample size. In this case, cqr estimators fail
due to singular design matrix as well as the ALASSO estimator. We discover, surprisingly,
that our wcqr estimators still work and behave quite well, as illustrated in Figure S3.
Numerical studies for s = 10 and γ0 = (−2, −2.5, 0.5, 0, · · · , 0) are also discussed in the
supplementary material, illustrated by Figures S4–S11. For the structure of the covariance
matrix, we consider another kind of setup: Σ2,ij = ρ|i−j|. We also consider a different choice
for p0 and p1 as 0.6 and 0.45, respectively, in order to test the performance under a different
probability of P(ϵi = 1). In addition, we also simulate the heavy-tailed distributions
t(3) instead of Gaussian distribution for P(T ≤t|ϵ = 1, Z). Figures S4–S7 show that
the ALASSO penalty signiﬁcantly decreases the FP for both estimators, which suggests
the superiority of ALASSO. Our estimators behave fairly close to the cqr estimator in
most cases. Although the TP of our estimators behave slightly worse, the FP shows a
relatively better performance. Not only does wcqr shows smaller deviation about estimated
coefﬁcients, but it also shows great stability, especially for the ALASSO penalty, in the case
of higher quantiles τ = 0.5. This shows the meaningful application of our estimators in
high quantiles. Figure S8 represents the case of n = 400, where the performances of all
criteria are greatly improved.
Figure S9 shows the performance for Σ2, which presents slightly better results than
the case of Σ1. Figure S10 is for a different pair of (p0, p1) = (0.6, 0.45), and our τs ranges
from 0 to 0.4, and τ = 0.3 turns out to be the quantile of 3 nonzero coefﬁcients, which ﬁts
our simulation results. Figure S11 simulates t(3) distribution in place of standard normal
distribution, displaying that our estimators behave signiﬁcantly well for heavy-tailed
distributions.
To conclude, wcqr estimators behaves comparably with the cqr estimator, with slightly
worse performance for TP but better for FP. Interestingly, for the higher correlations and
higher quantiles and heavy-tailed distribution, the superior performance the wcqr estima-
tors display show good potential applicability to more complex data and higher quantiles.
4.2. Real Data Analysis
In this subsection, we use the BMT dataset in [1] for practical application. As the
simulation illustrates, wcqr estimators display more stability to the complexity of data and
high quantiles than existing cqr estimators, which motivates us to conduct the data analysis
with our methods.
In this dataset, a total of 177 patients received a stem cell transplant for acute leukemia.
The failure event is relapse (REL, 56 patients), and death from causes related to the trans-
plant (transplant related mortality, TRM, 75 patients) is the competing risk. Forty-six
patients are censored, thus the censoring rate is 26%. Covariates that affect REL and TRM
includes sex, disease (lymphoblastic or myeloblastic leukemia), phase at transplant (Re-
lapse, CR1, CR2, CR3), source of stem cells (bone marrow and peripheral blood, coded as
BM+PB, or peripheral blood, coded as PB), and age. The link function is assumed to be
exponential.
Figures 3–5 report the numbers of selected variables as well as coefﬁcient estimates by
our weighted estimators compared with penalized quantile estimating equations proposed
by [8] and the penalty-free methods with τ ranging from 0 to 0.4.
From the ﬁgure we can see mainly our estimators select similar numbers of variables to
cqr estimators at lower quantiles, but in higher quantiles, the wcqr estimators lie between
the cqr-LASSO and cqr-ALASSO. For the intercept, in lower quantiles, ﬁve estimators
appears conincident with one another, although cqr-ALASSO estimators tend to be unstable,

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
Mathematics 2023, 11, 1295
11 of 23
whereas wcqr estimators shows stability here. For age, all estimators regard this variable as
unimportant, except that the two LASSO estimators probably overestimate the importance.
For sex:F, almost all estimators shrink the corresponding coefﬁcients to zero. The ALASSO
estimators tend to treat D:AML as an unimportant variable, except for quantiles around 0.1.
For phase:CR1 and phase:CR2, all estimators tend to select them in lower quantiles, but
wcqr tends to select phase:CR1 at higher quantiles larger than 0.21 but neglects phase:CR2
from 0.22 to 0.27. For phase:CR3, all the estimators show analogue performances but
with slight shifts. For source:PB, the wcqr estimators perform more stably than cqr for all
quantiles. The estimations for F1 based on the ﬁve methods are placed in Figure 6.
0.0
0.1
0.2
0.3
0.4
0
1
2
3
4
5
6
7
number of variables  selected by three methods
tau
number of selected variables
cqr.a
cqr.l
wcqr.a
wcqr.l
0.0
0.1
0.2
0.3
0.4
−2
−1
0
1
2
3
4
Estimation of intercept
tau
beta0
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
0.0
0.1
0.2
0.3
0.4
−0.4
−0.2
0.0
0.2
0.4
Estimation of beta_Age
tau
beta_Age
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
Figure 3. Variable selection and estimation results for intercept and βAge. The Y axis reports the
coefﬁcient values at different τ. Various colors of lines represent eight methods.
0.0
0.1
0.2
0.3
0.4
−0.8
−0.6
−0.4
−0.2
0.0
0.2
0.4
Estimation of beta_Sex:F
tau
beta_Sex:F
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
0.0
0.1
0.2
0.3
0.4
−1.0
−0.5
0.0
0.5
1.0
Estimation of beta_D:AML
tau
beta_D:AML
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
0.0
0.1
0.2
0.3
0.4
−1.0
−0.5
0.0
0.5
1.0
1.5
2.0
Estimation of beta_Phase:CR1
tau
beta_Phase:CR1
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
Figure 4. Estimation results for βSex:F, βD:AML, and βPhase:CR1.The Y axis reports the coefﬁcient values
at different τ. Various colors of lines represent eight methods.

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
Mathematics 2023, 11, 1295
12 of 23
0.0
0.1
0.2
0.3
0.4
−1.0
−0.5
0.0
0.5
1.0
1.5
Estimation of beta_Phase:CR2
tau
beta_Phase:CR2
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
0.0
0.1
0.2
0.3
0.4
−1.0
−0.5
0.0
0.5
1.0
1.5
Estimation of beta_Phase:CR3
tau
beta_Phase:CR3
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
0.0
0.1
0.2
0.3
0.4
−1.5
−1.0
−0.5
0.0
0.5
Estimation of beta_Source: PB
tau
beta_Source:PB
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
Figure 5. Estimation results for βPhase:CR2, βPhase:CR3 and βSource:PB .The Y axis reports the coefﬁcient
values at different τ. Various colors of lines represent eight methods.
0
5
10
15
20
0.00
0.05
0.10
0.15
0.20
0.25
0.30
Cumulative Incidence Estimate
t
F1(t)
cqr.a
cqr.l
wcqr.a
wcqr.l
Nonpenalized
Figure 6. Estimation of F1. The Y axis reports the estimated values of F1(t) at different t. Various
colors of lines represent eight methods.
To conclude, our wcqr estimators present stability and keep similar performances to
the results of cqr estimators. More importantly, our weighted estimates provide a relatively
general objective function for researchers to directly use R packages for application.

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
Mathematics 2023, 11, 1295
13 of 23
5. Conclusions
In this paper, we proposed a weighted method for competing risks quantile regression
model to transform the estimating equation to a common weighted objective function and
applied the LASSO and ALASSO penalization for variable selection. We established the
consistency and asymptotic normality for penalty-free estimators as well as the consistency
of variable selection. Monte Carlo simulations were conducted for several scenarios,
presenting good variable selection performance and stability. Finally, a real dataset was
utilized to illustrate the application of our methods, which is comparable with other
methods.
Supplementary Materials: The following supporting information can be downloaded at: https://
www.mdpi.com/article/10.3390/math11061295/s1, Figure S1: Case n = 200, s = 20, p0 = 0.8, p1 =
0.6. Reports of TPr, FPr, P1 and P2 at different τ. Four colors are used to represent the methods:
red for cqr, green for wcqr0, blue for wcqr1 and purple for wcqr2. Light colors represent LASSO
penalty and dark colors for ALASSO penalty. Figure S2: Case n = 200, s = 50, p0 = 0.8, p1 = 0.6.
Reports of TPr, FPr, P1 and P2 at different τ. Four colors are used to represent the methods: red for
cqr, green for wcqr0, blue for wcqr1 and purple for wcqr2. Light colors represent LASSO penalty
and dark colors for ALASSO penalty. Figure S3: Case n = 100, s = 100, p0 = 0.8, p1 = 0.6, Reports
of TPr, FPr, P1 and P2 at different τ. Various colors of line represent eight methods respectively.
Figure S4: Case n = 200, p0 = 0.8, p1 = 0.6. Comparision of TP and FP for four levels of ρ. In
each subplot, the Y axis reports the TP values at different τ. Various colors of line represent eight
methods respectively. Figure S5: Case n = 200, p0 = 0.8, p1 = 0.6, Plots of FP for four levels of
ρ. In each subplot, the Y axis reports the FP values at different τ. Various colors of line represent
eight methods respectively. Figure S6: Plots of P1 for four levels of ρ. In each subplot, the Y axis
reports the P1 values at different τ. Various colors of line represent eight methods respectively.
n = 200, p0 = 0.8, p1 = 0.6. Figure S7: Plots of P2 for four levels of ρ. In each subplot, the Y axis
reports the P2 values at different τ. Various colors of line represent eight methods respectively,
n = 200, p0 = 0.8, p1 = 0.6. Figure S8: Case n = 400, ρ = 0.5, p0 = 0.8, p1 = 0.6. Reports of TP, FP,
P1 and P2 at different τ. Various colors of line represent eight methods respectively. Figure S9: Case
n = 400, ρ = 0.5, p0 = 0.8, p1 = 0.6, Σ2. Reports of TP, FP, P1 and P2 at different τ. Various colors of
line represent eight methods respectively. Figure S10: Case n = 400, ρ = 0.5, p0 = 0.6, p1 = 0.45, Σ1.
Reports of TP, FP, P1 and P2 at different τ. Various colors of line represent eight methods respectively.
Figure S11: Case n = 400, ρ = 0.5, p0 = 0.8, p1 = 0.6, Σ2, t(3). Reports of TP, FP, P1 and P2 at different
τ. Various colors of line represent eight methods respectively.
Author Contributions: Conceptualization, E.L., J.P., M.T. (Manlai Tang), K.Y., W.K.H., X.D. and M.T.
(Maozai Tian); Methodology, E.L.; Software, E.L.; Validation, E.L.; Formal analysis, E.L.; Investigation,
E.L.; Resources, E.L.; Data curation, E.L., J.P., M.T. (Manlai Tang), K.Y., W.K.H., X.D. and M.T. (Maozai
Tian); Writing—original draft, E.L.; Writing—review & editing, E.L., J.P., M.T. (Manlai Tang), K.Y.,
W.K.H., X.D. and M.T. (Maozai Tian); Visualization, E.L.; Supervision, J.P., M.T. (Manlai Tang), K.Y.,
W.K.H. and M.T. (Maozai Tian); Project administration, E.L. All authors have read and agreed to the
published version of the manuscript.
Funding: This research was funded by National Natural Science Funds of China (Grant No. 12101015),
Scientiﬁc Research Foundation of North China University of Technology (No. 110051360002), the
Fundamental Research Funds for Beijing Universities, NCUT (NO.110052971921/007), National
Natural Science Foundation of China (No. 11861042), and the China Statistical Research Project (No.
2020LZ25).
Data Availability Statement: Publicly available datasets were analyzed in this study. These data can
be found here: 10.1038/bmt.2009.359.
Conﬂicts of Interest: The authors declare no conﬂict of interest.
Appendix A. Technical Details of Proofs
To simplify the presentation, we omit τ in such expressions as β(τ).

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
Mathematics 2023, 11, 1295
14 of 23
Since the weights wi depend on F∗
1 , we take wi as wi(F∗
1 ). Additionally, we deﬁne
Mn(β, F∗
1 ) = n−1 ∑n
i=1 mi(β, F∗
1 ) as the subgradient of the weighted quantile objective
function (11), where
mi(β, F∗
1 )
=
Zi{τ −wi(F∗
1 )I(g−1(Xi) ≤Z⊤
i β)}
=
Zi

τ −I{ϵi = 1, Ti ≤Ci, Ci ≤g(Z⊤
i β)}
−I{ϵi = 1, Ti ≤Ci, g−1(Ti) ≤Z⊤
i β, Ci > g(Z⊤
i β)}
−τ −F∗
1 (Ci)
1 −F∗
1 (Ci)
h
I{F∗
1 (Ci) ≤τ, Ci ≤g(Z⊤
i β)}(1 −I{Ti ≤Ci, ϵi = 1})
i
−τ −F∗
1 (Ci)
1 −F∗
1 (Ci) I{ϵi = 2, F∗
1 (Ci|Zi) ≤τ, Ti ≤g(Z⊤
i β), Ci > g(Z⊤
i β)}

Let M(β, F∗
1 ) = E{mn(β, F∗
1 )} = E{Z
 τ −H(g(Z⊤β)) −R(β, F∗
1 ) −J(β, F∗
1 )
}, where
H(t|Z)
=
Z t
−∞F1(u)g0(u)du + (1 −G(t))F1(t|Z),
R(β, F∗
1 )
=
EC|Z
τ −F∗
1 (C)
1 −F∗
1 (C) I{F∗
1 (C) ≤τ, C ≤g(Z⊤β)}(1 −I{T ≤C, ϵ = 1})
=
Z g(Z⊤β)
0
g0(u)I{F∗
1 (u) ≤τ}(1 −F1(u|Z))τ −F∗
1 (u)
1 −F∗
1 (u) du,
J(β, F∗
1 )
=
EC|ZI{ϵ = 2, F∗
1 (C) ≤τ, T ≤g(Z⊤β), C > g(Z⊤β)}τ −F∗
1 (C)
1 −F∗
1 (C)
=
(F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z))
Z ∞
g(Z⊤β) I{F∗
1 (u) ≤τ}τ −F∗
1 (u)
1 −F∗
1 (u) g0(u)du
where g0(u) is the density of censoring variable C conditionally on Z, and F0(t|Z) = P(T ≤
t|Z). It is noteworthy that J(β0, F1) ≡0, and it is easy to derive that M(β0, F1) ≡0.
Lemma A1. Assume assumptions A1–A3, C1–C3 hold. Then
∥ˆF1 −F1∥H
·= sup
t
sup
z
| ˆF1(t|z) −F1(t|z)| = op(n−1/2+r)
(A1)
for every r > 0.
Remark A1. Lemma A1 directly guarantees the consistency of our weight estimation wi( ˆF1) to
wi(F1), which is the w0i in Equation (6).
Proof. By condition C1 and A1 and [17], Ref. [5] has developed that for every r > 0,
supt<ν | ˆG(t) −G(t)| = o(n−1/2+r), a.s. This, coupled with C2, implies that
sup
x
n−1
n
∑
i=1
 I{Xi ≤x}I{δiϵi = 1}
1 −ˆG(Xi)

−n−1
n
∑
i=1
 I{Xi ≤x}I(δiϵi = 1)
1 −G(Xi)
 = o(n−1/2+r), a.s.
(A2)

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
Mathematics 2023, 11, 1295
15 of 23
Simultaneously , for t < ν, 1 −G(t) is uniformly bounded away from 0, thus by
Chebyshev’s inequality, for every r > 0,
P
(
n1/2−r
n−1
n
∑
i=1
 I{Xi ≤x}I(δiϵi = 1)
1 −G(Xi)

−n−1
n
∑
i=1
E
 I{Xi ≤x}I(δiϵi = 1)
1 −G(Xi)
|Zi
 ≥ε
)
≤n−2rVar(I{Xi ≤x}I(δiϵi = 1)|Zi)
ε2
→0, n →∞,
which holds for any x, that is
sup
x,z
n−1
n
∑
i=1
 I{Xi ≤x}I(δiϵi = 1)
1 −G(Xi)

−F1(x|Zi)
 = op(n−1/2+r).
(A3)
Combining Equations (A2) and (A3), we have
sup
x,z
∥ˆF1(x|Z) −F1(x|Z)∥= op(n−1/2+r)
holds uniformly for Z, that is,
∥ˆF1 −F1∥H
·= sup
t
sup
z
| ˆF1(t|z) −F1(t|z)| = op(n−1/2+r).
Lemma A2. For all positive values εn = o(1), we have
sup
∥β−β0∥≤εn,∥F∗
1 −F1∥≤εn
∥Mn(β, F∗
1 ) −M(β, F∗
1 ) −Mn(β0, F1)∥= op(n−1/2)
(A4)
Proof. Let Zij and mij denote the jth coordinates of Zi and mi, respectively. For nota-
tional simplicity, in the following we omit the subscript i in various expressions such as
Zi, Zij, Ti, Ci. Let Kj, j = 1, · · · , 5 be some positive constants. Note that for j = 1, · · · , p,
|mj(β, F∗
1 ) −mj(β′, F∗′
1 )|2 ≤B1 + B2 + B3 + B4,
where
B1
=
Z2
j |I{ϵ = 1, T ≤C, C ≤g(Z⊤β)} −I{ϵ = 1, T ≤C, C ≤g(Z⊤β′)}|
B2
=
Z2
j |I{ϵ = 1, T ≤C, T ≤g(Z⊤β), C > g(Z⊤β)}
−I{ϵ = 1, T ≤C, T ≤g(Z⊤β′), C > g(Z⊤β′)}|
B3
=
Z2
j

τ −F∗
1 (C)
1 −F∗
1 (C)
h
I{F∗
1 (C) ≤τ, C ≤g(Z⊤β)}(1 −I{T ≤C, ϵ = 1})
i
−τ −F∗′
1 (C)
1 −F∗′
1 (C)
h
I{F∗′
1 (C) ≤τ, C ≤g(Z⊤β′)}(1 −I{T ≤C, ϵ = 1})
i
B4
=
Z2
j

τ −F∗
1 (C)
1 −F∗
1 (C) I{ϵ = 2, F∗
1 (C|Z) ≤τ, T ≤g(Z⊤β), C > g(Z⊤β)}
−τ −F∗′
1 (C)
1 −F∗′
1 (C)
I{ϵ = 2, F∗′
1 (C) ≤τ, T ≤g(Z⊤β′), C > g(Z⊤β′)}


````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
Mathematics 2023, 11, 1295
16 of 23
It is easy to verify that
sup
β′:∥β−β′∥≤εn
|I(g(Z⊤β) < C) −I(g(Z⊤β′) < C)|
≤∥Z∥{I(g(Z⊤β) −εn < C) −I(g(Z⊤β) + εn < C)}
or multiplied by a constant, by Assumption C3. Therefore, by Assumptions A1 and A2,
E
 
sup
β′:∥β−β′∥≤εn
B1
!
= E
"
sup
β′:∥β−β′∥≤εn
Z2
j |I{C ≤g(Z⊤β)} −I{C ≤g(Z⊤β′)}|
#
≤E∥Z∥3{G(g(Z⊤β) + εn) −G(g(Z⊤β) −εn)}
≤K1εn.
Following similar arguments, we can show that
E
 
sup
β′:∥β−β′∥≤εn
B2
!
= E
"
sup
β′:∥β−β′∥≤εn
Z2
j I(ϵi = 1)
×|I{T ≤g(Z⊤β), C > g(Z⊤β)} −I{T ≤g(Z⊤β′), C > g(Z⊤β′)}|
i
≤E[∥Z∥3{G(g(Z⊤β) + εn) −G(g(Z⊤β) −εn)}
+∥Z∥3{F1(g(Z⊤β) + εn) −F1(g(Z⊤β) −εn)}]
≤K2εn.
Note that
B3 ≤Z2
j


1 −
1 −τ
1 −F∗
1 (C)

I{F∗
1 (C) ≤τ} −
"
1 −
1 −τ
1 −F∗′
1 (C)
#
I{F∗′
1 (C) ≤τ}

+Z2
j
I{C ≤g(Z⊤β)} −I{C ≤g(Z⊤β′)}

·= B31 + B32.
Similarly to B1, it is easy to verify that E

supβ′:∥β−β′∥≤εn B32

≤K1εn. Then
B31
=
Z2
j I{F∗
1 (C) < τ, F∗′
1 (C) < τ} (1 −τ)[F∗
1 (C) −F∗′
1 (C)]
(1 −F∗
1 (C))(1 −F∗′
1 (C))
+Z2
j I{F∗
1 (C) < τ < F∗′
1 (C)}
1 −τ
1 −F∗
1 (C)
+Z2
j I{F∗′
1 (C) < τ < F∗
1 (C)}
1 −τ
1 −F∗′
1 (C)
≤
Z2
j
F∗
1 (C) −F∗′
1 (C)
(1 −τ)
+Z2
j I{F∗
1 (C) < τ < F∗′
1 (C)} + Z2
j I{F∗′
1 (C) < τ < F∗
1 (C)}.

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
Mathematics 2023, 11, 1295
17 of 23
Since
E


sup
F∗′
1 :∥F∗
1 −F∗′
1 ∥H
I{F∗
1 (C) < τ < F∗′
1 (C)}


≤P{F∗
1 (C) < τ < F∗
1 (C) + εn}
≤G{F∗−1
1
(τ)} −G{F∗−1
1
(τ −τ)} ≤K3εn.
Then by Assumption A1, we have E

supβ′:∥β−β′∥≤εn B31

≤K4εn. Consequently,
E
 
sup
β′:∥β−β′∥≤εn
B3
!
≤K5εn.
Similar arguments to proving B3, by adding and subtracting τ−F∗′
1 (C)
1−F∗′
1 (C) I{ϵ = 2, F∗′
1 (C) ≤
τ, T ≤g(Z⊤β), C > g(Z⊤β)}, yields
B4
≤
Z2
j

τ −F∗
1 (C)
1 −F∗
1 (C) I{F∗
1 (C) ≤τ} −τ −F∗′
1 (C)
1 −F∗′
1 (C)
I{F∗′
1 (C) ≤τ}

+Z2
j
I{T ≤g(Z⊤β′), C > g(Z⊤β′)} −I{T ≤g(Z⊤β), C > g(Z⊤β)}

·=
B41 + B42.
By the proof of B31 and B2, we can easily get that E

supβ′:∥β−β′∥≤εn B41

≤K4εn and
E

supβ′:∥β−β′∥≤εn B42

≤K2εn. Thus E

supβ′:∥β−β′∥≤εn B4

≤K5εn.
Therefore, condition (3.2) of [18] holds with r = 2 and sj = 1/2, and condition (3.3)
is satisﬁed by remark 3(ii) of their paper. Thus, Lemma 2 holds by applying Theorem 3
of [18].
Proof of Theorem 1. Note that F1(t|Z) < τ is equivalent to t < g(Z⊤β0) and F1(g(Z⊤β0))
= τ. Therefore, when plugging in the true β0 and F1 into M, we get
M(β0, F1) = E{Z

τ −H(g(Z⊤β0)) −R(β0, F1) −J(β0, F1)

} = 0.
Because β0 is the solution of M(β, F1) with M(β, F1) being a continuous function of β in a
compact parameter neighborhood B.
Therefore, the consistency of ˆβ is the direct conclusion of Theorem 1 of [18], and we
only need verify conditions (1.1), (1.2), and (1.5’) in their paper, as (1.3) is trivially satisﬁed
and (1.4) follows from Lemma A1.
(1.1) By the subgradient condition of quantile regression [13], there exists a vector v with
coordinates |vi| ≤1 such that
∥Mn( ˆβ, ˆw)∥= n−1∥(Zivi) : i ∈Ξ∥= op(n−1/2)
(A5)
by Assumption A.1, where Ξ denotes a (p + 1)−element subset of {1, 2, · · · , n}.
(1.2) For any ε > 0 and β ∈B,
inf
∥β−β0∥≥ε ∥M(β, F1)∥
=
inf
∥β−β0∥≥ε ∥M(β, F1) −M(β0, F1)∥
≥
inf
∥β−β0∥≥ε ∥E[ZZ⊤(β −β0)]g′(ξ∗){1 −G(g(ξ∗)|Z)} f1(g(ξ∗)|Z)∥,

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
Mathematics 2023, 11, 1295
18 of 23
which is strictly positive under Assumptions A1 and A3. Here ξ∗is some value
between Z⊤β and Z⊤β0.
(1.5’) Let {an} be a sequence of positive numbers approaching zero as n →∞. Note that
E{∥ZiwiI(Xi ≤g(Z⊤
i β))∥2} ≤E(∥Zi∥2) ≤Kz, under Assumption A1. It then follows
from Chebyshev’s inequality that
sup
β∈B,∥F∗
1 −F1∥H≤an
∥Mn(β, F∗
1 ) −M(β, F∗
1 )∥= op(1).
Then the proof of Theorem 1 is complete with the conclusion of Theorem 1 of [18].
Proof of Theorem 2. The asymptotic normality of ˆβ relies on the results of Theorem 2
in [18]. We need to prove conditions (2.1)–(2.4), (2.5’), and (2.6’) in their paper. Conditions
(2.1), (2.4), and (2.5’) hold directly by (A5), Lemma A1, and Lemma A2, respectively.
Note that for any Ci lying above the τth conditional quantile Z⊤
i β0, the quantile ﬁt
will not be affected if we assign the entire weight to either (Zi, Ci) or (Zi, X+∞). Then we
obtain
Γ1(β0, F1)
=
∂M(β, F1)
∂β
β=β0
=
−E[ZZ⊤g′(Z⊤β0){1 −G(g(Z⊤β0)|Z)} f1(g(Z⊤β0)|Z)],
which is continuous at β0 and of full rank under Assumption A3. For all β ∈B , we deﬁne
the functional derivative of M(β, F∗
1 ) at F1 in the direction [F∗
1 −F1] as
Γ2(β, F1)[F∗
1 −F1]
= lim
ε→0
1
ε [M{β, F1 + ε(F∗
1 −F1)} −M{β, F1}]
= lim
ε→0
1
ε E[R(β, F1) −R(β, F1ε) + J(β, F1) −J(β, F1ε)]
where F1ε = F1 + ε(F∗
1 −F1). Since
lim
ε→0
1
ε EZ[R(β, F1) −R(β, F1ε)]
= EZ[A1(β) + A2(β)] +
(1 −τ)EZ
Z g(Z⊤β)
0
g0(u)I{F1(u|Z) ≤τ} F∗
1 (u|Z) −F1(u|Z)
1 −F1(u|Z)
du
where
A1(β)
=
lim
ε→0
1
ε
Z g(Z⊤β)
0
g0(u)(1 −F1(u))[I{F1(u|Z) ≤τ} −I{F1ε(u|Z) ≤τ}du]
A2(β)
=
lim
ε→0
1
ε
Z g(Z⊤β)
0
g0(u)(1 −F1(u))(1 −τ) I{F1ε(u|Z) ≤τ} −I{F1(u|Z) ≤τ}
1 −F1ε(u|Z)
du.
Similarly , we can derive
lim
ε→0
1
ε EZ[J(β, F1) −J(β, F1ε)]
= EZ[A3(β) + A4(β)] + (1 −τ)EZ[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)]
×
Z ∞
g(Z⊤β) g0(u)I{F1(u|Z) ≤τ} F∗
1 (u|Z) −F1(u|Z)
(1 −F1(u|Z))2
du

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Mathematics 2023, 11, 1295
19 of 23
where
A3(β)
=
[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)] lim
ε→0
1
ε
Z ∞
g(Z⊤β) g0(u)
I{F1(u|Z) ≤τ} −I{F1ε(u|Z) ≤τ}du
A4(β)
=
[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)](1 −τ)
lim
ε→0
1
ε
Z ∞
g(Z⊤β) g0(u) I{F1ε(u|Z) ≤τ} −I{F1(u|Z) ≤τ}
1 −F1ε(u|Z)
du.
For β such that g(Z⊤β) < g(Z⊤β0), A1(β) = 0, A2(β) = 0. For sufﬁciently small ε,
F−1
1ε (τ) > g(Z⊤β), then
A3(β)
=
[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)] lim
ε→0
1
ε
n
G(g(Z⊤β0)) −G(F−1
1ε (τ|Z))
o
A4(β)
=
(1 −τ)[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)] lim
ε→0
1
ε
n
˜G(F−1
1ε (τ|Z)) −˜G(g(Z⊤β0|Z))
o
where d ˜G(u|Z)
du
=
g0(u)
1−F1(u|Z).
For β such that g(Z⊤β) > g(Z⊤β0), A3(β) = 0, A4(β) = 0. For sufﬁciently small ε,
F−1
1ε (τ) < g(Z⊤β), then
A1(β)
=
lim
ε→0
1
ε
n
˘G(g(Z⊤β0|Z)) −˘G(F−1
1ε (τ|Z))
o
where d ˘G(u|Z)
du
= g0(u)(1 −F1(u|Z)) and
A2(β)
=
(1 −τ) lim
ε→0
1
ε
n
G(F−1
1ε (τ|Z)) −G(g(Z⊤β0))
o
.
For β = β0, note that I{F0(t|Z) < τ} = 1 for t ∈(0, g(Z⊤β)), then
A1(β)
=
lim
ε→0
1
ε
n
˘G(g(Z⊤β0|Z)) −˘G(F−1
1ε (τ|Z))
o
A2(β)
=
(1 −τ) lim
ε→0
1
ε
n
G(F−1
1ε (τ|Z)) −G(g(Z⊤β0))
o
and I{F0(t|Z) < τ} = 0 for t ∈(g(Z⊤β), ∞), then
A3(β)
=
[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)] lim
ε→0
1
ε
n
G(g(Z⊤β0)) −G(F−1
1ε (τ|Z))
o
A4(β)
=
(1 −τ)[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)]
· lim
ε→0
1
ε
n
˜G(F−1
1ε (τ|Z)) −˜G(g(Z⊤β0|Z))
o
.
By expanding ˜G(F−1
1ε (τ|Z)) (treated as a function of ε) around ε = 0, and using the
fact that d
dε F−1
1ε (τ|Z)|ε=0 = τ−F∗
1 (g(Z⊤β0))
f1(g(Z⊤β0))
(example 20.5 in [19]), we obtain
G(F−1
1ε (τ|Z)) = G(g(Z⊤β0)) + g0(g(Z⊤β0))τ −F∗
1 (g(Z⊤β0))
f1(g(Z⊤β0))
ε + O(ε2).

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
Mathematics 2023, 11, 1295
20 of 23
Similarly, we have
˘G(F−1
1ε (τ|Z))
=
˘G(g(Z⊤β0)) + g0(g(Z⊤β0))(1 −F1(g(Z⊤β0)))
·τ −F∗
1 (g(Z⊤β0))
f1(g(Z⊤β0))
ε + O(ε2).
˜G(F−1
1ε (τ|Z))
=
˜G(g(Z⊤β0)) +
g0(g(Z⊤β0))
1 −F1(g(Z⊤β0))
·τ −F∗
1 (g(Z⊤β0))
f1(g(Z⊤β0))
ε + O(ε2).
Therefore, for β such that g(Z⊤β) < g(Z⊤β0),
A3(β) + A4(β)
=
−[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)]g0(g(Z⊤β0))
τ −F∗
1 (g(Z⊤β0))
f1(g(Z⊤β0))
F1(g(Z⊤β0)) −τ
1 −F1(g(Z⊤β0)) ≡0
for β such that g(Z⊤β) ≥g(Z⊤β0),
A1(β) + A2(β)
=
g0(g(Z⊤β0))(F1(g(Z⊤β0)) −τ)τ −F∗
1 (g(Z⊤β0))
f1(g(Z⊤β0))
≡0.
That is
Γ2(β0, F1)[F∗
1 −F1]
= (1 −τ)EZ
Z g(Z⊤β)
0
g0(u)I{F1(u|Z) ≤τ} F∗
1 (u|Z) −F1(u|Z)
1 −F1(u|Z)
du
+(1 −τ)EZ[F0(g(Z⊤β)|Z) −F1(g(Z⊤β)|Z)]
×
Z ∞
g(Z⊤β) g0(u)I{F1(u|Z) ≤τ} F∗
1 (u|Z) −F1(u|Z)
(1 −F1(u|Z))2
du.
(A6)
With the process of Taylor expansion, we can verify condition (2.3) of [18] under
Assumptions A1 and A2.
Then, we verify condition (2.6). Combining (A6) and the analysis above, we have
Γ2(β0, F1)[ ˆF1 −F1]
=
(1 −τ)EZ
Z g(Z⊤β0)
0
g0(u)
ˆF1(u|Z) −F1(u|Z)
1 −F1(u|Z)
du
(A7)
Denote FG
1 (t|Z) = 1
n ∑n
i=1
I{Xi≤t,δiϵi=1}
1−G(Xi)
, NG
i (t) = I(Xi ≤t, δiϵi = 0), Yi(t) = I(Xi ≥
t), y(t) = P(X ≥t), λG(t) = lim∆→0 P(X ∈(t, t + ∆)|X ≥t), ΛG(t) = R t
0 λG(s)ds and
MG
i (t) = NG
i −R ∞
0 Yi(s)dΛG(s). Follow the proof in [5], supt∈[0,ν) ∥n1/2{ ˆG(t) −G(t) −
n−1/2 ∑n
i=1 G(t) R t
0 y(s)−1dMG
i }∥→0, from [17], and n−1 ∑n
i=1 Yi(t)I{Xi ≤x}I(δiϵi =
1)(1 −G(Xi))−1 converges to π(x, t) uniformly in both x ∈R and t ∈[0, ν), where
π(x, t) = EYi(t)I{Xi ≤x}I(δiϵi = 1)(1 −G(Xi))−1. Then

````

## PDF page 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
Mathematics 2023, 11, 1295
21 of 23
ˆF1(x|Z) −F1(x|Z) = FG
1 (x|Z) −F1(x|Z) + ˆF1(x|Z) −FG
1 (x|Z)
=
1
n
n
∑
i=1
ξ1,i(x) −1
n
n
∑
i=1
ˆG(Xi) −G(Xi)
ˆG(Xi)G(Xi)
I(Xi ≤x)I(δiϵi = 1)
≈
1
n
n
∑
i=1
ξ1,i(x) −1
n
n
∑
i=1
n−1 ∑n
j=1 Yi(s)y(s)−1dMG
j
G(Xi)
I(Xi ≤x)I(δiϵi = 1)
=
1
n
n
∑
i=1
ξ1,i(x) −1
n
n
∑
i=1
Z ∞
0
 
n
∑
j=1
Yj(s)I(Xj ≤x)I(δjϵj = 1)
nG(Xj)
!
dMG
i (s)
y(s)
≈
1
n
n
∑
i=1
ξ1,i(x) −1
n
n
∑
i=1
Z ∞
0
π(x, s)dMG
i (s)
y(s)
=
1
n
n
∑
i=1
{ξ1,i(x) −ξ2,i(x)},
where ≈denotes asymptotic equivalence uniformly in τ ∈[τL, τU], ξ1,i(x) = I(Xi ≤
x)I(δiϵi = 1)G(Xi)−1 −F1(x|Z) and ξ2,i = R ∞
0 π(x, s)y(s)−1dMG
i (s), i = 1, . . . , n. Similarly
derived as [5], R ∞
0 π(x, s)y(s)−1dMG
i is Lipshitz in x, ˆF1(x|Z) −F1(x|Z) converges weakly
to a mean zero Guassian process with covariance matrix Σ(x) = E{ξ1(x)′ξ1(x)}. Then
by (A7),
Γ2(β0, F1)[ ˆF1 −F1]
≈
(1 −τ)n−1
n
∑
i=1
Ez
"
Z
Z g(Z⊤β0)
0
g0(u)ξ1,i(u) −ξ2,i(u)
1 −F1(u|Z)
du
#
=
(1 −τ)n−1
n
∑
i=1
φi
(A8)
where
φi = EzZ
Z g(Z⊤β0)
0
g0(u)ξ1,i(u) −ξ2,i(u)
1 −F1(u|Z)
du
(A9)
is a random vector with mean 0 and E∥φi∥2 < ∞by Assumptions A1–A3.
Recall Mn(β0, F1) = n−1 ∑n
i=1 mi(β0, F1) being independent mean 0 random vectors.
mi(β0, F1)
=
Zi

τ −I{ϵi = 1, Ti ≤Ci, Ci ≤g(Z⊤
i β0)}
−I{ϵi = 1, Ti ≤Ci, g−1(Ti) ≤Z⊤
i β0, Ci > g(Z⊤
i β0)}
−τ −F1(Ci)
1 −F1(Ci)
h
I{F1(Ci) ≤τ, Ci ≤g(Z⊤
i β0)}(1 −I{Ti ≤Ci, ϵi = 1})
i
·=
Zi(τ −D1 −D2 −D3).
Since Emi(β0, F1) = 0, and DiDj = 0 for i̸ = j, it is easy to verify
Cov{mi(β0, F1)}
= EZ,CE

ZiZ⊤
i

τ(1 −τ)I(Ci > g(Z⊤
i β0)) + I(Ci ≤g(Z⊤
i β0)) F1(Ci)(1 −τ)2
1 −F1(Ci)

·= d1.
Then applying the central limit theorem gives
n1/2{Mn(β0, F1) + Γ2(β0, F1)[ ˆF1 −F1]} D→N(0, V),

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
Mathematics 2023, 11, 1295
22 of 23
where
V
=
Cov{mi(β0, F1) + (1 −τ)φi} ·= d1 + d2 + d2
d1
=
(1 −τ)E{mi(β0, F1)φ⊤}
d2
=
(1 −τ)2E{φ⊤φ}
Then the proof for (14) is thus complete by Theorem 2 of [18].
Proof of Theorem 3. Let ˆAn = {j : ˜βj̸ = 0}. We ﬁrst show that for any j̸ = A, P(j ∈
ˆAn) →0 as n →∞. Suppose there exists a k ∈ˆAc such that | ˜βk|̸ = 0. Let β∗be a vector
constructed by replacing ˜βk with 0 in ˜β. For simplicity, we write ˆwi = wi( ˆF1). Note that
|ρτ(a) −ρτ(b)| ≤|a −b| max{τ, 1 −τ} < |a −b|. Therefore, for large enough n,
Qp( ˜β, ˆwi) −Qp(β∗, ˆwi)
=
n
∑
i=1
ˆwi
n
ρτ(g−1(Xi) −Z⊤
i ˜β) −ρτ(g−1(Xi) −Z⊤
i β∗)
o
+
n
∑
i=1
(1 −ˆwi)
n
ρτ(g−1(X+∞) −Z⊤
i ˜β) −ρτ(g−1(X+∞) −Z⊤
i β∗)
o
+ pλn(| ˜βk|)
≥−2
n
∑
i=1
∥Zi∥· | ˆβk| + λn| ˆβk|−γ| ˜βk|.
By Theorem 1, ˆβk −βk = Op(n−1/2) and βk, thus ˆβk = Op(n−1/2). As ∑n
i=1 ∥Zi∥=
Op(1) and n−1λn| ˆβk|−γ ≥nr/γ−1λn →∞, which yields
Qp( ˜β, ˆwi) −Qp(β∗, ˆwi) ≥−2
n
∑
i=1
∥Zi∥· | ˆβk| + λn| ˆβk|−γ| ˜βk|
≥| ˜βk|n
h
−Op(1) + n−1λn| ˆβk|−γi
≥c∗nγ/2−1/2λn > 0, as
n →∞,
(A10)
where c∗is any positive constant. This contradicts the fact that Qp( ˜β, ˆwi) ≤Qp(β∗, ˆwi).
We next show that for any j ∈A, P(j /∈ˆAn) →0. We write bA = (bj, j ∈A) for any
vector b ∈Rp, and BAA as the sub-matrix of a (p + 1) × (p + 1) matrix B with both row
and column indices in A. By Taylor expansion
Mn(βA, F∗
1 )
=
Mn(β0A, F1) + Γ1AA(βA −β0A)
+Γ2AA(β0A, F1)[F∗
1 −F1] + op(n−1/2)
(A11)
uniformly over βA, F1 such that ∥βA −β0A∥= O(n−1/2) and ∥F∗
1 −F1∥H = o(n−1/2+r).
Let βA −β0A = n−1/2u , we have
nu⊤Mn(βA, ˆF1)
=
nu⊤{Mn(β0A, F1) + Γ2AA}
+n1/2u⊤Γ1AAu + op(n1/2)
(A12)
where Γ2AA = Γ2AA(β0A, F1)[ ˆF1 −F1]. Therefore, with probability tending to 1,
−nu⊤Mn(βA, ˆF1)
≥
−nu⊤{Mn(β0A, F1) + Γ2} −n1/2u⊤Γ1AAu + o(n1/2)
≥
k0n1/2+r
(A13)
for some positive k0 and r > 0. However, the subgradient condition (A5) requires that
∥nu⊤Mn(βA, ˆF1)∥+ λn ∑
j∈A
| ˆβj|−r|τ −I( ˜βj < 0)| ≤Op(max
i
∥Zi∥).
(A14)

````

## PDF page 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
Mathematics 2023, 11, 1295
23 of 23
When λn = o(n1/2) and Assumption A1 holds, (A13) and (A14) suggest that the
subgradient condition cannot hold if ∥˜βA −β0A∥= Kn−1/2 for some positive K. Using the
monotonicity argument in [20] , we can show that the subgradient condition also cannot
hold if ∥˜βA −β0A∥> Kn−1/2. Therefore, ∥˜βA −β0A∥≤Kn−1/2 with probability tending
to 1. Equivalently speaking, for all j ∈A, P(j ∈ˆAn) →1 or P(j /∈ˆAn) →0. The proof of
Theorem 3 is thus complete.
References
1.
Scrucca, L.; Santucci, A.; Aversa, F. Regression modeling of competing risk using R: An in depth guide for clinicians. Bone Marrow
Transpl. 2010, 45, 1388–1395. [CrossRef] [PubMed]
2.
Fine, J.P. ; Gray, R.J. A proportional hazards model for the subdistribution of a competing risk. J. Am. Stat. Assoc. 1999, 94,
496–509. [CrossRef]
3.
Fu, Z.; Parikh, C.R.; Zhou, B.J. Penalized variable selection in competing risks regression. Lifetime Data Anal. 2017, 23, 353–376.
[CrossRef] [PubMed]
4.
Koenker, R.W.; Bassett, G. Regression quantile. Econometrica 1978, 46, 33–50. [CrossRef]
5.
Peng, L.; Fine, J.P. Competing risks quantile regression. J. Am. Stat. Assoc. 2009, 104, 1440–1453. [CrossRef]
6.
Sun, Y.Q.; Wang, H.; Gilbert, P. Quantile regression for competing risks data with missing cause of failure. Stat. Sin. 2012, 22,
703–728. [CrossRef] [PubMed]
7.
Ahn, K.W.; Kim, S. Variable selection with group structure in competing risks quantile regression. Stat. Med. 2018, 37, 1577–1586.
[CrossRef] [PubMed]
8.
Li, E.; Tian, M.; Tang, M. Variable selection in competing risks models based on quantile regression. Stat. Med. 2019, 38, 4670–4685.
[CrossRef] [PubMed]
9.
Wang, H.J. ; Wang, L. Locally weighted censored quantile regression. J. Am. Stat. Assoc. 2009, 104, 1117–1128. [CrossRef]
10.
Tibshirani, R. Regression shrinkage and selection via the lasso. J. R. Stat. Soc. B. 1996, 58, 267–288. [CrossRef]
11.
Zou, H. The adaptive lasso and its oracle properties. J. Am. Stat. Assoc. 2006, 101, 121–152. [CrossRef]
12.
Gray, R.J. A class of k-sample tests for comparing the cumulative incidence of a competing risk. Ann. Stat. 1988, 16, 1141–1154.
[CrossRef]
13.
Koenker, R. Quantile Regression; Cambridge University Press: New York, NY, USA, 2005.
14.
Wang, H.J.; Zhou, J.; Li, Y. Variable selection for censored quantile regresion. Stat. Sin. 2013, 23, 145–167. [PubMed]
15.
Robins, J.M. ; Rotnitzky, A. Recovery of information and adjustment for dependent censoring using surrogate markers. In AIDS
Epidemiology Theorethodological Issues; Jewell, N., Dietz, K., Farewell, V., Eds.; Birkhäuser: Boston, MA, USA, 1992; pp. 24–33.
16.
Kaplan, E.L.; Meier, P. Nonparametric estimation from incomplete observations nonparametric estimation from incomplete
observations. J. Am. Stat. Assoc. 1958, 53, 457–481. [CrossRef]
17.
Pepe, M.S. Inference for Events With Dependent Risks in Multiple Endpoint Studies. J. Am. Stat. Assoc. 1991, 86, 770–778.
[CrossRef]
18.
Chen, X.; Linton, O.; Van Keilegom, I. Estimation of semiparametric models when the criterion function is not smooth. Econometrica
2003, 71, 1591–1608. [CrossRef]
19.
van der Vaart, A.W. Asymptotic Statistics; Cambridge University Press: Cambridge, UK, 1998.
20.
Jureckova, J. Asymptotic relations of m-estimates and r-estimates in linear regression. Ann. Statist. 1977, 5, 464–472. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

````

