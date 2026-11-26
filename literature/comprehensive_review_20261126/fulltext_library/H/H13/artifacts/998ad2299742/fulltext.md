# Methodological Tutorial Series for Epidemiological Studies: Beyond the Hazard Ratio: Causal Inference From Time-to-event Data With Dependent Censoring, Confounding, and Competing Risks

Original PDF: [original.pdf](original.pdf). SHA256: `998ad22997422ec9f8abddfe8ced85632eeea3698bd023c56d02edbc9a7eb0ff`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1; PDF label 1

Technical extraction; compare with original PDF page 1.

````text
Special Article
J Epidemiol 2026
Methodological Tutorial Series for Epidemiological Studies:
Beyond the Hazard Ratio: Causal Inference From Time-to-event Data
With Dependent Censoring, Confounding, and Competing Risks
Takuya Kawahara1, Sho Komukai2, Kosuke Inoue3, and Tomohiro Shinozaki4,5
1Clinical Research Promotion Center, The University of Tokyo Hospital, Tokyo, Japan
2Department of Health Data Science, Tokyo Medical University, Tokyo, Japan
3Department of Health Promotion and Behavioral Sciences, Graduate School of Medicine, Kyoto University, Kyoto, Japan
4Interfaculty Initiative in Information Studies, the University of Tokyo, Tokyo, Japan
5Department of Biostatistics, School of Public Health, Graduate School of Medicine, the University of Tokyo, Tokyo, Japan
Received December 5, 2025; accepted April 20, 2026; released online May 2, 2026
ABSTRACT
In epidemiological research, time-to-event outcomes, commonly referred to as survival outcomes, are a common subject of
investigation. Here, we ﬁrst describe the circumstances under which methods of survival analysis are necessary, review the roles of
hazard functions, and discuss the limitations of hazard ratios for causal inference. Second, we explain how confounding and
dependent censoring, which are common in observational studies, can be addressed by inverse probability weighting and
parametric g-formula estimators. We emphasize that hazards serve as building blocks for estimating counterfactual risks. Third, we
summarize recent developments in deﬁning causal estimands in the presence of competing risks, including risk without eliminating
competing events, net risk, and cumulative incidence under modiﬁed treatment. To illustrate how these challenges are addressed in
practice, we revisit a recent clinical study on pharmacological interventions for the onset of dementia. We further empirically
compare various estimands in the presence of competing events, including separable eﬀects, through simulations. Our overall aim
is to elucidate the need to move beyond routinely used methods of survival analysis, particularly the mere estimation of hazard
ratios, if the goal is to draw causal inferences. This paper provides an overview of causal survival analysis, focusing on how
confounding, dependent censoring, and competing risks can be addressed to estimate causal parameters of interest (counterfactual
survival functions or counterfactual risks), which are interpretable and often meaningful for investigators.
Key words: censoring; competing risk; confounding; inverse probability weighting; parametric g-formula
Copyright © 2026 Takuya Kawahara et al. This is an open access article distributed under the terms of Creative Commons Attribution License,
which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.
INTRODUCTION
In epidemiological research, time-to-event outcomes, commonly
referred to as survival outcomes, are often a subject of inves-
tigation. Since survival time is a positive, continuous variable (just
like weight or blood pressure), multiple summary measures are
possible to quantify group diﬀerences. Among these, the hazard
or, more typically, the hazard ratio, has been a popular eﬀect
measure in survival analyses, possibly because we can address two
critical challenges that frequently arise in survival analysis:
censoring and confounding. Speciﬁcally, Cox proportional hazards
modeling simultaneously handles both issues within a regression
framework.1
In practice, observational studies for survival outcomes
involving multiple exposure groups have conventionally relied
on a triad of methods: i) descriptive summarization of survival
distributions by the Kaplan–Meier estimator; ii) log-rank testing
for diﬀerences in survival distributions between groups; and iii)
Cox modeling to estimate adjusted hazard ratios. This “KM–log-
rank–Cox” paradigm has become the de facto standard. However,
direct transplantation of methods designed for randomized trials
into observational studies is increasingly being recognized as
potentially not yielding good causal inference. This is because
exposure allocations and censoring processes, which may depend
on the potential event processes in observational studies, are no
longer under experimental control.
We consider that the use of survival data does not inherently
justify the use of standard techniques for survival analysis as the
primary analytical approach. For example, Cox modeling provides
convenient access to hazard ratios while adjusting for confounders
but does not imply that hazard ratios are optimal or even
appropriate causal estimands in all contexts. The hazard ratio is
intrinsically a model-dependent quantity that can be diﬃcult to
interpret even under the correct modeling assumptions.
A promising alternative is to adopt an analytical framework that
explicitly targets counterfactual survival functions or counter-
factual risks. These quantities can be deﬁned without reference
to any speciﬁc statistical model and are intrinsically more inter-
Address for correspondence. Takuya Kawahara, Clinical Research Promotion Center, The University of Tokyo Hospital, 7-3-1 Hongo, Bunkyo-ku, Tokyo 113-8655,
Japan (e-mail: takuyakawahara@g.ecc.u-tokyo.ac.jp).
Advance Publication by J-STAGE
Journal of Epidemiology
DOI https://doi.org/10.2188/jea.JE20250662
HOMEPAGE https://jeaweb.jp/journal/index.html
JE20250662-1

````

## PDF page 2; PDF label 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
pretable as causal estimands. We refer to the approach of drawing
causal inferences using explicit counterfactual models as causal
survival analysis.2 Within this framework, we try to reconstruct
counterfactual scenarios such as “what would the survival experi-
ence have been in the absence of censoring?” and “what would
have been observed if all individuals had been exposed (or
unexposed)?” This perspective aligns naturally with the principle
of target trial emulation, which aims to formalize causal questions
by emulating a hypothetical randomized trial based on the
available observational data.3
The present paper provides an overview of causal survival
analysis, structured along the following three key dimensions.
First, we discuss causal eﬀect measures for survival outcomes,
highlighting the interpretability and limitations of hazard ratios,
even when they are identiﬁed as a counterfactual quantity under
suitable assumptions. Second, we review methodological strat-
egies to estimate counterfactual survival functions or counter-
factual risks, with an emphasis on adjusting for both confound-
ing and dependent censoring. Particular attention is given to
approaches that treat hazards not as eﬀect measures, but as
building blocks used to reconstruct the counterfactual survival
distribution. Third, we address the issue of competing risks,
discussing how causal eﬀects should be deﬁned and estimated
when competing events are present. We argue that neither survival
analysis methods nor conventional competing risks models, such
as the Fine–Gray subdistribution hazards model, fully resolve the
complications introduced by competing risks. However, recent
methodological developments, including separable eﬀects and
related approaches, oﬀer promising avenues for deriving causally
interpretable estimands under competing risks. Finally, we revisit a
recent clinical study that investigated the eﬀects of pharmaco-
logical interventions on the onset of dementia, to illustrate
how these challenges can be addressed in practice. We further
empirically compare estimates of various estimands through
simulations in the presence of competing events.
This paper provides an overview of causal survival analyses,
sharing similar aims with several recently published papers,
although those papers did not fully cover our topics. For example,
Denz et al reviewed statistical methods for time-to-event data, with
a particular focus on confounding adjustment.4 Their review
covers a broader range of approaches than ours, including doubly
robust estimators, but they did not address dependent censoring or
competing risks. Talbot et al5 recently published a demonstration
of implementing the targeted maximum likelihood estimator
(TMLE) for time-to-event data but did not address settings with
competing risks.
EFFECT MEASURES FOR TIME-TO-EVENT
OUTCOMES
How to summarize and compare distributions of
survival time
Let A denote a treatment or exposure (we use these words
interchangeably) that takes the value a in a well-deﬁned support,
for example, a = 0 for no treatment and a = 1 for the treatment of
interest. In survival analysis, the outcome variable T (eg, time in
years) is the “survival” time, measured from a deﬁned starting
point (“time zero”) to the time of the event of interest. The event in
question may be death (as implied by the word “survival”), but can
also represent other outcomes, such as disease onset or even a
beneﬁcial event such as hospital discharge (hence we often use the
term “time-to-event” outcome instead). If the event can occur
multiple times (eg, asthma attacks), we may deﬁne T as the time
to the ﬁrst onset of the event, although multiple time-to-event
variables can be deﬁned and treated within the framework of
recurrent event data analysis.6,7
As in the typical causal inference literature,2 we use the
counterfactual notation, using the potential time-to-event variable
Ta, which would be observed had treatment A been set at a.
Speciﬁcally, Ta=1 represents the potential survival time under
treatment and Ta=0 the potential survival time under no treatment
for binary treatments. Note that Ta=1 and Ta=0 cannot be simul-
taneously observed in the real world, and an unobservable poten-
tial variable (or variables) becomes counterfactual. To link the
potential variable Ta to the observable variable T, we assume
causal consistency2: Ta = T if A = a.
The time-to-event variable T is essentially a continuous variable
that only takes positive values, just like weight (in kilograms) or
blood pressure (in millimeters of mercury). Hence, in principle, we
can display T using histograms or empirical distribution functions
(viewed as cumulative histograms), which represent estimates
of probability density functions f(t) and cumulative distribution
functions F(t) of T, respectively. A distribution function is thus the
probability of an event developing by time t,
FðtÞ ¼ PrðT  tÞ ¼ PrðYt ¼ 1Þ;
where Yt = I(T ≤t) is an indicator of event occurrence by time t,
which takes a value of 1 if the event has occurred by t (ie, T ≤t)
and 0 otherwise (ie, T > t). The corresponding distribution and
density functions are deﬁned for potential time-to-event variables
as follows:
FaðtÞ ¼ PrðT a  tÞ ¼ PrðYa
t ¼ 1Þ;
f aðtÞ ¼ dFaðtÞ
dt
;
where Ya
t ¼ IðT a  tÞ is an indicator function of potential event
occurrence under A = a by time t.
The natural choice of causal contrast for comparing counter-
factual distributions is a diﬀerence in average survival times:
EðT a¼1Þ  EðT a¼0Þ;
which summarizes and compares the counterfactual distributions
through EðT aÞ ¼
R 1
0 t  f aðtÞdt ¼
R 1
0 SaðtÞdt, where Sa(t) = 1 −
Fa(t) = Pr(Ta > t) is a counterfactual survival function under
A = a. As explained later, however, the diﬀerence in averages is
generally diﬃcult to estimate in epidemiological or clinical study
settings. Hence, other choices of eﬀect measures are useful in
survival analysis, such as:
PrðYa¼1
t
¼ 1Þ  PrðYa¼0
t
¼ 1Þ ¼ Fa¼1ðtÞ  Fa¼0ðtÞ
¼ Sa¼0ðtÞ  Sa¼1ðtÞ
ðrisk difference at time tÞ;
PrðYa¼1
t
¼ 1Þ
PrðYa¼0
t
¼ 1Þ ¼ Fa¼1ðtÞ
Fa¼0ðtÞ
ðrisk ratio at time tÞ;
PrðYa¼1
t
¼ 0Þ
PrðYa¼0
t
¼ 0Þ ¼ Sa¼1ðtÞ
Sa¼0ðtÞ
ðsurvival ratio at time tÞ;
Fa¼1;1ð0:5ÞFa¼0;1ð0:5Þ ðdifference in median survival timeÞ;
E½minðT a¼1;ÞE½minðT a¼0;Þ ¼
Z 
0
Sa¼1ðtÞdt
Z 
0
Sa¼0ðtÞdt
ð-restricted mean survival time differenceÞ;
Causal Survival Analysis in Observational Studies
2 j J Epidemiol 2026

````

## PDF page 3; PDF label 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
where Fa,−1(p) is an inverse function of Fa(·) that returns a 100p
percentile of the distribution of Ta. Another representation of the
distribution of T is a hazard function:
aðtÞ ¼ f aðtÞ
SaðtÞ :
The hazard is interpretable as the “instantaneous rate” or
“intensity” of developing an event at time t, conditional on the
event not occurring until just before t. Counterfactual hazards
under diﬀerent treatment levels at time t may be compared in
terms of the ratio
a¼1ðtÞ
a¼0ðtÞ ;
which is popularly used as the hazard ratio at time t.
The functions f a(t), Fa(t), Sa(t), and λa(t) have a one-to-one
correspondence. That is, once any one of these functions is known,
the others can be derived. In principle, we can empirically identify
these functions through ideal randomized trials, which ensure con-
ditions of causal identiﬁability (ie, exchangeability, causal con-
sistency, and positivity).2 For example, the counterfactual survival
function is identiﬁed as
SaðtÞ ¼ SðtjA ¼ aÞ;
where S(t∣A = a) = Pr(T > t∣A = a) is a conditional survival func-
tion in the subpopulation with A = a, which equals the conditional
probability of observable T exceeding t given A = a. Accordingly,
once we identify at least one of the counterfactual functions for the
distribution of Ta, we can adequately summarize the distribution
by any of mean (unrestricted or restricted within a speciﬁc inter-
val), risk at a speciﬁc time point, median, and hazard at a speciﬁc
time point.
Estimating
eﬀect
measures
in
the
presence
of
censoring
If survival time T were to be fully observed for all individuals in
the randomized study, any of the functions representing the
distribution of Ta could be estimated without bias by the empirical
distribution within the subgroup with treatment A = a. For exam-
ple, from the dataset (Ai, Ti) obtained from participant i (i = 1,…,
n), average survival time diﬀerence E(Ta=1) −E(Ta=0) is estimated
by the mean in the empirical distribution
Xn
i¼1 AiTi
Xn
i¼1 Ai

Xn
i¼1ð1  AiÞTi
Xn
i¼1ð1  AiÞ
Similarly, the risk diﬀerence at t, PrðYa¼1
t
¼ 1Þ  PrðYa¼0
t
¼ 1Þ, is
estimated by the derived variable Yt,i = I(Ti ≤t):
Xn
i¼1 AiYt;i
Xn
i¼1 Ai

Xn
i¼1ð1  AiÞYt;i
Xn
i¼1ð1  AiÞ
These are essentially the same as the analysis of continuous and
binary outcomes, and we face no challenges in the estimation
process for survival outcomes in this setting.
However, in most cases, T suﬀers from censoring due to the
administrative end of follow-up (ie, follow-up ﬁnishes on a
prespeciﬁed date, at which point some participants remain free of
the event) or loss to follow-up before this date due to various
reasons, such as hospital transfer or death due to an unrelated event
like a traﬃc accident. Such censoring leaves actual times to events
unobserved, so we cannot directly use the empirical distribution to
estimate summary measures in the previous section.
Nevertheless, if the “time to censoring” is independent of the
time to event T within each treatment group, the Kaplan–Meier
estimator8,9 provides an unbiased estimate of survival functions
S(t∣A = a) in large samples. This allows unbiased estimates of
eﬀect measures to be obtained based on Sa(t) or Fa(t) under the
causal identiﬁability conditions.2 For example, once we obtain the
Kaplan–Meier estimate ^SKMðtjA ¼ aÞ throughout all t, the estimate
of average survival time for each treatment group can be obtained
as the area under ^SKMðtjA ¼ aÞ from t = 0 to the last observed time
that corresponds to ^SKMðtjA ¼ aÞ ¼ 0. The diﬀerence in these
areas gives an estimate of the average diﬀerence in survival time
between treatment groups. Unfortunately, because ^SKMðtjA ¼ aÞ is
only estimated through the time to the last observed event (denoted
by tlast), areas under ^SKMðtjA ¼ aÞ become unavailable after tlast if
the time for the last observed participant is censored. However, for
any t ≤tlast, we can estimate PrðYa¼1
t
¼ 1Þ  PrðYa¼0
t
¼ 1Þ ¼
Sa¼0ðtÞ  Sa¼1ðtÞ by
^SKMðtjA ¼ 0Þ  ^SKMðtjA ¼ 1Þ:
Likewise, when both ^SKMðtjA ¼ 1Þ and ^SKMðtjA ¼ 0Þ yield values
below 0.5, the diﬀerence in median survival times is estimated by
^S1
KMð0:5jA ¼ 1Þ  ^S1
KMð0:5jA ¼ 0Þ;
where
^S1
KMð0:5jA ¼ aÞ
returns
a
median
tmed
such
that
^SKMðtmedjA ¼ aÞ ¼ 0:5 from the Kaplan–Meier estimates. The
diﬀerence in restricted mean survival time is estimable for any τ
less than the minimum of tlast for A = 0 and A = 1, by calculating
the area under the curve of Kaplan–Meier estimates from t = 0 to τ:
Z 
0
^SKMðtjA ¼ 1Þdt 
Z 
0
^SKMðtjA ¼ 0Þdt:
Note that the (unrestricted and restricted) mean, risk, and
median estimates based on the Kaplan–Meier estimate reduce to
the corresponding empirical distribution summary when no ob-
served time is censored. When censoring is present, and if the
censoring is independent of the time to the event, the Kaplan–
Meier estimate is interpretable as the empirical distribution as if
censoring had been eliminated. Hence, all the above survival
contrasts estimated by the Kaplan–Meier estimator are interpret-
able as causal contrasts, provided the causal identiﬁability condi-
tions hold.2 That is, they compare counterfactual summaries under
diﬀerent conditions (ie, a = 1 vs a = 0) in the same population.
The role of estimating hazards in survival analysis
Survival analysis is often formulated in continuous time, as
described previously. However, causal survival methods are
frequently
implemented
using
discrete-time
representations
because this facilitates the incorporation of time-varying treat-
ments and covariates. We therefore introduce a discrete-time
framework while noting that the discrete- and continuous-time
representations are closely related. In particular, we consider the
discrete-time setting in which the follow-up time is divided by
intervals (ideally of the same length, eg, days, months, years)
k = 1,…, K, and Yk indicates the event occurrence by the end of
interval k.10 The survival function at k is then written as:
SðkjA ¼ aÞ
¼ PrðY1 ¼ 0jA ¼ aÞ PrðY2 ¼ 0jY1 ¼ 0; A ¼ aÞ
   PrðYk ¼ 0jYk1 ¼ 0; A ¼ aÞ:
Kawahara T, et al.
J Epidemiol 2026 j 3

````

## PDF page 4; PDF label 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Here, Pr(Yk = 1∣Yk−1 = 0, A = a) = 1 −Pr(Yk = 0∣Yk−1 = 0, A = a)
is a discrete-time analog of hazard λ(t∣A = a) at interval k among
A = a. Using Ck to denote censoring of T during interval k (1 if
censored before observing Yk, 0 otherwise), the independent cen-
soring assumption states that the discrete-time hazards are the same
between censored and uncensored participants at every interval k:
PrðYk ¼ 1jYk1 ¼ 0; A ¼ aÞ
¼ PrðYk ¼ 1jYk1 ¼ 0; Ck ¼ 0; A ¼ aÞ:
The independent censoring assumption thus implies that
SðkjA ¼ aÞ
¼ PrðY1 ¼ 0jC1 ¼ 0; A ¼ aÞ PrðY2 ¼ 0jY1 ¼ C2 ¼ 0; A ¼ aÞ
   PrðYk ¼ 0jYk1 ¼ Ck ¼ 0; A ¼ aÞ;
components of which are directly estimated by restricting “at-risk”
sets among each treatment group: b
PrðYk ¼ 0jYk1 ¼ Ck ¼ 0;
A ¼ aÞ ¼ 1  dk;a=nk;a with the number of events dk,a and the
size of the at-risk set nk,a (the number of patients who had
Yk−1 = Ck = 0) at interval k in the treatment group A = a.8,9 In other
words, hazards are estimable by similar calculation even with
censoring. The Kaplan–Meier estimator thus provides valid
estimates of the survival function because the survival function
is reconstructed by multiplying 1 – the estimated hazard function
across intervals at the times of observed events.8,9
To show another use of hazard, recall the formula for the
survival function in continuous timescale8,9:
SðtjA ¼ aÞ ¼ expfðtjA ¼ aÞg;
where ðtjA ¼ aÞ ¼
R t
0 ðsjA ¼ aÞds is a cumulative hazard func-
tion up to t. This function can be estimated by the Nelson–Aalen
estimator
^NAðtjA ¼ aÞ
¼ b
PrðY1 ¼ 1jC1 ¼ 0; A ¼ aÞ
þ b
PrðY2 ¼ 1jY1 ¼ C2 ¼ 0; A ¼ aÞ
þ    þ b
PrðYt ¼ 1jYt1 ¼ Ct ¼ 0; A ¼ aÞ:
Again,
^SNAðtjA ¼ aÞ ¼ expf ^NAðtjA ¼ aÞg reconstructs the
survival function through hazard estimates even with independent
censoring.
This is why we estimate the hazard function in survival
analysis. Like continuous and binary outcomes, our goal is to
summarize and compare counterfactual survival distributions
under diﬀerent treatment conditions (eg, a = 1 vs a = 0) in terms
of causally interpretable measures. Such eﬀect measures are
typically based on survival or cumulative distribution functions,
which are easily estimated through hazard functions (Figure 1).
Why use hazard ratios in survival analyses? And why
are hazard ratios hazardous in causal inference?
A counterfactual hazard function λa(t) is a one-to-one transforma-
tion of Fa(t) and Sa(t) that represents the hazards if all participants
had been treated (a = 1) or untreated (a = 0). This may tempt us to
consider that the contrast between λa=1(t) and λa=0(t) is also caus-
ally interpretable as is. Namely, the hazard ratio λa=1(t)/λa=0(t) is
directly estimated by the Cox proportional hazards model in ran-
domized trials, or by marginal structural Cox models in observa-
tional studies.11 However, interpreting the hazard ratio as the causal
eﬀect measure is diﬃcult, as pointed out in the literature.12–15
Figure 1.
One-to-one correspondence between survival functions S(tjA = a) (left panels), cumulative hazard functions
Λ(tjA = a) (middle panels), and hazard functions λ(tjA = a) (right panels) illustrated using simulated data. Red lines
show functions in the treated population (a = 1) and blue lines show those in the untreated population (a = 0). Black
lines represent estimates from a sample, speciﬁcally, the Kaplan–Meier estimates
^SKMðtjA ¼ aÞ, Nelson–Aalen
estimates ^NAðtjA ¼ aÞ, and nonparametric smoothed estimates for hazards implemented in Stata software. Red and
blue lines in the upper three panels correspond to the exponential distribution, while those in the lower three panels
correspond to the Weibull distribution.
Causal Survival Analysis in Observational Studies
4 j J Epidemiol 2026

````

## PDF page 5; PDF label 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Consider a causal directed acyclic graph (DAG) in Figure 2A
(a discussion on the use of DAGs can be found elsewhere16). This
causal DAG encodes the assumption that the randomized
treatment A aﬀects Y1 but not Y2, while an unmeasured variable
U aﬀects both Y1 and Y2. Table 1 presents hypothetical study data
that align with the DAG. For each time interval, hazard ratios
stratiﬁed by the unmeasured variable U are shown.
On the other hand, we can only observe data marginalized over
U. Table 1 also presents the crude (ie, unstratiﬁed by U) hazard
ratio for each interval (k = 1, 2). The crude hazard ratio at k = 1 is
0.5, equal to the hazard ratios stratiﬁed by U. However, although
we assumed that A has no direct eﬀect on Y2, the crude hazard
ratio at k = 2 is 1.43, deviating from 1 (no eﬀect).
This stems from the fact that the hazard is a conditional measure,
given that the event has not occurred up to the time point. In the
example, treatment A = 1 reduces the number of events at k = 1.
This means that more individuals with a high risk of the event
(U = 1) remain at risk at k = 2 in the A = 1 group compared with
the A = 0 group. In other words, the characteristics of participants
who remain event-free diﬀer between groups at a later time point.
The hazard ratio at k = 2 thus no longer compares the same
populations under diﬀerent treatment conditions. For a given
measure to allow causal interpretation, the measure must contrast
counterfactual summaries under diﬀerent conditions in the same
population. The hazard ratio does not generally meet this require-
ment, despite its comparison of two counterfactual distributions
through hazard functions! This “built-in selection bias”12 of the
hazard ratio can be understood as a form of collider stratiﬁca-
tion bias, arising from conditioning on a common eﬀect Y1 of
exposure A and an unmeasured variable U, as illustrated in
Figure 2B.
Hence, the hazard ratio generally lacks a causal interpretation,
except in special cases such as: 1) under the null hypothesis that A
has no eﬀect on the event of interest; and 2) when the proportional
hazards assumption holds. Even under the second case (in which a
constant hazard ratio is consistently estimated by the Cox model),
the hazard ratio can only be causally interpreted as the ratio of log-
survival (ie, logSa=1(t)/logSa=0(t)) and the pairwise odds of longer
survival times in the untreated participant compared to the treated
participant (ie, the odds of PrðT a¼1
i
< T a¼0
i0
Þ for randomly sampled
i and iA).17
Because of these limitations to the hazard ratio as a causal
measure, we instead focus on eﬀect measures based on counter-
factual survival functions. We introduce the estimation of coun-
terfactual risks in the presence of dependent censoring, con-
founding, and competing events in the following sections.
HOW TO MITIGATE CONFOUNDING BIAS AND
CENSORING DEPENDENT ON COVARIATES
Confounding (and independent censoring)
The Kaplan–Meier estimator for the survival function is commonly
used in the presence of censoring. In observational studies,
however, the presence of confounding implies that the crude
Kaplan–Meier estimates for each treatment group may yield a
biased estimate of the counterfactual survival function Sa(t). Con-
sequently, such comparisons of survival curves do not represent
causal eﬀects. Confounding occurs when a set of covariates L
inﬂuences both the treatment assignment A and the time to event T,
or (Y0, Y1,…, YK). In the presence of confounding, diﬀerences in
observed survival between treatment groups may reﬂect diﬀer-
ences in baseline characteristics rather than a causal eﬀect of the
treatment. Approaches to identifying a suﬃcient set of con-
founders can be found in previous literature in this tutorial series.18
If the causal identiﬁability conditions for an observational study
(causal consistency, conditional exchangeability, and positivity
conditional on confounders)2 are satisﬁed, confounding may be
mitigated using inverse probability of treatment weighting (IPTW)
based on the propensity score.19 IPTW will be applied to the
Kaplan–Meier estimator using weights derived from the propen-
sity score for each subject. Let e(L) = Pr(A = 1∣L) denote the
true propensity score, deﬁned as the conditional probability of
receiving treatment A = 1 given covariates L. Suppose the ob-
served event times (intervals) are ordered in ascending sequence as
0 < t1 < t2 < … < tJ < ∞. The IPTW Kaplan–Meier estimator for
Sa(t) is then given by
Figure 2.
Directed acyclic graphs. (A) The hypothetical dataset in Table 1 is consistent with the DAG, illustrating that A directly
aﬀects Y1 but has no direct eﬀect on Y2. (B) Conditioning on Y1 = 0 creates a non-causal association between A and
Y2 through the path A–Y1–U–Y2.
Table 1.
Hypothetical study data illustrating that interval-speciﬁc
hazard ratio (HR) may not be interpreted as a causal
eﬀect
U = 1
U = 0
In k = 1
Y1
Y1
1
0
N
1
0
N
A = 1
90
110
200
30
170
200
A = 0
180
20
200
60
140
200
HR ¼ 90=200
180=200 ¼ 0:5
HR ¼ 30=200
60=200 ¼ 0:5
Crude HR ¼ ð90þ30Þ=ð200þ200Þ
ð180þ60Þ=ð200þ200Þ ¼ 0:5
In k = 2
Y2
Y2
1
0
Y1 = 0
1
0
Y1 = 0
A = 1
99
11
110
51
119
170
A = 0
18
2
20
42
98
140
HR ¼ 99=110
18=20 ¼ 1:0
HR ¼ 51=170
42=140 ¼ 1:0
Crude HR ¼ ð99þ51Þ=ð110þ170Þ
ð18þ42Þ=ð20þ140Þ ¼ 1:43
Kawahara T, et al.
J Epidemiol 2026 j 5

````

## PDF page 6; PDF label 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
^Sa
IPTWðtÞ ¼
Y
j:tjt
1 
d w
j;a
nw
j;a
 
!
;
where d w
j;a and nw
j;a are the weighted number of events and the size
of the at-risk set at interval tj, respectively, among individuals
treated with A = a. This equation shows that the IPTW Kaplan–
Meier estimator can be obtained as the product of 1 – the esti-
mated hazard function across intervals at the times of observed
events, like the standard Kaplan–Meier estimator. However, the
hazard here is estimated with adjustment for confounding through
weighting of both the numerator and denominator. The weight
assigned to each individual is deﬁned as
Wi ¼ 1=½eðLiÞAif1  eðLiÞg1Ai:
Speciﬁcally, the weight is expressed as 1/e(L) for individuals
with A = 1, and 1/{1 −e(L)} for individuals with A = 0. Note that
in a marginally randomized trial, the IPTW Kaplan–Meier esti-
mator reduces to the standard Kaplan–Meier estimator. In practice,
the true propensity score e(L) is generally unknown and must be
estimated from the data, most commonly via logistic regression
modeling.
A variance estimator analogous in form to Greenwood’s
formula has been proposed for the IPTW Kaplan–Meier estimator,
and we can use a log-rank type test corresponding to the IPTW
Kaplan–Meier estimator for Sa=1(t) and Sa=0(t).20 These estimators
and tests are valid under the assumption of independent censoring
if the model for the propensity score is correctly speciﬁed. Other
methods using the propensity score to adjust for confounding
include propensity score matching.19
An alternative estimator for counterfactual survival function
Sa(t) is a parametric g-formula estimator. This approach involves
modeling the hazard given treatment and confounders. As we
adopt a discrete-time framework, we model the observed discrete
hazard Pr(Yk+1 = 1∣Yk = Ck+1 = 0, A, L) using the pooled logistic
regression model, such as
logit PrðYkþ1 ¼ 1jYk ¼ Ckþ1 ¼ 0; A; L; Þ
¼ 0;k þ 1A þ 2Ak þ 3Ak2 þ T
4L;
where β0,k is a time-speciﬁc intercept and β1, β2, and β3 are the
regression coeﬃcients; and L is a vector of covariates with
corresponding coeﬃcient vector β4. The superscript T denotes the
transpose. This model is the logistic model, ﬁtted to individual
records pooled over time (typically organized in long format10) to
estimate regression coeﬃcients. While the regression coeﬃcients
are assumed to be constant across time, this assumption can be
relaxed. Alternatively, we can ﬁt a Cox regression model. In
eMaterial 1, we compare these models in this setting.
The parametric g-formula estimator for Sa(t) is given by
^Sa
g-formðtÞ
¼ 1
n
X
n
i¼1
Y
t1
k¼0
f1  PrðYkþ1 ¼ 1jYk ¼ Ckþ1 ¼ 0; A ¼ a; Li; ^Þg;
where
PrðYkþ1 ¼ 1jYk ¼ Ckþ1 ¼ 0; A ¼ a; Li; ^Þ ¼ ½1 þ
expfð ^0;k þ ^1a þ ^2ak þ ^3ak2 þ ^T
4LiÞg1 is a predicted dis-
crete hazard at interval k + 1 for individual i evaluated at ^, the
maximum likelihood estimates of β. The term inside the sum-
mation, Qt1
k¼0f1  PrðYkþ1 ¼ 1jYk ¼ Ckþ1 ¼ 0; A ¼ a; Li; ^Þg,
represents the estimate of confounder-speciﬁc survival function
through t, or S(t∣A = a, Li). By averaging the estimated confounder-
speciﬁc survival functions over the empirical distribution of
confounders, we obtain an estimate of the counterfactual survival
function Sa(t) under the intervention A = a. Variance estimates can
then be obtained by bootstrapping.
Dependent censoring (and no confounding)
In this subsection, we consider the estimation of survival functions
for each treatment group under dependent censoring, where the
censoring process depends on the covariates. We assume no con-
founding (but still assume causal consistency and positivity con-
ditional on confounders), which means that Sa(t) = S(t∣A = a)
holds. A more general case that involves both dependent censoring
and confounding is addressed in the next subsection.
We assume that the censoring distribution depends on
covariates L, but the discrete-time hazards are the same between
censored and uncensored individuals given L at every interval k:
PrðYk ¼ 1jYk1 ¼ 0; A ¼ a; LÞ
¼ PrðYk ¼ 1jYk1 ¼ Ck ¼ 0; A ¼ a; LÞ:
To emphasize that independence holds only with respect to
baseline covariates, this assumption is sometimes referred to as
baseline-conditional independent censoring,21 or more simply as
conditional independent censoring. Covariates L are not consid-
ered as confounders in this subsection, but we assume that censor-
ing is independent given L. Using causal DAGs, we can more
transparently communicate whether L is suﬃcient in adjusting for
confounding or dependent censoring (see eMaterial 2).
In addition, we assume positivity for censoring. That is, among
individuals still at risk, the probability of remaining uncensored at
the next interval is positive within each treatment group and for
each observed level of covariates.
Under conditional independent censoring and positivity for cen-
soring, several methods have been proposed to estimate the survival
function Sa(t) = S(t∣A = a). One such method is the inverse prob-
ability of censoring-weighted (IPCW) Kaplan–Meier estimator.
This estimator is constructed by replacing weight Wi in the IPTW
Kaplan–Meier estimator with weights for censoring, deﬁned as
W C
j;i ¼
Y
k:k<tj
IðCkþ1;i ¼ 0Þ
PrðCkþ1 ¼ 0jCk;i ¼ Yk;i ¼ 0; Ai; LiÞ :
In contrast to weight Wi, IPCWs are inherently time-varying
because they reﬂect the time-dependent risk of censoring during
follow-up. This distinction highlights a practical point that
analysts should keep in mind when applying IPCW methods.
The probability included in the denominator of the weights is
generally unknown, meaning that estimation from the data is
needed. This probability can be estimated using standard survival
analysis models such as the pooled logistic model, for example:
logit PrðCkþ1 ¼ 1jYk ¼ Ck ¼ 0; A; L; Þ
¼ 0;k þ 1A þ 2Ak þ 3Ak2 þ T
4L:
This model is similar to the approach discussed in the parametric
g-formula estimator (see above), but now this model is ﬁtted for
conditional probability of censoring, instead of the discrete hazard
of the event. The accuracy of the estimated censoring probabilities
directly aﬀects the performance of the IPCW estimator, and model
misspeciﬁcation may lead to biased estimates.
The parametric g-formula provides an alternative approach to
handling dependent censoring. The same framework described
previously is followed and remains applicable under conditional
independent censoring given L, because censoring becomes
Causal Survival Analysis in Observational Studies
6 j J Epidemiol 2026

````

## PDF page 7; PDF label 7

Technical extraction; compare with original PDF page 7.

````text
independent once conditioned for L in the model. The estimate of
counterfactual survival function Sa(t) is obtained by estimating the
L-speciﬁc survival function among A = a, then integrating over
the covariate distribution.
Adjustment for both confounding and dependent
censoring
Given confounders L, we now assume that both conditional
exchangeability2 and conditional independent censoring (in addi-
tion to causal consistency, positivity with respect to treatment
and censoring conditional on confounders)2 are satisﬁed. The
weighted Kaplan–Meier estimator can account for confounding
using the IPTW method and addresses dependent censoring using
the IPCW method. The weight is deﬁned as the product of the
treatment and censoring weights, Wi  WC
j;i. Each component is
estimated using the respective approaches introduced in earlier
subsections. The Kaplan–Meier estimator with weights estimates
the counterfactual survival function Sa(t) without bias in large
samples. As before, this result holds provided that both the
propensity score model and the model for censoring probability
are correctly speciﬁed.
The parametric g-formula can also be applied in this setting. As
described in previous sections, the parametric g-formula relies on
modeling the discrete hazard function given treatment and con-
founders. Standard modeling approaches, such as pooled logistic
modeling, allow estimation of Sa(t) by appropriately adjusting
for both confounding and dependent censoring. The methods
introduced above can thus be applied directly without requiring
further modiﬁcation; the model for hazard function requires
correct speciﬁcation to obtain unbiased estimates of the coun-
terfactual survival function.
Bootstrap variance estimation is valid for both estimators, and
the variance estimator introduced previously is also valid when
applied to the weighted Kaplan–Meier estimator.20 In eMaterial 3,
we provide a concise review of estimators that can be used as
alternatives to weighted Kaplan–Meier and parametric g-formula.
In practice, the choice between the weighted Kaplan–Meier
estimator and the parametric g-formula depends on modeling
considerations and precision. IPTW and IPCW require modeling
the treatment assignment and censoring mechanisms, respectively,
and do not require speciﬁcation of a model for the hazard itself.
However, extreme weights may arise and can lead to instability,
particularly in small samples. In contrast, the parametric g-formula
requires explicit modeling of the hazard but may oﬀer greater
eﬃciency when the model is correctly speciﬁed. The choice
between these approaches should therefore consider the plausi-
bility of the respective modeling assumptions and the available
sample size.
ESTIMANDS IN THE PRESENCE OF COMPETING
EVENTS
A competing event (or risk) is any event that renders the event of
interest impossible to occur. In the presence of a competing event,
the standard methods of survival analysis introduced previously
may hinder causal interpretation, even when using the counter-
factual-based approach introduced above, if competing events are
not properly accounted for. Consider a hypothetical study in
which the primary outcome is the time to recovery from an
infectious disease. In this setting, death is a competing event,
because recovery cannot be observed once the patient has died.
Even in the absence of censoring, if death is treated as a censoring
event, the Kaplan–Meier estimator overestimates the probability
of recovery.22
A natural measure of the risk of each event (eg, recovery and
death) is the cumulative incidence function (CIF), deﬁned as the
proportion of patients who experience an event type r (= 1,…, R)
by time t, which is deﬁned in continuous timescale as
Z t
0
SðsÞhrðsÞds:
Here, SðtÞ ¼ expf
R t
0
PR
r¼1 hrðuÞdug denotes the probability of
not experiencing any type of event by t. The cause-speciﬁc hazard
function for event type r, denoted by hr(t), represents the
instantaneous rate of experiencing an event of type r at time t,
conditional on not experiencing any type of event until just before
t. With independent censoring, the nonparametric estimator,
which estimates S(t) with the Kaplan–Meier estimator and hr(t)dt
with the increment of the Nelson–Aalen estimator, provides
unbiased estimates in large samples.23 We do not consider
transitions from one state to another (eg, from recovery to death),
because recovery is the event of interest and death (before
recovery) is a competing event in the example given. If the
investigator is interested in the probability of death after recovery,
multistate models may better align with this aim.24
By deﬁnition, the CIF depends on the hazard of all event types,
meaning that no one-to-one correspondence exists between the
CIF for event type r and its cause-speciﬁc hazard in the presence
of competing events. This implies that a cause-speciﬁc hazard
model, which is equivalent to the Cox model that censors
individuals at the time of death (a competing event), does not
directly characterize the CIF. The model parameterizes the (log)
cause-speciﬁc hazard ratios.25
In contrast, the Fine–Gray model, which retains individuals
who die in risk sets even after death, is consistent with the CIF.
The modeled hazards, known as subdistribution hazards, are
directly linked to the CIF, and the model parameterizes the (log)
subdistribution hazard ratio.25 However, we do not pursue the
causal interpretation of these hazard models themselves, because
again, the hazard ratios, irrespective of whether they are cause-
speciﬁc or subdistribution, are subject to built-in selection bias.
In the following subsections, we brieﬂy review possible causal
target parameters in terms of the counterfactual risk with discrete-
time settings. Below, we focus on the risk of the event of interest
without referencing the event type r. In classical deﬁnitions, one
may consider r = 1 to denote the event of interest and r = 2,…, R
to denote competing events.
Risk without eliminating competing events
Consider the counterfactual indicator of the event of interest by
interval k had treatment A been set to a, Ya
k. This slightly extends
the notation introduced previously, where Ya
t was deﬁned as the
indicator of potential event occurrence under A = a by time t;
here, Ya
k speciﬁcally denotes the indicator of the potential event of
interest. This counterfactual outcome deﬁnes the counterfactual
risk, PrðYa
k ¼ 1Þ, which is referred to as the risk without
elimination of competing events. In a well-conducted randomized
trial with no loss to follow-up, this reduces to Pr(Yk = 1∣A = a),
an alternative representation of the treatment group-speciﬁc CIF
of the event of interest.26
Using the counterfactual outcomes Ya
k , the risk diﬀerence for
the event of interest by interval k is given by
Kawahara T, et al.
J Epidemiol 2026 j 7

````

## PDF page 8; PDF label 8

Technical extraction; compare with original PDF page 8.

````text
PrðYa¼1
k
¼ 1Þ  PrðYa¼0
k
¼ 1Þ:
This quantiﬁes the total eﬀect of treatment on the event of interest
through and not through a competing event.26 If PrðYa¼1
k
¼ 1Þ is
lower than PrðYa¼0
k
¼ 1Þ, this may indicate that the treatment
reduced the proportion of individuals who experienced the event
of interest, increased the proportion of individuals who experi-
enced a competing event, or both mechanisms operating together.
Net risk
If the goal is to estimate the direct eﬀect of treatment on the event
of interest (excluding pathways mediated through changes in the
number of individuals who experience competing events), the
total eﬀect may not be an appropriate measure.
Imagine a world in which competing events are eliminated, such
as in which deaths prior to recovery are somehow avoided.
Consider the counterfactual indicator of the event of interest by
interval k, had treatment A been set to a in this world, Ya;d¼0
k
, where
d = 0 denotes an intervention that eliminates competing events.
The counterfactual risk PrðYa;d¼0
k
¼ 1Þ represents the risk if all
individuals were treated with A = a and competing events had
somehow been eliminated. This risk is classically referred to as the
net risk or conditional risk.8 The net risk is widely used in
population-based cancer epidemiology, such as when investigators
aim to estimate the survival proportion as if cancer mortality were
the only possible cause of death; that is, under a hypothetical
scenario in which competing causes of death do not exist.27
Using the counterfactual outcomes Ya;d¼0
k
, the risk diﬀerence
on the event of interest by interval k is given by
PrðYa¼1;d¼0
k
¼ 1Þ  PrðYa¼0;d¼0
k
¼ 1Þ;
representing a special case of the controlled direct eﬀect.26,28 This
eﬀect quantiﬁes the treatment eﬀect on the event of interest in a
hypothetical world where competing events do not occur, thereby
capturing a treatment eﬀect on the event of interest that is not
mediated by the competing events. Although this estimand is
interpretable as a direct eﬀect, questions remain as to whether
such an intervention that eliminates competing events is feasible.
Cumulative incidence under modiﬁed treatments
Consider a modiﬁed treatment that preserves the direct eﬀect of the
original treatment A on the event of interest, while having no direct
eﬀect on other competing events. As an example, suppose that a
prophylaxis for prostate cancer mortality can be decomposed into
two separate components, P and O. The separable component P
directly aﬀects the progression of prostate cancer (event of interest)
while exerting no direct eﬀect on cardiovascular disease (com-
peting event), whereas the other component O directly aﬀects the
progression of cardiovascular disease, but not the progression of
prostate cancer (see Stensrud et al29 for further discussion of this
example).
Let Yp;o
k
denote the counterfactual indicator of the event of
interest by interval k under a modiﬁed treatment (P, O) = (p, o).
Then, Yp¼1;o¼0
k
represents the counterfactual prostate cancer
mortality under a modiﬁed treatment that preserves the direct
eﬀect with current prophylaxis (intervening to p = 1) on prostate
cancer mortality, but with other mechanisms removed (interven-
ing to o = 0). The eﬀect of the modiﬁed treatment on the event of
interest (a separable direct eﬀect) by interval k is given by
PrðYp¼1;o¼0
k
¼ 1Þ  PrðYp¼0;o¼0
k
¼ 1Þ:
This quantiﬁes a direct treatment eﬀect on the event of interest via
component P, independent of any inﬂuence from component O
by ﬁxing at O = 0 compared to no-prophylaxis (A = P = O = 0).
This estimand is motivated by treatment decomposition into
distinct
components
that
operate
through
diﬀerent
causal
pathways.29–33 While such interventions on components may
not be conceivable at the time of the current study, the separable
eﬀects framework nevertheless provides a concrete and useful
tool for disentangling treatment eﬀects along speciﬁc causal
pathways without eliminating competing events. In this sense, the
approach may oﬀer investigators an intuitive way to think about
how treatments work through diﬀerent mechanisms.
Estimation of the counterfactual risks
The conditions required to identify these estimands have been
discussed elsewhere,26,32 and thus are not repeated here. Im-
portantly for investigators, adjustment for common causes of the
competing event and the event of interest is required to obtain
estimands focused on direct eﬀects (see above).
A brief comment on estimation is warranted. These counter-
factual risks can be linked to the causal methods described in the
previous sections. The risk without eliminating competing events
may be estimated using the weighted Aalen–Johansen estimator or
the parametric g-formula under corresponding identiﬁability
assumptions.26 The net risk can be obtained by conceptually
treating competing events as censoring and applying appropriate
inverse probability weighting or g-formula approaches, each of
which relies on distinct modeling assumptions.26 Similarly,
cumulative incidence under modiﬁed treatment can be estimated
using weighting-based methods or the parametric g-formula.29
These connections may help applied researchers translate the
estimand framework into practical implementation. eTable 1
summarizes the links between estimands and the corresponding
estimators under independent or dependent censoring assumptions.
In eMaterial 4, we provide practical notes for the use of the R
package, gfoRmula,34 which allows estimation of the risk without
eliminating competing events and the net risk reviewed above by
the parametric g-formula estimator in its current version (1.1.1),
which runs on R (R Foundation for Statistical Computing, Vienna,
Austria).
ILLUSTRATIVE EXAMPLE OF CAUSAL SURVIVAL
ANALYSIS INVOLVING CONFOUNDING AND
COMPETING RISKS
Overview of the illustrative study35
In this section, we revisit a recent clinical study that examined the
comparative eﬀectiveness of glucagon-like peptide-1 receptor
agonists (GLP-1RAs) versus dipeptidyl peptidase-4 inhibitors
(DPP4is) on the risk of dementia among older adults with type 2
diabetes, as an illustrative example of causal survival analysis.
The study included individuals aged 66 years or older with a
diagnosis of diabetes who initiated treatment with GLP-1RAs or
DPP4is between January 1, 2017 and December 31, 2018. More
details on the treatment strategy, study outcomes, covariate ascer-
tainment, and statistical analysis can be found in the original
study.35
Adjusting
for
confounders
and
assessment
for
residual confounding: rationale and methods
In that study, nearest-neighbor propensity score matching with a
Causal Survival Analysis in Observational Studies
8 j J Epidemiol 2026

````

## PDF page 9; PDF label 9

Technical extraction; compare with original PDF page 9.

````text
1:2 ratio without replacement was applied to adjust for con-
founders. The ﬁnal analytical sample after propensity score match-
ing included 2,418 GLP-1RA initiators and 4,836 DPP4i initiators.
Although the authors included more than 50 baseline covariates in
the propensity score model, covering sociodemographic factors,
comorbidities, and medication use, they highlighted the remaining
concern of residual confounding in their limitations.35
One method to assess the potential for residual confounding
is to examine the timing of divergence in incidence curves
(Figure 3). Indeed, in most previous studies, survival curves for
GLP-1RA and comparator groups began to separate within the
ﬁrst 6 months following initiation of treatment. Although this
does not “guarantee” any absence of confounding bias, given the
unlikelihood that neuroprotective eﬀects would appear within
such a short timeframe, early curve separation may indicate the
presence of unmeasured confounding.
Addressing competing events (death): rationale and
methods
In dementia research, where the study population comprises older
adults, accounting for competing risks such as death is essential.
In the study, 49 patients (2.0%) in the GLP-1RA group and 155
patients (3.2%) in the DPP4i group died during follow-up. These
numbers are not negligible, given that the primary outcome
(dementia) occurred in 96 patients (4.0%) in the GLP-1RA group
and 217 patients (4.5%) in the DPP4i group.
The primary analysis used the Aalen–Johansen estimator to
calculate the total eﬀect while treating death as a competing event,
revealing a 30-month risk diﬀerence of −0.93% (95% conﬁdence
interval [CI], −2.33 to 0.23) and a risk ratio of 0.83 (95% CI,
0.61–1.05). The authors estimated the controlled direct eﬀect in
a sensitivity analysis, revealing a 30-month risk diﬀerence of
−1.03% (95% CI, −2.50 to 0.17) and a risk ratio of 0.81 (95% CI,
0.60–1.03).35
Although estimates were similar across total and direct eﬀect
estimands in this study, such consistency may not always occur
depending on the mechanisms underlying data generation. Even
direct eﬀect estimands (controlled and separable direct eﬀects) can
also take diﬀerent values.36 To illustrate this point, we simulated a
dataset in which none of the total eﬀect, controlled direct eﬀect, or
Figure 3.
Example of the early separation in cumulative incidence functions as an indicator of residual confounding. Figures
were drawn from simulated data based on ﬁndings from Inoue et al.35 If eﬀects appearing within a short timeframe are
biologically implausible, the early curve separation in panel (A) may indicate the presence of unmeasured
confounding, while the later separation in panel (B) may be more biologically explicable under certain contexts (eg,
onset of dementia).
Figure 4.
Examples of (A) cumulative incidences without eliminating competing events, (B) net risks, and (C) cumulative
incidences under modiﬁed treatments through k = 12, estimated from a simulated dataset. Total eﬀect, controlled
direct eﬀect, and a separable direct eﬀect are shown as risk diﬀerences in (A), (B) and (C), respectively. Treatment-
speciﬁc cumulative risks and risk diﬀerences are generally unequal. The simulation protocol can be found in
eMaterial 5, representing an extension of Appendix A by Stensrud et al.29 Following their notation, (AY, AD) is used
instead of (P, O) to represent the decomposition of A.
Kawahara T, et al.
J Epidemiol 2026 j 9

````

## PDF page 10; PDF label 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
separable direct eﬀect is equal in terms of absolute risk or risk dif-
ference (Figure 4). These estimands are also revealed to be dif-
ferentially aﬀected by unmeasured common causes of the event of
interest and the competing event.36 Investigators need to carefully
consider and select the estimand when investigating causal eﬀects,
particularly in the presence of a high risk of competing events.
CONCLUSION
In this tutorial paper, we have provided an overview of eﬀect
measures for time-to-event data subject to censoring, provided a
step-by-step approach to adjusting for dependent censoring and
confounding, and discussed causal estimands in the presence of
competing risks. We hope this paper motivates readers to
complement the conventional “KM–log-rank–Cox” paradigm with
approaches to causal survival analysis better suited to their speciﬁc
research questions. At the same time, the methods we have
described rely on assumptions, such as correct model speciﬁcation
and no unmeasured confounding for either treatment or censoring,
and these assumptions warrant careful consideration in practice.
These approaches are also highly relevant for applications of target
trial emulation, in which careful adjustment for dependent
censoring, confounding, and competing risks is essential to draw
valid causal inferences.
ACKNOWLEDGMENTS
We thank Dr Jessica Young for fruitful discussions on competing
risk analysis. We thank Dr Miho Ishimaru for permission to use
Figure 1. We also thank Dr Yuri Ito, Dr Atsushi Goto, Dr Masao
Iwagami, and Dr Yoshinori Takeuchi for organizing and
presenting the Pre Seminars 2 and 3 at the 34th Annual Meeting
of the Japanese Epidemiological Association. The authors thank
FORTE Science Communications for English language editing.
Data sharing: R code for our simulation is publicly available
at:
https://github.com/TakuyaKawahara/JE_Causal_Survival_
Analysis.
Contributors: All authors contributed to preparation, review, and
approval of the manuscript. TK supervised the whole manuscript.
Funding: This work was supported by JSPS KAKENHI Grant
Numbers 22K17301, 24K20742, and 24K14864. This research
was also supported by AMED (grant no. JP25jm0210107).
Conﬂicts of interest: Dr Kawahara has received lecture fees
from MeDiCU Inc., Novartis Pharma K.K., and Boehringer
Ingelheim outside this work. Dr Inoue was supported by grants
from the Japan Society for the Promotion of Science, the Japan
Agency for Medical Research and Development, and the Japan
Science and Technology. Dr Inoue has received consulting fees
from Cancerscan, Cykinso, Kagome, Mizkan, and AstraZeneca;
and speaking fees from AstraZeneca, Chugai Pharmaceutical Co.,
Ltd., Daiichi Sankyo, Tanabe Pharma Co., and DeSC Healthcare
Inc. outside this work. Dr Shinozaki was supported by KYOCERA
Corporation via contracts with the university. Dr Shinozaki has
received statistical consulting fees from TXP Medical; and lecture
fees from MeDiCU Inc., CMIC Holdings Co., Ltd., Santen
Pharmaceutical Co., Ltd., and Pﬁzer Japan outside this work.
SUPPLEMENTARY MATERIAL
Supplementary data related to this article can be found at https://
doi.org/10.2188/jea.JE20250662.
REFERENCES
1. Klein JP, Moeschberger ML. Survival Analysis: Techniques for
Censored and Truncated Data. Springer New York, NY; 2003.
2. Hernán MA, Robins JM. Causal Inference: What If. Chapman &
Hall/CRC; 2020.
3. Hernán MA, Robins JM. Using big data to emulate a target trial
when a randomized trial is not available. Am J Epidemiol. 2016;
183(8):758–764.
4. Denz R, Klaaßen-Mielke R, Timmesfeld N. A comparison of
diﬀerent methods to adjust survival curves for confounders. Stat
Med. 2023;42(10):1461–1479.
5. Talbot D, Diop A, Mésidor M, et al. Guidelines and best practices
for the use of targeted maximum likelihood and machine learning
when estimating causal eﬀects of exposures on time-to-event
outcomes. Stat Med. 2025;44(6):e70034.
6. Cook RJ, Lawless JF. The Statistical Analysis of Recurrent Events.
Springer New York, NY; 2007.
7. Amorim LD, Cai J. Modelling recurrent events: a tutorial for
analysis in epidemiology. Int J Epidemiol. 2015;44(1):324–333.
8. Lash TL, VanderWeele TJ, Haneuse S, Rothman KJ. Modern
Epidemiology (4th ed.). Wolters Kluwer; 2021.
9. Westreich D. Epidemiology by Design: A Causal Approach to the
Health Sciences. Oxford University Press; 2020.
10. Iwagami M, Ishimaru M, Takeuchi Y, Shinozaki T. Methodological
Tutorial Series for Epidemiological Studies: When and how to split
the follow-up time in the analysis of epidemiological or clinical
studies with follow-ups. J Epidemiol. 2025;35(4):161–169.
11. Hernán MA, Brumback B, Robins JM. Marginal structural models to
estimate the causal eﬀect of zidovudine on the survival of HIV-
positive men. Epidemiology. 2000;11(5):561–570.
12. Hernán MA. The hazards of hazard ratios. Epidemiology. 2010;21(1):
13–15.
13. Aalen OO, Cook RJ, Røysland K. Does Cox analysis of a
randomized survival study yield a causal treatment eﬀect? Lifetime
Data Anal. 2015;21(4):579–593.
14. Martinussen T, Vansteelandt S, Andersen PK. Subtleties in the
interpretation of hazard contrasts. Lifetime Data Anal. 2020;26(4):
833–855.
15. Stensrud MJ, Aalen JM, Aalen OO, Valberg M. Limitations of
hazard ratios in clinical trials. Eur Heart J. 2019;40(17):1378–1383.
16. Suzuki E, Shinozaki T, Yamamoto E. Causal diagrams: pitfalls and
tips. J Epidemiol. 2020;30(4):153–162.
17. Moser BK, McCann MH. Reformulating the hazard ratio to enhance
communication with clinical investigators. Clin Trials. 2008;5(3):
248–252.
18. Inoue K, Sakamaki K, Komukai S, Ito Y, Goto A, Shinozaki T.
Methodological Tutorial Series for Epidemiological Studies: Con-
founder selection and sensitivity analyses to unmeasured confounding
from epidemiological and statistical perspectives. J Epidemiol. 2025;
35(1):3–10.
19. Shiba K, Kawahara T. Using propensity scores for causal inference:
pitfalls and tips. J Epidemiol. 2021;31(8):457–463.
20. Xie J, Liu C. Adjusted Kaplan–Meier estimator and log-rank test
with inverse probability of treatment weighting for survival data.
Stat Med. 2005;24(20):3089–3110.
21. Kawahara T, Shinozaki T, Matsuyama Y. Doubly robust estimator
of risk in the presence of censoring dependent on time-varying
covariates: application to a primary prevention trial for coronary
events with pravastatin. BMC Med Res Methodol. 2020;20(1):204.
22. Andersen PK, Geskus RB, de Witte T, Putter H. Competing risks in
epidemiology: possibilities and pitfalls. Int J Epidemiol. 2012;41(3):
861–870.
23. Lin
DY.
Non-parametric
inference
for
cumulative
incidence
functions in competing risks studies. Stat Med. 1997;16(8):901–910.
24. Le-Rademacher JG, Therneau TM, Ou FS. The utility of multistate
models: a ﬂexible framework for time-to-event data. Curr Epidemiol
Rep. 2022;9(3):183–189.
25. Lau B, Cole SR, Gange SJ. Competing risk regression models for
epidemiologic data. Am J Epidemiol. 2009;170(2):244–256.
Causal Survival Analysis in Observational Studies
10 j J Epidemiol 2026

````

## PDF page 11; PDF label 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
26. Young JG, Stensrud MJ, Tchetgen Tchetgen EJ, Hernán MA. A
causal framework for classical statistical estimands in failure-time
settings with competing events. Stat Med. 2020;39(8):1199–1236.
27. Komukai S, Hattori S. Doubly robust estimator for net survival rate
in analyses of cancer registry data. Biometrics. 2017;73(1):124–133.
28. Robins JM, Greenland S. Identiﬁability and exchangeability for
direct and indirect eﬀects. Epidemiology. 1992;3(2):143–155.
29. Stensrud MJ, Young JG, Didelez V, Robins JM, Hernán MA.
Separable eﬀects for causal inference in the presence of competing
events. J Am Stat Assoc. 2022;117(537):175–183.
30. Robins JM, Richardson TS. Alternative Graphical Causal Models
and
the
Identiﬁcation
of
Direct
Eﬀects.
In:
Causality
and
Psychopathology: Finding the Determinants of Disorders and Their
Cures. Oxford University Press, UK; 2011:103–158.
31. Didelez V. Deﬁning causal mediation with a longitudinal mediator
and a survival outcome. Lifetime Data Anal. 2019;25(4):593–610.
32. Stensrud MJ, Hernán MA, Tchetgen Tchetgen EJ, Robins JM,
Didelez V, Young JG. A generalized theory of separable eﬀects in
competing event settings. Lifetime Data Anal. 2021;27(4):588–631.
33. Stensrud MJ, Robins JM, Sarvet A, Tchetgen Tchetgen EJ, Young
JG. Conditional separable eﬀects. J Am Stat Assoc. 2023;118(544):
2671–2683.
34. McGrath S, Lin V, Zhang Z, et al. gfoRmula: An R package for
estimating the eﬀects of sustained treatment strategies via the
parametric g-formula. Patterns (N Y). 2020;1(3):100008.
35. Inoue K, Saliba D, Gotanda H, et al. Glucagon-like peptide-1
receptor agonists and incidence of dementia among older adults with
type 2 diabetes. Ann Intern Med. 2025;178(9):1258–1267.
36. Kawahara T, McGrath S, Young JG. Illustrating implications of
misaligned causal questions and statistics in settings with compet-
ing events and interest in treatment mechanisms. Stat Med. 2026;
45(10–12):e70535.
Kawahara T, et al.
J Epidemiol 2026 j 11

````

