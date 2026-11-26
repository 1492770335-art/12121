# Learning optimal dynamic treatment regimes from longitudinal data

Original PDF: [original.pdf](original.pdf). SHA256: `388ec4739981ae319a19cd4d3eeaee3d747b04fc6b2a028751d9cb2c5f72d9e1`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
arXiv:2401.10867v1  [stat.ME]  19 Jan 2024
Learning Optimal Dynamic Treatment Regimes from
Longitudinal Data
Nicholas T. Williams, MPH1, Katherine L. Hoﬀman, MS1, Iván Díaz, PhD2, Kara E.
Rudolph, PhD1, and 2
1Department of Epidemiology, Mailman School of Public Health, Columbia University, New York, New York
2Division of Biostatistics, Department of Population Health Sciences, New York University Grossman School of
Medicine, New York, New York
Abstract
Studies often report estimates of the average treatment eﬀect (ATE). While the ATE summa-
rizes the eﬀect of a treatment on average, it does not provide any information about the eﬀect of
treatment within any individual. A treatment strategy that uses an individual’s information to
tailor treatment to maximize beneﬁt is known as an optimal dynamic treatment rule (ODTR).
Treatment, however, is typically not limited to a single point in time; consequently, learning an
optimal rule for a time-varying treatment may involve not just learning the extent to which the
comparative treatments’ beneﬁts vary across the characteristics of individuals, but also learning
the extent to which the comparative treatments’ beneﬁts vary as relevant circumstances evolve
within an individual.
The goal of this paper is to provide a tutorial for estimating ODTR
from longitudinal observational and clinical trial data for applied researchers. We describe an
approach that uses a doubly-robust unbiased transformation of the conditional average treat-
ment eﬀect. We then learn a time-varying ODTR for when to increase buprenorphine-naloxone
(BUP-NX) dose to minimize return-to-regular-opioid-use among patients with opioid use disor-
der. Our analysis highlights the utility of ODTRs in the context of sequential decision making:
the learned ODTR outperforms a clinically deﬁned strategy.
1

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
Epidemiological studies often report estimates of the average treatment eﬀect (ATE), which
is an estimand that summarizes the diﬀerences in an outcome of interest if all members of a popula-
tion had been given a treatment or exposure compared to if all members of the population had been
left untreated, unexposed, or treated in some other way. While the ATE can be a useful measure
of whether a treatment is beneﬁcial or harmful on average, it does not provide information about
whether the treatment is beneﬁcial or harmful for a particular individual. Indeed, it is possible that
a treatment that is beneﬁcial on average for a population, could beneﬁt some individuals but harm
others—in other words, exhibit treatment eﬀect heterogeneity.
Personalized medicine operates on the premise that treatment eﬀect heterogeneity should
be assumed, and aims to tailor clinical interventions to ‘the uniquely evolving health status of
each patient’, rather than adopting a one-size-ﬁts-all approach.11,12 The fundamental principle
underlying personalized medicine—and, indeed, all clinical medicine—is that treatments should be
administered to those who stand to beneﬁt from them, while avoiding unnecessary treatment for
those who would not beneﬁt. A treatment strategy that deterministically assigns treatment as a
function of an individual’s history is known as a dynamic treatment rule, a dynamic treatment rule
that maximizes stratum-speciﬁc beneﬁt to a patient is known as an optimal dynamic treatment
rule (ODTR).20 For example, in a recent comparative eﬀectiveness trial of two common treatments
for opioid use disorder (OUD), an optimal treatment rule was learned in which patients who were
homeless were found to have lower risk of return-to-regular-opioid-use (RROU) if treated with
injection naltrexone, whereas patients with stable housing were found to have lower risk of relapse
if treated with the alternative medication, buprenorphine-naloxone (BUP-NX).26
Treatment, however, is typically not limited to a single point in time. Rather, it may
involve a series of decisions and adjustments. This is the case for treating opioid use with medication,
where, for example, a clinician may choose to increase the prescribed dose over time. Consequently,
learning an optimal rule for a time-varying treatment may involve not just learning the extent to
which the comparative treatments’ beneﬁts vary across the clinical characteristics of individuals, but
also learning the extent to which the comparative treatments’ beneﬁts vary as clinical characteristics
or other relevant circumstances evolve within an individual.
To our knowledge, much of the work on time-varying ODTRs has focused on the theory
underlying identiﬁcation of the causal parameters and estimation strategies.5,15,20,43,44 Tutorials
and/or software packages to facilitate implementation of these estimators for applied researchers are
largely absent, which could, in part, explain why time-varying ODTRs have not been more widely
adopted in epidemiology. In this paper we aim to address this gap by describing a doubly-robust
approach (the DR-estimator or DR-learner) to estimate a time-varying ODTR from observational
or randomized data.
We begin by providing intuition for understanding static and dynamic treatment rules.
We then explain how to use the DR-estimator to learn an ODTR for a single time-point, and then
generalize the procedure to the time-varying setting. Last, we apply this framework to learn the
ODTR for adapting weekly BUP-NX dose with respect to minimizing RROU over the ﬁrst 6-weeks
of treatment among patients with OUD. After learning the ODTR, we compare the estimated risk
of RROU under the ODTR to the estimated risk of RROU using two previously deﬁned BUP-NX
dosing rules.28
Intuition
We begin with some intuition for the single time-point setting. Denote A as the treatment, and Y
the outcome on which we aim to assess the eﬀect. Deﬁne d(V ) as a function that takes an input
2

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
of pre-treatment variables V and maps it to a value of A. We call d(V ) a treatment rule. The
possibly counterfactual outcome Yd is then the hypothetical value of Y if A were assigned according
to treatment rule d(V ).
Dynamic treatment rules
Imagine a hypothetical world where everyone receives the same value of a treatment or exposure.
This type of intervention, or treatment rule, can be described as static, because, in this alternate
world, all members of the population receive the same treatment; regardless of the input, d always
outputs the same value of A. In our application, one example of a static intervention would be to
prescribe all patients the same dose of BUP-NX (scenarios 1 and 2 in Table 1).
Now imagine another world where, instead of everyone receiving the same treatment, treat-
ment is assigned to a subject as function of their measured history (denote this H); this intervention
or rule is referred to as being dynamic.9 Consider, for example, the ﬁnding that individuals diagnosed
with OUD and who are housing-unstable have lower risk of RROU when prescribed extended-release
injection naltrexone versus when prescribed BUP-NX.26 A relevant dynamic treatment rule may be
one in which clinicians use their patient’s housing status to decide which pharmaceutical treatment
to prescribe. This dynamic rule could contain additional measured covariates, such as the patient’s
age or the length of time since their diagnosis with OUD. We may choose some or all of these
variables in H, denoted as V , to be part of the dynamic rule. In other words, the output of d now
changes according to the input of V (scenario 3 in Table 1).
Treatment plans rarely can be reduced to a single decision; often, they vary over-time. For
example, a physician treating OUD may be tasked with making a sequence of treatment decisions
for increasing or not increasing BUP-NX dose for a single patient at every follow-up appointment.
Consider a study with discrete time-points (i.e., days, weeks, months) where, at each time-point, a
patient can either receive a dose increase or not. Instead of a single treatment rule d, there is now a
sequence of possible treatment rules for each time-point {1, ..., τ} : D = [d1(V1), . . . , dτ(Vτ)] where
each rule dt conditions on the observed history–including both baseline covariates and time-varying
covariates–until the current time-point, Vt (scenario 4 in Table 1).
We note that deﬁning a dynamic treatment rule as a rule that conditions on any variable in
Ht is only one possible deﬁnition. Others have deﬁned dynamic treatment rules as treatment regimes
that vary over time and condition only on time-varying covariates up until the current time-point;
and deﬁned static treatment rules as those that condition only on baseline information.3 Using this
alternative deﬁnition, only scenario 4 in Table 1 would be considered a dynamic treatment rule.
3

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Table 1: Examples of static and dynamic treatment rules.
Scenario
Treatment rule
1. All patients are prescribed BUP-NX at an initial visit. A dose of 16/4 mg/day
is prescribed for all patients. BUP-NX dose is held constant throughout the
course of treatment.
Static
2. All patients are prescribed BUP-NX at an initial visit. All patients receive an
initial dose 4/1 mg/day. The treatment plan includes a dose increase every
two-weeks until a maximum dose of 24/6 mg/day is reached.
Static
3. All patients are prescribed BUP-NX at an initial visit.
Patients are either
prescribed an initial dose of 4/1 mg/day or 16/4 mg/day depending on the
level of their self-reported withdrawal symptoms. Regardless of patient char-
acteristics, the treatment plan includes a dose increase of 4/1 mg/day every
two-weeks until a maximum dose of 24/6 mg/day is reached.
Dynamic
4. All patients are prescribed BUP-NX at an initial visit. All patients receive
an initial dose of 4/1 mg/day. At each two-week follow-up visit, patients who
report any opioid use since the most recent visit receive a 4/1 mg/day BUP-
NX dose increase, up to a maximum dose of 24/6 mg/day; patients who do
not report any opioid use remain at the most recently prescried dose.
Dynamic
Optimal dynamic treatment rules
In any particular application, dependent on the number of covariates and their possible values, there
are numerous potential dynamic treatment rules. We will denote the set of all possible treatment
rules as D. One of these treatment rules d in the set D is optimal in the sense that it will maximize
the beneﬁt of a treatment in the population.20 We can deﬁne a treatment as “beneﬁcial” for a
particular subgroup characterized by covariate values, V = v, if their—potentially unobserved—
counterfactual outcome of interest had they received treatment is greater (if the outcome is desirable;
or smaller, if the outcome is undesirable) than if they hadn’t received treatment.
If we consider the expected value of the counterfactual outcome under a given treatment
rule, E[Yd], it then follows that the ODTR is the dynamic rule, dopt, that of all possible rules, D,
maximizes (for desirable outcomes; or minimizes, for harmful outcomes) E[Yd], which can formally
be denoted:
dopt ≡arg max
d∈D
E[Yd].
In the context of OUD research, estimating the ODTR would be relevant for research questions such
as, “using information collected at intake, for which patients should we increase BUP-NX dosage
after one-month of treatment to minimize week-12 return-to-regular-opioid-use?”.
When a treatment rule may vary over time, the time-varying ODTR is the sequence of
treatment rules, Dopt, that maximizes (or minimizes) the expected value of the counterfactual
outcome under that sequence of rules over all time-points, E[YD], which can formally be denoted:
Dopt ≡arg max
D∈D
E[YD].
4

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
In the context of OUD research, estimating the time-varying ODTR would be relevant for research
questions such as, “using each patient’s baseline history and information obtained in their weekly
follow-up visits, for which patients should we increase dosage of BUP-NX each week to minimize
week-12 return-to-regular-opioid-use?”
Evaluating the expected outcome under the ODTR
After learning an ODTR, it is often of interest to estimate the expected counterfactual outcome had
the ODTR been applied. This target causal parameter is denoted ψ ≡E[Ydopt] when treatment is
ﬁxed in time or ψ ≡E[YDopt] when treatment may vary over time. It is interpreted as the expected
value of the counterfactual outcome under the optimal dynamic treatment rule—the average value
of the counterfactual outcome of interest if, possibly contrary to what was observed, treatment had
been assigned according to the optimal rule.
Estimation
Multiple strategies exist for estimating the ODTR; in general, approaches fall into two broad cat-
egories: methods based on regression of the conditional average treatment eﬀect (CATE; most
commonly Q-learning19,39 and A-learning20), and classiﬁcation methods that directly estimate
the ODTR (outcome weighted learning [OWL]45, residual weighted learning [RWL]46, and aug-
mented outcome weighted learning14). In this paper, we described a nonparametric doubly-robust
regression-based strategy to learn the ODTR.
Notation
We ﬁrst give some further notation that is necessary for describing how to estimate the longitudinal
ODTR. Formally, consider a discrete-time process, t = 1, ..., τ, where we observe n i.i.d. copies
O1, ..., On of O = (L1, A1, . . . , Lτ, Aτ, Y ) generated from some unknown joint probability distribu-
tion P. At each time-point t, covariates Lt precede a binary treatment indicator At and an outcome
Y . We use Ht = (L1, ..., Lt, A1, ..., At−1) to denote the history of all variables up until just before
At. As previously mentioned, Vt is the subset of covariates Ht that will be used in the rule for
assigning At. Capital letters (e.g., A) indicate random variables while lower-case letters (e.g., a)
indicate realizations of a random variable. Symbols with a subscript n represent values estimated
from data (e.g., Pn is an estimate of P).
The blip function and DR-estimation of the ODTR for a single time-point
The conditional average treatment eﬀect (CATE), commonly referred to as the blip function24, is a
key component of learning the optimal rule using regression-based approaches.34 Using, ﬁrst, causal
notation, and second, notation as a function of the observed data, the blip function is deﬁned as:
B(V ) = E[Y1 −Y0|V ] ≡E
h
E[Y | H, A = 1] −E[Y | H, A = 0]
V
i
.
(1)
Assuming the counterfactual outcome for an observation under their observed treatment level is
the value of the outcome that we did actually observe (consistency), that all common causes of the
exposure and outcome are measured and adjusted for (no-unmeasured confounding or exchange-
ability), and that the probability of experiencing all treatment levels is non-zero for all observations
(positivity), the two are equal32. The optimal treatment for a given observation is assigned ac-
cording to the sign of the estimated blip, Bn(V ). For example, if we wish to maximize E[Yd], then
5

````

## PDF page 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
we would assign treatment to individuals where Bn(V ) is positive and not assign treatment where
Bn(V ) is negative:
dopt(V ) ≡I(B(V ) > 0).
(2)
Equation 1 reveals a simple substitution estimator for dopt(V ). We can ﬁrst estimate Q(H, A) =
E[Y | H, A]. We can then obtain estimates of the CATE: Q(H, A = 1) −Q(H, A = 0) by predicting
Qn(H, A) where A is ﬁxed to 1 and 0 respectively. The estimate Bn(V ) is then given by regressing
Qn(H, A = 1)−Qn(H, A = 0) on V and then predicting from this model with V equal to the values
observed (V = v).
While simple, performance of this estimator can be poor,10 and we can improve upon this
strategy by means of an unbiased transformation of B(V ). A function D(O) of the data is said to be
an unbiased transformation if E[D(O) | V ] = B(V ). We focus on the augmented inverse probability
weighting (AIPW)25 transformation of the ATE:
D(Q, g)(O) = 2A −1
g(A, H)

Y −Q(H, A)

+ Q(H, A = 1) −Q(H, A = 0),
(3)
where g(A, H) = P(A = a | H). This is an improvement, because the AIPW transformation is
doubly-robust; it requires, in addition to the estimation of Q(H, A), an estimate for the probability
of receiving the observed treatment g(A, H). If either Q(H, A) or g(A, H) is consistently estimated
we may obtain an unbiased estimate of B(V ). The double robustness property also allows us to use
ﬂexible, data-adaptive algorithms for model ﬁtting and make inferences about our estimates using
standard statistical theory.
Pseudo code for this algorithm is presented in Algorithm 1.
Algorithm 1 Estimation of dopt
1: m ←Regress(outcome = Y, predictors = {H, A})
2: g ←Regress(outcome = A, predictors = H)
3: Qn(H, A = 1) ←Predict(model = m, predictors = {H, A = 1})
4: Qn(H, A = 0) ←Predict(model = m, predictors = {H, A = 0})
5: gn ←A× Predict(g, H) + (1 −A) × (1−Predict(g, H))
6: Dn(Q, g) ←AIPW_Transformation(Y, Qn(H, A = 1), Qn(H, A = 0), gn)
⊲Equation 3
7: ˜m ←Regress(outcome = Dn(Q, g), predictors = V )
8: ˜Bn(V ) ←Predict(model = ˜m, predictors = V )
9: dn,opt(V ) ←I( ˜Bn(V ) > 0)
10: return dn,opt(V )
Extension of the DR-estimator to allow the ODTR to change over time
How can we move from estimating a single rule to estimating a sequence of rules?
Consider a
study with two time-points. The ODTR, Dopt, is the sequence of rules [d1, d2] that maximizes
E[YA1=d1,A2=d2].
All rules must have support in the data. This means that we must observe observations
that follow each rule. Intuitively, this leads us to begin at the last time-point, where we maximize
the expected value of the counterfactual outcome under a treatment rule at the last time-point.
The optimal rule d2,opt is the rule that maximizes E[YA2=d2]. This is the same estimation problem
as already discussed and thus we can use Algorithm 1 to generate an estimate of d2,opt. With an
6

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
estimate of d2,opt, our goal of estimating Dopt has now changed from ﬁnding [d1, d2] to maximize
E[YA1=d1,A2=d2] to ﬁnding d1 to maximize E[YA1=d1,A2=d2,opt].
The optimal treatment rule for treatment at the ﬁrst time-point is then the rule that
maximizes the expected value of the counterfactual outcome in a world where treatment at the
second time-point has already been optimally assigned. To solve this, we must redeﬁne the blip
function:
B1(V ) = E[YA1=1,A2=d2,opt −YA1=0,A2=d2,opt | V1]
= E

E

E[Y | H2, A2 = d2,opt]
 H1, A1 = 1

−E

E[Y | H2, A2 = d2,opt]
 H1, A1 = 0
  V1

.
We can estimate E(E[Y | H2, A2 = d2,opt] | H1, A1) by regressing ˜Y = Q2(H2, A2 = d2,opt), the
expected value of Q2 when A2 is set to d2,opt, on H1 and A1. The optimal rule for A1 is then given
by d1,opt = I(B1(V ) > 0), and Dopt = [d1,opt, d2,opt].
We can generalize this procedure to any time-horizon, τ, and also apply the strategy of
using doubly-robust unbiased transformations of Bt(V ). Pseudo code for this algorithm is presented
in Algorithm 2. First we amend the notation for the result of the AIPW transformation15 (4) as
Dt(dt+1,opt, Q, g) to highlight that the optimal rule at the current time is deﬁned with respect to
the distribution of the counterfactual outcome if at the next time-point treatment was optimally
assigned:
Dt(dt+1,opt, Q, g)(O) =
τ
X
s=t
 2At −1
gt(At, Ht)
s
Y
k=t+1
1(Ak = dk,opt)
gk(Ak, Hk)

×

Qs+1(Hs+1, ds+1,) −Qs(Hs, As)

+ Qt(Ht, At = 1) −Qt(Ht, At = 0).
(4)
Note that when t = τ or when τ = 1, Dt(dt+1,opt, Q, g) reduces to Equation 3.
Algorithm 2 Generalization of Algorithm 1 to estimate Dopt
1: ˜Y ←Y
2: for t = τ, . . . , 1 do
3:
m ←Regress(outcome = ˜Y , predictors = {Ht, At})
4:
g ←Regress(outcome = At, predictors = Ht)
5:
Qn(Ht, At = 1) ←Predict(model = m, predictors = {Ht, At = 1})
6:
Qn(Ht, At = 0) ←Predict(model = m, predictors = {Ht, At = 0})
7:
gn,t ←At× Predict(model = g, predictors = Ht)
+ (1 −At) × (1−Predict(model = g, predictors = Ht))
8:
Dn,t(Q, g) ←AIPW_Transformation(Y, Qn(Ht, At = 1), Qn(Ht, At = 0), gn,t)
⊲Equation 4
9:
˜m ←Regress(outcome = Dn,t(Q, g), predictors = Vt)
10:
˜Bn,t(Vt) ←Predict(model = ˜m, predictors = Vt)
11:
dn,t,opt ←I( ˜Bn,t(Vt) > 0)
12:
˜Y ←Predict(model = m, predictors = {Ht, A = dn,t,opt)}
13: end for
14: Dn,opt ←[dn,1,opt, . . . , dn,τ,opt]
15: return Dn,opt
7

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
The regressions in the above estimation algorithms can be ﬁtted by data-adaptive, machine-
learning algorithms, allowing for ﬂexible modelling while maintaining valid statistical inference. One
could use, for example, a decision tree to estimate ˜B(V ) and generate interpretable decision rules.
An R package to implement the method we describe is available for download from GitHub.
We conducted a limited simulation study to evaluate correct implementation of the estimator. How-
ever, we acknowledge that these simulations are not informative of general estimator performance.
Results of the simulation are presented in the Supplementary Materials.
Approaches to estimating the expected counterfactual outcome value under the
ODTR
The mean counterfactual outcome had the ODTR been applied can be estimated using diﬀerent
techniques such as targeted minimum loss-based estimation33,34 or estimators based on doubly-
robust unbiased transformations17. In addition to the standard set of assumptions for identifying
causal estimands from observational data, we refer readers to van der Laan and Luedtke 34 for
technical details on the necessary conditions required for consistently (i.e., approximately “unbiased”
as sample size increases) estimating the mean outcome under the learned ODTR and its conﬁdence
intervals. Intuitively, these assumptions include the assumption that the outcome regressions and
propensity scores are estimated correctly, as well as the assumption that the estimated functions are
“smooth enough”, although this assumption can be bypassed using sample splitting.36 Importantly,
the assumptions also include an assumption that the blip function is non-zero, that is, P(B(V ) =
0) = 0, so that no unit has a conditional average treatment eﬀect of exactly zero.
Example analysis: Learning the ODTR of when to increase BUP-NX
dose to minimize RROU
Learning an ODTR for BUP-NX dosage is of interest, because, currently, dosing decisions are made
at the discretion of addiction medicine clinicians and vary substantially, even among clinicians given
uniform guidance as part of clinical trials28. Under-dosing of medication used in treating OUD,
like BUP-NX, is relatively common and considered a contributing factor to poor OUD treatment
outcomes.4,8 Recently, Rudolph et al. 28 examined a time-varying, clinically-deﬁned dosing strategy
where BUP-NX dose was increased whenever a patient indicated opioid use in the prior week, and
found that this strategy resulted in a 7% reduced risk of RROU by week 12 of treatment compared
to a treatment strategy where BUP-NX dose was held constant. It is of interest to know whether
an ODTR learned from the data could reduce risk of RROU even further.
We used the DR-estimator described in Section 3.3 to learn a time-varying ODTR for when
to increase BUP-NX dose during the ﬁrst 6-weeks of treatment to minimize RROU. We compared
the estimated expected value of RROU under the learned ODTR to the estimated expected value
of RROU under two clinically deﬁned dosing strategies: 1) holding dose constant after three-weeks
of treatment (constant dosing rule; d0); and 2) increasing dose in response to opioid use during the
previous week (dynamic dosing rule; d1). Note that d1 was prespeciﬁed, is only a function of opioid
use at the prior week, and may not be optimal. In comparison, Dopt is learned, is a function of all
baseline and time-varying covariates, and is optimal.
We used data from the BUP-NX arms of three harmonized comparative eﬀectiveness trials
of medications for the treatment of OUD that were part of the NIDA Clinical Trials Network,
n = 2, 199 patients.13,22,29,40 Details of the treatment arms, sample size, and study years for each
trial in the harmonized cohort is shown in Table 2.
8

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
Table 2: Individual Clinical Trial Network (CTN) studies comprising the harmonized BUP-NX study cohort.
Study
CTN0027
CTN0030 Phase II
CTN0051
Study years
2006-2010
2006-2009
2014-2017
Sample size
1269
360
570
Study length (weeks)
24
12
24
Alternate arma
methadone
BUP-NX/drug counseling
XR-NTXb
a Subjects were randomized to receive this treatment arm or BUP-NX with standard medical care.
b Extended-release naltrexone.
We used RROU as the outcome of interest, deﬁned as the last day of 7-days of non-
study opioid use, or the ﬁrst-day of the fourth consecutive week of at-least-once-weekly non-study
opioid use. Non-study opioid use was determined using urine drug screens and timeline follow-
back interviews.
Missed visits and urine screening refusal were considered a positive for opioid
use, consistent with the primary trial papers and previous secondary analyses,13,22,27,28,41 and is
considered a reasonable assumption given prior research. In all three trials, BUP-NX was dispensed
for self-administration with dose and dose adjustments prescribed according to clinical judgment.
Our time-varying treatment of interest was an increase in the maximum weekly dispensed BUP-NX
dose from the prior-week, a binary (0/1) variable.28
Baseline confounders of the time-varying BUP-NX dose increase and time to RROU re-
lationship included race/ethnicity, age, biological sex, highest level of past opioid withdrawal dis-
comfort, past-year substance use disorders, history of neurological injury, history of psychiatric
disorders, history of IV drug use, and past-30 day drug use. Time-varying confounders included
most recently prescribed BUP-NX dose and an indicator of non-study opioid use during the prior
week.
Cross-ﬁt (CF) estimates of Qt(Ht, At) and gt(Ht, at) were ﬁt using the discrete super
learner35 with a learner library that included ℓ-1 regularization31, multivariate adaptive regression
splines [MARS]7, and gradient boosting.30 Super learning combines predictions from a set of user-
deﬁned learners using another algorithm, called the meta-learner.2,35 We used a "winner-take-all"
meta-learner, with the winner (the discrete super learner) chosen as the learner with the best cross-
validated mean squared error. For a full explanation of the super learner, we refer the reader to van
der Laan et al. 35 and Phillips et al. 21. Cross-ﬁt estimates of ˜Bt(V ) were ﬁt using ℓ-1 regularization.
We used a longitudinal sequentially doubly robust17 (SDR) estimator to estimate the mean
counterfactual week-6 relapse under each dosing strategy, ψ ≡[E(Yd0), E(Yd1), and E[YDn,opt)]. The
SDR estimator incorporated the same super learner library that was used for ﬁtting Qt(Ht, At) and
gt(Ht, at). We summarize our results using risk ratios (RR), comparing the mean counterfactual
week-6 RROU from the learned ODTR and the dosing rule from Rudolph et al. 28 to the constant
dose rule. Variances were estimated using the sample variance of the inﬂuence function of the log
RR.17 We used R23 (version 4.2.1) for all analyses with the lmtp6,42 packages. Code to replicate
the analyses is available on GitHub.
Results
The number of patients who would have BUP-NX dose increased or held constant and were observed
as having naturally followed a given rule are shown in Table 3. Table 3 also provides the estimated
expected risk of week-6 RROU under the dosing rules. Under the rule of increasing dose in response
to prior-week opioid use, d1, many individuals would receive dose increases early in treatment, but
fewer as treatment progresses. This is because the likelihood of using opioids decreases in time
as BUP-NX treatment continues.
In contrast, under the learned ODTR (without cross-ﬁtting),
9

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
BUP-NX dose would be increased for all patients every week of treatment, excluding week three.
Inspecting the models for ˜Bt(V ) revealed that none of the variables in Vt were retained as selected
features and that the models reduced to intercept-only models with the optimal rule for a given
week corresponding to the sign of Dn,t(Q, g).
We ﬁnd evidence that the learned ODTR would reduce the risk of RROU compared to
holding BUP-NX dose constant by 16.6% ( ˆ
RR: 0.83, 95% CI: 0.68, 1.02). Applying the dynamic
dosing rule, d1, from Rudolph et al. 28, we estimated a 10.5% ( ˆ
RR: 0.90, 95% CI: 0.84, 0.96)
reduction in risk of RROU compared to holding dose constant. Comparing the learned ODTR to
the dynamic dosing rule, we estimated a 6.8% reduction in risk oﬀRROU, however this diﬀerence
was not meaningful ( ˆ
RR: 0.93, 95% CI = 0.77, 1.13).
Table 3: Number of patients randomized to receive BUP-NX that were observed as following a given rule:
(Increase) increased dose under the rule and were observed as increasing dose, or (Constant) had a con-
stant dose under the rule and were observed as having a constant dose; and, estimates of the expected
counterfactual week-6 RROU under the given rule ( ˆψ).
Wk. 2
3
4
5
ˆψ ≡E[YD]
Learned ODTR, Dn,opt
Based on the CF
ODTR
Increase
236
30
84
44
0.324
Constant
319
888
292
285
95% CI = 0.261,0.387
Total
555
918
376
329
Based on the
ODTR learned
without CF
Increase
320
0
118
69
Constant
0
1109
0
0
Total
320
1109
118
69
Constant dosing rule
Total
1028
1109
947
928
0.388
Dn,opt a
675
180
611
545
95% CI = 0.358, 0.419
d1 b
375
269
227
125
Rudolph et al. 28 dynamic dosing rule, d1
Increase
147
59
40
24
0.348
Constant
605
702
685
698
95% CI = 0.327, 0.369
Total
752
761
725
722
a No. of dose increases that would have been indicated applying Dn,opt
b No. of dose increases that would have been indicated applying d1
Discussion
The average treatment eﬀect is a limited causal eﬀect measure insofar as it ignores treatment ef-
fect heterogeneity that may be practically important for improving treatment success for certain
subgroups of patients. While state-of-the-art methods exist for quantifying treatment eﬀect hetero-
geneity and for estimating optimal treatment rules,5,14,15,18–20,39,44–46 the papers establishing the
theory for these methods are not always approachable for the applied analyst.
Here, we provided intuition for dynamic treatment regimes and optimal dynamic treatment
regimes and presented a doubly-robust and ﬂexible modeling algorithm for estimating the ODTR
for both single time-point and time-varying treatments.
We applied this algorithm to learn a
longitudinal ODTR to minimize RROU over 6-weeks of BUP-NX MOUD treatment. We found
10

````

## PDF page 11

Technical extraction; compare with original PDF page 11.

````text
evidence that the learned optimal rule would decrease the risk of week-6 RROU compared to a
strategy where BUP-NX dose is held constant for the duration of treatment, and compared similarly
well to a pre-speciﬁed dynamic dosing strategy where BUP-NX dose was increased in response to
opioid use in the prior week.
The learned ODTR resulted in a treatment strategy where BUP-NX dose would be in-
creased at weeks two, four, and ﬁve of treatment, irrespective of patient history. This ODTR is not
particularly surprising given that: 1) under-dosing of BUP-NX is common,8 2) a key contributor to
poor OUD treatment outcomes,4 and 3) we considered only the ﬁrst six weeks of treatment, during
which time evidence suggests that dose should be increased regularly until a minimum threshold
(e.g., 16 mg1) is reached.28 We used a relatively simple model to estimate the ODTR, however,
any regression technique in the machine learning literature could be used, including more ﬂexible,
data-adaptive algorithms.
While we focused on presenting a single approach for learning the longitudinal ODTR,
other methods exist. Assuming their respective assumptions are satisﬁed, all of the algorithms pre-
viously mentioned in the Estimation Section are asymptotically consistent estimators of the ODTR;
however, their ﬁnite sample performance may vary. As a result, one algorithm may perform better
than another in any particular analysis.38 It is also plausible that the optimal treatment strategy
is a simple, static treatment rule, as may be the case with our illustrative application. With this in
mind, another approach, which we refer to as ODTR ensembles ,5,15,18 allows the analyst to spec-
ify a set of ODTR estimation algorithms (e.g., including both regression- and classiﬁcation-based
methods together with simple, static interventions) to “compete” against each other in estimating
the ODTR, with the optimal strategy data-adaptively chosen. We also limited our discussion to
learning the optimal decision rule for binary treatments and a single outcome. However, the de-
scribed approach can be modiﬁed to handle categorical exposures,37 resource constrained settings,16
informative-censoring,15 and survival outcomes.5
11

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
References
[1] Substance
Abuse
et
al.
Medications
for
opioid
use
disorder
for
healthcare
and
addiction
professionals,
policymakers,
patients,
and
families:
Treatment
improvement
protocol
tip
63.
2021.
URL
https://store.samhsa.gov/sites/default/files/SAMHSA_Digital_Download/PEP21-02-01-002.pdf.
[2] Leo Breiman. Stacked regressions. Machine Learning, 24, 1996. doi: 10.1007/BF00117832.
[3] Lauren E Cain, James M Robins, Emilie Lanoy, Roger Logan, Dominique Costagliola, and
Miguel A Hernán. When to start treatment?
a systematic approach to the comparison of
dynamic regimes using observational data.
The international journal of biostatistics, 6(2),
2010.
[4] Thomas D’Aunno, Sunggeun Ethan Park, and Harold A Pollack. Evidence-based treatment
for opioid use disorders: A national study of methadone dose levels, 2011–2017. Journal of
Substance Abuse Treatment, 96, 2019.
[5] Iván Díaz, Oleksandr Savenkov, and Karla Ballman. Targeted learning ensembles for optimal
individualized treatment rules with time-to-event outcomes. Biometrika, 105(3):723–738, 2018.
doi: 10.1093/biomet/asy017.
[6] Iván Díaz, Nicholas Williams, Katherine Hoﬀman, and Edward Schneck. Non-parametric causal
eﬀects based on longitudinal modiﬁed treatment policies. Journal of the American Statistical
Association, 2021. doi: 10.1080/01621459.2021.1955691.
[7] Jerome H Friedman. Multivariate adaptive regression splines. The Annals of Statistics, pages
1–67, 1991.
[8] Adam J Gordon, Wei-Hsuan Lo-Ciganic, Gerald Cochran, Walid F Gellad, Terri Cathers, David
Kelley, and Julie M Donohue. Patterns and quality of buprenorphine opioid agonist treatment
in a large medicaid program. Journal of Addiction Medicine, 9(6), 2015.
[9] Miguel A Hernán and James M Robins. Causal Inference: What If, chapter Time-varying
treatments. Chapman & Hall/CRC, Boca Raton, 2020.
[10] Edward H Kennedy. Towards optimal doubly robust estimation of heterogeneous causal eﬀects.
arXiv preprint arXiv:2004.14497, 2020.
[11] Michael R Kosorok and Eric B Laber. Precision medicine. Annual review of statistics and its
application, 6:263–286, 2019.
[12] Michael R Kosorok, Eric B Laber, Dylan S Small, and Donglin Zeng. Introduction to the theory
and methods special issue on precision medicine and individualized policy discovery, 2021.
[13] Joshua D Lee, Edward V Nunes Jr, Patricia Novo, Ken Bachrach, Genie L Bailey, Snehal Bhatt,
Sarah Farkas, Marc Fishman, Phoebe Gauthier, Candace C Hodgkins, et al.
Comparative
eﬀectiveness of extended-release naltrexone versus buprenorphine-naloxone for opioid relapse
prevention (X:BOT): a multicentre, open-label, randomised controlled trial. The Lancet, 391
(10118):309–318, 2018.
12

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
[14] Ying Liu, Yuanjia Wang, Michael R. Kosorok, Yingqi Zhao, and Donglin Zeng. Augmented
outcome-weighted learning for estimating optimal dynamic treatment regimens. Statistics in
Medicine, 37(26):3776–3788, 2018. doi: https://doi.org/10.1002/sim.7844.
[15] Alexander Luedtke and Mark van der Laan.
Super-learning of an optimal dynamic treat-
ment rule.
The International Journal of Biostatistics, 12:305–332, 05 2016.
doi: 10.1515/
ijb-2015-0052.
[16] Alexander R Luedtke and Mark J van der Laan. Optimal individualized treatments in resource-
limited settings. The International Journal of Biostatistics, 12(1):283–303, 2016.
[17] Alexander R. Luedtke, Oleg Sofrygin, Mark J. van der Laan, and Marco Carone. Sequential
double robustness in right-censored longitudinal models, 2018.
[18] Lina M. Montoya, Mark J. van der Laan, Alexander R. Luedtke, Jennifer L. Skeem, Jeremy R.
Coyle, and Maya L. Petersen. The optimal dynamic treatment rule superlearner: considera-
tions, performance, and application to criminal justice interventions. The International Journal
of Biostatistics, 2022. doi: 10.1515/ijb-2020-0127.
[19] Erica E. M. Moodie, Bibhas Chakraborty, and Michael S. Kramer. Q-learning for estimating
optimal dynamic treatment rules from observational data. Canadian Journal of Statistics, 40
(4):629–645, 2012. doi: https://doi.org/10.1002/cjs.11162.
[20] Susan A Murphy. Optimal dynamic treatment regimes. Journal of the Royal Statistical So-
ciety: Series B (Statistical Methodology), 65(2):331–355, 2003. doi: https://doi.org/10.1111/
1467-9868.00389.
[21] Rachael V Phillips, Mark J van der Laan, Hana Lee, and Susan Gruber. Practical considerations
for specifying a super learner. International Journal of Epidemiology, 52(4):1276–1285, 2023.
[22] Jennifer S Potter, Elise N Marino, Maureen P Hillhouse, Suzanne Nielsen, Katharina Wiest,
Catherine P Canamar, Judith A Martin, Alfonso Ang, Rachael Baker, Andrew J Saxon, et al.
Buprenorphine/naloxone and methadone maintenance treatment outcomes for opioid analgesic,
heroin, and combined users: ﬁndings from starting treatment with agonist replacement thera-
pies (START). Journal of Studies on Alcohol and Drugs, 74(4):605–613, 2013.
[23] R Core Team. R: A Language and Environment for Statistical Computing. R Foundation for
Statistical Computing, Vienna, Austria, 2022. URL https://www.R-project.org/.
[24] James M Robins. Optimal structural nested models for optimal sequential decisions. In Pro-
ceedings of the Second Seattle Symposium in Biostatistics: analysis of correlated data, pages
189–326. Springer, 2004.
[25] James M Robins, Andrea Rotnitzky, and Lue Ping Zhao. Estimation of regression coeﬃcients
when some regressors are not always observed. Journal of the American Statistical Association,
89(427):846–866, 1994.
[26] Kara E Rudolph, Iván Díaz, Sean X Luo, John Rotrosen, and Edward V Nunes. Optimizing
opioid use disorder treatment with naltrexone or buprenorphine. Drug and Alcohol Dependence,
228:109031, 2021.
13

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
[27] Kara E Rudolph, Nicholas T Williams, Ivan Díaz, Sean X Luo, John Rotrosen, and Edward V
Nunes. Optimally choosing medication type for patients with opioid use disorder. American
Journal of Epidemiology, 2022.
[28] Kara E Rudolph, Nicholas T Williams, Alicia T Singham Goodwin, Matisyahu Shulman, Marc
Fishman, Iván Díaz, Sean Luo, John Rotrosen, and Edward V Nunes.
Buprenorphine &
methadone dosing strategies to reduce risk of relapse in the treatment of opioid use disorder.
Drug and alcohol dependence, 239:109609, 2022.
[29] Andrew J Saxon, Walter Ling, Maureen Hillhouse, Christie Thomas, Albert Hasson, Alfonso
Ang, Geetha Doraimani, Gudaye Tasissa, Yuliya Lokhnygina, JeﬀLeimberger, et al. Buprenor-
phine/naloxone and methadone eﬀects on laboratory indices of liver health: a randomized trial.
Drug and alcohol dependence, 128(1-2):71–76, 2013.
[30] Yu Shi, Guolin Ke, Damien Soukhavong, James Lamb, Qi Meng, Thomas Finley, Taifeng Wang,
Wei Chen, Weidong Ma, Qiwei Ye, Tie-Yan Liu, and Nikita Titov. lightgbm: Light Gradient
Boosting Machine, 2022. URL https://CRAN.R-project.org/package=lightgbm. R package
version 3.3.2.
[31] Robert Tibshirani.
Regression shrinkage and selection via the lasso.
Journal of the Royal
Statistical Society: Series B (Methodological), 58(1):267–288, 1996.
[32] Mark J van der Laan. Statistical inference for variable importance. The International Journal
of Biostatistics, 2(1), 2006.
[33] Mark J van der Laan and Susan Gruber. Targeted minimum loss based estimation of causal
eﬀects of multiple time point interventions. The International Journal of Biostatistics, 8, 2012.
doi: 10.1515/1557-4679.1370.
[34] Mark J van der Laan and Alexander R Luedtke. Targeted learning of the mean outcome under
an optimal dynamic treatment rule. Journal of Causal Inference, 3(1):61–95, 2015.
[35] Mark J van der Laan, Eric C Polley, and Alan E Hubbard. Super learner. Statistical Applications
in Genetics and Molecular Biology, 6(1), 2007.
[36] Mark J van der Laan, Sherri Rose, Wenjing Zheng, and Mark J van der Laan. Cross-validated
targeted minimum-loss-based estimation. Targeted learning: causal inference for observational
and experimental data, pages 459–474, 2011.
[37] Mark J van der Laan, Jeremy Coyle, Nima Hejazi, Ivana Malenica, Rachael Phillips, and Alan
Hubbard. Targeted Learning in R: Causal Data Science with the tlverse Software Ecosystem.
2023. URL https://tlverse.org/tlverse-handbook/.
[38] Yuanjia Wang, Peng Wu, Ying Liu, Chunhua Weng, and Donglin Zeng.
Learning optimal
individualized treatment rules from electronic health record data. In 2016 IEEE International
Conference on Healthcare Informatics (ICHI), pages 65–71, 2016. doi: 10.1109/ICHI.2016.13.
[39] Christopher John Cornish Hellaby Watkins. Learning from delayed rewards. 1989.
[40] Roger D Weiss, Jennifer Sharpe Potter, Scott E Provost, Zhen Huang, Petra Jacobs, Albert
Hasson, Robert Lindblad, Hilary Smith Connery, Kristi Prather, and Walter Ling. A multi-
site, two-phase, prescription opioid addiction treatment study (POATS): rationale, design, and
methodology. Contemporary Clinical Trials, 31(2):189–199, 2010.
14

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
[41] Roger D Weiss, Jennifer Sharpe Potter, David A Fiellin, Marilyn Byrne, Hilary S Connery,
William Dickinson, John Gardin, Margaret L Griﬃn, Marc N Gourevitch, Deborah L Haller,
et al. Adjunctive counseling during brief and extended buprenorphine-naloxone treatment for
prescription opioid dependence: a 2-phase randomized controlled trial. Archives of general
psychiatry, 68(12):1238–1246, 2011.
[42] Nicholas
T
Williams
and
Iván
Díaz.
lmtp:
An
R
package
for
estimating
the
causal
eﬀects
of
modiﬁed
treatment
policies.
Observational
Studies,
2023.
URL
https://muse.jhu.edu/article/883479.
[43] Baqun Zhang, Anastasios A. Tsiatis, Eric B. Laber, and Marie Davidian. Robust estimation
of optimal dynamic treatment regimes for sequential treatment decisions. Biometrika, 100(3):
681–694, 2013. doi: 10.1093/biomet/ast014.
[44] Ying-Qi Zhao, Donglin Zeng, Eric B. Laber, and Michael R. Kosorok. New statistical learning
methods for estimating optimal dynamic treatment regimes. Journal of the American Statistical
Association, 110(510):583–598, 2015. doi: 10.1080/01621459.2014.937488.
[45] Yingqi Zhao, Donglin Zeng, A. John Rush, and Michael R. Kosorok. Estimating individu-
alized treatment rules using outcome weighted learning. Journal of the American Statistical
Association, 107(499):1106–1118, 2012. doi: 10.1080/01621459.2012.695674.
[46] Xin Zhou, Nicole Mayer-Hamblett, Umer Khan, and Michael R. Kosorok. Residual weighted
learning for estimating individualized treatment rules.
Journal of the American Statistical
Association, 112(517):169–187, 2017. doi: 10.1080/01621459.2015.1093947.
A
Simulation
We considered the following DGM:
W1 ∼U(−1, 1)
W2 ∼U(−1, 1)
P(A1 = 1) = expit(0.5 −1.3W1 + 0.4W2)
W3 ∼U(−1, 1) × 1.25A1 + 0.25
P(A2 = 1) = expit(0.5 + 0.4A1 −1.5W3)
Y ∼N(0.4 −0.4A1 −A2W3 −4A1W1 + 0.08A1A2 + A2W3 −4A1W1 −2A1W2 −0.1A2 + 1.5W1, 1)
We evaluated estimator performance in terms of absolute bias, absolute bias scaled by
√n, and 95% conﬁdence interval (CI) coverage. We conducted 1000 simulations for sample sizes
n ∈{500, 1000, 10000}. The true value of ψ is approximately 0.248.
Table 4: Simulation results.
n
ˆψ
|Bias|
√n × |Bias|
95% CI Covr.
500
2.269
0.023
0.514
0.929
1000
2.267
0.021
0.653
0.925
10000
2.250
0.004
0.378
0.875
15

````

