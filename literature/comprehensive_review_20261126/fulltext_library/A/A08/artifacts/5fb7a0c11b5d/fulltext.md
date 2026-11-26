# Multi-stage optimal dynamic treatment regimes for survival outcomes with dependent censoring

Original PDF: [original.pdf](original.pdf). SHA256: `5fb7a0c11b5d1ac2840bc8173d57c8b3e2046959b97ff53deac3574035821795`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
arXiv:2012.03294v2  [stat.ME]  12 May 2022
Multi-stage optimal dynamic treatment regimes
for survival outcomes with dependent censoring
Hunyong Cho*, Shannon T. Holloway†, David J. Couper‡,
and Michael R. Kosorok§
May 13, 2022
Abstract
We propose a reinforcement learning method for estimating an optimal dy-
namic treatment regime for survival outcomes with dependent censoring. The es-
timator allows the failure time to be conditionally independent of censoring and
dependent on the treatment decision times, supports a ﬂexible number of treat-
ment arms and treatment stages, and can maximize either the mean survival time
or the survival probability at a certain time point. The estimator is constructed
using generalized random survival forests and can have polynomial rates of con-
vergence. Simulations and data analysis results suggest that the new estimator
brings higher expected outcomes than existing methods in various settings. An R
package dtrSurv is available on CRAN.
Keywords: Precision medicine; Dynamic treatment regime; Survival analysis; Rein-
forcement learning; Random forest; Conditionally independent censoring; Empirical
process.
1
Introduction
Multi-stage treatments are becoming more prevalent in medicine. Chronic conditions
such as cancer, auto-immune disease, HIV, and heart disease, often require multiple
treatments over a long period. Cancer patients may receive multiple rounds of chemo-
and/or biological therapies (Habermann et al., 2006; Huang et al., 2020). Auto-immune
disease patients might receive additional treatments in response to relapses (Edwards &
Cambridge, 2006; Hogan & Radhakrishnan, 2013). Traditionally such chronic diseases
have been treated following a one-size-ﬁts-most approach by which the standard of care
*Department of Biostatistics, University of North Carolina at Chapel Hill, hunycho@live.unc.edu
†Department of Statistics, North Carolina State University
‡Collaborative Studies Coordinating Center, Department of Biostatistics, University of North Carolina at Chapel Hill,
david couper@live.unc.edu
§ Department of Biostatistics, Department of Statistics and Operations Research, University of North Carolina at Chapel
Hill
1

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
is selected as the treatment or treatment plan that will likely beneﬁt most patients with
a similar condition, i.e., the treatment that is optimal only in the sense of the marginal
effects.
However in recent years, a more personalized approach to the treatment of chronic
diseases has become of interest. Dynamic treatment regimes formalize a data-driven
approach to treatment by optimizing the overall outcome of interest and providing treat-
ment suggestions that are based on the patient’s information available at each point of
the decision making process (Murphy, 2003; Kosorok & Moodie, 2015; Kosorok &
Laber, 2019; Tsiatis et al., 2019). In part because they utilize all available information,
such optimized dynamic treatment regimes are often found to be more beneﬁcial than
a traditional set of ﬁxed treatment plans (Kidwell, 2015). Further, because optimal
dynamic treatment regimes focus on the overall or long-term outcome, they are more
advantageous than applying multiple single-stage treatment rules that only optimize
the stage-level outcomes.
Finding an optimal dynamic treatment regime is a reinforcement learning problem
(Sutton & Barto, 2018), wherein an action by an agent, or a physician, changes both
the immediate reward and the environment of the next stage and the learner, or the
statistician, searches for the rule of actions that brings the most overall reward. Rein-
forcement learning problems are often solved using the Q-learning algorithm (Watkins,
1989; Zhu et al., 2015; Zhao et al., 2011; Zhang et al., 2017; Qian & Murphy, 2011),
which deﬁnes the value as the expected cumulative sum of discounted rewards and
optimizes the set of rules using backward recursion.
There are some challenges in using Q-learning in biomedical research that involves
survival outcomes. As the failure time is often censored, any approach should take
into account the missing information, for example, using redistribution of the failure
probability as in the Kaplan-Meier (Efron, 1967; Robertson & Uppuluri, 1984) or in-
verse probability weighting (Robins et al., 1994; Robins & Rotnitzky, 1992; Wahed
& Tsiatis, 2006; Orellana et al., 2010). Furthermore, in multi-stage contexts, patients
may not be able to make all the planned visits due to failure or dropping out of the
study, making the total number of treatments received to vary among patients. Without
addressing these missing information issues, backward recursion in Q-learning is not
readily applicable.
Another signiﬁcant challenge posed in survival analysis is that the treatment timing
may not be ﬁxed, may even depend on a patient’s status or previous treatment history,
and could have association with the failure time. In such scenarios, the three events,
failure, proceeding to the next treatment, and censoring, may have mutual associations,
and they compete so that only the earliest event is observed. For example, a cancer pa-
tient whose physical condition has improved has a longer expected survival time and, at
the same time, may want to take another round of chemotherapy earlier than expected.
However, the full joint distribution of those events is not identiﬁable without knowl-
edge of their dependence structure (Tsiatis, 1975). Thus, the dependency between the
events needs to be carefully addressed.
Several methods regarding the estimation of dynamic treatment regimes for survival
outcomes have been proposed in the literature. Goldberg & Kosorok (2012) ﬁrst devel-
oped a dynamic treatment regime estimator for survival outcomes using a Q-learning
framework. To address the problems introduced by a different number of treatments
2

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
as well as by censoring, the authors proposed modifying the survival data so that each
observation has the same number of treatment stages without missing values and using
a standard Q-learning framework along with inverse probability weighting to account
for censoring. However, censoring was assumed to be completely independent of all
covariates and event times. The estimated Q-function and the resulting decision rules
would be thus subject to bias for data with dependent censoring.
Huang et al. (2014) addressed a similar problem using backward recursion. Their
motivating problem was a recurrent disease clinical trial where patients receive an ini-
tial treatment followed by a salvage treatment if patients experience either treatment
resistance or relapse. Simoneau et al. (2019) extended the dynamic treatment regime
estimator for non-censored outcomes via weighted least squares (Wallace & Moodie,
2015) into the censored time-to-event data setting. Both of these methods use a linear
accelerated failure time model, which carries a risk of model misspeciﬁcation and re-
sults in a restrictive policy class. Thus, a more ﬂexible model is needed to allow for
more relaxed distributional assumptions. Wahed & Thall (2013) proposed a dynamic
treatment regime estimator using full speciﬁcation of the likelihood and Xu et al. (2016)
developed a Bayesian alternative, where the disease progression dynamic was modeled
using a dependent Dirichlet process prior with a Gaussian process measure. However,
their policy classes are ﬁnite-dimensional and, thus, may not be able to consider diverse
patient characteristics and contexts sufﬁciently.
Each of the existing methods described above has its limitations. First, not all
methods allow for a ﬂexible number of treatment stages and/or treatment levels. For
example, the methods in Wahed & Thall (2013) and Huang et al. (2014) were designed
for a two-stage decision problem, and the Simoneau et al. (2019) approach is restricted
to binary treatments. Second, the outcomes of interest in most methods are limited
to the mean survival time. Jiang et al. (2017) proposed an optimal dynamic treatment
regime estimator that maximizes the t-time survival probability. However, none of the
methods permit choosing the criterion except Wahed & Thall (2013). Third, strong
structural assumptions are employed for all of these methods, with the exception of
Goldberg & Kosorok (2012). Assumptions, such as the accelerated failure time model
or the proportional hazards models used by the existing methods, are subject to model-
misspeciﬁcation, may limit the policy class, and, consequently, may invoke loss in the
value of the optimal policy. Finally, the censoring assumption of Goldberg & Kosorok
(2012) is restrictive. Censoring is associated with failure time in many medical ap-
plications, although it is often reasonable to assume independence of censoring after
conditioning on patient historical information. See Table 1 for a summary of those
methods and assumptions.
In this manuscript, we develop a general dynamic treatment regime estimator for
censored time-to-failure outcomes that addresses all of the limitations discussed for
the existing estimators. Our estimator maximizes either the mean survival time or the
survival probability at a certain time using backward recursion. As the objective may
not be expressed as the sum of intermediate rewards, a standard Q-learning algorithm
is not applicable. Instead, the conditional survival probability information, rather than
the summarized Q-values, is appended to the previous stage information. A general-
ized random survival forest is developed for this task, where survival curves for each
individual, instead of just observed survival or censoring time, is fed into the random
3

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
method
K
|Ak|
criterion
T
C
{π}
the new method
ﬁnite
ﬁnite
E[T ∧τ], S(t0)
NP
CI
ﬂexible
Goldberg & Kosorok (2012)
ﬁnite
ﬁnite
E[T ∧τ]
NP
independent
ﬂexible
Huang et al. (2014)
2+
2+
E[T ]
AFT
CI
linear
Jiang et al. (2017)
ﬁnite
2
S(t)
PH
CI
linear
Simoneau et al. (2019)
ﬁnite
2
E[T ]
AFT
CI
linear
Wahed & Thall (2013)
ﬁnite
ﬁnite
E[T ], S(t0)
AFT
CI
ﬁxed
Xu et al. (2016)
ﬁnite
ﬁnite
E[T ]
BNP
CI
ﬁxed
Table 1: Assumptions of the existing and the proposed methods. K, the number of
stages; |Ak|, the number of treatment arms at stage k; criterion, the target value to
be optimized; T , failure time model; C, censoring assumption; {π}, policy class; 2+,
can be generalized to more than two; NP, non-parametric; AFT, accelerated failure
time; PH, proportional hazards; BNP, Bayesian non-parametric; CI, conditional inde-
pendence; ﬁxed, a ﬁxed number of distinct treatment rules.
survival forest. A general implementation of our method is available on CRAN, R
package dtrSurv.
The key contributions of our work are the ﬂexibility of the proposed method and the
exposition of its theoretical properties. The target value can be either the mean survival
time or the survival probability at a certain time. The method allows for a ﬂexible
number of treatment stages as well as a ﬂexible number of treatment arms at each stage.
Censoring can be conditionally independent. The conditional survival probability is
modeled nonparametrically using a random survival forest-based algorithm. We further
show the consistency of the random survival forests and the estimated regime values as
well as their rates of convergence.
The remainder of the manuscript is organized as follows. In Section 2, we give
notation and describe the dynamic treatment rule estimators. Theoretical properties
of the estimators are derived in Section 3, and their performance is illustrated through
simulations in Section 4. Section 5 is devoted to the application of the proposed method
to a cardiovascular disease cohort study and a two-stage leukemia clinical trial. We
conclude the paper by discussing future research directions in Section 6.
2
The method
2.1
Data setup and notation
We assume that each of n independent patients can have a maximum of K visits, or
treatment stages, with a study length τ > 0. At the kth stage, k = 1, 2, ..., K, the
ith patient, among the nk ≤n available patients, receives treatment Ak,i ∈Ak, if
he or she has survived and has not dropped out by the beginning of the stage, where
Ak is the ﬁnite treatment space for the kth stage. Throughout this manuscript, we
often drop the subject index i when it does not cause confusion. Our interest lies in
estimating the survival distribution Sπ of the overall failure time T of patients if they
followed a dynamic treatment regime π = (π1, π2, ...πK)⊤and then ﬁnding the ‘best’
rule π∗, which optimizes a certain criterion φ. An (optimal) dynamic treatment regime
is a series of stage-wise policies πk that map historical information hk ∈Hk to a
4

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Figure 1: An examples of two patients with different censoring statuses after their third
visit.
(best) treatment ak ∈Ak. For φ, we consider φµ(S) = −R
t>0(t ∧τ)dS(t) and
φσ,t0(S) = S(t0) for some 0 < t0 ≤τ. Without loss of generality, we assume that a
prolonged time to event is preferred; thus the objective is to maximize φ(S) over the
regimes.
We observe the time to next treatment Uk,i of the ith patient which is a random or
ﬁxed quantity that depends on the historical information Hk,i ∈Hk available at the
beginning of the kth stage and the treatment assignment Ak,i. At the kth stage, we
observe either the ith patient’s failure, advancement to next treatment, or censoring.
The times from the beginning of the stage to each of these events are denoted as Tk,i,
Uk,i, and Ck,i, respectively. The length of the stage Xk,i for the ith patient is deﬁned by
the minimum of these times, and the hypothetically uncensored stage length is deﬁned
as Vk,i = Tk,i ∧Uk,i. For the last stage, VK,i = TK,i. We denote the kth stage
censoring and treatment indicators as δk,i = 1(Vk,i ≤Ck,i) and γk,i = 1(Tk,i ≤Uk,i),
respectively. When Ck,i < Vk,i, γk,i is not observable. The baseline time at stage k
is deﬁned as Bk,i = Pk−1
j=1 Xj,i, k > 1, and B1,i = 0. Let Ti, Ci, Xi = Ti ∧Ci,
and δi = 1(Ti ≤Ci) denote the overall failure time, overall censoring time, overall
observed time, and overall censoring indicator, respectively. We denote Zk,i ∈Zk
as the covariate information of the ith patient that is newly available at the beginning
of the kth stage. Thus, Hk,i may include historical information such as Ak′,i, Bk′,i,
Zk′,i, k′ = 1, 2, ..., k −1 and Zk,i; where dk denotes the dimension of Hk,i for
k = 1, 2, .., K. The number nk of patients eligible for treatment assignment at the
beginning of stage k is Pn
i=1 1(Uk,i ≤Tk,i ∧Ck,i). See Figure 1 for an illustration.
The notation is summarized in Table S1 of the Supplementary Material.
2.2
Overview of the method
As is the case in Q-learning, our estimator optimizes the intermediate stage decision
assuming that all the later decisions are optimal, and thus backward recursion is used.
5

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
Our method is based on the observation that the remaining life Lk at stage k is deﬁned
recursively as a convolution of Lk+1 and the uncensored current stage length Vk and
that
Sk(t | Hk, Ak, δk = 1) =
Z
Sk+1(t −Vk | Hk+1, Ak+1, δk = 1)
dP(Vk, Hk+1, Ak+1 | Hk, Ak, δk = 1),
(1)
where Sk(t | ·) = 1 for all t < 0, and Sk(t | γk−1 = 1) = 1(t < 0), for k = K −
1, K −2, ..., 1. Under the covariate-conditionally independent censoring assumption,
the contribution of the censored cases is incorporated into the equation by redistributing
the probability to the right (Efron, 1967):
Sk(t | Hk, Ak) =
Z 
δkSk+1(t −Xk | Hk+1, Ak+1)
+ (1 −δk)
n
1(Xk > t) + 1(Xk ≤t) Sk+1(t | Hk+1, Ak+1)
Sk+1(Xk | Hk+1, Ak+1)
o
× dP(Xk, Hk+1, Ak+1, δk | Hk, Ak).
(2)
This is the key formula we rely on in optimizing the distribution of Lk. This convolu-
tion makes it unnecessary to estimate the joint distribution of Uk and Tk. Throughout
this manuscript we assume that Lk is independent of Ck conditionally on Hk and Ak,
k = 1, 2, ..., K.
Assuming the standard causal inference assumptions, which we will formally intro-
duce in Subsection 3.2 (Assumption 9–11), we can translate Sk(t | Hk, Ak = a) into
the counterfactual quantity Sa
k(t | Hk). Thus, the regime is estimated using the fol-
lowing procedure: 1. estimating the conditional survival distribution Sk(t | Hk, Ak)
of the remaining life Lk for k = K; 2. optimizing the survival distribution over Ak to
have ˆπk and ˆS∗
k(t | Hk) ≡ˆSk(t | Hk, Ak = ˆπk(Hk)) for k = K; 3. augmenting the
estimated optimal curves by the previous stage lengths, i.e., ˆS∗
k(t −Xk−1 | Hk, Ak)
for k = K; and, 4. repeating steps 1–3 for k = K −1, K −2, ..., 1. A high-level
summary is provided in Algorithm 1, and we describe the regime estimation procedure
more in detail next.
Algorithm 1. the proposed dynamic treatment regime estimator.
Result: A dynamic treatment regime estimate ˆπ = (ˆπ1, ˆπ2, ..., ˆπK)⊤
for stage k = K, K −1, ..., 1 do
Input:
n
Hk, Ak, δk, ( ˆS∗
k+1(· −Xk | Hk+1)
onk
i=1 for k < K and
{(Hk, Ak, δk, Vk)}nk
i=1 for k = K
;
Obtain ˆSk(· | Hk, Ak) via generalized random survival forest (Algorithm S1);
Obtain ˆπk(h) = arg maxa∈Ak φk
n
ˆSk(· | Hk = h, Ak = a)
o
;
Deﬁne ˆS∗
k(· | Hk) = ˆSk(· | Hk, Ak = ˆπk(Hk));
6

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
At the beginning of the last stage, there are nK patients who have neither experi-
enced failure nor been censored. The data for these patients are used to estimate the
terminal stage covariate-conditional survival probability SK(· | HK, AK) for each
treatment arm using random survival forests. Then the optimal regime for the ﬁnal
stage is estimated by ˆπK = arg maxa∈AK φK
n
ˆSK(·, a)
o
, where ˆSk is the estimate of
Sk and φk is deﬁned adaptively for the intermediate and terminal survival probabilities,
k = 1, .., K. Speciﬁcally, φµ
k
n
Sk(· | Hk)
o
= Bk −
R
t>Xk(t ∧τ)dSk(t | Hk) and
φσ,t0
k
n
Sk(· | Hk)
o
= Sk(t0 −Bk | Hk). In Proposition C of the Supplementary Ma-
terial, we show that backward recursion is legitimate for the choices of φ = φµ, φσ,t0.
The optimized survival information of the ﬁnal stage, ˆS∗
K, is carried back to the pre-
vious stage; the ith patient with a stage length XK−1,i is given a probabilistic augmen-
tation so that the resulting survival probability of remaining life LˆπK
K−1 at the second to
the last stage is ˆS∗
K(t−XK−1,i | HK,i). The probabilistic augmentation can be thought
of drawing single (B = 1) or many (B > 1) LK−1,i,(b)’s from ˆS∗
K(t−XK−1,i | HK,i)
for subject i so that {LK−1,i,(b) : b = 1, 2, ..., B} is obtained with an equal weight 1
B .
For those who have already experienced failure or censoring by the end of the stage,
no augmentation is required.
Next, the conditional distribution of the remaining life from the beginning of the
(K −1)st stage is estimated by the random survival forests based on the nK−1 patients.
Then estimation of Sk, πk, and S∗
k is recursively performed until we reach the ﬁrst stage
and obtain ˆπ = (ˆπ1, ˆπ2, ..., ˆπK)⊤.
For the intermediate stages (k < K), however, unlike the last stage, the patients’ re-
maining life Lk is not observed as a single value but is given in the form of a stochastic
process, or a set of random draws per person. For this speciﬁc type of data, we develop
a generalized random survival forest that implements this analytically without random
draws. See Section B of the Supplementary Material for further details. We also note
that having single draws LK,i,(b) per person, in fact, is sufﬁcient to derive the rate of
convergence, and the random forest estimation ˆSk,(b) that uses single draws could be
easily done using off-the-shelf software. However, since estimation based on multiple
draws ˆSk is usually favorable in terms of precision, we use ˆSk for data analyses.
One consideration for the φσ,t0 criterion is that the choice of φ may not be practical
for patients who already survived t0, since treatment decision becomes irrelevant for
them with such a criterion. Thus a composite criterion, φσ,t0,µ(S) = {S(t0), E[T ∧τ]},
of ﬁrstly maximizing S(t0) until time t0 and secondly maximizing E[T ∧τ] afterward
is suggested in practice, where the values are evaluated lexicographically.
3
Theoretical properties
We show consistency and rates of convergence of the generalized random survival
forests and the proposed dynamic treatment regime estimator ˆπ. The consistency of
a regime is established in terms of its value, which will be deﬁned in Subsection 3.2.
As consistency and the rate of convergence are developed using different theoretical
approaches, we give two different sets of assumptions.
7

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
3.1
Convergence properties of generalized random survival forests
We have assumptions regarding the tree-based estimator terminal node size and split-
ting rules. The ﬁrst assumption forces the terminal node size to be both sufﬁciently
large absolutely and sufﬁciently small relative to the sample size.
Assumption 1 (Terminal node size). The minimum size nmin of the terminal nodes
grows at the following rate: nmin ≍nβ, 1
2 < β < 1, where a ≍b implies both
a = O(b) and b = O(a).
Next, we give deﬁnitions of regular trees and random split trees that are often used
for consistency proofs in the random forest literature (Meinshausen (2006), Wager &
Walther (2015), Cui et al. (2017), Wager & Athey (2018)).
Deﬁnition 1 (Random-split and α-regular trees and forests). A tree is called a random-
split tree if each feature is given a minimum probability (ϕ/d) of being the split variable
at each intermediate node, where 0 < ϕ < 1 and d is the dimension of the feature
space. A tree is α-regular, if every daughter node has at least α fraction of the training
sample in the corresponding parent node. A random forest is called a random-split
(α-regular) forest, if each of its member trees is random-split (α-regular).
Assumption 2 (α-regular and random split trees). Trees are α-regular and random-
split with a constant 0 < ϕ < 1.
Assumption 3 (Lipschitz continuous and bounded survival and censoring probability).
There exist constants LS and LG such that |Sk(t | h1) −Sk(t | h2)| ≤LS∥h1 −h2∥
and |Gk(t | h1) −Gk(t | h2)| ≤LG∥h1 −h2∥for all h1, h2 ∈Hk, t ∈[0, τ −Bk],
and k = 1, 2, ..., K, where Gk is the censoring survival distribution at the kth stage,
and Sk(τ −−Bk|hk)Gk(τ −−Bk|hk) > c1 for all hk with γk−1 = 0—i.e., patients
who made visit k—and some constant c1 > 0.
Assumption 4 (Weakly dependent historical information at each stage). The patient
history information Hk at stage k is given as a dk-dimensional vector lying in a subset
Hk of [0, 1]dk, and its joint (fHk) and marginal (fHk,j) densities are bounded so that
ζ−1 ≤fHk(h) ≤ζ and ζ−1 ≤fHk,j(hj) ≤ζ for all h ∈Hk and hj ∈Hk,j for
some constant ζ ≥1 and j = 1, 2, ..., dk except that there may exist a ﬁnite number of
hj ∈Hk,j along each coordinate j.
Assumption 4 allows non-hyperrectangular or categorical history spaces. For ex-
ample, the baseline survival times, (B1 ≤B2 ≤B3 ≤...), have hypertriangular-
shaped support, and the treatment history could be categorical.
Assumption 5 (Terminal stage sample size). There exists a constant c2 ∈(0, 1) and
an integer N such that, for all n ≥N, nK ≥c2n almost surely.
Assumption 5 enables the use of large sample theory for all intermediate and termi-
nal stages. One such example in the dynamic treatment regime setting is the existence
of constants M1, M2 ∈(0, 1) and subsets Nk ⊂Hk such that pr(Hk ∈Nk) <
M1, pr(Uk < Tk ∧Ck | hk) = 0 for all hk ∈Nk but pr(Uk < Tk ∧Ck | hk) > M2
for all hk̸ ∈Nk for all k < K.
8

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
In the following theorem, we establish a uniform consistency of the generalized
random survival forests, which are constructed using the estimates of the next-stage
survival probability ( ˆSk+1). This theorem considers a setting where the current stage
treatment (Ak) could be a part of history (Hk), and no optimization over treatment is
yet made. The proof is provided in Section D of the Supplementary Material.
Theorem 1 (Uniform consistency of a generalized random survival forest). Suppose
Assumptions 1–5 hold. Let ˆSk+1 be an estimator of the next-stage survival probability
Sk+1 that is uniformly consistent in both h ∈Hk and t ∈[0, τ], for stage k. Then, the
generalized random survival forest ˆSk(t | h) built based on
n Hk,i, δk,i, ˆSk+1(· −Xk
| Hk+1,i)
onk
i=1 is uniformly consistent. Speciﬁcally, for each k = 1, 2, ..., K,
sup
t∈[0,τ],hk∈Hk
| ˆSk(t | hk) −Sk(t | hk)| →0,
in probability as n →∞.
We now provide non-asymptotic tail bounds for ˆSk,(b), or the stage k random sur-
vival forest estimator constructed using a single random draw per subject {(Lk,i,(b), δk,i) :
Lk,i,(b) ∼ˆSk+1(t −Xk|Hk+1), i = 1, ..., nk}. We leave it as future work to de-
rive the uniform rate of convergence result for the generalized random survival forests
( ˆSk(t|h; Sk+1)), or random forests based on multiple or inﬁnitely many draws per sub-
ject. However, since the asymptotic variance of ˆSk can be shown to be smaller than or
equal to that of ˆSk,(b), ˆSk is believed to have at least the same rate of uniform conver-
gence.
To derive a uniform rate of convergence for the survival curves, we assume a differ-
ent set of assumptions than those used in Theorem 1. We will have a stratiﬁed random
split assumption—which will be deﬁned soon and is a stronger condition than Assump-
tion 2—and a terminal node size assumption that is more relaxed than Assumption 1.
We also assume a stronger assumption on the covariate distribution—continuous his-
tory spaces on unit hypercubes—which could be reﬁned, but we leave it as future work.
Deﬁnition 2. A tree is called a ‘stratiﬁed random split tree,’ if for each terminal node
made of s splits, the number of splits on each variable is greater than or equal to ⌊s
dϕ⌋,
where d is the number of covariates, ϕ > 0 is ﬁxed, and ⌊a⌋is the greatest integer less
than or equal to a.
One way to achieve the stratiﬁed random splitting is to make splits only among the
candidate variables that have not attained the required budget, or ⌊s
dϕ⌋splits, at every
other r intermediate nodes, where r ≥1.
Assumption 6 (Stratiﬁed random split trees). Trees are constructed under stratiﬁed
random splitting with a ﬁxed constant 0 < ϕ < 1.
Assumption 7 (Terminal node size 2). The minimum size nmin of the terminal nodes
grows satisfying the following rate: limn→∞
log n log log n
nmin
= 0.
9

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
Assumption 8 (Weakly dependent historical information at each stage 2). The patient
history information Hk at stage k is given as a dk-dimensional vector lying in Hk =
[0, 1]dk with its density bounded so that ζ−1 ≤fHk(h) ≤ζ for all h ∈Hk for some
constant ζ ≥1.
Now we state Theorem 2. The proof is provided in the Supplementary Material.
Theorem 2 (Non-asymptotic bounds for ˆSk,(b)). Suppose Assumptions 3 and 8 hold.
Let a single-draw-per-person random survival forest ˆSk,(b) be built under Assumptions
2, 6, and 7 for each stage k = K, K −1, ..., 1. Then, for each k, there exists an n0
such that for all n > n0 the following holds with probability ≥1 −2(K−k+1)
√n
:
sup
t≤τ,hk
| ˆSk,(b)(t; hk) −Sk(t; hk)| ≤rn,
(3)
where rn is precisely deﬁned in Section E of the Supplementary Material and has the
same rate as r′
n = max
(q
log(n){log(nmin)+log log(n)}
nmin
,
  nmin
n
 log((1−α)−1)
log(α−1)
0.991ϕ
maxl dl
)
.
3.2
Convergence properties of the dynamic treatment regime esti-
mator
We give convergence properties of the dynamic treatment regime estimator using the
causal inference framework. With this framework, the theoretical properties are appli-
cable to broader settings than sequentially randomized experiments. A counterfactual
outcome is deﬁned as an outcome that would have been obtained if a person had a
treatment option contrary to his/her actual treatment. To denote the counterfactual out-
comes pertaining to a counterfactual treatment or treatment policy, we add a superscript
to the corresponding random variables or survival functions. For example, Sπ
k (t|Hk)
is a counterfactual survival probability of the remaining life if treatment was given to a
person with history Hk according to a treatment rule π from stage k to K. We assume
the following three standard causal inference assumptions (Hern´an & Robins, 2020;
Rubin, 2005; Cole & Frangakis, 2009).
Assumption 9 (Stable unit treatment value assumption, or SUTVA). Each person’s
counterfactual dynamics, such as failure time, time to next treatment, and censoring,
are not affected by the treatments or history of other patients. Moreover, each treatment
has only one version, or if there are multiple versions, their differences are irrelevant.
Assumption 10 (Sequential ignorability). Treatment assignment is given independently
of the counterfactual outcomes, conditionally on the individual’s historical informa-
tion, where the outcomes include all future random quantities such as failure time, time
to next treatment, and censoring time.
Assumption 11 (Positivity). For each stage k = 1, 2, ..., K, given historical informa-
tion, the probability of having each treatment a ∈Ak is greater than a constant L > 0.
Or, pr(Ak = a|Hk = h) > L for all a ∈Ak, h such that pr(Hk = h) > 0.
10

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
The following theorem states that the dynamic treatment regime estimator has a
value consistent for the value of the optimal regime. We deﬁne the value V of a treat-
ment regime π as the criterion value of the survival probability if all individuals in a
population follow the treatment regime. We use V(π) = φ(Sπ) to denote the value of
π, and V inherits the superscript of φ.
Theorem 3 (Consistency of the dynamic treatment regime estimator). Let ˆπ denote
the optimal dynamic treatment regime estimator that is built following Algorithm 1 and
Assumptions 1–2. Assume that, for each stage, the generalized random forests are built
either at once with Ak ⊂Hk (“pooled forests”) or for each treatment arm (“separate
forests”). Further, assume Assumptions 3–5, and 9–11. Then, for each φ = φµ, φσ,t0,
|V(π) −V(ˆπ)| →0,
in probability as n →∞.
Now we present Theorem 4, a rate of convergence result. Proofs of both theorems
and a subsequent corollary are given in Section F of the Supplementary Material.
Theorem 4 (Rate of convergenceof the dynamic treatment regime estimator). Suppose
Assumptions 3, 8, and 9–11 hold. Let the single-draw-per-subject random survival
forest ˆSk,(b) in Theorem 1 now be built under Assumptions 2,6–7 for each treatment
a ∈Ak and each stage k = 1, 2..., K to build ˆπ. Then, for each φ = φµ, φσ,t0, the
following is true in probability as n →∞:
V(π) −V(ˆπ) = OP (√rn).
Corollary 1 (Polynomial rate of convergence). Assume the same conditions as in The-
orem 4. Then, nmin can be chosen so that, for some η > 0,
V(π) −V(ˆπ) = OP (n−η/2).
(4)
4
Simulations
We perform simulations to study the performance of the proposed method and compare
those results to that of existing methods. The overall scheme of the simulations follows
the pattern in Goldberg & Kosorok (2012), where they mimicked a cancer clinical trial
using the tumor size and wellness dynamics. We adapt their data generating mechanism
so that dependence among censoring, tumor size, and wellness is incorporated in the
mechanism, and deterministic processes are relaxed into more realistic ones.
In the hypothetical trial, patients can go through up to K = 3 treatment rounds
during the trial with length of the trial, τ = 10. Each patient has tumor size ρ(t) and
wellness ω(t) at time t ∈[0, 10] that affect the timing of failure or treatment. For each
stage, patients are given either a more aggressive (A = 1) or a less aggressive (A = 0)
treatment.
11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
Scenario 1
Scenario 2
Scenario 3
Scenario 4
(base)
(small p)
(large p)
(moderate censoring)
p
5
2
10
5
βF (1)
(0, −3, 2, 2, 1, −1, −1)⊤
(0, −2, 2, 0)⊤
(0, −2, 2⊤
4 , −1⊤
4 , −2⊤
2 )
(0, −3, 2, 2, 1, −1, −1)⊤
βF (0)
(0, −1, 1, 1, 1, 1, 1)⊤
(0, −1, 1, 1)⊤
(0, −1, 1⊤
4 , 1⊤
4 , 0⊤
2 )
(0, −1, 1, 1, 1, 1, 1)⊤
βC(1)
(−3, .2, .2⊤
3 , −.2⊤
2 )⊤
(−3, .2, .2, −.2)⊤
(−3, .2, .2⊤
4 , −.2⊤
3 , 0⊤
3 )⊤
(−2, .2, .2⊤
3 , −.2⊤
2 )⊤
βC(0)
(−3, .1, .2⊤
3 , .2⊤
2 )⊤
(−3, .1, .2, .2)⊤
(−3, .1, .2⊤
4 , .2⊤
3 , 0⊤
3 )⊤
(−2, .1, .2⊤
3 , .2⊤
2 )⊤
Table 2: The failure time and censoring hazard coefﬁcients and dimensions of covari-
ates in Scenarios 1 to 4. βF (·) and βC(·), the log hazard ratios of the counterfactual
failure and censoring times, respectively.
The patient failure time and censoring time are governed by the respective hazard
processes:
λF (c) = 1
5
(
ρ(u)
ω(u)eg(Hk)⊤βF (Ak) + 1

ω(u) < 0.1
)
,
(5)
λC(u) = eg(Hk)⊤βC(Ak),
where the tumor size (ρ) and wellness (ω) follow the Ornstein-Uhlenbeck process,
g(Hk) = {1, log(Bk + 1), Zk
⊤}⊤, βF (a) and βC(a) are the hazard ratios for the
failure and censoring time given treatment a (Table 4), and the baseline covariates at
the kth stage follow a p−variate normal distribution conditioning on the previous stage
value. The treatment is allocated according to a Bernoulli trial with propensity
π(Hk) =
n
1 + exp(−g(Hk)⊤βπ)
o−1
,
(6)
where the coefﬁcient is βπ = (−1, 1, −1
21⊤
p )⊤for the observational data setting and
βπ = 0p+2 for the randomized trial setting. See Section G of the Supplementary
Material for a detailed description of the dynamics.
Simulations are run with two sample sizes, n = 300 and 1000. For each simula-
tion setting, we have nrep = 200 simulation replicates, and we estimate the optimal
treatment rule based on both the φµ and φσ,t0=5,µ criteria. We compare the proposed
method with the methods in Goldberg & Kosorok (2012) and Simoneau et al. (2019).
We further compare the results with the observed policy characterized by (6) and the
estimated optimal zero-order model, where all patients are given the same embedded
treatment regime, which is the best on average over all embedded regimes. In partic-
ular, in implementing the Goldberg & Kosorok (2012) method, the linear Q-function
space and the random forest-based approximation space were separately used. The val-
ues of the estimated regimes are evaluated by generating an uncensored sample of size
neval = 10000 according to the estimated policies.
Figure 2 LEFT shows how the truncated mean survival time (φµ) of each esti-
mated policy behaves under different settings. For most of the settings, on average, all
estimated regimes have greater values than the zero-order model, and the zero-order
model has a higher value than the observed policy. This implies that the standard of
care improves the overall survival time of patients over the observed policies and that
individualized treatment rules can further enhance the outcomes.
12

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
6.28
5.84 5.91 5.73 5.76
4.52
6.45
5.96
6
5.99 5.97
5.3
5.69
5.25
5.81 5.79
5.15
3.13
6.25
5.87 5.92 5.83 5.74
4.52
6.44
5.94 5.93 6.2
5.76
4.52
6.51
5.95 6.01 6.2 5.97
5.3
6.02
5.38
5.98
6.33
5.2
3.13
6.42
5.98 5.91 6.03
5.76
4.52
6.33
5.87 5.94 6.17
5.4
4.54
6.43
5.96 6.04 6.16
5.51
4.98
6.2
5.31
5.79
6.26
4.78
3.92
6.27
5.9 5.93 5.93
5.3
4.54
6.5
5.96 5.96
6.4
5.66
4.54
6.5
5.96 6.05
6.38
5.53
4.98
6.45
5.43
5.87
6.64
4.82
3.92
6.47
6
5.96
6.33
5.63
4.54
observational
n=300
observational
n = 1000
RCT
n=300
RCT
n = 1000
moderate censoring rate
 d = 5
moderate censoring rate
 d = 2
moderate censoring rate
 d = 10
high censoring rate
 d = 5
A
B
C
D
E
F
A
B
C
D
E
F
A
B
C
D
E
F
A
B
C
D
E
F
3
4
5
6
3
4
5
6
3
4
5
6
3
4
5
6
method
Truncated mean survival time
0.57
0.53 0.54 0.52 0.53
0.4
0.58
0.53 0.54 0.54 0.53
0.47
0.52 0.5
0.54 0.53
0.49
0.27
0.57
0.54 0.54 0.54 0.52
0.4
0.59
0.54 0.54
0.57
0.53
0.4
0.59
0.53 0.54 0.56
0.53
0.47
0.55
0.5
0.56
0.59
0.49
0.27
0.59
0.54 0.54 0.56
0.53
0.4
0.58
0.53 0.54
0.57
0.48
0.4
0.58
0.53 0.54 0.56
0.47
0.44
0.57
0.5
0.54
0.59
0.45
0.34
0.57
0.54 0.54 0.55
0.47
0.4
0.6
0.54 0.54
0.59
0.51
0.4
0.59
0.53 0.54
0.58
0.48
0.44
0.61
0.51
0.55
0.63
0.45
0.34
0.6
0.54 0.54
0.59
0.5
0.4
observational
n=300
observational
n = 1000
RCT
n=300
RCT
n = 1000
moderate censoring rate
 d = 5
moderate censoring rate
 d = 2
moderate censoring rate
 d = 10
high censoring rate
 d = 5
A
B
C
D
E
F
A
B
C
D
E
F
A
B
C
D
E
F
A
B
C
D
E
F
0.2
0.3
0.4
0.5
0.6
0.2
0.3
0.4
0.5
0.6
0.2
0.3
0.4
0.5
0.6
0.2
0.3
0.4
0.5
0.6
method
Survival probability at t = 5
method
A: the proposed method
B: Goldberg & Kosorok (2012), RF
C: Goldberg & Kosorok (2012), linear
D: Simoneau et al. (2019)
E: zero−order model
F: observed policy
Figure 2: The estimated mean truncated survival time (LEFT) and the estimated sur-
vival probability at time t = 5 (RIGHT) under each estimated policy. Each dot rep-
resents one simulation replicate. The box plots are the quartile summary of the points
and the black dots are the average values of each method. Each row of boxes represents
a data generation scenarios, and each column of boxes represents a combination of a
study design and a sample size.
Figure 2 LEFT also shows that among the individualized treatment rules, the pro-
posed method outperforms the other methods in many settings. Even when the method
exhibits lower or about the same performance as the other methods for the small sample
size, it often has higher performance than the others for the larger sample size. See, for
example, the high censoring cases (the last row) of either the observational or the RCT
setting. In the settings where the dimension of the covariate is high (the third row), the
method of Simoneau et al. (2019) often has high values.This might be because of the
doubly robustness property of the method and the fact that the true optimal decision
rule might be close to a linear function, as suggested by the linear interaction of the
stage-wide hazard functions in (5). The method of Simoneau et al. (2019), however,
often does not provide estimates when either the sample size of the terminal stage is
small due to censoring or failure or the dimension of covariates is large.
Figure 2 RIGHT shows the simulation results in terms of the survival probability at
t0 = 5, or φσ,5. Note that the estimated regimes for the proposed method are distinct
between LEFT and RIGHT but are the same for the other methods. The proposed
estimator shows better performance in terms of the policy values under most settings,
giving us similar interpretations as the previous results.
The computational complexity for estimating a dynamic treatment regime is O(n2 log(n)
PK
k=1 |Ak||Hk|). Using the R package dtrSurv, the estimation of a three-stage
regime in these simulations takes less than several (20) seconds for n = 300 (n =
1000).
13

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
5
Data examples—The Atherosclerosis Risk in Com-
munities (ARIC) Study
We illustrate the use of dynamic treatment regimes using two biomedical studies—
the Atherosclerosis Risk in Communities (ARIC) Study and a study of acute myeloid
leukemia. The latter analysis is provided in Section H·2 of the Supplementary Material.
We derive an optimal dynamic treatment regime for cardiovascular failure events
using the ARIC Study. ARIC is a community-based observational cohort study where a
total of 15,792 individuals aged 45–64 had been recruited at four centers in U.S. (Wash-
ington County, MD; Forsyth County, NC; Jackson, MS; and Minneapolis, MN) in
1987–1989 (Wright et al., 2021). The data are available on approval of the ARIC Data
Coordinating Center (https://sites.cscc.unc.edu/aric/distribution-agreements).
The main goal of ARIC is to identify cardiovascular risk factors. Each participant was
examined for their medical, social, behavioral, and demographic information up to
seven times until 2019. We analyze the most recent data with enough number of sur-
vival events—the ﬁfth visit (n = 6527, in 2011–2013) and the sixth visit (n = 3996,
in 2016–2017). The seventh visit (n = 3853, in 2018–2019) was not included due to a
small number of observed events.
Out of the 6,527 subjects who made at least ﬁve visits, we further narrowed down
the focus to those who already had or had had heart diseases or heart failure (n = 945)
at their baseline visit. The age range of this high-risk group is 66–90 years at the
beginning of their ﬁfth visit, and among them, 69% were White, 53% were female,
15.1% and 11.4% had experienced prevalent heart failure and coronary heart diseases at
their ﬁrst visit, respectively, and 41% died of circulatory diseases until τ = 2700 days
from the ﬁfth visit. We regard deaths due to other causes as censored. Administrative
censoring includes those who survived 2700 days. Of those who made visits 5 and
6, 31% and 57% were censored, respectively. Besides the cause-speciﬁc mortality,
we also derive all-cause mortality-based dynamic treatment regimes—i.e., other cause
deaths are also regarded as failure—and the resulting censoring rates are 12.6% and
50% for the two visits.
The ARIC study followed participant use of Statin (HMG CoA reductase inhibitors)
and anti-coagulants, which have been shown to be effective in reducing cardiovascular
diseases and mortality (Mills et al., 2008; Johansen et al., 2014; Schneeweiss et al.,
2012). These medications, however, may not be as effective and can even be detrimen-
tal for some patients. For example, long-term use of anti-coagulants could increase
the risk of cardiovascular calciﬁcations (Schurgers et al., 2004). Statin, although it has
been considered safe for most patients, still has side effects such as type II diabetes and
has interactions with multiple medications (Thompson et al., 2016; Ramkumar et al.,
2016). Thus, a personalized dynamic strategy for prescribing these medications could
enhance long-term survival outcomes, especially for those who had experienced heart
disease or failure.
We develop two-stage optimal dynamic treatment regimes for prescribing a Statin
and anti-coagulant combination. We follow the 80-20 cross-validation scheme for the
value function estimation described in Section H·1 of the Supplementary Material.
The numbers of patients in each treatment arm are 279 (none), 492 (Statin), 60 (anti-
14

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
coagulant), and 114 (both) at visit 5, and the corresponding numbers for visit 6 are
110, 230, 38, and 68. The tailoring variables include gender, race, age, number of
years on cigarette, the baseline prevalent heart failure history, the baseline coronary
heart disease history, and heart failure history at visit 5. Also, for each of visits 5 and
6, BMI, waist-to-hip ratio, alcohol consumption, hypertension, blood glucose level,
smoking status, blood HDL cholesterol level, and Aspirin use are included. For visit 6,
the past-visit medication history (i.e., visit 5 medications) is included. We assume that
the four-level treatment classiﬁcation satisﬁes Assumption 9, and also that the effects
of the unmeasured confounders are negligible. Missing values were imputed by the
multivariate imputation with chained equations (Van Buuren & Groothuis-Oudshoorn,
2011). With a small fraction of missing values—less than 3% for several variables
and less than 1% or none for most—we present the results based on the ﬁrst imputed
dataset. Because the Simoneau et al. (2019) method was implemented using R package
DTRreg the current version (1.7) of which allows binary treatment arms only, the
method was applied for ﬁnding the optimal anti-coagulant regime instead. Also, as
the method suffers from unstable estimation issue with high-dimensional covariates, a
subset of the mentioned covariates were considered for the method. More details of
the model for the Simoneau et al. (2019) method are described in Section H·1 of the
Supplementary Material.
Figure 3 illustrates the cross-validation-based value estimates of each estimator.
The proposed method provides the largest average survival time and six-year (2200
days) survival probability than other methods for both optimization criteria (φµ, φσ,2200)
and event types (cardiovascular, all-cause). The zero-order model recommends Statin
for visit 5 and both for visit 6 for most of the cross-validation replicates. On the other
hand, the proposed method has various prescription options for different subjects. The
higher values of the suggested method over the zero-order model values highlight the
beneﬁt of individualized treatment rules. The higher performance of the suggested
method over the other competing methods is likely attributed to the model misspeciﬁ-
cation issues in other methods, such as linearity and independent censoring.
6
Discussion
In this paper, we introduced a new dynamic treatment regime estimator for survival
outcomes. The estimator is versatile in the sense that it allows for a ﬂexible number
of treatment stages and arms, it gives a non-linear decision rule that maximizes either
the mean survival time or the survival probability, and it permits dependent censoring.
In this section, we discuss some considerations when using our method and how the
method can be further extended.
The proposed estimator assumes that the distribution is well characterized by the
treatment stages rather than the natural passage of time. That is, the cohort at each
treatment stage might include patients that received the stage treatment on day 10 as
well as patients that received the stage treatment on day 1000. Thus, this method is ef-
fective when the disease dynamic is considered stationary between stage transitions or
when the treatment effect contains a relatively stronger signal than that of the baseline
disease dynamics.
15

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
2573.574
2550.846
2509.168
2529.544
2560.703
2567.229
2200
2300
2400
2500
2600
2700
the proposed method
Goldberg & Kosorok (2012), linear
zero−order model
Goldberg & Kosorok (2012), RF
Simoneau et al. (2019)
observed
Truncated mean survival time
0.909
0.895
0.868
0.878
0.901
0.906
0.6
0.7
0.8
0.9
1.0
the proposed method
Goldberg & Kosorok (2012), linear
zero−order model
Goldberg & Kosorok (2012), RF
Simoneau et al. (2019)
observed
Six year survival probability
2440.185
2434.832
2324.246
2335.149
2411.036
2436.963
2000
2200
2400
2600
the proposed method
Goldberg & Kosorok (2012), linear
zero−order model
Goldberg & Kosorok (2012), RF
Simoneau et al. (2019)
observed
Truncated mean survival time
0.815
0.813
0.726
0.746
0.802
0.814
0.5
0.6
0.7
0.8
0.9
the proposed method
Goldberg & Kosorok (2012), linear
zero−order model
Goldberg & Kosorok (2012), RF
Simoneau et al. (2019)
observed
Six year survival probability
Figure 3: Estimated truncated mean survival time (LEFT) and estimated six-year sur-
vival probability (RIGHT) of the dynamic treatment regime estimators for preventing
the cardiovascular-speciﬁc (TOP) and all-cause (BOTTOM) mortality. Each dot rep-
resents one cross-validation replicate. The black square dots are the average values of
each method.
The proposed method assumes an unrestricted policy class. In practice, however,
clinicians and patients may prefer understandable, simple rules. A linear rule, for ex-
ample, is often of interest. By posing a Cox-type proportional hazards assumption on
top of our method, the resulting policy class becomes a set of linear classiﬁers. The
task then reduces to replacing the generalized random survival forest with the gener-
alized Cox model, which essentially does a Cox regression based on multiple random
draws.
In this paper, treatment timing (Uk) was not given as a policy variable but as a
part of history for the next stage. Recently, Nie et al. (2021) worked on ﬁnding op-
timal treatment regimes that provide the best treatment timing. Finding a timing for
optimizing the overall survival probability is interesting future work.
Another interesting extension of the proposed method is optimizing a speciﬁc quan-
tile of the survival distribution, such as the median survival time. However, this task
introduces a unique challenge with respect to the backward recursion. Speciﬁcally,
the optimal decisions made for later stages may not be optimal once earlier decisions
moderate the distribution. Thus, an exhaustive search may be needed to ﬁnd an opti-
mal policy. An extension of the quantile-optimal dynamic treatment regime estimators
developed by Wang et al. (2018) and Linn et al. (2017) to right-censored data would be
interesting future work.
Acknowledgement
This research was funded in part by grant P01 CA142538 from the National Cancer In-
stitute. The authors thank Donglin Zeng for bringing the composite criterion optimiza-
tion into the discussion and the editors and anonymous reviewers for their constructive
16

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
feedback. The ARIC study has been funded in whole or in part with Federal funds
from the National Heart, Lung, and Blood Institute, National Institutes of Health, De-
partment of Health and Human Services, under Contract nos. (HHSN268201700001I,
HHSN268201700002I,HHSN268201700003I,HHSN268201700004I,HHSN268201700005I).
The authors thank the staff and participants of the ARIC study for their important con-
tributions. The authors also thank Peter F. Thall, Abdus S. Wahed, and Yanxun Xu for
providing the leukemia study data.
Supplementary material
Supplementary Material available online includes the summary of notation in Section
A, more details about the generalized random survival forests in Section B, the proofs
of the theorems in Sections C–F, and more details about the simulations and data ex-
amples in Sections G–H.
References
COLE, S. R. & FRANGAKIS, C. E. (2009). The consistency statement in causal infer-
ence: a deﬁnition or an assumption? Epidemiology 20, 3–5.
CUI, Y., ZHU, R., ZHOU, M. & KOSOROK, M. (2017). Consistency of survival tree
and forest models: splitting bias and correction. arXiv preprint arXiv:1707.09631 .
EDWARDS, J. C. & CAMBRIDGE, G. (2006). B-cell targeting in rheumatoid arthritis
and other autoimmune diseases. Nature Reviews Immunology 6, 394–403.
EFRON, B. (1967). The two sample problem with censored data. In Proceedings of
the ﬁfth Berkeley symposium on mathematical statistics and probability, vol. 4.
GOLDBERG, Y. & KOSOROK, M. R. (2012). Q-learning with censored data. Annals
of statistics 40, 529.
HABERMANN, T. M., WELLER, E. A., MORRISON, V. A., GASCOYNE, R. D., CAS-
SILETH, P. A., COHN, J. B., DAKHIL, S. R., WODA, B., FISHER, R. I., PETER-
SON, B. A. et al. (2006). Rituximab-chop versus chop alone or with maintenance
rituximab in older patients with diffuse large b-cell lymphoma. Journal of clinical
oncology 24, 3121–3127.
HERN ´AN, M. A. & ROBINS, J. M. (2020). Causal inference: What if.
HOGAN, J. & RADHAKRISHNAN, J. (2013). The treatment of minimal change disease
in adults. Journal of the American Society of Nephrology 24, 702–711.
HUANG, H.-J., YANG, L.-Y., TUNG, H.-J., KU, F.-C., WU, R.-C., TANG, Y.-H.,
CHANG, W.-Y., JUNG, S.-M., WANG, C.-C., LIN, C.-T. et al. (2020). Manage-
ment and clinical outcomes of patients with recurrent/progressive ovarian clear cell
carcinoma. Journal of the Formosan Medical Association 119, 793–804.
17

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
HUANG, X., NING, J. & WAHED, A. S. (2014). Optimization of individualized dy-
namic treatment regimes for recurrent diseases. Statistics in medicine 33, 2363–
2378.
JIANG, R., LU, W., SONG, R. & DAVIDIAN, M. (2017). On estimation of optimal
treatment regimes for maximizing t-year survival probability. Journal of the Royal
Statistical Society: Series B (Statistical Methodology) 79, 1165–1185.
JOHANSEN, M. E., GREEN, L. A., SEN, A., KIRCHER, S. & RICHARDSON, C. R.
(2014). Cardiovascular risk and statin use in the united states. The Annals of Family
Medicine 12, 215–223.
KIDWELL, K. M. (2015). Chapter 2: Dtrs and smarts: Deﬁnitions, designs, and appli-
cations. In Adaptive Treatment Strategies in Practice: Planning Trials and Analyzing
Data for Personalized Medicine. SIAM, pp. 7–23.
KOSOROK, M. R. & LABER, E. B. (2019). Precision medicine. Annual review of
statistics and its application 6, 263–286.
KOSOROK, M. R. & MOODIE, E. E. (2015). Adaptive treatment strategies in practice:
planning trials and analyzing data for personalized medicine. SIAM.
LINN, K. A., LABER, E. B. & STEFANSKI, L. A. (2017). Interactive q-learning for
quantiles. Journal of the American Statistical Association 112, 638–649.
MEINSHAUSEN, N. (2006). Quantile regression forests. Journal of Machine Learning
Research 7, 983–999.
MILLS, E. J., RACHLIS, B., WU, P., DEVEREAUX, P. J., ARORA, P. & PERRI, D.
(2008). Primary prevention of cardiovascular mortality and events with statin treat-
ments: a network meta-analysis involving more than 65,000 patients. Journal of the
American College of Cardiology 52, 1769–1781.
MURPHY, S. A. (2003). Optimal dynamic treatment regimes. Journal of the Royal
Statistical Society: Series B (Statistical Methodology) 65, 331–355.
NIE, X., BRUNSKILL, E. & WAGER, S. (2021). Learning when-to-treat policies.
Journal of the American Statistical Association 116, 392–409.
ORELLANA, L., ROTNITZKY, A. & ROBINS, J. M. (2010). Dynamic regime marginal
structural mean models for estimation of optimal dynamic treatment regimes, part i:
main content. The international journal of biostatistics 6.
QIAN, M. & MURPHY, S. A. (2011). Performance guarantees for individualized treat-
ment rules. Annals of statistics 39, 1180.
RAMKUMAR, S., RAGHUNATH, A. & RAGHUNATH, S. (2016). Statin therapy: review
of safety and potential side effects. Acta Cardiologica Sinica 32, 631.
ROBERTSON, J. B. & UPPULURI, V. (1984). A generalized kaplan-meier estimator.
The Annals of Statistics , 366–371.
18

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
ROBINS, J. M. & ROTNITZKY, A. (1992). Recovery of information and adjustment
for dependent censoring using surrogate markers. In AIDS epidemiology. Springer,
pp. 297–331.
ROBINS, J. M., ROTNITZKY, A. & ZHAO, L. P. (1994). Estimation of regression
coefﬁcients when some regressors are not always observed. Journal of the American
statistical Association 89, 846–866.
RUBIN, D. B. (2005). Bayesian inference for causal effects. Handbook of statistics
25, 1–16.
SCHNEEWEISS, S., GAGNE, J. J., PATRICK, A. R., CHOUDHRY, N. K. & AVORN, J.
(2012). Comparative efﬁcacy and safety of new oral anticoagulants in patients with
atrial ﬁbrillation. Circulation: Cardiovascular Quality and Outcomes 5, 480–486.
SCHURGERS, L. J., AEBERT, H., VERMEER, C., B ¨ULTMANN, B. & JANZEN, J.
(2004). Oral anticoagulant treatment: friend or foe in cardiovascular disease? Blood
104, 3231–3232.
SIMONEAU, G., MOODIE, E. E., NIJJAR, J. S., PLATT, R. W. & INVESTIGATORS, S.
E. R. A. I. C. (2019). Estimating optimal dynamic treatment regimes with survival
outcomes. Journal of the American Statistical Association , 1–24.
SUTTON, R. S. & BARTO, A. G. (2018). Reinforcement learning: An introduction.
The MIT Press.
THOMPSON, P. D., PANZA, G., ZALESKI, A. & TAYLOR, B. (2016).
Statin-
associated side effects. Journal of the American College of Cardiology 67, 2395–
2410.
TSIATIS, A. (1975). A nonidentiﬁability aspect of the problem of competing risks.
Proceedings of the National Academy of Sciences 72, 20–22.
TSIATIS, A. A., DAVIDIAN, M., T, H. S. & LABER, E. B. (2019). Dynamic Treatment
Regimes: Statistical Methods for Precision Medicine. CRC press.
VAN BUUREN, S. & GROOTHUIS-OUDSHOORN, K. (2011). mice: Multivariate im-
putation by chained equations in r. Journal of statistical software 45, 1–67.
WAGER, S. & ATHEY, S. (2018). Estimation and inference of heterogeneous treatment
effects using random forests. Journal of the American Statistical Association 113,
1228–1242.
WAGER, S. & WALTHER, G. (2015). Adaptive concentration of regression trees, with
application to random forests. arXiv preprint arXiv:1503.06388 .
WAHED, A. S. & THALL, P. F. (2013). Evaluating joint effects of induction–salvage
treatment regimes on overall survival in acute leukaemia. Journal of the Royal Sta-
tistical Society: Series C (Applied Statistics) 62, 67–83.
19

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
WAHED, A. S. & TSIATIS, A. A. (2006). Semiparametric efﬁcient estimation of sur-
vival distributions in two-stage randomisation designs in clinical trials with censored
data. Biometrika 93, 163–177.
WALLACE, M. P. & MOODIE, E. E. (2015). Doubly-robust dynamic treatment regi-
men estimation via weighted least squares. Biometrics 71, 636–644.
WANG, L., ZHOU, Y., SONG, R. & SHERWOOD, B. (2018). Quantile-optimal treat-
ment regimes. Journal of the American Statistical Association 113, 1243–1254.
WATKINS, C. J. C. H. (1989). Learning from delayed rewards. Ph.D. thesis.
WRIGHT, J. D., FOLSOM, A. R., CORESH, J., SHARRETT, A. R., COUPER, D., WA-
GENKNECHT, L. E., MOSLEY JR, T. H., BALLANTYNE, C. M., BOERWINKLE,
E. A., ROSAMOND, W. D. et al. (2021). The aric (atherosclerosis risk in communi-
ties) study: Jacc focus seminar 3/8. Journal of the American College of Cardiology
77, 2939–2959.
XU, Y., MULLER, P., WAHED, A. S. & THALL, P. F. (2016). Bayesian nonparametric
estimation for dynamic treatment regimes with sequential transition times. Journal
of the American Statistical Association 111, 921–950.
ZHANG, Y., LABER, E. B., DAVIDIAN, M. & TSIATIS, A. A. (2017).
Estima-
tion of optimal treatment regimes using lists. Journal of the American Statistical
Association,(just-accepted) .
ZHAO, Y., ZENG, D., SOCINSKI, M. A. & KOSOROK, M. R. (2011). Reinforcement
learning strategies for clinical trials in nonsmall cell lung cancer. Biometrics 67,
1422–1433.
ZHU, R., ZENG, D. & KOSOROK, M. R. (2015). Reinforcement learning trees. Jour-
nal of the American Statistical Association 110, 1770–1784.
20

````

