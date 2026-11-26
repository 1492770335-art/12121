# Policy Learning for Optimal Dynamic Treatment Regimes with Observational Data

Original PDF: [original.pdf](original.pdf). SHA256: `4aef40abfe18f288f25ad66d6d2e0b565fbe2a3a203395df3dd9f817e8ee9979`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

FORMULA CHECK REQUIRED: original PDF page 1.

````text
arXiv:2404.00221v7  [stat.ME]  20 May 2025
Policy Learning for Optimal Dynamic Treatment
Regimes with Observational Data
Shosei Sakaguchi∗
May 21, 2025
Abstract
Public policies and medical interventions often involve dynamic treatment as-
signments, in which individuals receive a sequence of interventions over multiple
stages.
We study the statistical learning of optimal dynamic treatment regimes
(DTRs) that determine the optimal treatment assignment for each individual at
each stage based on their evolving history.
We propose a novel, doubly robust,
classiﬁcation-based method for learning the optimal DTR from observational data
under the sequential ignorability assumption. The method proceeds via backward
induction: at each stage, it constructs and maximizes an augmented inverse prob-
ability weighting (AIPW) estimator of the policy value function to learn the op-
timal stage-speciﬁc policy. We show that the resulting DTR achieves an optimal
convergence rate of n´1{2 for welfare regret under mild convergence conditions on
estimators of the nuisance components.
Keywords: Backward induction; Double robustness; Dynamic treatment; Policy
learning; Sequential ignorability.
∗Faculty of Economics, The University of Tokyo, 7-3-1 Hongo, Bunkyo-ku, Tokyo 113-0033, Japan.
Email: sakaguchi@e.u-tokyo.ac.jp.

````

## PDF page 2

Technical extraction; compare with original PDF page 2.

````text
1
Introduction
Public policies and medical interventions often involve dynamics in their treatment as-
signments. For example, some job training programs oﬀer training sessions over multiple
stages (e.g., Lechner, 2009; Rodr´ıguez et al., 2022). In clinical medicine, physicians se-
quentially administer treatments in response to patients’ evolving conditions (e.g., Wang
et al., 2012; Pelham Jr et al., 2016). Multi-stage treatment assignments are also common
educational programs spanning multiple grades (e.g., Krueger, 1999; Ding and Lehrer,
2010) and in dynamic marketing strategies (e.g., Liu, 2023).
This study focuses on the optimal allocation of sequential treatments (Robins, 1986),
in which individuals receive interventions over multiple stages. In this context, treat-
ment eﬀects at each stage are often heterogeneous depending on prior treatments and
related states. Thus, adapting sequential treatment allocation to evolving information
can substantially enhance the welfare gains of multi-stage interventions.
We study statistical learning for optimal sequential treatment assignment using data
from quasi-experimental or observational studies. Throughout this paper, we assume se-
quential ignorability (Robins, 1997), meaning that treatment assignment at each stage is
independent of potential outcomes, conditional on the history of prior treatments and ob-
served states. Under this assumption, we propose a novel method for learning the optimal
dynamic treatment regime (DTR), a sequence of stage-speciﬁc policies that determines
the optimal treatment for each individual at each stage based on their history up to that
point.
In developing our approach, we build on recent advances in doubly robust policy learn-
ing (Athey and Wager, 2021; Zhou et al., 2023b) and extend them to dynamic settings.
We propose a doubly robust, classiﬁcation-based method for learning the optimal DTR
via backward induction, which sequentially estimates the optimal policy from the ﬁnal
stage to the ﬁrst. At each step, the method constructs an augmented inverse probabil-
ity weighting (AIPW) estimator of the policy value function by combining estimators of
the propensity score and the action value function (Q-function) for future policies, while
using cross-ﬁtting. The Q-functions are estimated via ﬁtted Q-evaluation (Munos and
Szepesv´ari, 2008; Fonteneau et al., 2013; Le et al., 2019), a method for oﬄine policy eval-
uation in reinforcement learning. The optimal policy at each stage is then estimated by
2

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
maximizing the estimated policy value function over a pre-speciﬁed class of stage-speciﬁc
policies. This procedure yields the estimated DTR as a sequence of policies across all
stages.
The proposed approach is computationally eﬃcient due to its stepwise backward op-
timization, which is particularly advantageous given the complexity of optimizing DTRs
over multiple stages.
Furthermore, leveraging a classiﬁcation-based framework (Zhao
et al., 2012; Kitagawa and Tetenov, 2018), our approach can enhance the interpretability
of DTRs by allowing for the use of interpretable policy classes, such as decision trees,
for each stage. It can also accommodate various dynamic treatment problems, including
optimal stopping/starting problems, by appropriately constraining the class of feasible
DTRs. An important example of an optimal stopping problem in economics is unemploy-
ment insurance programs that reduce beneﬁt levels after a certain duration (e.g., Meyer,
1995; Kolsrud et al., 2018). In this context, a DTR determines the timing of beneﬁt
reductions for each unemployed individual.
We study the statistical properties of the proposed approach in terms of welfare regret,
deﬁned as the average outcome loss of the estimated DTR relative to the optimal one.
This is a nontrivial task, because the stage-speciﬁc policies within the DTR are estimated
sequentially, rather than simultaneously, and state variables are inﬂuenced by past treat-
ments. The main theoretical contribution of this paper is to establish the convergence
rate for welfare regret, linking it to the convergence rates of the nuisance component es-
timators (propensity scores and Q-functions) in terms of the mean-squared error (MSE).
Our key result identiﬁes conditions on the nuisance component estimators and the class
of DTRs under which the resulting DTR achieves the minimax optimal convergence rate
of n´1{2 for regret. For instance, if all nuisance components are estimated with an MSE
convergence rate of n´1{4 – a rate attainable by many machine learning methods under
suitable structural assumptions – and the complexity of the DTR class is appropriately
constrained, the resulting DTR achieves regret convergence to zero at the optimal rate of
n´1{2. This result parallels those of Athey and Wager (2021) and Zhou et al. (2023b), who
study doubly robust policy learning in single-stage settings, and aligns with the principles
of double machine learning (Chernozhukov et al., 2018).
We illustrate the proposed method through an empirical application to data from
3

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Project STAR (e.g., Krueger, 1999). Speciﬁcally, we learn the optimal DTR for allocating
each student to either a regular-size class with a teacher aide or a small-size class without
one during their early education (kindergarten and grade 1). The estimated DTR uses
students’ intermediate academic performance to determine the optimal class type for the
subsequent grade.
Our empirical results demonstrate that the optimal DTR leads to
better academic outcomes for students compared to uniform class-type allocations.
Related Literature
Although many studies have explored the statistical decision/learning of treatment choice,
most have focused on the single-stage setting.1 Among these, this study is most closely
related to Athey and Wager (2021) and Zhou et al. (2023b), who develop doubly robust
policy learning in single-stage settings and show that the n´1{2-upper bound on regret
can be achieved even in observational data settings. This paper seeks to extend their
approach and results to the multi-stage dynamic treatment choice problem.
There is an expanding literature on the estimation of optimal DTRs, with various
methods proposed having been proposed.2 Oﬄine Q-learning (Watkins and Dayan, 1992)
is arguably the most widely used method for estimating optimal DTRs (e.g., Murphy,
2005; Moodie et al., 2012; Zhang et al., 2018). Murphy (2005) shows that the performance
of the DTR obtained via Q-learning depends on the accuracy of the Q-function estimates;
if the estimated Q-functions deviate from the true ones, the resulting DTR can be far
from optimal. Our approach also estimates Q-functions as part of its procedure. However,
by leveraging propensity score models, it is more robust and accurate than Q-learning.
This study is also related to the classiﬁcation-based, inverse probability weighting
approach for estimating optimal DTRs (e.g., Zhao et al., 2015; Sakaguchi, 2025). This
approach uses inverse propensity weighted outcomes to estimate the value function of a
DTR and maximizes it to estimate the optimal DTR over a pre-speciﬁed class of DTRs.
However, the use of inverse probability-weighted outcomes can sometimes lead to exces-
1A partial list includes Manski (2004), Hirano and Porter (2009), Stoye (2009; 2012), Qian and Murphy
(2011), Bhattacharya and Dupas (2012), Tetenov (2012), Zhao et al. (2012), Kitagawa and Tetenov
(2018), Athey and Wager (2021), Mbakop and Tabord-Meehan (2021), Kitagawa et al. (2023), Zhou
et al. (2023b), and Viviano (2025), among others.
2Chakraborty and Murphy (2014), Laber et al. (2014), Kosorok and Laber (2019), and Li et al. (2023)
provide reviews of the literature.
4

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
sively high variance, which may result in suboptimal DTRs (Doroudi et al., 2018). Our
approach improves upon this method by incorporating models of Q-functions, thereby
enhancing its overall performance.
Doubly robust estimation for optimal DTRs has also been proposed by Zhang et al.
(2013), Wallace and Moodie (2015), and Ertefaie et al. (2021). Zhang et al. (2013) suggest
estimating the optimal DTR by maximizing an AIPW estimator of the welfare function
over an entire class of DTRs.
However, this approach faces computational challenges
for two reasons: (i) the nuisance components to be estimated depend on each speciﬁc
DTR, and (ii) the method maximizes the estimated welfare function simultaneously over
the entire class of DTRs. Our approach addresses these issues by (i) ensuring that the
nuisance components depend only on the estimated policies for future stages, and (ii) es-
timating the optimal DTR through stage-wise backward optimization. Section 5 provides
further details on this comparison.3 Wallace and Moodie (2015) develop a doubly robust
estimation method based on Q-learning and G-estimation (Robins, 2004). Ertefaie et al.
(2021) propose a doubly robust approach for Q-learning and investigate the statistical
properties of the estimated parameters in the Q-functions. By contrast, our focus is on
the statistical properties of welfare regret for the estimated DTR.
In the context of policy learning for optimal stopping/starting problems, Nie et al.
(2021) develop a doubly robust learning approach with computational feasibility and
show upper bounds on the associated regret. Our framework encompasses this problem
as a speciﬁc case.
This study also relates to the literature on (oﬄine) reinforcement learning in terms of
multi-stage decision problems. However, most works assume a Markov decision process,
which this study does not rely on. In the context of non-Markov decision processes, Jiang
and Li (2016), Thomas and Brunskill (2016), and Kallus and Uehara (2020) propose
doubly robust methods for evaluating DTRs, but they do not focus on optimizing DTRs.
Finally, in the econometric literature on dynamic treatment analysis, Heckman and
Navarro (2007) and Heckman et al. (2016) use exclusion restrictions to identify average
dynamic treatment eﬀects, though their focus is not on the identiﬁcation of optimal DTRs.
3Zhang and Zhang (2018) also propose a backward induction approach to estimate optimal DTRs based
on estimators of Q-functions and propensity scores, but their method is not robust to misspeciﬁcation of
the Q-functions. See Footnote 9 for further details.
5

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
Han (2023) proposes a method to characterize the sharp partial ordering of counterfactual
welfares of DTRs within an instrumental variable setting. Ida et al. (2024) empirically
demonstrate that the optimal DTR outperforms optimal static targeting policies in the
context of energy-saving rebate programs.
Structure of the Paper
The remainder of the paper is organized as follows. Section 2 outlines the dynamic treat-
ment choice problem. Section 3 presents the doubly robust approach for learning the
optimal DTRs through backward induction. Section 4 shows the statistical properties of
the proposed approach. Section 5 compares the proposed approach with that of Zhang
et al. (2013). Section 6 presents a simulation study to evaluate the ﬁnite sample perfor-
mance of the approach. Section 7 shows the empirical application results. All proofs of
the main theorem and auxiliary lemmas are provided in Appendix.
2
Setup
Section 2.1 introduces the dynamic treatment framework, following the dynamic potential
outcome framework of Robins (1986, 1997) and Murphy (2003). Subsequently, we deﬁne
the dynamic treatment choice problem in Section 2.2.
2.1
Dynamic Treatment Framework
We consider a ﬁxed number of stages, T pă 8q, for multiple treatment assignments. Let
At ” t0, . . . , dt ´ 1u for t “ 1, . . . , T denote the set of possible treatment arms at stage t,
where dt (ě 2) is the number of treatment arms at stage t, which may vary across stages.
We observe the assigned treatment At P At for each individual at each stage t. Let St be
a vector of the state variables observed prior to treatment assignment at stage t, which
may depend on past treatments. At each stage t, we observe the outcome Yt after the
treatment intervention. The state vector St (for t ě 2) may include previous outcomes
pY1, . . . , Yt´1q. Throughout this paper, for any time-dependent object Vt, we denote by
V t ” pV1, . . . , Vtq its history up to stage t, and by V s:t ” pVs, . . . , Vtq the partial history
from stage s up to stage t (for s ď t). For example, At denotes the treatment history up
6

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
to stage t.
Let Z ” pAT, ST, Y Tq denote the vector of all observed variables. We deﬁne the history
at stage t as Ht ” pAt´1, Stq, which is the information available to the decision-maker when
selecting the treatment at stage t. Note that H1 “ pS1q, where S1 represents individual
characteristics observed prior to the beginning of the sequential treatment intervention.
We denote the supports of Ht and Z by Ht and Z, respectively.
To formalize our results, we adopt the dynamic potential outcomes framework (Robins,
1986; Hern´an et al., 2001; Murphy, 2003). Let At ” A1 ˆ ¨ ¨ ¨ ˆ At. For each at P At, we
deﬁne Yt patq as the potential outcome for stage t, representing the outcome that would
be realized at stage t if the treatment history up to that stage were at. We assume that
the outcome at each stage is not inﬂuenced by treatments in future stages. Since the state
variables St may also depend on past treatments, we deﬁne the potential state variables
as Stpat´1q for each t ě 2 and at´1 P At´1. For t “ 1, we set S1pa0q “ S1 for notational
convenience. The observed outcomes and state variables are thus deﬁned as Yt ” YtpAtq
and St ” StpAt´1q, respectively.
Let Stpat´1q ” pS1, S2pa1q, . . . , Stpat´1qq be the history of the potential state vari-
ables. We deﬁne the vector Ht
`
at´1
˘
”
`
at´1, Stpat´1q
˘
as the potential history real-
ized when the prior treatments are at´1.
For t “ 1, we set H1 pa0q “ H1.
The ob-
served history is then deﬁned as Ht ” Ht
`
At´1
˘
.
We denote by P the distribution
of all underlying variables
´
AT,
␣
STpaT´1q
(
aT ´1PAT ´1 , tY TpaTquaT PAT
¯
, where Y TpaTq ”
pY1pa1q, Y2pa2q, . . . , YTpaTqq.
From an observational study, we observe Zi ”
`
Ai,T, Si,T, Y i,T
˘
for individuals i “
1, . . . , n, where Ai,T “ pAi,1, . . . , Ai,Tq, Si,T “ pSi,1, . . . , Si,Tq, and Y i,T “ pYi,1, . . . , Yi,Tq.
The observed outcome Yi,t and state variables Si,t are deﬁned as Yi,t ” Yi,tpAi,tq and
Si,t ” Si,tpAi,t´1q, respectively, with Yi,t patq and Si,t
`
at´1
˘
being the potential out-
come and state variables, respectively.
Let Si,TpaT´1q ” pSi,1, Si,2pa1q, . . . , Si,TpaT´1qq
and Y i,TpaTq ” pYi,1pa1q, . . . , Yi,TpaTqq. We assume that the vectors of random variables
´
Ai,T,
␣
Si,T
`
aT´1
˘(
aT ´1PAT ´1 ,
␣
Y i,T paTq
(
aT PAT
¯
, for i “ 1, . . . , n, are independent and
identically distributed (i.i.d) under the distribution P. We denote by Hi,t ” pAi,t´1, Si,tq
the history of the i-th individual at stage t.
We deﬁne et pht, atq ” P pAt “ at | Ht “ htq as the propensity score of treatment at at
7

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
stage t with history ht. In the observational data setting we study, the propensity scores
are unknown to the analyst. This contrasts with the experimental data setting, in which
the propensity scores are known from the experimental design.4
Throughout the paper, we assume that the underlying distribution P satisﬁes the
following assumptions.
Assumption 2.1 (Sequential Ignorability). For any t “ 1, . . . , T and aT P AT,
tYt patq , . . . , YT paTq , St`1patq, . . . , STpaT´1qu KK At | Ht.
Assumption 2.2 (Bounded Outcomes). There exists M ă 8 such that the support of
Ytpatq is contained in r´M{2, M{2s for all t P t1, . . . , Tu and at P At.
Assumption 2.1 is also referred to as the dynamic unconfoundedness assumption or
sequential conditional independence assumption, and is commonly used in the literature
on dynamic treatment eﬀect analysis (Robins, 1997; Murphy, 2003). This assumption
implies that the treatment assignment at each stage is independent of current and future
potential outcomes, as well as future state variables, conditional on the history up to that
point. In observational studies, this assumption holds when a suﬃcient set of confounders
is controlled for at each stage. Assumptions 2.2 is a standard assumption in the literature
on estimating optimal DTRs.
2.2
Dynamic Treatment Choice Problem
The aim of this study is to develop a method for learning optimal DTRs using data from
an observational study. We deﬁne a policy for each stage t as πt : Ht ÞÑ At, a map from
the history space for stage t to the treatment space for stage t. A policy πt determines
which treatment is assigned to each individual at stage t based on their history ht. We
deﬁne a DTR as π ” pπ1, . . . , πTq, a sequence of stage-speciﬁc policies. The DTR guides
the treatment choice for each individual from the ﬁrst to the ﬁnal stage, based on their
evolving history up to each stage.
4Even when data are obtained from a sequential multiple assignment randomized trial (SMART),
propensity scores may be unknown due to non-compliance with assigned treatments or attrition at certain
stages.
8

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
Given a ﬁxed DTR π, we deﬁne the welfare of π as
W pπq ” E
« Tÿ
t“1
ÿ
atPAt
˜
Ytpatq ¨
tź
s“1
1tπspHspas´1qq “ asu
¸ﬀ
.
This expression represents the expected total outcome realized when treatments are as-
signed sequentially according to the DTR π.5
We consider choosing a DTR from a pre-speciﬁed class of DTRs denoted by Π ”
Π1 ˆ¨ ¨ ¨ˆΠT, where Πt represents a class of policies for stage t (i.e., a class of measurable
functions πt : Ht Ñ At). For example, Laber and Zhao (2015), Tao et al. (2018), Sun and
Wang (2021), Blumlein et al. (2022), and Zhou et al. (2023a) use a class of decision trees
(Breiman et al., 1984) for Πt, and Zhang et al. (2018) use a class of list-form policies for
Πt. These policy classes enhance the interpretability of the resulting DTRs.
Our framework also accommodates cases where only a part of the history, ˜ht, a sub-
vector of ht, is used for treatment choice by constraining Πt to be a class of functions
of ˜ht. This is particularly relevant given the increasing dimension of the entire history
ht over time, where only a sub-history may be informative for optimal treatment choice.
Additionally, our framework can encompass the optimal stopping/starting problem by
constraining the class Π of DTRs as follows.
Example 2.1 (Optimal Starting/Stopping Problem). Suppose that the number of treat-
ment arms dt is time-invariant (dt “ K for some constant K) and that arm 0 represents
no treatment. Our framework can accommodate the optimal starting problem, in which
the decision-maker determines when to start assigning one of the arms at P t1, . . . , K ´1u
for each unit. This problem can be incorporated into our framework by constraining the
class Π of DTRs such that for any t P t2, . . . , Tu and pπt, htq P Πt ˆ Ht, πtphtq “ at´1 if
at´1 ‰ 0. The optimal stopping problem can also be speciﬁed in a similar manner.
An important example of an optimal stopping problem in economics is unemployment
insurance programs that reduce beneﬁt levels after a certain duration (e.g., Meyer, 1995;
5We can also deﬁne and consider welfare with weighted outcomes as follows:
W pπq
“
E
”řT
t“1
ř
atPAt
´
γtYtpatq ¨ śt
s“1 1tπspHspas´1qq “ asu
¯ı
, where γt represents the weight assigned to the
outcome at stage t. For instance, γt can be a discount factor γt with γ being a discount rate. If we focus
solely on the ﬁnal-stage outcome, we set γT “ 1 and γ1 “ ¨ ¨ ¨ “ γT ´1 “ 0.
9

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
Kolsrud et al., 2018). In this context, a DTR determines the timing of beneﬁt reductions
for each unemployed individual.
Given a pre-speciﬁed class Π of DTRs, we impose an overlap condition on AT, related
to the structure of Π, as follows.
Assumption 2.3 (Overlap Condition). There exists η P p0, 1q for which η ď etpht, atq
holds for any t P t1, . . . , Tu and any pair pht, atq P Ht ˆ At such that there exists πt P Πt
that satisﬁes πtphtq “ at.
When Π is structurally constrained, Assumption 2.3 is weaker than the common over-
lap condition that requires etpht, atq P p0, 1q for all pht, atq P Ht ˆ At and t. For example,
in the optimal stopping problem, Assumption 2.3 does not require etpht, 0q ą 0 for any ht
such that as in ht is 0 for some s ă t.
The ultimate goal of our analysis is to choose an optimal DTR that maximizes the
welfare W p¨q over Π. We are especially interested in learning the optimal DTR from
observational data that satisﬁes the sequential ignorability assumption (Assumption 2.1).
The following section presents a novel step-wise approach to learning the optimal DTR.
3
Learning of the Optimal DTR
In this section, we propose a doubly robust approach to learning the optimal DTRs
through backward induction. Section 3.1 ﬁrst introduces Q-function (action-value func-
tion) and the ﬁtted Q-evaluation, a method to estimate the Q-functions. This section also
discusses identiﬁability of the optimal DTR through the backward-induction procedure.
Section 3.2 then presents our proposed approach to learning the optimal DTRs.
3.1
Fitted Q-evaluation and Backward Induction
For any DTR π and class Π of DTRs, we denote their partial sequences by πs:t ”
pπs, . . . , πtq and Πs:t ” Πs ˆ ¨ ¨ ¨ ˆ Πt, respectively, for s ď t.6
We deﬁne the policy
6For any object vs:t and ws:t (s ď t), vt:t and wt:t correspond to vt and wt, respectively.
10

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
value of πt:T for stage t as
Vt pπt:Tq ” E
« Tÿ
s“t
ÿ
asPAs
˜
Yspasq ¨ 1tAt´1 “ at´1u ¨
sź
ℓ“t
1tπℓ
`
Hℓpaℓ´1q
˘
“ aℓu
¸ﬀ
,
where we assume 1tA0 “ a0u “ 1 for t “ 1. Vt pπt:Tq represents the average total outcome
from stage t to stage T that is realized when the treatment assignments before stage t
follow At´1 (i.e., assignments in the observational data), and those from stage t follow
πt:T. With some abuse of terminology, we refer to Vt pπt:Tq as the policy value function of
πt:T. Note that V1pπ1:Tq “ Wpπq.
Given a ﬁxed DTR π, we deﬁne Q-functions (state-action-value functions), recursively,
as follows:
QTphT , aTq ” E rYT|HT “ hT, AT “ aT s ,
(1)
QπT
T´1phT´1, aT´1q ” E rYT´1 ` QT phT, πTpHTqq|HT´1 “ hT´1, AT´1 “ aT´1s ,
(2)
and, for t “ T ´ 2, . . . , 1,
Q
πpt`1q:T
t
pht, atq ” E
“
Yt ` Q
πpt`2q:T
t`1
pHt`1, πt`1pHt`1qq|Ht “ ht, At “ at
‰
.
(3)
We refer to Q
πpt`1q:T
t
pht, atq as the Q-function for πpt`1q:T . The Q-function Q
πpt`1q:T
t
pht, atq
represents the average total outcome when the history Ht and treatment At correspond
to ht and at at stage t, and the future treatment assignments follow πpt`1q:T .
When
t “ T, we denote Q
πpT `1q:T
T
p¨, ¨q “ QTp¨, ¨q. Note that ErQ
πpt`1q:T
t
pHt, πtpHtqqs “ Vtpπt:Tq
and ErQπ2:T
1
pH1, π1pH1qqs “ Wpπq hold under Assumption 2.1.7 In what follows, for any
function fp¨, ¨q : Ht ˆ At Ñ R and policy πtp¨q : Ht Ñ At, we denote fpht, πtphtqq shortly
by fpht, πtq (e.g., Q
πpt`1q:T
t
pht, πtphtqq is denoted by Q
πpt`1q:T
t
pht, πtq).
Given a ﬁxed DTR π, we can use the sequential deﬁnitions in equations (1)–(3) to
estimate the sequence tQ
πpt`1q:T
t
p¨, ¨qut“1,...,T of the Q-functions for π. This approach is
referred to as the ﬁtted Q-evaluation (Munos and Szepesv´ari, 2008; Fonteneau et al.,
2013; Le et al., 2019) in the reinforcement learning literature and comprises multiple
steps as follows:
7See, for example, Tsiatis et al.(2019, Section 6.4) or Lemma B.2.
11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
• Regress YT on pHT, ATq to obtain pQT p¨, ¨q as the estimated regression function for
QT p¨, ¨q;
• Regress YT´1 ` pQT pHT, πTq on pHT´1, AT´1q to obtain pQπT
T´1p¨, ¨q as the estimated
regression function for QπT
T´1p¨, ¨q;
• Recursively, for t “ T ´ 2, . . . , 1, regress Yt ` pQ
πpt`2q:T
t`1
pHt`1, πt`1q on pHt, Atq to
obtain pQ
πpt`1q:T
t
p¨, ¨q as the estimated regression function for Q
πpt`1q:T
t
p¨, ¨q.
We can apply ﬂexible/nonparametric regression methods, including machine learning
methods (e.g., random forests, lasso, neural networks), to the regression in each step.
Given the deﬁnitions of the Q-functions, we can optimize the DTR through backward
induction. To present the idea, we here assume that the generative distribution function P
is known and that the pair pP, Πq satisﬁes Assumptions 2.1, 2.2, and 2.3. The backward-
induction approach in the population problem is a step-wise process proceeding as follows.
In the ﬁrst step, the approach optimizes the ﬁnal-stage policy over ΠT by solving
π˚,B
T
“ arg max
πT PΠT
E rQTpHT, πTqs .
Then, recursively, from t “ T ´ 1 to 1, the approach optimizes the t-th stage policy over
Πt by solving
π˚,B
t
“ arg max
πtPΠt
E
„
Q
π˚,B
pt`1q:T
t
pHt, πtq

.
Note that the objective function E
„
Q
π˚,B
pt`1q:T
t
pHt, πtq

corresponds to the policy value
Vtpπt, π˚,B
pt`1q:T q under the sequential ignorability assumption (Assumption 2.1). The entire
procedure yields the DTR π˚,B ” pπ˚,B
1
, ¨ ¨ ¨ , π˚,B
T
q.
We denote the optimal DTR over Π by π˚,opt “ arg max
πPΠ
Wpπq. Importantly, the DTR
π˚,B obtained through backward induction does not necessarily correspond to the optimal
DTR π˚,opt when Π is structurally constrained, as noted by Li et al. (2023) and Sakaguchi
(2025). To ensure that backward induction yields the optimal DTR, the policy class Πt
for each stage t (ě 2) needs to be correctly speciﬁed. The following assumption gives a
suﬃcient condition for the backward optimization to attain optimality.
12

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
Assumption 3.1 (Correct Speciﬁcation). There exists π˚
2:T “ pπ˚
2, . . . , π˚
Tq P Π2:T such
that for any t “ 2, . . . , T,
Q
π˚
pt`1q:T
t
pHt, π˚
t q ě sup
πtPΠt
Q
π˚
pt`1q:T
t
pHt, πtq a.s.
Assumption 3.1 requires that for each stage t ě 2, Πt includes a policy that can
select the optimal arm among all feasible arms in tπtphtq : πt P Πtu pĎ Atq for any
history ht. This assumption is satisﬁed when Πt (for t “ 2, . . . , T) is ﬂexible enough
or correctly speciﬁed in relation to treatment eﬀect heterogeneity.8 We suppose that Π
satisﬁes Assumption 3.1.
Note that Assumption 3.1 is a suﬃcient but not a necessary condition. To illustrate
this, Appendix D provides an example demonstrating cases where backward induction
can achieve optimality even when Assumption 3.1 is not satisﬁed.
A stronger version of Assumption 3.1 is that each Πt (t ě 2) contains the ﬁrst-best
policy; that is, there exists π˚,F B
2:T
“ pπ˚,F B
2
, . . . , π˚,F B
T
q P Π2:T such that for any t “
2, . . . , T,
Q
π˚,F B
pt`1q:T
t
´
Ht, π˚,F B
t
¯
ě max
atPAt Q
π˚,F B
pt`1q:T
t
pHt, atq a.s.
The ﬁrst-best policy π˚,F B
t
is the policy that selects the best treatment arm for any
history ht. Li et al. (2023) and Sakaguchi (2025) argue that the availability of the ﬁrst-
best policies is a fundamental assumption for the optimality of the backward optimization.
However, Assumption 3.1 is practically weaker than this. For example, in the optimal
starting problem (Example 2.1), although Πt may not include the ﬁrst-best policy π˚,F B
t
due to structural constraints from the optimal starting problem, Assumption 3.1 does not
require its feasibility. Similarly, when each policy in Πt depends only on a sub-history ˜ht
(a subvector of ht), Assumption 3.1 requires that the optimal policy is available for the
sub-history, rather than for the entire history.
The following lemma formalizes the optimality of the backward-induction procedure
under Assumption 3.1.
8Zhang et al. (2013) discuss how to correctly specify Πt based on the model for treatment eﬀect
heterogeneity. Zhao et al. (2015) use a reproducing kernel Hilbert space for each Πt as a ﬂexible class of
polices.
13

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
Lemma 3.1. Under Assumptions 2.1, 2.3, and 3.1, π˚,B is the optimal DTR over Π; i.e.,
Wpπ˚,Bq ě Wpπq for all π P Π.
Proof. See Appendix B.1.
3.2
Learning of the Optimal DTRs through Backward Induction
This section presents a backward optimization procedure to learn the optimal DTRs
using an AIPW estimator of the policy value function. Following the doubly robust policy
learning approaches of Athey and Wager (2021) and Zhou et al. (2023b), we employ cross-
ﬁtting to estimate the policy value function and learn the optimal policy independently.
We randomly divide the dataset tZi : i “ 1, . . . , nu into K evenly-sized folds (e.g., K “ 5).
Let Ik Ď t1, . . . , nu be the set of indices of the data in the k-th fold, and I´k denote the
set of indices of the data excluded from the k-th fold. In what follows, for any statistic
ˆf, we denote by ˆf ´k the corresponding statistic calculated using the data excluded from
the k-th fold. Let kpiq denote the fold number that contains the i-th observation.
The proposed approach is based on backward induction and thus consists of multiple
steps. As a preliminary step, we estimate the propensity scores tetp¨, ¨qut“1,...,T for all
stages and the Q-function QTp¨, ¨q for the ﬁnal stage using the data excluded in each cross-
ﬁtting fold. For each k, we denote by ˆe´k
t p¨, ¨q and pQ´k
T p¨, ¨q, respectively, the estimators of
etp¨, ¨q and QTp¨, ¨q using data not contained in the k-th cross-ﬁtting fold. Any regression
methods, including machine learning methods (e.g., random forests and neural networks),
can be used to estimate etp¨, ¨q and QTp¨, ¨q.
Given tˆe´k
t p¨, ¨qut“1,...,T and pQ´k
T p¨, ¨q for each k “ 1, . . . , K, we estimate the optimal
DTR sequentially as follows. In the ﬁrst step, regarding the ﬁnal stage T, we construct a
score function of the treatment aT for stage T as
pΓi,TpaTq ” Yi,T ´ pQ´kpiq
T
pHi,T, Ai,Tq
ˆe´kpiq
T
pHi,T, Ai,Tq
¨ 1tAi,T “ aTu ` pQ´kpiq
T
pHi,T, aTq.
(4)
Given a policy πT , the sample mean p1{nq řn
i“1 pΓi,TpπTpHi,Tqq is an AIPW estimator of
the policy value VTpπTq for stage T.
14

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
We then ﬁnd the best candidate policy for stage T by solving
ˆπT “ arg max
πT PΠT
1
n
nÿ
i“1
pΓi,T pπTpHi,Tqq .
In the next step, we consider stage T ´ 1. Given the estimated policy ˆπT from the
previous step, for each k-th cross-ﬁtting fold, we estimate the Q-function QˆπT
T´1p¨, ¨q for
ˆπT by regressing Yi,T´1 ` pQTpHi,t, ˆπTq on pHi,T´1, Ai,T´1q using the observations whose
indices are not included in Ik. This corresponds to the second step of the ﬁtted-value
Q-evaluation, and any regression method can be applied at this step. We denote the
resulting estimator of QˆπT
T´1p¨, ¨q by pQˆπT ,´k
T´1 p¨, ¨q for each k.
We subsequently construct the score function of aT´1 as follows:
pΓˆπT
i,T´1paT´1q ” Yi,T´1 ` pΓi,TpˆπTpHi,Tqq ´ pQˆπT ,´kpiq
T´1
pHi,T´1, Ai,T´1q
ˆe´kpiq
T´1 pHi,T´1, Ai,T´1q
¨ 1tAi,T´1 “ aT´1u
` pQˆπT ,´kpiq
T´1
pHi,T´1, aT´1q.
Given a policy πT´1, the sample mean p1{nq řn
i“1 pΓˆπT
i,T´1pπT´1pHi,T´1qq is an AIPW es-
timator of the policy value VT´1pπT´1, ˆπT q. We then ﬁnd the best candidate policy for
stage T ´ 1 by solving
ˆπT´1 “ arg max
πT ´1PΠT ´1
1
n
nÿ
i“1
pΓˆπT
i,T´1 pπT´1pHi,T´1qq .
Recursively, for t “ T ´2, . . . , 1, we learn the optimal policy as follows. For each cross-
ﬁtting index k, we ﬁrst estimate the Q-function Q
ˆπpt`1q:T
t
by regressing Yi,t` pQ
ˆπpt`2q:T
t`1
pHi,t`1, ˆπt`1q
on pHi,t, Ai,tq using the observations whose indices are not in Ik (the ﬁtted Q-evaluation).
Any regression method can be applied at this step.
We next construct the score function of at as
pΓ
ˆπpt`1q:T
i,t
patq ” Yi,t ` pΓ
ˆπpt`2q:T
i,t`1
pˆπt`1pHi,t`1qq ´ pQ
ˆπpt`1q:T ,´kpiq
t
pHi,t, Ai,tq
ˆe´kpiq
t
pHi,t, Ai,tq
¨ 1tAi,t “ atu
` pQ
ˆπpt`1q:T ,´kpiq
t
pHi,t, atq.
(5)
15

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
We then ﬁnd the best candidate policy for stage t by solving
ˆπt “ arg max
πtPΠt
1
n
nÿ
i“1
pΓ
ˆπpt`1q:T
i,t
pπtpHi,tqq ,
where the objective function p1{nq řn
i“1 pΓ
ˆπpt`1q:T
i,t
pπtpHi,tqq is an AIPW estimator of the
policy value Vtpπt, ˆπpt`1q:T q.
Throughout this procedure, we obtain the sequence ˆπ ” pˆπ1, . . . , ˆπTq, which serves as
the estimator for the optimal DTR. Algorithm 1 summarizes the entire procedure.9 In the
following section, we will show statistical properties of the resulting DTR ˆπ with respect
to its welfare regret.
Algorithm 1 Doubly robust backward-induction learning
1: Input: K (the number of cross-ﬁtting folds); tZi : i “ 1, . . . , nu (dataset)
2: Construct ˆe´k
t p¨, ¨q (t “ 1, . . . , T) and pQ´k
T p¨, ¨q for each k P t1, . . . , Ku
3: Compute pΓi,TpaTq (equation (4)) for each aT P AT and i P t1, . . . , nu
4: Learn the optimal policy by setting ˆπT “ arg max
πT PΠT
p1{nq řn
i“1 pΓi,T pπTpHi,Tqq
5: for t “ T ´ 1 to 1 do
6:
Construct pQ
ˆπpt`1q:T ,´k
t
p¨, ¨q for each k P t1, . . . , Ku (Fitted Q-evaluation)
7:
Compute pΓ
ˆπpt`1q:T
i,t
patq (equation (5)) for each at P At and i P t1, . . . , nu
8:
Learn the optimal policy by setting
ˆπt “ arg max
πtPΠt
1
n
nÿ
i“1
pΓ
ˆπpt`1q:T
i,t
pπtpHi,tqq
9: end for
10: return ˆπ “ pˆπ1, . . . , ˆπTq
9 Our proposed method diﬀers from that of Zhang and Zhang (2018) in the construction of the objective
function pΓˆπpt`1q:T
i,t
, even in the binary treatment setting considered by Zhang and Zhang (2018), although
both approaches use Q-functions and propensity scores. In their approach, the objective function at
each stage t depends only on the propensity score for that stage and the Q-functions for that and future
stages. As a result, it is not robust to misspeciﬁcation of Q-functions for future stages – even when the
propensity scores are correctly speciﬁed – and thus does not attain double robustness. Speciﬁcally, in
their framework (following the notation in Zhang and Zhang (2018)), if Qk is misspeciﬁed, then rVk is no
longer a consistent estimator of Vk, which in turn leads to inconsistency in their estimators of the policy
value, pCk, and the optimal policy, ˆgopt
C,k.
16

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
4
Statistical Properties
Given a DTR π P Π, we deﬁne the regret of π by Rpπq ” max˜πPΠ Wp˜πq ´ Wpπq, the loss
of the welfare of π relative to the maximum welfare achievable in Π. We study statistical
properties of ˆπ with respect to its regret Rpˆπq. This section shows the rate of convergence
of Rpˆπq depending on the convergence rates of the estimators of the nuisance components,
tˆe´k
t p¨, ¨qut“1,...,T and t pQ
πpt`1q:T ,´k
t
p¨, ¨qut“1,...,T, and the complexity of Π.
Let pQ
πpt`1q:T ,pnq
t
p¨, ¨q and ˆepnq
t p¨, ¨q denote the estimators of the Q-function Q
πpt`1q:T
t
p¨, ¨q
for πpt`1q:T and the propensity score etp¨, ¨q, respectively, using a sample of size n randomly
drawn from the distribution P. For t “ T, we denote pQ
πpT `1q:T ,pnq
T
p¨, ¨q “ pQpnq
T p¨, ¨q for
notational convenience.
We suppose that t pQ
πpt`1q:T ,pnq
t
p¨, ¨qut“1,...,T and tˆepnq
t p¨, ¨qut“1,...,T
satisfy the following assumption.
Assumption 4.1 (Double Robustness). (i) There exists τ ą 0 such that the following
holds: For all t “ 1, . . . , T, s “ 1, . . . , t, and m P t0, 1u,
sup
as:tPAs:t
E
«
sup
πpt`1q:T PΠpt`1q:T
´
pQ
πpt`1q:T ,pnq
t
pHt, atq ´ Q
πpt`1q:T
t
pHt, atq
¯2
ﬀ
ˆ E
»
–
˜
1
śt´m
ℓ“s ˆepnq
ℓpHℓ, aℓq
´
1
śt´m
ℓ“s eℓpHℓ, aℓq
¸2ﬁ
ﬂ“ Op1q
nτ .
(ii) There exists n0 P N such that for any n ě n0 and t “ 1, . . . , T,
sup
atPAt,πpt`1q:T PΠpt`1q:T
pQ
πpt`1q:T ,pnq
t
pHt, atq ă 8 and
min
atPAt ˆepnq
t pHt, atq ą 0
hold a.s.
As we will see later, the ?n-consistency of the regret Rpˆπq to zero can be achieved
when Assumption 4.1 (i) holds with τ “ 1. This is not very strong or restrictive. For
example, Assumption 4.1 (i) is satisﬁed with τ “ 1 when
sup
atPAt
E
«
sup
πpt`1q:T PΠpt`1q:T
´
pQ
πpt`1q:T ,pnq
t
pHt, atq ´ Q
πpt`1q:T
t
pHt, atq
¯2
ﬀ
“ Op1q
?n and
sup
as:tPAs:t
E
»
–
˜
1
śt
ℓ“s ˆepnq
ℓpHℓ, aℓq
´
1
śt
ℓ“s eℓpHℓ, aℓq
¸2ﬁ
ﬂ“ Op1q
?n
17

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
hold for all t “ 1, . . . , T and s “ 1, . . . , t.
The uniform MSE convergence rate of
pQ
πpt`1q:T ,pnq
t
pHt, atq for the ﬁtted Q-evaluation is not a standard result, but some exist-
ing results are applicable with some modiﬁcations (e.g., Zhang et al., 2018; Kallus and
Uehara, 2020). For example, Kallus and Uehara (2020) argue that the FQE estimators
t pQ
πpt`1q:T ,pnq
t
: t “ 1, . . . , Tu for a ﬁxed DTR π can be viewed as M-estimators that minimize
p1{nq řT
t“1
řn
i“1
`
Yi,t ` Q
πpt`2q:T
t`1
pHi,t`1, πt`1q ´ Q
πpt`1q:T
t
pHi,t, πtq
˘2 over (semi/non)parametric
classes of Q-functions, where Q
πpT `2q:T
T`1
pHi,T`1, πT`1q “ 0 by convention. This formulation
enables the use of existing results on (semi/nonparametric) M-estimation to derive uni-
form convergence rates for pQπpt`1q:T ,pnq
t
for each t.
Note also that Assumption 4.1 (i) encompasses the property of double robustness; that
is, Assumption 4.1 (i) holds if either pQ
πpt`1q:T ,pnq
t
p¨, ¨q is uniformly consistent or ˆepnq
t p¨, ¨q is
consistent, provided that Assumption 4.1 (ii) holds.
We next consider the complexity of the class Π of DTRs and the classes Πt of stage-
speciﬁc policies. Following Zhou et al. (2023b), we use the ǫ-Hamming covering number
to measure the complexity of the class of policy sequences πs:t P Πs ˆ ¨ ¨ ¨ ˆ Πt for each s
and t such that s ď t.
Deﬁnition 4.1. (i) For any stages s and t such that s ď t, given a set of history points
thp1q
t , . . . , hpnq
t u Ď Ht, we deﬁne the Hamming distance between two sequences of policies
πs:t, π1
s:t P Πs:t as dhpπs:t, π1
s:tq ” n´1 řn
i“1 1tπsphpiq
s q ‰ π1
sphpiq
s q _ ¨ ¨ ¨ _ πtphpiq
t q ‰ π1
tphpiq
t qu,
where we denote hpiq
t
“ papiq
t´1, spiq
t q and hpiq
ℓ
(ℓ“ s, . . . , t ´ 1) is the subvector of hpiq
t
such
that hpiq
ℓ
“ papiq
ℓ´1, spiq
ℓq P Hℓ. Let Ndh
´
ǫ, Πs:t,
!
hp1q
t , . . . , hpnq
t
)¯
be the smallest number of
sequences of policies πp1q
s:t , πp2q
s:t , . . . in Πs:t such that for any πs:t P Πs:t, there exists πpiq
s:t
satisfying dhpπs:t, πpiq
s:tq ď ǫ. We deﬁne the ǫ-Hamming covering number of Πs:t as
Ndhpǫ, Πs:tq ” sup
!
Ndh
´
ǫ, Πs:t,
!
hp1q
t , . . . , hpnq
t
)¯ˇˇˇn ě 1, hp1q
t , . . . , hpnq
t
P Ht
)
.
(ii) We deﬁne the entropy integral of Πs:t as κpΠs:tq “
ş1
0
a
log Ndh pǫ2, Πs:tqdǫ.
Note that when s “ t, Ndhpǫ, Πs:tq “ Ndhpǫ, Πtq and κpΠs:tq “ κpΠtq. We assume that
the policy class Πt for each t is not excessively complex in terms of the covering number.
Assumption 4.2 (Complexity of Πt). For all t “ 1, . . . , T, Ndhpǫ, Πtq ď C exppDp1{ǫqωq
holds for any ǫ ą 0 and some constants C, D ą 0 and 0 ă ω ă 0.5.
18

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
This assumption implies that the covering number of Πt does not grow too quickly, but
allows log Ndhpǫ, Πtq to grow at a rate of 1{ǫ. This assumption is satisﬁed, for example, by
a class of ﬁnite-depth trees (see Zhou et al. (2023b, Lemma 4)). In the case of a binary
action set (i.e., |At| “ 2), a VC-class of πt also satisﬁes Assumption 4.2. Zhou et al.
(2023b, Remark 4) shows that the entropy integral κpΠtq is ﬁnite under Assumption 4.2.
Regarding the class Π of entire DTRs, its entropy integral κpΠq is ﬁnite as well under
Assumption 4.2.
Lemma 4.2. Under Assumption 4.2, κpΠq ă 8.
Proof. See Appendix B.1.
The following theorem presents the main result of this paper, showing the rate of
convergence for the regret of the DTR ˆπ obtained using the proposed approach.
Theorem 4.3. Under Assumptions 2.1–2.3, 3.1, 4.1, and 4.2,
Rpˆπq “ Op
`
κpΠq ¨ n´1{2˘
` Oppn´ mint1{2,τ{2uq.
Proof. See Appendix A.
This theorem establishes the convergence rate of the regret Rpˆπq for the proposed
method. When Assumption 4.1 (i) holds with τ “ 1, the approach achieves the optimal
rate n´1{2 for the regret convergence.10 This result is comparable to those of Athey and
Wager (2021) and Zhou et al. (2023b), who study doubly robust policy learning in single-
stage settings.11 The asymptotic upper bound also increases with the number of time
stages T, through the entropy integral κpΠq of the class of DTRs.
In the proof of Theorem 4.3, we consider the derivation of the asymptotic upper
bound on Rpˆπq. This is, however, a non-trivial task because the stage-speciﬁc policies
in ˆπ “ pˆπ1, . . . , ˆπTq are estimated sequentially, rather than simultaneously. If the DTR
were estimated simultaneously across all stages, one could adapt the theoretical analysis
10In the case of binary treatment at each stage, Sakaguchi (2025) shows that the minimax optimal rate
of convergence for the regret is V1:T ¨ n´1{2, where V1:T is the VC-dimension of the class of DTRs.
11In the single-stage binary treatment setting, Athey and Wager (2021) use the speciﬁc growth rate of
the entropy in a VC class and obtain a slightly stronger result compared to using the ﬁxed entropy class.
19

````

## PDF page 20

FORMULA CHECK REQUIRED: original PDF page 20.

````text
of Zhou et al. (2023b).
However, the sequential nature of the estimation precludes a
direct application of their approach. Despite this challenge, Appendix A presents novel
analytical techniques to evaluate the regret of the sequentially estimated DTR.
5
Existing Approach
An alternative doubly robust approach for estimating the optimal DTR is maximizing
an AIPW estimator of the welfare function simultaneously over the entire class of DTRs.
Speciﬁcally, we have
ˆπAIP W “ arg max
πPΠ
x
W AIP Wpπq with
(6)
x
W AIP Wpπq “ 1
n
nÿ
i“1
Tÿ
t“1
´
ˆψ´kpiq
it
pπtq ¨ Yit
´
´
ˆψ´kpiq
it
pπtq ´ ˆψ´kpiq
i,t´1
`
πt´1
˘¯
¨ pQ
πpt`1q:T ,´kpiq
t
pHit, πtq
¯
and ˆψ´kpiq
it
pπtq ”
`śt
s“1 1 tAis “ πspHisqu
˘
{pśt
s“1 ˆe´kpiq
t
pHis, Aisqq, where x
W AIP Wpπq is
an AIPW estimator of Wpπq. This approach was originally proposed by Zhang et al.
(2013) without cross-ﬁtting and under binary treatment at each stage, but its statistical
properties were not established.12 One advantage of this method is that it does not require
the correct speciﬁcation of Π (Assumption 3.1) for consistent estimation of the optimal
DTR.
However, this approach faces two computational challenges. First, since the nuisance
components tQ
πpt`1q:T
t
ut“1,...,T depend on each speciﬁc DTR π, implementing the method
requires estimating tQ
πpt`1q:T
t
ut“1,...,T for every candidate DTR π.13 Nie et al. (2021) high-
light this computational burden. Second, maximizing x
W AIP Wpπq simultaneously across
all stages is computationally demanding, especially when T is not very small, as the prob-
lem is non-convex. These computational issues make the approach intractable unless the
class of DTRs Π is small (e.g., consisting of a limited number of candidate policies).
12Jiang and Li (2016), Thomas and Brunskill (2016), and Kallus and Uehara (2020) propose AIPW
estimators of welfare functions for evaluating ﬁxed DTRs, but their focus is not on optimizing DTRs.
13A heuristic alternative to solve this diﬃculty, proposed by Zhang et al. (2013), is to ﬁrst esti-
mate the optimal policy by Q-learning, denoted by ˆπQ
t , and then use the optimal Q-function estimate
pQ
ˆπQ
pt`1q:T ,´kpiq
t
pHit, atq instead of pQ
πpt`1q:T ,´kpiq
t
pHit, atq when constructing and maximizing x
W AIP W pπq.
This approach avoids the need to estimate Q
πpt`1q:T
t
for each πpt`1q:T .
20

````

## PDF page 21

FORMULA CHECK REQUIRED: original PDF page 21.

````text
In contrast, our proposed approach oﬀers notable computational advantages: (i) the
nuisance components tQ
ˆπpt`1q:T
t
ut“1,...,T depend only on the previously estimated policies
ˆπpt`1q from earlier steps in the backward optimization, and (ii) the backward optimiza-
tion is computationally more eﬃcient than joint optimization across all stages. While
our approach requires estimating the Q-function Q
ˆπpt`1q:T
t
at each step of the sequential
procedure, the associated computational cost is relatively modest.
Although the simultaneous maximization approach (6) is not our primary proposal,
we show its statistical properties as follows.14
Theorem 5.1. Under Assumptions 2.1–2.3, 4.1, and 4.2,
RpˆπAIP Wq “ Op
`
κpΠq ¨ n´1{2˘
` Oppn´ mint1{2,τ{2uq.
(7)
Proof. See Appendix C.
This theorem shows that ˆπAIP W attains the same convergence rate for regret as our
proposed approach, ˆπ, under the same conditions regarding the MSE convergence rate
of the nuisance component estimators and the complexity of the DTR class. Since the
simultaneous optimization approach does not require the correct speciﬁcation of the DTR
class, Theorem 5.1 does not rely on Assumption 3.1.
6
Simulation Study
We conduct a simulation study to examine the ﬁnite sample performance of the ap-
proach presented in Section 3. We consider two data generating processes (DGPs), labeled
DGP1 and DGP2, each of which consists of two stages of binary treatment assignment
pA1, A2q P t0, 1u2, associated second-stage potential outcomes tY2 pa1, a2quta1,a2uPt0,1u2, 20
state variables pSp1q
1 , . . . , Sp20q
1
q observed at the ﬁrst stage, and one state variable S2 ob-
14Sakaguchi (2025, Theorem E.1) shows statistical properties of this approach in the case of binary
treatment.
21

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
served at the second stage. Each DGP is structured as follows:
pSp1q
1 , . . . , Sp20q
1
q1 ∼Np0, I20q;
S2 pa1q “ sign
´
Sp1q
1
¯
¨ a1 ` Sp2q
1
`
´
Sp3q
1
¯2
` Sp4q
1
` ε1 with ε1 „ Np0, 1q;
Y2 pa1, a2q “ φpa1, S2pa1qq ¨ a2 ` 0.5 ¨ S2pa1q ` Sp4q
1
´
´
Sp5q
1
¯2
` Sp6q
1
` ε2 with ε2 „ Np0, 1q;
A1 ∼Ber
´
1{p1 ` e0.5Sp2q
1
´0.5Sp3q
1
´Sp5q
1 q
¯
, A2 ∼Ber
´
1{p1 ` e0.5Sp5q
1
`0.5S2´0.2A1q
¯
.
In DGPs 1 and 2, we specify φpa1, S2pa1qq as φpa1, S2pa1qq “ signpS2pa1q ¨ pa1 ´ 1{2qq and
φpa1, S2pa1qq “ S2pa1q ` pa1 ´ 1{2q, respectively. In each DGP, the ﬁrst-stage treatment
a1 inﬂuences the outcome Y2 through both direct and indirect channels: (i) a direct eﬀect
on Y2 via treatment eﬀect heterogeneity Y2pa1, 1q ´ Y2pa1, 0q; (ii) an indirect eﬀect on Y2
via the second-stage state S2pa1q.
We compare the performance of the proposed approach (labeled “DR”) with those
of three existing methods: Q-learning without and with policy search (labeled “Q-learn”
and “Q-search,” respectively) and the IPW classiﬁcation-based approach with backward
optimization (labeled “IPW”).15 For each method, we use generalized random forests
(Athey et al., 2019) to estimate nuisance components. We set K “ 5 for cross-ﬁtting in
the proposed approach.
For DR, Q-search, and IPW, we use a class of DTRs Π “ Π1 ˆ Π2 with Π1 being the
class of depth-1 decision trees of H1, and Π2 being the class of depth-2 decision trees of
H2. In DGP1, Π2 is correctly speciﬁed in the sense of Assumption 3.1, whereas in DGP2,
Π2 is misspeciﬁed, potentially leading to a loss of optimality in backward optimization.
Note that Q-learn consistently estimates the optimal DTRs in both DGPs. We solve
the optimization problems involving decision trees using the exact learning algorithm
proposed by Zhou et al. (2023b).
Tables 1 and 2 present the results of 500 simulations with sample sizes of n “ 250,
500, 1000, 2000, and 4000 for DGPs 1 and 2, respectively. In each simulation, welfare is
15Following Murphy (2005), we separately consider Q-learning with and without policy search. In
Q-learning with policy search, the optimal policy for each stage t is chosen from a pre-speciﬁed pol-
icy class Πt, speciﬁcally estimated as ˆπt “ arg max
πtPΠt
řn
i“1 pQ
ˆπpt`1q:T
t
pHit, πtq.
In contrast, Q-learning
without policy search optimizes the policy for each stage t over all measurable policies, such as
ˆπtphtq “ arg max
atPAt
řn
i“1 pQ
ˆπpt`1q:T
t
pht, atq for any ht. This approach consistently estimates the ﬁrst-best
DTR unless the Q-functions are misspeciﬁed.
22

````

## PDF page 23

FORMULA CHECK REQUIRED: original PDF page 23.

````text
calculated using a test sample of 50,000 observations randomly drawn from the same DGP.
The results show that DR consistently outperforms the other methods in terms of mean
welfare across all sample sizes for both DGPs. For example, in DGP1 with a small sample
size (n “ 500), DR achieves over 40% higher welfare than any other method. Notably, DR
surpasses Q-learn even in DGP2, where the DTR class is misspeciﬁed, although Q-learn
consistently estimates the optimal DTR.
Appendix E presents additional simulation results that examine the eﬀects of mis-
speciﬁcation of either the Q-functions or propensity scores. The results demonstrate the
doubly robust property of the proposed method.
7
Empirical Application
We apply the proposed approach to data from Project STAR (e.g., Krueger, 1999; Ding
and Lehrer, 2010), where we study the optimal allocation of students to regular-size classes
(22 to 25 students per teacher) with a full-time teacher aide and small-size classes (13
to 17 students per teacher) without one in their early education (kindergarten and grade
1).16 We use a dataset of 1,877 students who were assigned to either regular-size classes
with a full-time teacher aide or small-size classes without one in kindergarten.17 Among
these students, 702 were randomly assigned to regular-size classes with a teacher aide,
while the remaining students were assigned to small-size classes without a teacher aide
in kindergarten (labeled “grade K”). Upon their progression to grade 1, students were
expected to remain in the same class type. However, about 10% of students switched
class types on their own (see, e.g., Ding and Lehrer (2010) for a detailed discussion). We
leverage this variation to estimate the optimal DTR and consider this empirical task in
the observational data setting.
We investigate the optimal allocation of students to the two class types in grades K
and 1, based on their socioeconomic backgrounds, educational environment, and interme-
diate academic achievement. Each student’s academic achievement is measured by their
16Krueger (1999) reports that the presence of a teacher aide did not have a signiﬁcant impact on
student test scores. However, whether teaching aides have eﬀects on academic attainment has not been
examined by accounting for multiple stages of treatment and treatment eﬀect heterogeneity.
17We exclude regular-size classes without a teacher aide, as they are unlikely to be preferable to either
regular-size classes with an aide or small-size classes without one for any student.
23

````

## PDF page 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
percentile rank on combined reading and mathematics test scores taken at the end of
grade 1. The welfare objective for the administrator is assumed to be maximizing the
population average of this academic achievement measure.
We deﬁne the ﬁrst and second stages (t “ 1 and t “ 2) as grades K and 1, respectively.
We deﬁne the action set At “ taide, smallu, where the treatment variable At is labeled
“aide” if a student is in a regular-size class with a teacher aide at stage t, and “small”
if the student is in a small-size class. The outcome variable Y2 denotes the percentile
rank of the combined reading and mathematics scores at the end of grade 1. We do not
incorporate the ﬁrst-stage outcome into the objective function Wpπq.
We use seven variables in H1p“ S1q: student gender, student ethnicity (White/Asian
or other), eligibility for free or reduced-price school lunch, school location type (rural
or non-rural), teacher’s degree (bachelor’s or higher), years of teaching experience, and
teacher ethnicity (White or other). For the second-stage state variables S2, we include
three variables: reading, math, and total test scores at the end of kindergarten. Recall
that H2 “ pA1, S1, S2q. We assume that the academic and socio-economic information
contained in H2 satisﬁes the conditional ignorability assumption (Assumption 3.1) for
grade 1, as these factors are strongly associated with the self-selection of class type. Since
there is no self-selection in kindergarten, the ignorability condition for the ﬁrst stage is
assured.
The class of DTRs Π “ Π1ˆΠ2 is deﬁned as follows. For the policy class Π1 associated
with class allocation in grade K, we employ a class of depth-1 trees that may take splitting
variables from teacher degree, teacher experience, and school location type.
For the
policy class Π2 associated with class allocation in grade 1, we use a class of depth-2 trees
that may take splitting variables from reading, math, and total test scores at the end of
kindergarten, as well as the kindergarten class type. Note that we exclude student gender,
student ethnicity, and teacher ethnicity as splitting variables, as using them for treatment
choice would be discriminatory.
In applying the proposed approach, we employ 5-fold cross-ﬁtting and use generalized
random forests (Athey et al., 2019) to estimate the nuisance components. The decision
trees are optimized using the exact learning algorithm of Zhou et al. (2023b).
Figure 1 shows the DTR estimated using the proposed approach.
The policy for
24

````

## PDF page 25

FORMULA CHECK REQUIRED: original PDF page 25.

````text
grade K class allocation uses teacher experience to determine the class type, indicating
that teachers with 19 years of experience or less should be assigned to small-size classes.
The policy for grade 1 class allocation uses total and reading test scores at the end of
kindergarten to determine each student’s class type. For instance, under the estimated
policy, students with a total test score below 914 are assigned to the small-size class in
grade 1.
Table 3 presents estimates of the welfare contrasts for the optimal DTR, π˚,opt, relative
to uniformly assigning all students to either aides or small classes in both grades (i.e.,
Wpπ˚,optq ´ ErY2paide, aideqs and Wpπ˚,optq ´ ErY2psmall, smallqs). The table also reports
the proportion of students allocated to each arm pa1, a2q P taide, smallu2. These estimates
were obtained using 5-fold cross-validation. The results show that class-type allocations
under the optimal DTR improve academic achievement by 8.16% and 1.27%, respectively,
compared to uniform allocations to aides or small-size classes. Additionally, under the
DTR allocation, around 23% of students are placed in regular-size classes with a teacher
aide in either grade K or 1. Given the higher cost of small-size classes relative to regular-
size classes with a teacher aide on a per-student basis (Word et al., 1990)18, this ﬁnding
suggests that allocation based on the DTR can reduce the costs associated with class-size
reduction while simultaneously improving students’ academic achievement.
8
Conclusion
We studied the statistical learning of the optimal DTR using observational data and de-
veloped a novel doubly robust approach for learning it under the assumption of sequential
ignorability. Based on backward induction, the approach learns the optimal DTR sequen-
tially, ensuring computational tractability. Our main result shows that the resulting DTR
achieves the optimal convergence rate of n´1{2 for welfare regret under mild conditions
on the MSE convergence rate for estimators of the propensity scores and Q-functions.
The simulation study conﬁrms that the proposed approach outperforms other methods
in ﬁnite sample settings. Applying the proposed approach to Project STAR data, we
estimate the optimal DTR for the sequential allocation of students to regular-size classes
18According to Word et al. (1990), adding a full-time aide in Grades K-3 across Tennessee cost approx-
imately 75 million dollars annually, while reducing class sizes by one-third cost around 196 to 205 million
dollars per year.
25

````

## PDF page 26

Technical extraction; compare with original PDF page 26.

````text
with a teacher aide and small-size classes without one in early education.
26

````

## PDF page 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
Tables
Table 1: Monte Carlo simulation results for DGP1
Sample size (n)
Method
250
500
1000
2000
4000
Q-learn
0.20
0.31
0.43
0.57
0.68
(0.12)
(0.11)
(0.10)
(0.07)
(0.03)
Q-search
0.17
0.29
0.40
0.53
0.64
(0.19)
(0.21)
(0.21)
(0.16)
(0.10)
IPW
0.24
0.29
0.37
0.45
0.55
(0.13)
(0.14)
(0.16)
(0.14)
(0.13)
DR
0.29
0.44
0.61
0.70
0.72
(0.17)
(0.17)
(0.11)
(0.04)
(0.02)
Notes: Each cell shows the mean welfare, with the standard deviation in parentheses, for each method
and sample size. These values are calculated based on 500 simulations using a test sample of 50,000
observations randomly drawn from DGP1.
Table 2: Monte Carlo simulation results for DGP2
Sample size (n)
Method
250
500
1000
2000
4000
Q-learn
1.31
1.69
1.78
1.84
1.89
(0.36)
(0.11)
(0.08)
(0.05)
(0.03)
Q-search
1.26
1.58
1.54
1.52
1.54
(0.48)
(0.18)
(0.09)
(0.04)
(0.08)
IPW
1.30
1.42
1.56
1.68
1.81
(0.21)
(0.17)
(0.19)
(0.21)
(0.19)
DR
1.51
1.77
1.95
2.01
2.04
(0.26)
(0.24)
(0.14)
(0.07)
(0.03)
Notes: Each cell shows the mean welfare, with the standard deviation in parentheses, for each method
and sample size. These values are calculated based on 500 simulations using a test sample of 50,000
observations randomly drawn from DGP2.
Table 3: Empirical results for optimal class-type allocation
Welfare contrast
Share of students in each allocation arm pa1, a2q
(aide, aide)
(small, small)
(aide, aide)
(small, aide)
(aide, small)
(small, small)
8.16%
1.27%
1.0%
17.2%
5.1%
76.7%
Notes: The ﬁrst and second columns present the estimates of the welfare contrasts, deﬁned as
Wpπ˚,optq ´ ErY2paide, aideqs and Wpπ˚,optq ´ ErY2psmall, smallqs, respectively. The third through
sixth columns show the estimated shares of students assigned to the four allocation arms, pa1, a2q P
taide, smallu2, by the optimal DTR.
27

````

## PDF page 28

FORMULA CHECK REQUIRED: original PDF page 28.

````text
Figure
Figure 1: Estimated DTR for class-type allocation in grades K and 1
(a) Policy for grade K
Teacher’s experience ď 19 years
Small
True
Aide
False
(b) Policy for grade 1
Total test score ď 926
Total test score ď 913
Small
True
Aide
False
True
Reading test score ď 434
Aide
True
Small
False
False
Notes: This ﬁgure illustrates the estimated DTR from Section 7. Panels (a) and (b) display the
estimated policy trees for the class-type allocation in grades K and 1, respectively.
28

````

## PDF page 29

FORMULA CHECK REQUIRED: original PDF page 29.

````text
Appendix
A
Proof of Theorem 4.3
This appendix presents the proof of Theorem 4.3, along with some auxiliary lemmas. Our
goal is to derive an asymptotic upper bound on Rpˆπq. This is, however, a non-trivial task
because the components of the DTR, ˆπ “ pˆπ1, . . . , ˆπTq, are estimated sequentially rather
than simultaneously. We therefore cannot directly apply the theoretical analysis of Athey
and Wager (2021) and Zhou et al. (2023b), who study doubly robust policy learning in
single-stage settings. To address this, we present a novel analysis to derive an asymptotic
upper bound on Rpˆπq.
We begin by noting that Lemma 3.1 allows us to analyze the welfare regret, Rpˆπq “
Wpπ˚,optq´Wpˆπq, by evaluating the welfare diﬀerence Wpπ˚,Bq´Wpˆπq between the DTR
π˚,B derived from the population backward optimization problem and the estimated DTR
ˆπ. This reformulation facilitates the analysis of Rpˆπq.
Given the estimated DTR ˆπ, we deﬁne Rˆπt:T
t
pπtq ” Vtpπt, ˆπpt`1q:T q ´ Vtpˆπt:Tq for any
πt P Πt and t “ 1, . . . , T. Rˆπt:T
t
pπtq measures the deviation of policy πt from the sequence
of estimated policies ˆπt:T at stage t with respect to the value function. For t “ T, we
denote RˆπT :T
T
pπT q “ VTpπTq ´ VTpˆπTq.
The following lemma provides a useful result for analyzing the regret Rpˆπq, relating
the regret of the entire DTR to the stage-speciﬁc regrets.
Lemma A.1. Under Assumptions 2.1, 2.3, and 3.1, the regret of ˆπ is bounded from above
as
Rpˆπq ď Rˆπ1:T
1
pπ˚,B
1
q `
Tÿ
t“2
2t´2
ηt´1Rˆπt:T
t
pπ˚,B
t
q.
(A.8)
Proof. See Appendix B.2.
The result (A.8) enables us to evaluate Rpˆπq by evaluating each stage-speciﬁc regret
Rˆπt:T
t
pπ˚,B
t
q (t “ 1, . . . , T), which is simpler to analyze as we will see.
29

````

## PDF page 30

FORMULA CHECK REQUIRED: original PDF page 30.

````text
Given a ﬁxed DTR π “ pπ1, . . . , πTq, we deﬁne
rVi,TpπT q ” Yi,T ´ QTpHi,T, Ai,Tq
eT pHi,T, Ai,Tq
¨ 1tAi,T “ πTpHi,Tqu ` QTpHi,T, πTq,
pVi,TpπT q ” Yi,T ´ pQ´kpiq
T
pHi,T, Ai,Tq
ˆe´kpiq
T
pHi,T, Ai,Tq
¨ 1tAi,T “ πT pHi,Tqu ` pQ´kpiq
T
pHi,T, πTq ,
and recursively for t “ T ´ 1, . . . , 1:
rVi,tpπt:Tq ” Yi,t ` rVi,t`1pπpt`1q:T q ´ Q
πpt`1q:T
t
pHi,t, Ai,tq
etpHi,t, Ai,tq
¨ 1tAi,t “ πtpHi,tqu
` Q
πpt`1q:T
t
pHi,t, πtq,
pVi,tpπt:Tq ” Yi,t ` pVi,t`1pπpt`1q:T q ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, Ai,tq
ˆe´kpiq
t
pHi,t, Ai,tq
¨ 1tAi,t “ πtpHi,tqu
` pQ
πpt`1q:T ,´kpiq
t
pHi,t, πtq.
(A.9)
Note that the sample mean p1{nq řn
i“1 rVi,t pπt:Tq is an oracle estimate of the policy value
function Vtpπt:Tq with oracle access to tQπs:T
s
p¨, ¨qus“t`1,...,T and tesp¨, ¨qus“t,...,T. Lemma
B.2 in Appendix B.1 shows that p1{nq řn
i“1 rVi,t pπt:T q is an unbiased estimator of the policy
value Vtpπt:Tq under the sequential ignorability (Assumption 2.1).
Following the analysis of Zhou et al. (2023b), for each stage t “ 1, . . . , T, we de-
ﬁne the policy value diﬀerence function ∆tp¨; ¨q : Πt:T ˆ Πt:T Ñ R, the oracle inﬂuence
diﬀerence function r∆tp¨; ¨q : Πt:T ˆ Πt:T Ñ R, and the estimated policy value diﬀer-
ence function p∆tp¨; ¨q : Πt:T ˆ Πt:T Ñ R, as follows: For πa
t:T “ pπa
t , . . . , πa
Tq P Πt:T and
πb
t:T “ pπb
t, . . . , πb
Tq P Πt:T,
∆tpπa
t:T; πb
t:Tq ” Vtpπa
t:Tq ´ Vtpπb
t:Tq,
(A.10)
r∆tpπa
t:T; πb
t:Tq ” 1
n
nÿ
i“1
rVi,t pπa
t:Tq ´ 1
n
nÿ
i“1
rVi,t
`
πb
t:T
˘
,
(A.11)
p∆tpπa
t:T; πb
t:Tq ” 1
n
nÿ
i“1
pVi,t pπa
t:Tq ´ 1
n
nÿ
i“1
pVi,t
`
πb
t:T
˘
.
From the deﬁnitions, the stage-speciﬁc regret Rˆπt:T
t
pπ˚,B
t
q is expressed as
Rˆπt:T
t
pπ˚,B
t
q “ ∆t
´
π˚,B
t
, ˆπpt`1q:T ; ˆπt:T
¯
.
30

````

## PDF page 31

FORMULA CHECK REQUIRED: original PDF page 31.

````text
In what follows, we evaluate Rˆπt:T
t
pπ˚,B
t
q for each t.
A standard argument of the
statistical learning theory (e.g., Lugosi, 2002) gives
Rˆπt:T
t
pπ˚,B
t
q “ ∆t
´
π˚,B
t
, ˆπpt`1q:T ; ˆπt:T
¯
ď ∆t
´
π˚,B
t
, ˆπpt`1q:T ; ˆπt:T
¯
´ p∆t
´
π˚,B
t
, ˆπpt`1q:T ; ˆπt:T
¯
ď
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ p∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
ď
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
`
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|p∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|,
(A.12)
where the ﬁrst inequality follows because ˆπt maximizes p1{nq řn
i“1 pΓ
ˆπpt`1q:T
i,t
pπtpHi,tqq over
Πt; hence, p∆t
´
π˚,B
t
, ˆπpt`1q:T ; ˆπt:T
¯
ď 0.
We can now evaluate Rˆπt:T
t
pπ˚,B
t
q by evaluating
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
(A.13)
and
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|p∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|.
(A.14)
As for the former, we apply the uniform concentration result of Zhou et al.
(2023b,
Lemma 2) for the oracle inﬂuence diﬀerence function to obtain the following lemma.
Lemma A.2. Suppose that Assumptions 2.1, 2.2, 2.3, and 4.2 hold. Then, for any stage
t P t1, 2, . . . , Tu and δ P p0, 1q, with probability at least 1 ´ 2δ, the following holds:
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
ď
˜
54.4
?
2κpΠt:Tq ` 435.2 `
c
2 log 1
δ
¸ c
M˚
t:T
n
` o
ˆ 1
?n
˙
,
(A.15)
where M˚
t:T ” M ¨
´
1 ` 2η´T`t´1 ` řT´t
s“1 3η´s¯
ă 8.
31

````

## PDF page 32

FORMULA CHECK REQUIRED: original PDF page 32.

````text
Proof. See Appendix B.1.
To evaluate the latter (equation (A.14)), we consider extending the analytical approach
of Athey and Wager (2021) and Zhou et al. (2023b), which leverages orthogonal moments
and cross-ﬁtting, to the sequential multi-stage setting. A key challenge arises from the
recursive structure of pVi,tpπt:T q, which depends on pVi,t`1pπpt`1q:T q as deﬁned in equation
(A.9). This dependency prevents a direct application of the existing analytical techniques.
To address this, we develop an extension that accommodates the recursive nature of the
value function.
Speciﬁcally, we further decompose pVi,tpπt:Tq by introducing the following functionals:
ˇVi,TpπTq ” Yi,T ´ QTpHi,T, Ai,Tq
ˆe´kpiq
T
pHi,T, Ai,Tq
¨ 1tAi,T “ πTpHi,Tqu ` QT pHi,T, πTq ;
ˇVi,tpπt:Tq ” Yi,t ` rVi,t`1pπpt`1q:T q ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, Ai,tq
ˆe´kpiq
t
pHi,t, Ai,tq
¨ 1tAi,t “ πtpHi,tqu
` pQ
πpt`1q:T ,´kpiq
t
pHi,t, πtq.
for t “ 1, . . . , T ´ 1. The functional ˇVi,tpπt:Tq is similar to pVi,tpπt:Tq, but it replaces the
estimated future value function pVi,t`1pπpt`1q:T q with the oracle one rVi,t`1pπpt`1q:T q. As a
result, ˇVi,tpπt:T q does not have a recursive structure.
We can then decompose pVi,tpπt:Tq as follows:
pVi,tpπt:Tq “ ˇVi,tpπt:T q `
1
ˆe´kpiq
t
pHi,t, πtq
´
pVi,t`1pπpt`1q:T q ´ rVi,t`1pπpt`1q:T q
¯
“ ˇVi,tpπt:T q `
T´1
ÿ
s“t
1
śs
ℓ“t ˆe´kpiq
ℓ
pHi,ℓ, πℓq
´
ˇVi,s`1pπps`1q:T q ´ rVi,s`1pπps`1q:T q
¯
.
We hence have
pVi,tpπt:T q ´ rVi,tpπt:Tq “
Tÿ
s“t
´
ˇV :
i,t,spπt:Tq ´ rV :
i,t,spπt:Tq
¯
(A.16)
with
ˇV :
i,t,spπt:Tq ”
1
śs´1
ℓ“t ˆe´kpiq
ℓ
pHi,ℓ, πℓq
ˇVi,spπs:Tq and rV :
i,t,spπt:Tq ”
1
śs´1
ℓ“t ˆe´kpiq
ℓ
pHi,ℓ, πℓq
rVi,spπs:Tq,
32

````

## PDF page 33

FORMULA CHECK REQUIRED: original PDF page 33.

````text
where we deﬁne śs´1
ℓ“t ˆe´kpiq
ℓ
pHi,ℓ, πℓq “ 1 for s ď t.
Using the result (A.16), we can bound (A.14) from above as
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
ˇˇˇp∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q
ˇˇˇ
ď
Tÿ
s“t
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
ˇˇˇ ˇ∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q
ˇˇˇ ,
(A.17)
where
ˇ∆:
t,spπa
t:T; πb
t:Tq ” 1
n
nÿ
i“1
ˇV :
i,t,s pπa
t:Tq ´ 1
n
nÿ
i“1
ˇV :
i,t,s
`
πb
t:T
˘
and
r∆:
t,spπa
t:T; πb
t:Tq ” 1
n
nÿ
i“1
rV :
i,t,s pπa
t:Tq ´ 1
n
nÿ
i“1
rV :
i,t,s
`
πb
t:T
˘
.
The bound in (A.17) is easier to analyze than (A.14) because ˇVi,tpπt:Tq does not have
a recursive structure, though some complexity arises from the dependence of rV :
i,t,s pπa
t:Tq
on the estimated propensity scores
!
ˆe´kpiq
ℓ
p¨, ¨q
)
ℓ“t,...,s´1. The extended analysis in Ap-
pendix B.3 leads to the following lemma.
Lemma A.3. Suppose that Assumptions 2.1, 2.2, 2.3, and 4.1 hold.
Then, for any
integers s and t such that 1 ď t ď s ď T, the following holds:
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
ˇˇˇ ˇ∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q
ˇˇˇ
“ Oppn´ mint1{2,τ{2uq.
Proof. See Appendix B.3.
Combining all the above results yields the desired proof.
Proof of Theorem 4.3. Combining the inequalities (A.12) and (A.17) with Lemmas A.2
and A.3, we obtain
Rˆπt:T
t
pπ˚,B
t
q “ Op
`
κpΠt:T q ¨ n´1{2˘
` Oppn´ mint1{2,τ{2uq
33

````

## PDF page 34

FORMULA CHECK REQUIRED: original PDF page 34.

````text
for all t “ 1, . . . , T. This result proves Theorem 4.3 via the inequality (A.8) in Lemma
A.1.
B
Preliminary Results and Proofs of Lemmas 3.1,
4.2, A.1, A.2, and A.3
B.1
Preliminary Results and Proofs of Lemmas 3.1, 4.2, and
A.2
This section presents several preliminary results and proofs of Lemmas 3.1, 4.2, and A.2.
We begin by providing the proof of Lemma 4.2.
Lemma B.1 below establishes a connection between the ǫ-Hamming covering numbers
of classes for stage-speciﬁc policies and a class for sequences of policies, and will be used
to prove Lemma 4.2.
Lemma B.1. Given a class of DTRs Π “ Π1 ˆ ¨ ¨ ¨ ˆ ΠT, for any integers s and t such
that 1 ď s ď t ď T, the following inequality holds:
Ndhppt ´ s ` 1qǫ, Πs:tq ď
tź
ℓ“s
Ndhpǫ, Πℓq.
Proof. Fix a set of history points thp1q
t , . . . , hpnq
t u Ď Hh.
For any integer ℓ(ď t), let
hpiq
ℓpĎ hpiq
t q be the partial history up to stage ℓ. Let Kℓ” Ndhpǫ, Πℓ, thp1q
ℓ, . . . , hpnq
ℓuq. For
each ℓP ts, . . . , tu, we denote by rΠℓ”
´
πp1q
ℓ, . . . , πpKℓq
ℓ
¯
the set of policies such that for
any πℓP Πℓ, there exists πpiq
ℓ
P rΠℓsatisfying dhpπℓ, πpiq
ℓq ď ǫ. Such a set of policies exists
from the deﬁnition of Ndhpǫ, Πℓ, thp1q
ℓ, . . . , hpnq
ℓuq.
Fix πs:t P Πs:t, and deﬁne rΠs:t ” rΠs ˆ ¨ ¨ ¨ ˆ rΠt. Let ˜πs:t “ p˜πs, . . . , ˜πtq P rΠs:t be such
that for any ℓP ts, . . . , tu, dhpπℓ, ˜πℓq ď ǫ. Then
dhpπs:t, ˜πs:tq “ 1
n
nÿ
i“1
1tπsphpiq
s q ‰ ˜πsphpiq
s q _ ¨ ¨ ¨ _ πtphpiq
t q ‰ ˜πtphpiq
t qu
ď
tÿ
ℓ“s
˜
1
n
nÿ
i“1
1tπℓphpiq
ℓq ‰ ˜πℓphpiq
ℓqu
¸
34

````

## PDF page 35

FORMULA CHECK REQUIRED: original PDF page 35.

````text
“
tÿ
ℓ“s
dhpπℓ, ˜πℓq ď pt ´ s ` 1qǫ.
Therefore, for any πs:t P Πs:t, there exists ˜πs:t P rΠs:t such that dhpπs:t, ˜πs:tq ď pt ´ s `
1qǫ. Since
ˇˇˇrΠs:t
ˇˇˇ “ śt
ℓ“s
ˇˇˇrΠℓ
ˇˇˇ “ śt
ℓ“s Ndhpǫ, Πℓ, thp1q
ℓ, . . . , hpnq
ℓuq, where | ¨ | denotes the
cardinality, we have
Ndh
´
pt ´ s ` 1qǫ, Πs:t, thp1q
t , . . . , hpnq
t u
¯
ď
tź
ℓ“s
Ndh
´
ǫ, Πℓ, thp1q
ℓ, . . . , hpnq
ℓu
¯
.
As this holds for any n and any set of history points thp1q
t , . . . , hpnq
t u, the result in the
statement holds.
Using Lemma B.1, we present the proof of Lemma 4.2 below.
Proof of Lemma 4.2.
Note that Π “ Π1:T.
Applying Lemma B.1 to Π, we have
NHpǫ2, Πq ď śT
t“1 NHpǫ2{T, Πtq. Then
κpΠq “
ż 1
0
a
log NH pǫ2, Πqdǫ ď
ż 1
0
g
f
f
e
Tÿ
t“1
log NHpǫ2{T, Πtqdǫ
ď
Tÿ
t“1
ż 1
0
a
log NHpǫ2{T, Πtqdǫ
ď T
ż 1
0
d
log C ` D
ˆ?
T
ǫ
˙2ω
dǫ
ď T
ż 1
0
a
log Cdǫ ` T
ż 1
0
d
D
ˆ?
T
ǫ
˙2ω
dǫ
“ T
a
log C `
?
T p2`ωq?
D
ż 1
0
ǫ´ωdǫ “ T
a
log C `
?
T p2`ωqD
1 ´ ω
ă 8,
where the third and last lines follow from Assumption 4.2.
✷
We next give several preliminary results. We ﬁrst deﬁne the conditional policy value
35

````

## PDF page 36

FORMULA CHECK REQUIRED: original PDF page 36.

````text
of πt:T for stage t as, for any ht “ pat´1, stq P Ht,
Vt pπt:T ; htq ” E
»
–
Tÿ
s“t
ÿ
a1
t:sPAt:s
˜
Yspat´1, a1
t:sq ¨
sź
ℓ“t
1tπℓ
`
Hℓpat´1, a1
t:pℓ´1qq
˘
“ a1
ℓu
¸ˇˇˇˇˇˇ
Ht “ ht
ﬁ
ﬂ,
where Hℓpapt´1q, a1
t:pℓ´1qq “ Htpapt´1qq for ℓ“ t. Note that E rVtpπt:T; Htqs “ Vtpπt:Tq. For
ease of notations, for any stages s and t such that s ě t and any policy sequence πt:s P Πt:s,
we deﬁne
rYt:s
`
at´1, πt:s
˘
”
ÿ
a1
t:sPAt:s
˜
Yspat´1, a1
t:sq ¨
s
ź
ℓ“t
1tπℓ
`
Hℓpat´1, a1
t:pℓ´1qq
˘
“ a1
ℓu
¸
.
Let rYt
`
at´1, πt
˘
denote rYt:s
`
at´1, πt:s
˘
when t “ s. Note that, for any πt:T P Πt:T and
ht “ pat´1, stq P Ht, V pπt:T ; htq can be written as
E
« Tÿ
s“t
rYt:s
`
at´1, πt:s
˘
ˇˇˇˇˇHt “ ht
ﬀ
“ Vtpπt:T; htq.
The following lemma will used in the proofs of Lemmas 3.1, A.2, and A.3.
Lemma B.2. Suppose that Assumption 2.1 holds. Then, for any stage t and DTR π P Π,
the following hold:
(i) Q
πpt`1q:T
t
pht, πtq “ Vtpπt:T ; htq for any ht P Ht;
(ii) E
”
rVi,tpπt:T q
ı
“ Vtpπt:Tq for any i “ 1, . . . , n.
Proof. We ﬁrst prove (i), where we basically follow the proof of Tsiatis et al.
(2019,
equation (6.53)). For t “ T, the following holds for any hT “ paT´1, sTq P HT:
QTphT, πTq “ E rYT|AT “ πTphT q, HT “ hTs
“ E rYTpATq|AT “ πTphT q, HT “ hts
“ E
“
YTpaT´1, πTphTqq|AT “ πTphTq, HT “ ht
‰
“
ÿ
aT PAT
E
“
YTpaT´1, aTq ¨ 1taT “ πT phTqu
ˇˇAT “ aT, HT “ ht
‰
“
ÿ
aT PAT
E
“
YTpaT´1, aTq ¨ 1taT “ πT phTqu
ˇˇHT “ ht
‰
36

````

## PDF page 37

FORMULA CHECK REQUIRED: original PDF page 37.

````text
“ E
« ÿ
aT PAT
YTpaT´1, aTq ¨ 1taT “ πT pHTpaT´1qqu
ˇˇˇˇˇHT “ hT
ﬀ
“ VTpπT ; hTq,
(B.1)
where the ﬁfth equality follows from Assumption 2.1.
For any integer t such that t ă T, the following holds for any ht “ pat´1, stq P Ht:
E
“
Yt ` Vt`1pπpt`1q:T ; Ht`1q|At “ πtphtq, Ht “ ht
‰
“ E
«
Yt patq `
Tÿ
s“t`1
rYpt`1q:spat´1, πtphtq, πpt`1q:sq
ˇˇˇˇˇAt “ πtphhq, Ht “ ht
ﬀ
“
ÿ
atPAt
˜
E
«
Yt
`
at´1, at
˘
`
Tÿ
s“t`1
rYpt`1q:spat´1, at, πpt`1q:sq
ˇˇˇˇˇAt “ at, Ht “ ht
ﬀ
¨ 1tπtphtq “ atu
¸
“
ÿ
atPAt
˜
E
«
Yt
`
at´1, at
˘
`
Tÿ
s“t`1
rYpt`1q:spat´1, at, πpt`1q:sq
ˇˇˇˇˇHt “ ht
ﬀ
¨ 1tπtphtq “ atu
¸
“ E
«
Yt
`
at´1, πtphtq
˘
`
Tÿ
s“t`1
rYpt`1q:spat´1, πtphtq, πpt`1q:sq
ˇˇˇˇˇHt “ ht
ﬀ
“ E
«
Yt
`
at´1, πtphtq
˘
`
Tÿ
s“t`1
rYpt`1q:spAt´1, πtphtq, πpt`1q:sq
ˇˇˇˇˇHt “ ht
ﬀ
“ E
« Tÿ
s“t
rYspat´1, πt:sq
ˇˇˇˇˇHt “ ht
ﬀ
“ Vtpπt:T ; htq,
(B.2)
where the ﬁrst equality follows from the law of total expectations, and the third equality
follows from Assumption 2.1.
When t “ T ´ 1,
QπT
T´1phT´1, πT´1q “ E rYT´1 ` QTpHT, πTq|AT´1 “ πT´1phT´1q, HT´1 “ hT´1s
“ E rYT´1 ` VTpπT; HTq|AT´1 “ πT´1phT´1q, HT´1 “ hT´1s
“ VT´1pπpT´1q:T; hT´1q,
where the second and third equalities follow from equations (B.1) and (B.2), respectively.
Recursively applying the same argument from t “ T ´ 2 to 1, we have Q
πpt`1q:T
t
pht, πtq “
Vtpπt:T; htq for any t and ht P Ht, which leads to the result (i).
37

````

## PDF page 38

FORMULA CHECK REQUIRED: original PDF page 38.

````text
We proceed to prove (ii). Given a ﬁxed DTR π “ pπ1, . . . , πTq, to simply notation, we
deﬁne the independent copies of trVi,tpπt:T q : t “ 1, . . . , Tu as follows:
rVTpπT q ” YT ´ QTpHT, ATq
eTpHT, ATq
¨ 1tAT “ πTpHTqu ` QTpHT, πTpHTqq,
and, recursively for t “ T ´ 1, . . . , 1,
rVtpπt:T q ” Yt ` rVt`1pπpt`1q:T q ´ Q
πpt`1q:T
t
pHt, Atq
etpHt, Atq
¨ 1tAt “ πtpHtqu
` Q
πpt`1q:T
t
pHt, πtpHtqq.
Note that E
”
rVTpπTq
ı
“ E
”
rVi,TpπT q
ı
and E
”
rVtpπt:T q
ı
“ E
”
rVi,tpπt:T q
ı
for any i and t.
We ﬁrst consider the case that t “ T. Regarding the ﬁrst component in rVTpπTq, for
any hT P HT,
E
„
YT ¨ 1tAT “ πT pHTqu
eTpHT, ATq
ˇˇˇˇHT “ hT

“ E
„
E rYT|AT “ πT pHTq, HTs ¨ 1tAT “ πTpHTqu
eTpHT, ATq
ˇˇˇˇHT “ hT

“ E
„
QTpHT, πTq ¨ 1tAT “ πTpHTqu
eT pHT, ATq
ˇˇˇˇHT “ hT

,
where the last equality follows from the deﬁnition of QTpHT, πTq.
Therefore, we have
E
”
rVTpπTq
ˇˇˇHi,T “ hT
ı
“ E
„
pQTpHT, ATq ´ QTpHT, ATqq ¨ 1tAT “ πTpHTqu
eT pHT, ATq
ˇˇˇˇHT “ hT

` QTphT, πTq
“ QTphT, πTq “ VTpπT ; hTq,
(B.3)
where the last equality follows from the result (i). We consequently have E
”
rVTpπTq
ı
“
ErVTpπT; HTqs “ VTpπTq.
When t “ T ´ 1, for any hT´1 P HT´1,
E
„´
YT´1 ` rVTpπTq
¯
¨ 1tAT´1 “ πT´1pHT´1qu
eT pHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

38

````

## PDF page 39

FORMULA CHECK REQUIRED: original PDF page 39.

````text
“ E
„´
YT´1 ` E
”
rVTpπTq
ˇˇˇHT
ı¯
¨ 1tAT´1 “ πT´1pHT´1qu
eT pHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

“ E
„
pYT´1 ` VTpπT; HTqq ¨ 1tAT´1 “ πT´1pHT´1qu
eTpHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

“ E
„
pYT´1 ` QTpHT, πTqq ¨ 1tAT´1 “ πT´1pHT´1qu
eT pHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

“ E rE rYT´1 ` QTpHT, πTq|AT´1 “ πT´1pHT´1q, HT´1s
ˆ1tAT´1 “ πT´1pHT´1qu
eTpHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

“ E
„
QπT
T´1pHT´1, AT´1q ¨ 1tAT´1 “ πT´1pHT´1qu
eTpHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

,
where the second equality follows from the result (B.3); the third equality follow from the
result (i); the last equality follows from the deﬁnition of the Q-function QπT
T´1p¨, ¨q.
Therefore, for any hT´1 P HT´1,
E
”
rVT´1pπpT´1q:T q
ˇˇˇHT´1 “ hT´1
ı
“ E
„´
YT´1 ` rVTpπTq ´ QπT
T´1pHT´1, AT´1q
¯
¨ 1tAT´1 “ πT´1pHT´1qu
eT pHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

` QπT
T´1phT´1, πT´1q
“ E
„`
QπT
T´1pHT´1, AT´1q ´ QπT
T´1pHT´1, AT´1q
˘
¨ 1tAT´1 “ πT´1pHT´1qu
eTpHT´1, AT´1q
ˇˇˇˇHT´1 “ hT´1

` QπT
T´1phT´1, πT´1q
“ QπT
T´1phT´1, πT´1q “ VT´1pπpT´1q:T ; hT´1q,
where the last equality follows from the result (i). Hence, we have E
”
rVT´1pπpT´1q:T q
ı
“
E
“
VT´1pπpT´1q:T; HT´1q
‰
“ VT´1pπpT´1q:T q.
Recursively applying the same argument from t “ T ´ 2 to 1, we have E
”
rVtpπt:T q
ı
“
Vtpπt:Tq for any t, which proves the result (iii).
We next provide the proof of Lemma 3.1, which extends the proof of Tsiatis et al.
(2019, equation (7.21)) to the case under Assumption 3.1.
Proof of Lemma 3.1. Let π P Π be ﬁxed. Under Assumptions 2.3 and 3.1, π˚,B satis-
ﬁes the condition in Assumption 3.1. For any t “ 1, . . . , T, comparing the welfares of
39

````

## PDF page 40

FORMULA CHECK REQUIRED: original PDF page 40.

````text
pπ1:pt´1q, π˚,B
t:T q and pπ1:t, π˚,B
pt`1q:T q yields:
Wpπ1:pt´1q, π˚,B
t:T q ´ Wpπ1:t, π˚,B
pt`1q:T q
“ V1pπ1:pt´1q, π˚,B
t:T q ´ V1pπ1:t, π˚,B
pt`1q:T q
“ E
„
Q
π2:pt´1q,π˚,B
t:T
1
pH1, π1q ´ Q
π2:t,π˚,B
pt`1q:T
1
pH1, π1q

“ E
„
E
„
Q
π˚,B
pt`1q:T
t
pHt, π˚,B
t
q ´ Q
π˚,B
pt`1q:T
t
pHt, πtq
ˇˇˇˇA1 “ π1pH1q, . . . , At´1 “ πt´1pHt´1q, Ht´1

ě 0,
where we denote Wpπ1:p0q, π˚,B
1:T q “ Wpπ˚,Bq and Wpπ1:T, π˚,B
pT`1q:Tq “ Wpπq for t “ 1 and
t “ T, respectively; the second equality follows from Lemma B.2 (i); the third equality
follows from the deﬁnitions of the Q-functions; the inequality follows from Assumption
3.1. We therefore obtain Wpπ1:pt´1q, π˚,B
t:T q ě Wpπ1:t, π˚,B
pt`1q:T q for any t “ 1, . . . , T.
Applying this result, we have
Wpπ˚,Bq ´ Wpπq “
Tÿ
t“1
´
Wpπ1:pt´1q, π˚,B
t:T q ´ Wpπ1:t, π˚,B
pt`1q:T q
¯
ě 0.
Since this result holds for any π P Π, we obtain the result in Lemma 3.1.
✷
The following lemma, which follows from Lemma 2 in Zhou et al. (2023b) and its
proof, plays important roles in the proofs of Theorem 4.3.
Lemma B.3. Fix integers s and t such that 1 ď s ď t ď T.
For any as:t P As:t,
let tΓ:
ipas:tqun
i“1 be i.i.d. random variables with bounded supports. For any πs:t P Πs:t,
we deﬁne rQpπs:tq ” p1{nq řn
i“1 Γ:
ipπs:tq, where Γ:
ipπs:tq ” Γ:
ippπspHi,sq, . . . , πtpHi,tqqq and
Qpπs:tq ” Er rQpπs:tqs. For any πa
s:t, πb
s:t P Πs:t, let r∆pπa
s:t, πb
s:tq ” rQpπa
s:tq ´ rQpπb
s:tq and
∆pπa
s:t, πb
s:tq ” Qpπa
s:tq ´ Qpπb
s:tq. Then, when κpΠs:tq ă 8, the following holds: For any
δ P p0, 1q, with probability at least 1 ´ 2δ,
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇr∆pπa
s:t, πb
s:tq ´ ∆pπa
s:t, πb
s:tq
ˇˇˇ ď
˜
54.4
?
2κpΠs:tq ` 435.2 `
c
2 log 1
δ
¸ c
V ˚
s:t
n
` o
ˆ 1
?n
˙
,
40

````

## PDF page 41

FORMULA CHECK REQUIRED: original PDF page 41.

````text
where V ˚
s:t ” supπa
s:t,πb
s:tPΠs:t E
„´
Γ:
ipπa
s:tq ´ Γ:
ipπb
s:tq
¯2
ă 8.
Using Lemma B.3, we present the proof of Lemma A.2 as follows.
Proof of Lemma A.2.
Given a ﬁxed DTR π “ pπ1, . . . , πTq, we deﬁne the recursive
expression for t “ T, . . . , 1 as
rΓ
πpt`1q:T
i,t
pat:T q ”
Yi,t ` rΓ
πpt`2q:T
i,t`1
papt`1q:T q ´ Q
πpt`1q:T
t
pHi,t, Ai,tq
etpHi,t, Ai,tq
¨ 1tAi,t “ atu
` Q
πpt`1q:T
t
pHi,t, atq,
where we assume rΓ
πpt`1q:T
i,t
pat:Tq “ 0 when t “ T ` 1. For any πpt`1q:T P Πpt`1q:T and
π1
t:T “ pπ1
t, . . . , π1
Tq P Πt:T, let rΓ
πpt`1q:T
i,t
pπ1
t:Tq ” rΓ
πpt`1q:T
i,t
pπ1
tpHi,tq, . . . , π1
TpHi,Tqq. Note that
rΓ
πpt`1q:T
i,t
pπt:Tq “ rVi,tpπt:Tq.
Fix πpt`1q:T P Πpt`1q:T . For any πa
t:T, πb
t:T P Πt:T, we deﬁne
r∆πpt`1q:T pπa
t:T, πb
t:Tq ” 1
n
nÿ
i“1
´
rΓ
πpt`1q:T
i,t
pπa
t:Tq ´ rΓ
πpt`1q:T
i,t
pπb
t:Tq
¯
and
∆πpt`1q:T pπa
t:T, πb
t:Tq ” E
«
1
n
nÿ
i“1
´
rΓ
πpt`1q:T
i,t
pπa
t:Tq ´ rΓ
πpt`1q:T
i,t
pπb
t:Tq
¯ﬀ
.
Note that
r∆πpt`1q:Tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q “ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q,
where r∆tp¨; ¨q is deﬁned in (A.11). Noting that
∆πpt`1q:T pπa
t , πpt`1q:T ; πb
t, πpt`1q:T q “ E
”
rVi,tpπa
t , πpt`1q:T q
ı
´ E
”
rVi,tpπb
t, πpt`1q:T q
ı
,
Lemma B.2 leads to
∆πpt`1q:Tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q “ ∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q,
where ∆tp¨; ¨q is deﬁned in (A.10).
41

````

## PDF page 42

FORMULA CHECK REQUIRED: original PDF page 42.

````text
Therefore, it follows for (A.13) that
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆tpπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
“
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|r∆πpt`1q:T pπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ ∆πpt`1q:T pπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
ď
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t:T ,πb
t:T PΠt:T
|r∆πpt`1q:T pπa
t:T; πb
t:Tq ´ ∆πpt`1q:T pπa
t:T ; πb
t:Tq|.
(B.4)
Fix πpt`1q:T P Πpt`1q:T . Note that
!
rΓ
πpt`1q:T
i,t
pat:Tq
)
i“1,...,n are i.i.d. random variables
with bounded supports under Assumptions 2.2 and 2.3 and that κpΠt:T q is ﬁnite from
Lemma 4.2 and κpΠt:T q ď κpΠq. Therefore, ﬁxing πpt`1q:T and applying Lemma B.3 with
Γ:
ipat:Tq “ rΓ
πpt`1q:T
i,t
pat:Tq leads to the following result: For any δ P p0, 1q, with probability
at least 1 ´ 2δ,
sup
πa
t:T ,πb
t:T PΠt:T
|r∆πpt`1q:T pπa
t:T; πb
t:T q ´ ∆πpt`1q:T pπa
t:T; πb
t:Tq|
ď
˜
54.4
?
2κpΠt:Tq ` 435.2 `
c
2 log 1
δ
¸ d
V
πpt`1q:T ,˚
t:T
n
` o
ˆ 1
?n
˙
,
(B.5)
with V
πpt`1q:T ,˚
t:T
” supπa
t:T ,πb
t:T PΠt:T E
„´
rΓ
πpt`1q:T
i,t
pπa
t:Tq ´ rΓ
πpt`1q:T
i,t
pπb
t:Tq
¯2
.
Under Assumptions 2.2 and 2.3, V
πpt`1q:T ,˚
t:T
ď M˚
t:T ă 8 for any πpt`1q:T . Therefore,
combining (B.4) and (B.5) leads to the result (A.15).
✷
B.2
Proof of Lemma A.1
We present the proof of Lemma A.1 in this section. The following lemma is a general
version of Lemma A.1.
Lemma B.4. Fix π “ pπ1, . . . , πTq P Π. Let Rπt:T
t
p˜πtq ” Vtp˜πt, πpt`1q:T q ´ Vtpπt:T q for any
˜πt P Πt. Then, under Assumptions 2.1, 2.3, and 3.1, the regret of π is bounded from above
as
Rpπq ď Rπ1:T
1
pπ˚,B
1
q `
Tÿ
t“2
2t´2
ηt´1Rπt:T
t
pπ˚,B
t
q.
42

````

## PDF page 43

FORMULA CHECK REQUIRED: original PDF page 43.

````text
Proof. For any t, deﬁne Rtpπt:T q ” Vtpπ˚,B
t:T q ´ Vtpπt:Tq, which is a partial regret of πt:T for
stage t. Under Assumptions 2.3 and 3.1, π˚,B satisﬁes the condition in Assumption 3.1.
For any integers s and t such that 1 ď t ă s ď T,
Vtpπ˚,B
t
, . . . , π˚,B
T
q ´ Vtpπ˚,B
t
, . . . , π˚,B
s´1, πs, . . . , πTq
“ E
«śs´1
ℓ“t 1tAℓ“ π˚,B
ℓ
pHℓqu
śs´1
ℓ“t eℓpHℓ, Aℓq
¨
ˆ
Q
π˚,B
ps`1q:T
s
`
Hs, π˚,B
s
˘
´ Q
πps`1q:T
s
pHs, πsq
˙ﬀ
ď
1
ηs´tE
„ˆ
Q
π˚,B
ps`1q:T
s
`
Hs, π˚,B
s
˘
´ Q
πps`1q:T
s
pHs, πsq
˙
“
1
ηs´t
´
Vspπ˚,B
s:T q ´ Vspπs:Tq
¯
“
1
ηs´tRs pπt:T q ,
(B.6)
where the ﬁrst equality follows from Lemma B.2 (i) and Assumption 2.1; the inequality
follows from Assumptions 2.3 and 3.1; the second equality follows from Lemma B.2 (i).
For t “ T and T ´ 1, we have
RT pπTq “ VTpπ˚,B
T
q ´ VTpπTq “ RπT
T pπ˚,B
T
q;
RT´1
`
πpT´1q:T
˘
“
”
VT´1
´
π˚,B
T´1, π˚,B
T
¯
´ VT´1
´
π˚,B
T´1, πT
¯ı
`
”
VT´1
´
π˚,B
T´1, πT
¯
´ VT´1 pπT´1, πTq
ı
ď 1
ηRπT
T pπ˚,B
T
q ` R
πpT ´1q:T
T´1
´
π˚,B
T´1
¯
“ 1
ηRTpπTq ` R
πpT ´1q:T
T´1
´
π˚,B
T´1
¯
,
where the inequality follows from (B.6).
Generally, for k “ 2, . . . , T ´ 1, it follows that
RT´k
`
πpT´kq:T
˘
“ VT´k
´
π˚,B
T´k, . . . , π˚,B
T
¯
´ VT´k pπT´k, . . . , πTq
“
Tÿ
s“T´k
”
VT´k
´
π˚,B
T´k, . . . , π˚,B
s
, πs`1, . . . , πT
¯
´ VT´k
´
π˚,B
T´k, . . . , π˚,B
s´1, πs, . . . , πT
¯ı
“
Tÿ
s“T´k`1
”
VT´k
´
π˚,B
T´k, . . . , π˚,B
s
, πs`1, . . . , πT
¯
´ VT´k
´
π˚,B
T´k, . . . , π˚,B
s´1, πs, . . . , πT
¯ı
` R
πpT ´kq:T
T´k
pπ˚,B
T´kq
43

````

## PDF page 44

FORMULA CHECK REQUIRED: original PDF page 44.

````text
ď
Tÿ
s“T´k`1
”
VT´k
´
π˚,B
T´k, . . . , π˚,B
T
¯
´ VT´k
´
π˚,B
T´k, . . . , π˚,B
s´1, πs, . . . , πT
¯ı
` R
πpT ´kq:T
T´k
pπ˚,B
T´kq
ď
Tÿ
s“T´k`1
1
ηs´T`k Rs pπt:T q ` R
πpT ´kq:T
T´k
pπ˚,B
T´kq,
where the second equality follows from the telescoping sum; the third equality follows
from the deﬁnition of R
πpT ´kq:T
T´k
pπ˚,B
T´kq; the ﬁrst inequality follows from Lemma B.2 and
Assumption 3.1; the last line follows from (B.6).
Then, recursively, the following hold:
RT´1
`
πpT´1q:T
˘
ď 1
ηRT pπTq ` R
πpT ´1q:T
T´1
pπ˚,B
T´1q
“ 1
ηRπT
T
´
π˚,B
T
¯
` R
πpT ´1q:T
T´1
pπ˚,B
T´1q,
RT´2
`
πpT´2q:T
˘
ď 1
ηRT´1
`
πpT´1q:T
˘
` 1
η2RT pπT q ` R
πpT ´2q:T
T´2
pπ˚,B
T´2q
ď 2
η2RπT
T
´
π˚,B
T
¯
` 1
ηR
πpT ´1q:T
T´1
´
π˚,B
T´1
¯
` R
πpT ´2q:T
T´2
pπ˚,B
T´2q,
...
RT´k
`
πpT´kq:T
˘
ď
kÿ
s“1
2k´s
ηk´s`1R
πpT ´s`1q:T
T´s`1
pπ˚,B
T´s`1q ` R
πpT ´kq:T
T´k
pπ˚,B
T´kq.
Therefore, setting k “ T ´ 1 and noting that R1 pπ1:Tq “ Rpπq, we obtain
Rpπq ď
T´1
ÿ
s“1
2T´1´s
ηT´s R
πpT ´s`1q:T
T´s`1
pπ˚,B
T´s`1q ` Rπ1:T
1
pπ˚,B
1
q
“ Rπ1:T
1
pπ˚,B
1
q `
T´1
ÿ
s“1
2s´1
ηs R
πps`1q:T
s`1
pπ˚,B
s`1q.
Setting t “ s ` 1 in the above equation leads to the result.
The proof of Lemma A.1 is given below.
Proof of Lemma A.1. Lemma A.1 follows immediately from Lemma B.4 with setting
π “ ˆπ.
✷
44

````

## PDF page 45

FORMULA CHECK REQUIRED: original PDF page 45.

````text
B.3
Proof of Lemma A.3
This section presents the proof of Lemma A.3. We here extend the analytical strategy of
Athey and Wager (2021) and Zhou et al. (2023b), which leverages orthogonal moments
and cross-ﬁtting, to the sequential multi-stage setting.
We begin by introducing several notational deﬁnitions.
For any at:s P At:s and
πa
t:s, πb
t:s P Πt:s (t ď s), let Gat:s
i,πa
t:s,πb
t:s ” śs
ℓ“t 1tπa
ℓpHi,ℓq “ aℓu ´ śs
ℓ“t 1tπb
ℓpHi,ℓq “ aℓu.
Given a ﬁxed DTR π “ pπ1, . . . , πTq, with some abuse of notation, we deﬁne
rVi,TpaT q ” Yi,T ´ QTpHi,T, aTq
eT pHi,T, aTq
¨ 1tAi,T “ aT u ` QTpHi,T, aTq,
ˇVi,TpaT q ” Yi,T ´ pQ´kpiq
T
pHi,T, aTq
ˆe´kpiq
T
pHi,T, aTq
¨ 1tAi,T “ aTu ` pQ´kpiq
T
pHi,T, aTq,
and, recursively, for t “ T ´ 1, . . . , 1,
rV
πpt`1q:T
i,t
patq ” Yi,t ` rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
etpHi,t, atq
¨ 1tAi,t “ atu
` Q
πpt`1q:T
t
pHi,t, atq,
ˇV
πpt`1q:T
i,t
patq ” Yi,t ` rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
ˆe´kpiq
t
pHi,t, atq
¨ 1tAi,t “ atu
` pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq,
where, for t “ T, we denote rV
πpT `1q:T
i,T
patq “ rVi,TpaT q and ˇV
πpT `1q:T
i,T
patq “ ˇVi,TpaTq.
For integers s and t such that 1 ď t ď s ď T and at:s P At:s, let
rS
at:s
t:s pπa
t:s, πb
t:s, πps`1q:Tq
” 1
n
nÿ
i“1
Gat:s
i,πa
t:s,πb
t:s ¨
˜ śs´1
ℓ“t 1tAi,ℓ“ aℓu
śs´1
ℓ“t ˆe´kpiq
ℓ
pHi,ℓ, aℓq
¸
¨
´
ˇV
πps`1q:T
i,s
pasq ´ rV
πps`1q:T
i,s
pasq
¯
,
For the case s “ t, We denote rS
at:t
t:t pπa
t:t, πb
t:t, πpt`1q:T q “ rSat
t pπa
t , πb
t, πpt`1q:T q. When s “ T,
we also denote rSat:T
t:T pπa
t:T , πb
t:Tq “ rSat:T
t:T pπa
t:T, πb
t:T, πpT`1q:T q where
rS
at:T
t:T pπa
t:T , πb
t:Tq “ 1
n
nÿ
i“1
G
at:T
i,πa
t:T ,πb
t:T ¨
˜ śT´1
ℓ“t 1tAi,ℓ“ aℓu
śT´1
ℓ“t ˆe´kpiq
ℓ
pHi,ℓ, aℓq
¸
¨
´
ˇVi,TpaT q ´ rVi,TpaTq
¯
.
45

````

## PDF page 46

FORMULA CHECK REQUIRED: original PDF page 46.

````text
Note that each term in (A.17) can be expressed as
ˇ∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q
“
ÿ
at:sPAt:s
rS
at:s
t:s pπa
t , πpt`1q:s, πb
t, πpt`1q:s, πps`1q:Tq.
Hence, regarding (A.17), it follows that
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
| ˇ∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
ď
ÿ
at:sPAt:s
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|rS
at:s
t:s pπa
t , πpt`1q:s, πb
t, πpt`1q:s, πps`1q:T q|.
(B.7)
This result enables us to evaluate (A.17) through evaluating
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|rSat:s
t:s pπa
t , πpt`1q:s, πb
t, πpt`1q:s, πps`1q:T q|
for each at:s P At:s.
Lemma B.5. Suppose that Assumptions 2.1, 2.2, 2.3, 4.1, and 4.2 hold. Then for any
integers s and t such that 1 ď s ď t ď T,
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrSas:t
s:t pπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ ď Oppn´ mint1{2,τ{2uq.
(B.8)
Proof. We ﬁrst consider the case that t ă T. For any integers s and t such that 1 ď s ď
t ă T, we deﬁne
rSas:t
s:t,pAqpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
nÿ
i“1
Gas:t
i,πa
s:t,πb
s:t
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
ˆ
´
pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
ˆ
ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙
;
rSas:t
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
nÿ
i“1
Gas:t
i,πa
s:t,πb
s:t
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
ˆ
´
rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
46

````

## PDF page 47

FORMULA CHECK REQUIRED: original PDF page 47.

````text
ˆ
˜
1 tAi,t “ atu
ˆe´kpiq
t
pHi,t, atq
´ 1 tAi,t “ atu
et pHi,t, atq
¸
;
rS
as:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
nÿ
i“1
G
as:t
i,πa
s:t,πb
s:t
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
ˆ
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯
ˆ
˜
1 tAi,t “ atu
ˆe´kpiq
t
pHi,t, atq
´ 1 tAi,t “ atu
et pHi,t, atq
¸
.
Using these deﬁnitions, we can decompose rSas:t
s:t pπa
s:t, πb
s:t, πpt`1q:T q as follows:
rSas:t
s:t pπa
s:t, πb
s:t, πpt`1q:T q
“ rS
as:t
s:t,pAqpπa
s:t, πb
s:t, πpt`1q:T q ` rS
as:t
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q ` rS
as:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q.
We hence have
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t pπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
ď
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pAqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
`
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
`
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrSas:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
(B.9)
In what follows, we will prove that:
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pAqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ OP
`
n´1{2˘
;
(B.10)
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ OP
`
n´1{2˘
;
(B.11)
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrSas:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ OP
`
n´ mint1{2,τ{2u˘
.
(B.12)
Then we can obtain the result (B.8) from equation (B.9).
Throughout the proof, without loss of generality, we assume that n ą n0, where n0
is deﬁned in Assumption 4.1. We begin by examining rSas:t
s:t,pAqpπa
s:t, πb
s:t, πpt`1q:T q, which we
47

````

## PDF page 48

FORMULA CHECK REQUIRED: original PDF page 48.

````text
further decompose as follows:
rSas:t
s:t,pAqpπa
s:t, πb
s:t, πpt`1q:T q “ rSas:t
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q ` rSas:t
s:t,pA2qpπa
s:t, πb
s:t, πpt`1q:T q,
where
rSas:t
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
nÿ
i“1
Gas:t
i,πa
s:t,πb
s:t ¨
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
ˆ
´
pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯ ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙
;
rS
as:t
s:t,pA2qpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
nÿ
i“1
G
as:t
i,πa
s:t,πb
s:t ¨
˜ śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¸
ˆ
´
pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯ ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙
.
For each fold index k, we deﬁne
rSas:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
ÿ
iPIk
Gas:t
i,πa
s:t,πb
s:t ¨
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
ˆ
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯ ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙
.
Fix k P t1, . . . , Ku. We now consider rS
as:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q. Since pQ
πpt`1q:T ,´k
t
p¨, atq
is computed using the data in the rest K´1 folds, when the data S´k ” tZi : i R Iku in the
rest K ´1 folds is conditioned, pQ
πpt`1q:T ,´k
t
p¨, at:T q is ﬁxed; hence, rS
as:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q
is a sum of i.i.d. bounded random variables under Assumptions 2.2, 2.3, and 4.1 (ii).
It follows that
E
«
G
as:t
i,πa
s:t,πb
s:t ¨
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¨
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
ˆ
ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙ˇˇˇˇS´k

“ E
«
G
as:t
i,πa
s:t,πb
s:t ¨
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¨
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
ˆE
„ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙ˇˇˇˇHi,t
ˇˇˇˇS´k

“ E
«
G
as:t
i,πa
s:t,πb
s:t ¨
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¨
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
48

````

## PDF page 49

FORMULA CHECK REQUIRED: original PDF page 49.

````text
ˆ
ˆ
1 ´ et pHi,t, atq
et pHi,t, atq
˙ˇˇˇˇS´k

“ 0.
Hence, ﬁxing πpt`1q:T , supπa
s:T ,πb
s:T PΠs:t
ˇˇˇrS
as:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ can be written as
sup
πa
s:T ,πb
s:T PΠs:t
ˇˇˇrS
as:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
“ 1
K
sup
πa
s:T ,πb
s:T PΠs:t
ˇˇˇˇˇ
1
n{K
ÿ
iPIk
G
as:t
i,πa
s:t,πb
s:t ¨
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
ˆ
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯ ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙
´ E
«
1
n{K
ÿ
iPIk
G
as:t
i,πa
s:t,πb
s:t ¨
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
ˆ
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯ ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙ˇˇˇˇS´k
ˇˇˇˇ .
By applying Lemma B.3 while ﬁxing S´k and setting i P Ik and
Γ:
ipas:tq “
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯ ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙
,
the following holds: @δ ą 0, with probability at least 1 ´ 2δ,
sup
πa
s:T ,πb
s:T PΠs:t
ˇˇˇrSas:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
ď o
`
n´1{2˘
`
´
54.4κ pΠs:tq ` 435.2 `
a
2 logp1{δq
¯
ˆ
»
–
sup
πs:T PΠs:T
E
»
–
´
G
as:t
i,πa
s:t,πb
s:t
¯2
¨
˜śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¸2
ˆ
´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯2 ˆ
1 ´ 1 tAi,t “ atu
et pHi,t, atq
˙2ˇˇˇˇˇ S´k
ﬀO´ n
K
¯ﬀ1{2
ď o
`
n´1{2˘
`
?
K ¨
´
54.4κ pΠs:tq ` 435.2 `
a
2 logp1{δq
¯
¨
ˆ1
η
˙t´s`1
ˆ
g
f
f
f
eE
„´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯2ˇˇˇˇ S´k

n
,
49

````

## PDF page 50

FORMULA CHECK REQUIRED: original PDF page 50.

````text
where the last inequality follows from
´
G
as:t
i,πa
s:t,πb
s:t
¯2
ď 1 a.s. and Assumption 2.3 (overlap
condition). Note that κ pΠs:tq is ﬁnite by Lemma 4.2 and the inequality κ pΠs:tq ď κ pΠq.
From Assumptions 2.2 and 4.1 (ii), we have
sup
πpt`1q:T PΠpt`1q:T
E
„´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯2
ă 8.
Hence, Markov’s inequality yields
sup
πpt`1q:T PΠpt`1q:T
E
„´
pQ
πpt`1q:T ,´k
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯2ˇˇˇˇ S´k

“ Opp1q.
Combining these results, we obtain
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:T ,πb
s:T PΠs:t
ˇˇˇrSas:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ Op
ˆ 1
?n
˙
.
(B.13)
Consequently,
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:T ,πb
s:T PΠs:t
ˇˇˇrS
as:t
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
ď
K
ÿ
k“1
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:T ,πb
s:T PΠs:t
ˇˇˇrSas:t,k
s:t,pA1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ Op
ˆ 1
?n
˙
.
We next consider rS
as:t
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q (we will consider rS
as:t
s:t,pA2qpπa
s:t, πb
s:t, πpt`1q:T q
later). We begin by decomposing rSas:t
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q as follows:
rSas:t
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q “
K
ÿ
k“1
´
rSas:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q ` rSas:t,k
s:t,pB2qpπa
s:t, πb
s:t, πpt`1q:T q
¯
,
where
rSas:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
ÿ
iPIk
Gas:t
i,πa
s:t,πb
s:t
´
rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
ˆ
˜śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸
1 tAi,t “ atu
et pHi,t, atq ;
rS
as:t,k
s:t,pB2qpπa
s:t, πb
s:t, πpt`1q:T q ” 1
n
ÿ
iPIk
G
as:t
i,πa
s:t,πb
s:t
´
rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
50

````

## PDF page 51

FORMULA CHECK REQUIRED: original PDF page 51.

````text
ˆ
˜ śt
ℓ“s 1tAi,ℓ“ aℓu
śt
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
śt
ℓ“s 1tAi,ℓ“ aℓu
śt
ℓ“s eℓpHi,ℓ, aℓq
¸
.
Fix k P t1, . . . , Ku. As for rS
as:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q, taking the conditional expecta-
tion given the date S´k in the rest k ´ 1 folds leads to
E
”
rSas:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇS´k
ı
“ E
«
1
n{K
ÿ
iPIk
Gas:t
i,πa
s:t,πb
s:t
´
rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
ˆ
˜śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸
1 tAi,t “ atu
et pHi,t, atq
ˇˇˇˇˇS´k
ﬀ
“ E
«
1
n{K
ÿ
iPIk
G
as:t
i,πa
s:t,πb
s:tE
”
rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
ˇˇˇHi,t, Ai,t “ at
ı
ˆ
˜śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸
1 tAi,t “ atu
et pHi,t, atq
ˇˇˇˇˇS´k
ﬀ
“ E
«
1
n{K
ÿ
iPIk
G
as:t
i,πa
s:t,πb
s:t
`
Q
πpt`1q:T
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
˘
ˆ
˜śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸
1 tAi,t “ atu
et pHi,t, atq
ˇˇˇˇˇS´k
ﬀ
“ 0,
where the third equality follows from Lemma B.2 (i).
Note that conditional on S´k,
rSas:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q is a sum of i.i.d.
bounded random variables under Assump-
tions 2.2, 2.3, and 4.1 (ii), and its conditional mean is zero. Hence, ﬁxing πpt`1q:T and
conditioning on S´k, we can apply Lemma B.3 with setting i P Ik and
Γ:
ipas:tq “
´
rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
¯
ˆ
˜śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸
1 tAi,t “ atu
et pHi,t, atq
to obtain the following: @δ ą 0, with probability at least 1 ´ 2δ,
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrSas:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
51

````

## PDF page 52

FORMULA CHECK REQUIRED: original PDF page 52.

````text
ď o
`
n´1{2˘
`
´
54.4κ pΠs:tq ` 435.2 `
a
2 logp1{δq
¯
ˆ
„
sup
πs:T PΠt:T
E
„´
Gas:t
i,πa
s:t,πb
s:t
¯2
¨
´
rV
πpt`2q:T
i,t`1
pπt`1pHi,t`1qq ´ Q
πpt`1q:T
t
pHi,t, atq
¯2
˜śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸2 ˆ1 tAi,t “ atu
et pHi,t, atq
˙2
ˇˇˇˇˇˇ
S´k
ﬁ
ﬂ
O´ n
K
¯
ﬁ
ﬂ
1{2
ď o
`
n´1{2˘
`
?
K ¨
´
54.4κ pπt:T q ` 435.2 `
a
2 logp1{δq
¯
¨
˜T´t
ÿ
j“0
3M
ηj
¸
ˆ
g
f
f
f
eE
„´
1
śt´1
ℓ“s eℓpHi,ℓ,aℓq ´
1
śt´1
ℓ“s ˆe´k
ℓ
pHi,ℓ,aℓq
¯2ˇˇˇˇS´k

n
,
where the last inequality follows from
´
Gas:t
i,πa
s:t,πb
s:t
¯2
ď 1 a.s. and Assumptions 2.2 and 2.3.
From Assumptions 2.3 and 4.1 (ii), we have
E
»
–
˜
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
1
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸2ﬁ
ﬂă 8.
Hence, Markov’s inequality leads to
E
»
–
˜
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
´
1
śt´1
ℓ“s ˆe´k
ℓpHi,ℓ, aℓq
¸2ˇˇˇˇˇˇ
S´k
ﬁ
ﬂ“ Opp1q.
Note also that κpΠs:tq ă 8 by Lemma 4.2. Combining these results, we have
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrSas:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ Op
ˆ 1
?n
˙
.
(B.14)
By applying the same argument to derive (B.14), we also obtain
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrS
as:t,k
s:t,pB2qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ Op
ˆ 1
?n
˙
.
Consequently,
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrS
as:t,k
s:t,pBqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
52

````

## PDF page 53

FORMULA CHECK REQUIRED: original PDF page 53.

````text
ď
K
ÿ
k“1
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrSas:t,k
s:t,pB1qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
`
K
ÿ
k“1
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrS
as:t,k
s:t,pB2qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
“ Op
ˆ 1
?n
˙
,
which proves equation (B.11).
We next consider to bound supπpt`1q:T PΠpt`1q:T supπa
s:t,πa
s:tPΠs:t
ˇˇˇrSas:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
from above. It follows that
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
“
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇˇˇ
1
n
nÿ
i“1
Gas:t
i,πa
s:t,πb
s:t
śt´1
ℓ“s 1tAi,ℓ“ aℓu
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯
ˆ
˜
1 tAi,t “ atu
ˆe´kpiq
t
pHi,t, atq
´ 1 tAi,t “ atu
et pHi,t, atq
¸ˇˇˇˇˇ
ď 1
n
nÿ
i“1
ˇˇˇQ
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
ˇˇˇ
ˆ
ˇˇˇˇˇ
1
śt
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
et pHi,t, atq ¨ śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
ˇˇˇˇˇ
ď 1
n
nÿ
i“1
ˇˇˇQ
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
ˇˇˇ ¨
ˇˇˇˇˇ
1
śt
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt
ℓ“s eℓpHi,ℓ, aℓq
ˇˇˇˇˇ
` 1
n
nÿ
i“1
ˇˇˇQ
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
ˇˇˇ
ˆ
ˇˇˇˇˇ
1
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
ˇˇˇˇˇ
ˆ
1
etpHi,t, atq
˙
ď
d
1
n
nÿ
i“1
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯2
ˆ
g
f
f
e1
n
nÿ
i“1
˜
1
śt
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt
ℓ“s eℓpHi,ℓ, aℓq
¸2
`
ˆ1
η
˙ d
1
n
nÿ
i“1
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯2
ˆ
g
f
f
e1
n
nÿ
i“1
˜
1
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¸2
53

````

## PDF page 54

FORMULA CHECK REQUIRED: original PDF page 54.

````text
where the last inequality follows from Cauchy-Schwartz inequality and Assumption 2.3
(overlap condition). Maximizing over Πpt`1q:T and taking the expectation of both sides
yields:
E
«
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
ﬀ
ď E
«
sup
πpt`1q:T PΠpt`1q:T
d
1
n
nÿ
i“1
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯2
ˆ
g
f
f
e1
n
nÿ
i“1
˜
1
śt
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt
ℓ“s eℓpHi,ℓ, aℓq
¸2
ﬁ
ﬃﬂ
` η´1E
«
sup
πpt`1q:T PΠpt`1q:T
d
1
n
nÿ
i“1
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯2
ˆ
g
f
f
e1
n
nÿ
i“1
˜
1
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¸2
ﬁ
ﬃﬂ
ď
g
f
f
e1
n
nÿ
i“1
E
«
sup
πpt`1q:T PΠpt`1q:T
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯2
ﬀ
ˆ
g
f
f
f
e1
n
nÿ
i“1
E
»
–
˜
1
śt
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt
ℓ“s eℓpHi,ℓ, aℓq
¸2ﬁ
ﬂ
` η´1
g
f
f
e1
n
nÿ
i“1
E
«
sup
πpt`1q:T PΠpt`1q:T
´
Q
πpt`1q:T
t
pHi,t, atq ´ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq
¯2
ﬀ
ˆ
g
f
f
f
e1
n
nÿ
i“1
E
»
–
˜
1
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¸2ﬁ
ﬂ
“
K
ÿ
k“1
g
f
f
eE
«
sup
πpt`1q:T PΠpt`1q:T
´
Q
πpt`1q:T
t
pHt, atq ´ pQ
πpt`1q:T ,´k
t
pHi,t, atq
¯2
ﬀ
ˆ
g
f
f
eE
«ˆ
1
śt
ℓ“s ˆe´k
ℓ
pHℓ, aℓq ´
1
śt
ℓ“s eℓpHℓ, aℓq
˙2ﬀ
` η´1
K
ÿ
k“1
g
f
f
eE
«
sup
πpt`1q:T PΠpt`1q:T
´
Q
πpt`1q:T
t
pHt, atq ´ pQ
πpt`1q:T ,´k
t
pHt, atq
¯2
ﬀ
54

````

## PDF page 55

FORMULA CHECK REQUIRED: original PDF page 55.

````text
ˆ
g
f
f
f
eE
»
–
˜
1
śt´1
ℓ“s ˆe´kpiq
ℓ
pHℓ, aℓq
´
1
śt´1
ℓ“s eℓpHℓ, aℓq
¸2ﬁ
ﬂ
“ O
`
n´τ{2˘
,
where the second inequality follows from Cauchy-Schwartz inequality and the last line
follows from Assumption 4.1 (i). Then applying Markov’s inequality leads to
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrSas:t
s:t,pCqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ OP
`
n´τ{2˘
,
(B.15)
which proves equation (B.12).
Now let us consider rSas:t
s:t,pA2qpπa
s:t, πb
s:t, πpt`1q:T q. Note that
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrSas:t
s:t,pA2qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
ď
sup
πpt`1q:T PΠpt`1q:T
1
n
nÿ
i“1
ˇˇˇˇˇ
1
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
ˇˇˇˇˇ
ˆ
ˇˇˇ pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
ˇˇˇ ¨
ˇˇˇˇ1 ´ 1 tAi,t “ atu
et pHi,t, atq
ˇˇˇˇ
ď
ˆ1
η
˙ g
f
f
e1
n
nÿ
i“1
˜
1
śt´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
´
1
śt´1
ℓ“s eℓpHi,ℓ, aℓq
¸2
ˆ
d
1
n
nÿ
i“1
sup
πpt`1q:T PΠpt`1q:T
´
pQ
πpt`1q:T ,´kpiq
t
pHi,t, atq ´ Q
πpt`1q:T
t
pHi,t, atq
¯2
,
where the last inequality follows from Assumption 2.3 (overlap condition) and Cauchy-
Schwartz inequality. Then, by applying the same argument to derive (B.15), we obtain
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pA2qpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ “ OP
`
n´τ{2˘
.
Combining this result with (B.13) leads to:
sup
πpt`1q:T PΠpt`1q:T
sup
πa
s:t,πa
s:tPΠs:t
ˇˇˇrSas:t
s:t,pAqpπa
s:t, πb
s:t, πpt`1q:T q
ˇˇˇ
ď
K
ÿ
k“1
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrS
as:t,k
s:t,pA1q pπs:tq
ˇˇˇ `
sup
πa
s:t,πb
s:tPΠs:t
ˇˇˇrS
as:t
s:t,pA2q pπs:tq
ˇˇˇ
55

````

## PDF page 56

FORMULA CHECK REQUIRED: original PDF page 56.

````text
“ OP
`
n´ mint1{2,τ{2u˘
.
This result proves equation (B.10).
Consequently, combining equations (B.9)–(B.12), we obtain the result (B.8).
We next consider the case that t “ T. In this case, rSat:T
t:T pπa
t:T, πb
t:Tq is decomposed as
rSat:T
t:T pπa
t:T, πb
t:Tq “ rSat:T
t:T,pAqpπa
t:T, πb
t:Tq ` rSat:T
t:T,pBqpπa
t:T, πb
t:Tq ` rSat:T
t:T,pCqpπa
t:T, πb
t:Tq,
where
rSat:T
t:T,pAqpπa
t:T, πb
t:Tq ” 1
n
nÿ
i“1
Gat:T
i,πa
t:T ,πb
t:T
śT´1
ℓ“s 1tAi,ℓ“ aℓu
śT´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
ˆ
´
pQ´kpiq
T
pHi,T, aTq ´ QT pHi,T, aTq
¯ ˆ
1 ´ 1 tAi,T “ aTu
eT pHi,T, aTq
˙
;
rSat:T
t:T,pBqpπa
t:T, πb
t:Tq ” 1
n
nÿ
i“1
Gat:T
i,πa
t:T ,πb
t:T
śT´1
ℓ“s 1tAi,ℓ“ aℓu
śT´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
ˆ pYi,T ´ QT pHi,T, aTqq
˜
1 tAi,T “ aTu
ˆe´kpiq
T
pHi,T, aTq
´ 1 tAi,T “ aTu
eT pHi,T, aTq
¸
;
rSat:T
t:T,pCqpπa
t:T, πb
t:Tq ” 1
n
nÿ
i“1
Gat:T
i,πa
t:T ,πb
t:T
śT´1
ℓ“s 1tAi,ℓ“ aℓu
śT´1
ℓ“s ˆe´kpiq
ℓ
pHi,ℓ, aℓq
ˆ
´
QT pHi,T, aTq ´ pQ´kpiq
T
pHi,T, aTq
¯ ˜
1 tAi,T “ aTu
ˆe´kpiq
T
pHi,T, aTq
´ 1 tAi,T “ aTu
eT pHi,T, aTq
¸
.
The same arguments to derive the results (B.10)–(B.12) also show that
sup
πa
t:T ,πa
t:T PΠt:T
ˇˇˇrSat:T
t:T,pAqpπa
t:T, πb
t:Tq
ˇˇˇ “ OP
`
n´1{2˘
;
sup
πa
t:T ,πa
t:T PΠt:T
ˇˇˇrSat:T
t:T,pBqpπa
t:T, πb
t:Tq
ˇˇˇ “ OP
`
n´1{2˘
;
sup
πa
t:T ,πa
t:T PΠt:T
ˇˇˇrSat:T
t:T,pCqpπa
t:T, πb
t:Tq
ˇˇˇ “ OP
`
n´ mint1{2,τ{2u˘
.
Therefore,
sup
πa
t:T ,πa
t:T PΠt:T
ˇˇˇrS
at:T
t:T pπa
t:T, πb
t:T q
ˇˇˇ
ď
sup
πa
t:T ,πa
t:T PΠt:T
ˇˇˇrS
at:T
t:T,pAqpπa
t:T, πb
t:Tq
ˇˇˇ `
sup
πa
t:T ,πa
t:T PΠt:T
ˇˇˇrS
at:T
t:T,pBqpπa
t:T , πb
t:Tq
ˇˇˇ
56

````

## PDF page 57

FORMULA CHECK REQUIRED: original PDF page 57.

````text
`
sup
πa
t:T ,πa
t:T PΠt:T
ˇˇˇrS
at:T
t:T,pCqpπa
t:T, πb
t:Tq
ˇˇˇ
“ OP
`
n´ mint1{2,τ{2u˘
,
which leads to the result (B.8).
We ﬁnally presents the proof of Lemma A.3.
Proof of Lemma A.3. From equation (B.7), we have
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
| ˇ∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q ´ r∆:
t,spπa
t , πpt`1q:T ; πb
t, πpt`1q:T q|
ď
ÿ
at:sPAt:s
sup
πpt`1q:T PΠpt`1q:T
sup
πa
t ,πb
tPΠt
|rS
at:s
t:s pπa
t , πpt`1q:s, πb
t, πpt`1q:s, πps`1q:T q|
ď
ÿ
at:sPAt:s
sup
πps`1q:T PΠps`1q:T
sup
πa
t:s,πb
t:sPΠt
|rSat:s
t:s pπa
t:s, πb
t:s, πps`1q:Tq|.
The result then follows from Lemma B.5.
C
Proof of Theorem 5.1
This appendix provides the proof of Theorem 5.1.
Proof of Theorem 5.1. We begin by noting that the objective function x
W AIP Wpπq can be
expressed as x
W AIP Wpπq “ p1{nq řn
i“1 pVi,1pπq, where pVi,1p¨q is deﬁned in Appendix A. A
standard argument from statistical learning theory (e.g., Lugosi, 2002) leads to
RpˆπAIP Wq “ ∆1
`
π˚,opt; ˆπAIP W˘
ď ∆1
`
π˚,opt; ˆπAIP W˘
´ p∆1
`
π˚,opt; ˆπAIP W˘
ď
sup
πa,πbPΠ
|∆1pπa; πbq ´ p∆1pπa; πbq|
ď
sup
πa,πbPΠ
|∆1pπa; πbq ´ r∆1pπa; πbq| `
sup
πa,πbPΠ
|p∆1pπa; πbq ´ r∆1pπa; πbq|,
(C.1)
where the ﬁrst inequality follows because ˆπAIP W maximizes p1{nq řn
i“1 pVi,1pπq over Π;
hence, p∆1
`
π˚,opt; ˆπAIP W˘
ď 0.
57

````

## PDF page 58

FORMULA CHECK REQUIRED: original PDF page 58.

````text
Regarding supπa,πbPΠ |∆1pπa; πbq ´ r∆1pπa; πbq|, under Assumptions 2.2, 2.3, and the
result in Lemma 4.2, we can apply Lemma B.3 to obtain the following result: For any
δ P p0, 1q, with probability at least 1 ´ 2δ,
sup
πa,πbPΠ
|r∆1pπa; πbq ´ ∆1pπa; πbq| ď
˜
54.4
?
2κpΠq ` 435.2 `
c
2 log 1
δ
¸ c
V ˚
n
` o
ˆ 1
?n
˙
,
(C.2)
where V ˚ ” supπa,πbPΠ E
„´
rΓ
πa
2:T
i,1 pπaq ´ rΓπ2:T
i,1 pπbq
¯2
ă 8.
Regarding supπa,πbPΠ |p∆1pπa; πbq ´ r∆1pπa; πbq|, we have p∆1pπa; πbq ´ r∆1pπa; πbq “
ř
aT PAT rS
aT
1:Tpπa, πbq.
Applying the result (B.8) in Lemma B.5 to rS
aT
1:Tpπa, πbq for each
aT gives
sup
πa,πbPΠ
|p∆1pπa; πbq ´ r∆1pπa; πbq| “ Op
`
n´ mint1{2,τ{2u˘
.
(C.3)
Combining the results (C.1)-(C.3) leads to the result (7).
✷
D
Example: Optimality and Suboptimality of Back-
ward Induction
This appendix illustrates that Assumption 3.1 (i.e., the correct speciﬁcation of Π) is
a suﬃcient but not necessary condition for the optimality of the backward induction
approach. Speciﬁcally, we provide two simple examples: one where backward induction
results in suboptimality and another where it achieves optimality, both when Assumption
3.1 is not satisﬁed. These examples, which are adapted from Sakaguchi (2025), consider
a two-period setting (T “ 2) with binary treatments (A1 “ A2 “ t0, 1u).
For the ﬁrst example, we consider the data-generating process (DGP) P that satisﬁes
the following:
ErY2p1, 1qs “ 1.0, ErY2p1, 0qs “ 0.5, ErY2p0, 1qs “ 0.0, ErY2p0, 0qs “ 0.6;
Y1p0q “ Y1p1q “ 0 a.s.;
A1 and A2 are independently distributed as Berp1{2q.
(D.1)
58

````

## PDF page 59

FORMULA CHECK REQUIRED: original PDF page 59.

````text
The welfare Wpπq depends only on the second-stage outcomes. Suppose that the historical
information is H1 “ H and H2 “ pA1q.
As an example of a misspeciﬁed class of DTRs, we consider a class of uniform DTRs;
that is, Πt “ tc0
t, c1
tu for t “ 1, 2, where c0
t and c1
t denote constant functions such that
c0
tphtq “ 0 and c1
tphtq “ 1 for any ht. Under the assumed DGP, Π2 “ tc0
2, c1
2u does not sat-
isfy Assumption 3.1, because Q2p1, c1
tq ą Q2p1, c0
tq but Q2p0, c0
tq ą Q2p0, c1
tq, where we use
the result that Q2pa1, π2q “ ErY2pa1, π2pa1qqs under sequential ignorability (Assumption
2.1).
The optimal DTR over the class of constant DTRs is
pπ˚,opt
1
, π˚,opt
2
q “
arg max
pπ1,π2qPtc0
1,c1
1uˆtc0
2,c1
2u
E rY2pπ1pH1q, π2pπ1pH1qqqs “ pc1
1, c1
2q,
and its welfare is Wpπ˚,opt
1
, π˚,opt
2
q “ ErY2p1, 1qs “ 1.0. However, the solution pπ˚,B
1
, π˚,B
2
q
of the backward-induction approach is pc0
1, c0
2q because
(1st step)
π˚,B
2
“ arg max
π2Ptc0
2,c1
2u
ErQ2pH2, π2qs “ arg max
π2Ptc0
2,c1
2u
E rY2pA1, π2qs “ c0
2;
(2nd step)
π˚,B
1
“ arg max
π1Ptc0
1,c1
1u
ErQ1pH1, π˚,B
2
qs “ arg max
π1Ptc0
1,c1
1u
E
”
Y2pπ1, π˚,B
2
q
ı
“ c0
1.
Hence, the backward-induction solution π˚,B “ pc0
1, c0
2q diﬀers from the optimal one
π˚,opt “ pc1
1, c1
2q over Π, and results in a suboptimal welfare Wpπ˚,Bq “ ErY2p0, 0qs “ 0.6.
This simple example illustrates that when the DTR class Π is not correctly speciﬁed, the
backward-induction approach does not necessarily yield the optimal DTR.
Next, we illustrate that the misspeciﬁcation of Π does not necessarily result in the
suboptimality of the backward-induction approach. Suppose that the DGP P satisﬁes
condition (D.1) with ErY2p0, 1qs “ 0.0 replaced by ErY2p0, 1qs “ 0.4, where Π2 “ tc0
2, c1
2u
still does not satisfy Assumption 3.1. In this case, the backward-induction solution be-
comes π˚,B “ pc1
1, c1
2q, whereas the optimal DTR π˚,opt remains unchanged. Therefore,
the backward-induction solution coincides with the optimal one, showing that the correct
speciﬁcation of Π (Assumption 3.1) is not a necessary condition for the optimality of the
backward-induction approach.
59

````

## PDF page 60

FORMULA CHECK REQUIRED: original PDF page 60.

````text
E
Additional Simulation Results
This appendix presents additional simulation results that examine the eﬀects of misspec-
iﬁcation of either the Q-functions or propensity scores. We use the same DGPs and class
of DTRs as in Section 6. For both the Q-functions and the propensity scores, we consider
two types of estimators. The ﬁrst type, as in Section 6, is based on generalized random
forests (Athey et al., 2019) and represents correctly speciﬁed models. The second type
relies on misspeciﬁed models: it estimates the Q-functions via linear regression (for Q-
learning with and without policy search), using the predictor sets pD2, D2 ¨ H2, H2q and
pD1, D1 ¨ H1, H1q for stages 2 and 1, respectively; and estimates the propensity scores via
probit regression for e2 and e1, using H1 as predictors in both cases.
Tables E.1 and E.2 report the results from 500 simulations for DGPs 1 and 2, respec-
tively, using sample sizes n “ 250, 500, 1000, 2000, and 4000. In each simulation, welfare
is evaluated on a test sample of 50,000 observations independently drawn from the same
DGP. The results indicate that Q-learning, Q-search, and IPW are adversely aﬀected by
misspeciﬁcation of the nuisance functions – particularly at larger sample sizes – in both
DGPs. In contrast, DR consistently outperforms the other methods, even when either
the Q-functions or the propensity scores are misspeciﬁed. Its performance remains largely
robust to such misspeciﬁcation in each DGP. These ﬁndings underscore the doubly robust
property of the proposed method.
60

````

## PDF page 61

Technical extraction; compare with original PDF page 61.

````text
Table E.1: Monte Carlo simulation results for DGP1 with Missspeciﬁcation
Speciﬁcation
Sample Size
Method
Q-function
PS
250
500
1000
2000
4000
Q-learn
correct
-
0.20 (0.12)
0.31 (0.11)
0.43 (0.10)
0.57 (0.07)
0.68 (0.03)
miss
-
0.25 (0.09)
0.28 (0.07)
0.31 (0.05)
0.33 (0.04)
0.33 (0.03)
Q-search
correct
-
0.17 (0.19)
0.29 (0.21)
0.40 (0.21)
0.53 (0.16)
0.64 (0.10)
miss
-
0.23 (0.16)
0.23 (0.16)
0.23 (0.16)
0.22 (0.16)
0.18 (0.15)
IPW
-
correct
0.24 (0.13)
0.29 (0.14)
0.37 (0.16)
0.45 (0.14)
0.55 (0.13)
-
miss
0.24 (0.11)
0.29 (0.12)
0.32 (0.12)
0.39 (0.13)
0.44 (0.14)
DR
correct
miss
0.24 (0.14)
0.37 (0.16)
0.54 (0.15)
0.67 (0.08)
0.72 (0.03)
miss
correct
0.34 (0.17)
0.46 (0.15)
0.59 (0.11)
0.67 (0.04)
0.69 (0.03)
correct
correct
0.29 (0.17)
0.44 (0.17)
0.61 (0.11)
0.70 (0.04)
0.72 (0.02)
Notes: The columns labeled “Speciﬁcation” indicate the speciﬁcations of the Q-functions and propen-
sity scores (PS), respectively, where “correct” and “miss” refer to correct speciﬁcation and misspeci-
ﬁcation. Each cell in the last ﬁve columns reports the mean welfare, with the standard deviation in
parentheses, for each method, speciﬁcation, and sample size. These values are calculated based on
500 simulations using a test sample of 50,000 observations randomly drawn from DGP1.
Table E.2: Monte Carlo simulation results for DGP2 with Missspeciﬁcation
Speciﬁcation
Sample Size
Method
Q-function
PS
250
500
1000
2000
4000
Q-learn
correct
-
1.31 (0.36)
1.69 (0.11)
1.78 (0.08)
1.84 (0.05)
1.89 (0.05)
miss
-
1.46 (0.07)
1.50 (0.05)
1.52 (0.04)
1.53 (0.03)
1.54 (0.03)
Q-search
correct
-
1.26 (0.48)
1.58 (0.18)
1.54 (0.09)
1.52 (0.04)
1.54 (0.04)
miss
-
1.44 (0.15)
1.44 (0.12)
1.44 (0.10)
1.43 (0.08)
1.42 (0.08)
IPW
-
correct
1.30 (0.21)
1.42 (0.17)
1.56 (0.19)
1.68 (0.21)
1.81 (0.21)
-
miss
1.32 (0.18)
1.41 (0.13)
1.49 (0.10)
1.51 (0.07)
1.52 (0.07)
DR
correct
miss
1.44 (0.21)
1.63 (0.23)
1.78 (0.22)
1.87 (0.19)
1.99 (0.19)
miss
correct
1.56 (0.23)
1.69 (0.25)
1.85 (0.23)
1.95 (0.16)
2.02 (0.16)
correct
correct
1.51 (0.26)
1.77 (0.24)
1.95 (0.14)
2.01 (0.07)
2.04 (0.07)
Notes: The columns labeled “Speciﬁcation” indicate the speciﬁcations of the Q-functions and propen-
sity scores (PS), respectively, where “correct” and “miss” refer to correct speciﬁcation and misspeci-
ﬁcation. Each cell in the last ﬁve columns reports the mean welfare, with the standard deviation in
parentheses, for each method, speciﬁcation, and sample size. These values are calculated based on
500 simulations using a test sample of 50,000 observations randomly drawn from DGP2.
61

````

## PDF page 62

FORMULA CHECK REQUIRED: original PDF page 62.

````text
References
Athey, S., J. Tibshirani, and S. Wager (2019): “Generalized Random Forests,”
The Annals of Statistics, 47, 1148–1178.
Athey, S. and S. Wager (2021): “Policy Learning with Observational Data,” Econo-
metrica, 89, 133–161.
Bhattacharya, D. and P. Dupas (2012): “Inferring welfare maximizing treatment
assignment under budget constraints,” Journal of Econometrics, 167, 168–196.
Blumlein, T., J. Persson, and S. Feuerriegel (2022): “Learning Optimal Dynamic
Treatment Regimes Using Causal Tree Methods in Medicine,” in Proceedings of the 7th
Machine Learning for Healthcare Conference, vol. 182, 146–171.
Breiman, L., J. Friedman, C. Stone, and R. Olshen (1984): Classiﬁcation and
Regression Trees, The Wadsworth and Brooks-Cole statistics-probability series, Taylor
& Francis.
Chakraborty, B. and S. A. Murphy (2014): “Dynamic Treatment Regimes,” Annual
Review of Statistics and Its Application, 1, 447–464.
Chernozhukov, V., D. Chetverikov, M. Demirer, E. Duflo, C. Hansen,
W. Newey, and J. Robins (2018): “Double/Debiased Machine Learning for Treat-
ment and Structural Parameters,” The Econometrics Journal, 21, 1–68.
Ding, W. and S. F. Lehrer (2010): “Estimating Treatment Eﬀects from Contaminated
Multiperiod Education Experiments: The Dynamic Impacts of Class Size Reductions,”
The Review of Economics and Statistics, 92, 31–42.
Doroudi, S., P. S. Thomas, and E. Brunskill (2018): “Importance Sampling for
Fair Policy Selection,” in Proceedings of the Conference on Uncertainty in Artiﬁcial
Intelligence (UAI), 5239–5243.
Ertefaie, A., J. R. McKay, D. Oslin, and R. L. Strawderman (2021): “Robust
Q-learning,” Journal of the American Statistical Association, 116, 368–381.
Fonteneau, R., S. A. Murphy, L. Wehenkel, and D. Ernst (2013): “Batch Mode
Reinforcement Learning based on the Synthesis of Artiﬁcial Trajectories,” Annals of
Operations Research, 208, 383–416.
Han, S. (2023): “Optimal dynamic treatment regimes and partial welfare ordering,”
Journal of the American Statistical Association, 1–11.
62

````

## PDF page 63

FORMULA CHECK REQUIRED: original PDF page 63.

````text
Heckman, J. J., J. E. Humphries, and G. Veramendi (2016): “Dynamic treatment
eﬀects,” Journal of Econometrics, 191, 276–292.
Heckman, J. J. and S. Navarro (2007): “Dynamic discrete choice and dynamic
treatment eﬀects,” Journal of Econometrics, 136, 341–396.
Hern´an, M. A., B. Brumback, and J. M. Robins (2001): “Marginal Structural
Models to Estimate the Joint Causal Eﬀect of Nonrandomized Treatments,” Journal of
the American Statistical Association, 96, 440–448.
Hirano, K. and J. Porter (2009): “Asymptotics for statistical treatment rules,”
Econometrica, 77, 1683–1701.
Ida, T., T. Ishihara, K. Ito, D. Kido, T. Kitagawa, S. Sakaguchi, and
S. Sasaki (2024): “Dynamic Targeting: Experimental Evidence from Energy Rebate
Programs,” NBER Working Paper: 32561.
Jiang, N. and L. Li (2016): “Doubly Robust Oﬀ-policy Value Evaluation for Rein-
forcement Learning,” in Proceedings of the 33rd International Conference on Machine
Learning, PMLR, 652–661.
Kallus, N. and M. Uehara (2020): “Double Reinforcement Learning for Eﬃcient
Oﬀ-Policy Evaluation in Markov Decision Processes,” Journal of Machine Learning
Research, 21, 6742–6804.
Kitagawa, T., S. Sakaguchi, and A. Tetenov (2023): “Constrained Classiﬁcation
and Policy Learning,” arXiv preprint arXiv:2106.12886.
Kitagawa, T. and A. Tetenov (2018): “Who Should Be Treated? Empirical Welfare
Maximization Methods for Treatment Choice,” Econometrica, 86, 591–616.
Kolsrud, J., C. Landais, P. Nilsson, and J. Spinnewijn (2018): “The Optimal
Timing of Unemployment Beneﬁts: Theory and Evidence from Sweden,” American
Economic Review, 108, 985–1033.
Kosorok, M. R. and E. B. Laber (2019): “Precision Medicine,” Annual Review of
Statistics and Its Application, 6, 263–286.
Krueger, A. B. (1999): “Experimental Estimates of Education Production Functions,”
The Quarterly Journal of Economics, 114, 497–532.
63

````

## PDF page 64

FORMULA CHECK REQUIRED: original PDF page 64.

````text
Laber, E. B., D. J. Lizotte, M. Qian, W. E. Pelham, and S. A. Murphy
(2014): “Dynamic Treatment Regimes: Technical Challenges and Applications,” Elec-
tronic Journal of Statistics, 8, 1225–1272.
Laber, E. B. and Y.-Q. Zhao (2015): “Tree-Based Methods for Individualized Treat-
ment Regimes,” Biometrika, 102, 501–514.
Le, H., C. Voloshin, and Y. Yue (2019): “Batch Policy Learning under Constraints,”
in International Conference on Machine Learning, PMLR, 3703–3712.
Lechner, M. (2009): “Sequential Causal Models for the Evaluation of Labor Market
Programs,” Journal of Business & Economic Statistics, 27, 71–83.
Li, Z., J. Chen, E. Laber, F. Liu, and R. Baumgartner (2023): “Optimal Treat-
ment Regimes: A Review and Empirical Comparison,” International Statistical Review,
91, 427–463.
Liu, X. (2023): “Dynamic Coupon Targeting Using Batch Deep Reinforcement Learning:
An Application to Livestream Shopping,” Marketing Science, 42, 637–658.
Lugosi, G. (2002): “Pattern Classiﬁcation and Learning Theory,” in Principles of Non-
parametric Learning, ed. by L. Gyrﬁ, Vienna: Springer, 1–56.
Manski, C. F. (2004): “Statistical Treatment Rules for Heterogeneous Populations,”
Econometrica, 72, 1221–1246.
Mbakop, E. and M. Tabord-Meehan (2021): “Model selection for treatment choice:
Penalized welfare maximization,” Econometrica, 89, 825–848.
Meyer, B. D. (1995): “Lessons from the U.S. Unemployment Insurance Experiments,”
Journal of Economic Literature, 33, 91–131.
Moodie, E., B. Chakraborty, and M. S. Kramer (2012): “Q-learning for Estimat-
ing Optimal Dynamic Treatment Rules from Observational Data,” Canadian Journal
of Statistics, 40, 629–645.
Munos, R. and C. Szepesv´ari (2008): “Finite-Time Bounds for Fitted Value Itera-
tion,” Journal of Machine Learning Research, 9, 815–857.
Murphy, S. A. (2003): “Optimal Dynamic Treatment Regimes,” Journal of the Royal
Statistical Society: Series B (Statistical Methodology), 65, 331–355.
64

````

## PDF page 65

FORMULA CHECK REQUIRED: original PDF page 65.

````text
——— (2005): “A Generalization Error for Q-learning,” Journal of Machine Learning
Research, 6, 1073–1097.
Nie, X., E. Brunskill, and S. Wager (2021): “Learning When-to-Treat Policies,”
Journal of the American Statistical Association, 116, 392–409.
Pelham Jr, W. E., G. A. Fabiano, J. G. Waxmonsky, A. R. Greiner, E. M.
Gnagy, W. E. Pelham III, S. Coxe, J. Verley, I. Bhatia, K. Hart, et al.
(2016):
“Treatment Sequencing for Childhood ADHD: A Multiple-Randomization
Study of Adaptive Medication and Behavioral Interventions,” Journal of Clinical Child
& Adolescent Psychology, 45, 396–415.
Qian, M. and S. A. Murphy (2011): “Performance Guarantees for Individualized
Treatment Rules,” The Annals of Statistics, 39, 1180.
Robins, J. M. (1986): “A New Approach to Causal Inference in Mortality Studies With
a Sustained Exposure Period—Application to Control of the Healthy Worker Survivor
Eﬀect,” Mathematical Modelling, 7, 1393–1512.
——— (1997):
“Causal Inference From Complex Longitudinal Data in Latent Vari-
able Modeling and Applications to Causality,” in Lecture Notes in Statistics, ed. by
M. Berkane, New York: Springer, 69–117.
——— (2004): “Optimal Structural Nested Models for Optimal Sequential Decisions,” in
Proceedings of the Second Seattle Symposium in Biostatistics. Lecture Notes in Statis-
tics, ed. by D. Y. Lin and P. J. Heagerty, New York: Springer, 189–326.
Rodr´ıguez, J., F. Saltiel, and S. Urz´ua (2022): “Dynamic Treatment Eﬀects of
Job Training,” Journal of Applied Econometrics, 37, 242–269.
Sakaguchi, S. (2025): “Estimation of Optimal Dynamic Treatment Assignment Rules
Under Policy Constraints,” Quantitative Economics, forthcoming.
Stoye, J. (2009): “Minimax regret treatment choice with ﬁnite samples,” Journal of
Econometrics, 151, 70–81.
——— (2012): “Minimax regret treatment choice with covariates or with limited validity
of experiments,” Journal of Econometrics, 166, 138–156.
Sun, Y. and L. Wang (2021): “Stochastic Tree Search for Estimating Optimal Dynamic
Treatment Regimes,” Journal of the American Statistical Association, 116, 421–432.
65

````

## PDF page 66

FORMULA CHECK REQUIRED: original PDF page 66.

````text
Tao, Y., L. Wang, and D. Almirall (2018): “Tree-Based Reinforcement Learning for
Estimating Optimal Dynamic Treatment Regimes,” The Annals of Applied Statistics,
12, 1914–1938.
Tetenov, A. (2012): “Statistical treatment choice based on asymmetric minimax regret
criteria,” Journal of Econometrics, 166, 157–165.
Thomas, P. and E. Brunskill (2016): “Data-Eﬃcient Oﬀ-Policy Policy Evaluation
for Reinforcement Learning,” in Proceedings of the 33rd International Conference on
Machine Learning, PMLR, 2139–2148.
Tsiatis, A. A., M. Davidian, S. T. Holloway, and E. B. Laber (2019): Dy-
namic Treatment Regimes: Statistical Methods for Precision Medicine, Chapman and
Hall/CRC.
Viviano, D. (2025): “Policy targeting under network interference,” Review of Economic
Studies, 92, 1257–1292.
Wallace, M. P. and E. E. Moodie (2015): “Doubly-Robust Dynamic Treatment
Regimen Estimation via Weighted Least Squares,” Biometrics, 71, 636–644.
Wang, L., A. Rotnitzky, X. Lin, R. E. Millikan, and P. F. Thall (2012):
“Evaluation of Viable Dynamic Treatment Regimes in a Sequentially Randomized Trial
of Advanced Prostate Cancer,” Journal of the American Statistical Association, 107,
493–508.
Watkins, C. J. and P. Dayan (1992): “Q-learning,” Machine learning, 8, 279–292.
Word, E., J. Johnston, H. P. Bain, B. D. Fulton, J. B. Zaharies, M. N. Lintz,
C. M. Achilles, J. Folger, and C. Breda (1990): “The State of Tennessee’s
Student/Teacher Achievement Ratio (STAR) Project: Technical Report (1985-1990).”
Tennessee State Department of Education.
Zhang, B., A. A. Tsiatis, E. B. Laber, and M. Davidian (2013): “Robust Esti-
mation of Optimal Dynamic Treatment Regimes for Sequential Treatment Decisions,”
Biometrika, 100, 681–694.
Zhang, B. and M. Zhang (2018): “C-learning: A new classiﬁcation framework to
estimate optimal dynamic treatment regimes,” Biometrics, 74, 891–899.
66

````

## PDF page 67

FORMULA CHECK REQUIRED: original PDF page 67.

````text
Zhang, Y., E. B. Laber, M. Davidian, and A. A. Tsiatis (2018): “Interpretable
Dynamic Treatment Regimes,” Journal of the American Statistical Association, 113,
1541–1549.
Zhao, Y., D. Zeng, A. J. Rush, and M. R. Kosorok (2012): “Estimating Individ-
ualized Treatment Rules Using Outcome Weighted Learning,” Journal of the American
Statistical Association, 107, 1106–1118.
Zhao, Y. Q., D. Zeng, E. B. Laber, and M. R. Kosorok (2015): “New Statistical
Learning Methods for Estimating Optimal Dynamic Treatment Regimes,” Journal of
the American Statistical Association, 110, 583–598.
Zhou, N., L. Wang, and D. Almirall (2023a): “Estimating tree-based dynamic
treatment regimes using observational data with restricted treatment sequences,” Bio-
metrics, 79, 2260–2271.
Zhou, Z., S. Athey, and S. Wager (2023b): “Oﬄine Multi-Action Policy Learning:
Generalization and Optimization,” Operations Research, 71, 148–183.
67

````

