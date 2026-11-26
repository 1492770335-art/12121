# Cause-distinct incidence for resolving confusion in competing risk analysis: a critical review

Original PDF: [original.pdf](original.pdf). SHA256: `fe7ec617f7f37758d22ed4dc5de7cc968ab53baec00ef444dda518722ace93b1`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1; PDF label 1

FORMULA CHECK REQUIRED: original PDF page 1.

````text
TYPE Mini Review
PUBLISHED 16 March 2026
DOI 10.3389/fams.2026.1777018
OPEN ACCESS
EDITED BY
Pedro Alberto Morettin,
University of São Paulo, Brazil
REVIEWED BY
Mohammad Anamul Haque,
Shahjalal University of Science and
Technology, Bangladesh
*CORRESPONDENCE
Tsuyoshi Nakamura
naka@nagasaki-u.ac.jp
RECEIVED 29 December 2025
REVISED 25 January 2026
ACCEPTED 26 January 2026
PUBLISHED 16 March 2026
CITATION
Nakamura T, Yamada T and Nose Y
(2026) Cause-distinct incidence for
resolving confusion in competing risk
analysis: a critical review.
Front. Appl. Math. Stat. 12:1777018.
doi: 10.3389/fams.2026.1777018
COPYRIGHT
© 2026 Nakamura, Yamada and Nose.
This is an open-access article distributed
under the terms of the Creative
Commons Attribution License (CC BY).
The use, distribution or reproduction in
other forums is permitted, provided the
original author(s) and the copyright
owner(s) are credited and that the
original publication in this journal is
cited, in accordance with accepted
academic practice. No use, distribution
or reproduction is permitted which does
not comply with these terms.
Cause-distinct incidence for
resolving confusion in competing
risk analysis: a critical review
Tsuyoshi Nakamura1*, Tomomi Yamada2 and Yoshiaki Nose3
1School of Environmental Sciences, Nagasaki University, Nagasaki, Japan, 2Department of Medical
Innovation, The University of Osaka Hospital, Osaka, Japan, 3Graduate School of Medical Sciences,
Kyushu University, Fukuoka, Japan
An event that hinders or changes the possibility of observing the event of
interest is called a competing risk. For instance, clinical studies involving patients
with multimorbidity or critically severe illnesses often require the evaluation of
competing risks, as the occurrence of other events may preclude the primary
event of interest. Cause-speciﬁc incidence and the Fine–Gray hazard have
been widely used and have become the default methodological approaches in
competing risk analysis. Nevertheless, some clinicians are unable to correctly
interpret the results obtained from the competing risk analysis. Recently, the
cause-distinct incidence has been introduced to resolve drawbacks in competing
risk analysis, but because this confusion is widespread among biostatisticians, it
may take considerable time to resolve. During this period, clinical researchers
may continue to publish articles with incorrect interpretations. This study
aimed to address these misinterpretations and accelerate clariﬁcation of the
prevailing drawbacks.
KEYWORDS
cause-distinct incidence, cause-speciﬁc incidence, hazard, competing risk, Kaplan-
Meier, subdistribution hazard
1 Introduction
Populations susceptible to competing risks include those with multimorbidity
or critically severe illnesses such as cancer, cardiovascular diseases, stroke, diabetes,
nephrology, and chronic obstructive pulmonary disease (COPD). Failure to account for
these competing risks in time-to-event analyses may result in biased risk estimates [1].
However, the decision to conduct competing risk analysis is not always straightforward [2].
Gray [3] disclosed that the cause-speciﬁc hazard does not correspond directly to the
cause-speciﬁc incidence. This observation led to the development of the Fine–Gray or the
subdistribution hazard [4]. Both cause-speciﬁc incidence and subdistribution hazard have
become the default methods for estimating the incidence of outcomes over time in the
presence of competing risks [5, 6].
Nevertheless, some clinicians are confused about how to correctly apply the competing
risk analysis and interpret the results. Koller et al. [7] studied the latest 50 articles published
on competing risks in some of the highest ranked journals between 2000 and 2010
and found that only 20% (10/50) explicitly applied the competing risks methodology,
and 18% (9/50) discussed these risks as a possible issue. Macek et al. [8] noted that
“When interpreting the results obtained with the aid of the CSH method, it should
be borne in mind that the competing events are treated as the censored observations.
Frontiers in Applied Mathematics and Statistics
01
frontiersin.org

````

## PDF page 2; PDF label 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
Nakamura et al.
10.3389/fams.2026.1777018
Regarding the SHR (subdistribution hazard ratio) method, the cases
which have experienced a competing event are not censored, and
remain within the data set. Having juxtaposed potential advantages
and disadvantages of both approaches, speciﬁc indications for their
application were worked out.” Putter et al. [9] evaluated the ratio
between the cause-speciﬁc hazard and the subdistribution hazard to
obtain some signiﬁcant ﬁndings but concluded that “More research
is needed to assess the behavior of the estimators of the cumulative
incidence functions.”
Nakamura and Yamada [10] demonstrated that the cause-
speciﬁc incidence may not properly represent treatment eﬀects
when competing risks are signiﬁcantly diﬀerent between groups
and that the subdistribution hazard can be aﬀected by independent
censoring. They introduced the cause-distinct incidence to resolve
confusion in the interpretation of the cause-speciﬁc incidence,
the Kaplan–Meier estimate, and type-speciﬁc survivor functions.
However, since this confusion is widespread among biostatisticians,
it will take some time to completely resolve. In the meantime,
clinical researchers may continue to write articles with incorrect
interpretations. The main objective of this study is to correct
these misinterpretations and promote the dissemination of accurate
methods and interpretations.
2 Notations and symbols
(T, δ) denotes a pair of random variables, where T represents
a failure time and δ represents an event. Without the loss of
generality, we consider two mutually exclusive events, designated
as 0 and 1, which will be termed Type-0 and Type-1, respectively.
For example, (T = t, δ = j) indicates that a Type-j failure occurs at
time t, (j = 0 or 1). In clinical studies, Type-0 and Type-1 events are
often referred to as primary and competing events, respectively.
Hazards and survivor functions are deﬁned as follows:
λ(t) = lim
→0
P(t ≤T < t + |t ≤T)

=
1
P(t ≤T) lim
→0
P(t ≤T < t + )

λj(t) = lim
→0
P(t ≤T < t + , δ = j|t ≤T)

=
1
P(t ≤T) lim
→0
P(t ≤T < t + , δ = j)

where λ(t) is the overall hazard, and λj(t) is Type-j hazard in
the presence of the other event, (j = 0, 1). We assume λ(t) =
λ0(t) + λ1(t). Both λ(t) and λj(t) do not depend on independent
censoring [10].
The cumulative hazard and cumulative Type-j hazard are
denoted as (t) =
 t
0 λ(s)ds and j(t) =
 t
0 λj(s)ds, respectively,
(j = 0, 1). It holds that (t) = 0(t) + 1(t). Further, the
survivor function and Type-j survivor function are denoted as
S(t) = exp

−(t)

and Sj(t) = exp

−j(t)

, respectively, (j =
0, 1). It holds that S(t) = S0(t)S1(t).
Since hazards are unaﬀected by censoring that is independent of
failure times, hazards are directly estimated from censored follow-
up data.
3 Estimation using follow-up data
We brieﬂy deﬁne the method to obtain the estimates of the
hazard λ(t) and λj(t) using follow-up data of a homogeneous
sample. Let t0
1 < t0
2 < ...... < t0
m and t1
1 < t1
2 < ...... < t1
n,
respectively represent the Type-0 and Type-1 failure times observed
in a sample.
Let Y(t) denote the number of subjects at risk at t. Assume
(T = t, δ = j) occurs, the estimates of λ(t) and λj(t) are both
1/Y(t) and that of the other Type λ1−j(t) = 0, (j = 0, 1). The
estimates of the survivor functions S(t) and Sj(t) are obtained as
follows: S(0) = Sj(0) = 1. Then S(t) = S(t −0) exp{−λ(t)} and
Sj(t) = Sj(t −0) exp{−λj(t)}, here S(t) counts both types of events,
while Sj(t) counts only Type-j events ignoring other types of events.
An approximation exp{−λ(t)}
=
1 −λ(t) is manually
performed. Then, we have S0(t) = 
t0
k≤t
(1 −λ0(t0
k)} and S1(t) =

t1
k≤t
(1 −λ1(t1
k)}, generally termed as Type-0 and Type-1 Kaplan–
Meier estimates, respectively.
4 Cause-distinct or cause-speciﬁc
incidences
Cause-speciﬁc incidence (CS-incidence) fj(t) and cause-distinct
incidence (CD-incidence) f ∗
j (t) are deﬁned as fj(t) = λj(t)S(t) and
f ∗
j (t) = λj(t)Sj(t), respectively.
Since f0(t) = f ∗
0 (t)S1(t), CS-incidence is more sensitive to S1(t)
when compared to f ∗
0 (t).
This causes the CS-incidence to fail to properly represent a
treatment eﬃcacy when S1(t) diﬀers between groups. The issue is
described in detail later in this article.
Anderson et al. [11] noted that “The key feature of competing
risks is that the one-to-one correspondence between cause-speciﬁc
hazard and cumulative incidence is lost”. That is, λj(t) and fj(t)
do not correspond one-to-one to each other. However, there is a
one-to-one correspondence between any two of λj(t), f ∗
j (t), and
Sj(t) [10].
The cumulative incidence, cumulative cause-speciﬁc incidence
(CCS-incidence), and the cumulative cause-distinct incidence
(CCD-incidence) are given as F(t) =
 t
0 f (s)ds, Fj(t) =
 t
0 fj(s)ds,
and F∗
j (t) =
 t
0 f ∗
j (s)ds, respectively, where Fj(t) is often termed as
cause-speciﬁc incidence function (CIF) in literature.
It holds that F(t)
=
F0(t) + F1(t), F(t) is a distribution
function, or F(∞) = 1, while Fj(t) is a sub-distribution function,
or Fj(∞) < 1. On the other hand, F∗
j (t) is a distribution function,
that is F∗
j (∞) = 1. Therefore, F∗
j (t) is interpreted as a probability,
but Fj(t) is not. It holds that Sj(t) + F∗
j (t) = 1 (j = 0, 1) [10]. This
equation is useful in interpreting the Kaplan–Meier estimates in the
following section.
Frontiers in Applied Mathematics and Statistics
02
frontiersin.org

````

## PDF page 3; PDF label 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
Nakamura et al.
10.3389/fams.2026.1777018
Proposition: It holds that Fj(t)<F∗
j (t). Consequently, one
minus Type-j Kaplan–Meier estimate is larger than the Type-j
cause-speciﬁc incidence Fj(t).
Proof: Without loss of generality, we consider j = 0. Since
f0(t) = f ∗
0 (t)S1(t) < f ∗
0 (t), we have F0(t)<F∗
0(t). This indicates
that Type-0 CIF is always less than Type-0 CCD-incidence F∗
0(t).
As previously described, F∗
0(t)
=
1 −S0(t) and S0(t) equals
the Type-0 Kaplan–Meier estimate. Therefore, one minus Type-
0 Kaplan–Meier estimate equals F∗
0(t). Thus, one minus Type-0
speciﬁc Kaplan–Meier estimate is larger than F0(t).
5 Kaplan–Meier or CIF
The Kaplan–Meier estimate regarding Type-0 events as failure
and ignoring Type-1 events is generally termed Type-0 Kaplan–
Meier estimate. In the following references, the Type-0 Kaplan–
Meier estimate is abbreviated as Kaplan–Meier estimate or Kaplan–
Meier curve. The one minus Type-0 Kaplan–Meier estimate is often
also abbreviated as Kaplan–Meier estimate.
Schuster et al. [12] reported “The Kaplan–Meier method
overestimated the cumulative incidence of depressive symptoms.
Instead, the CIF should be used.” Some recent review articles on
competing risk analysis also reached the same conclusion. Lacny
et al. [13] pointed out that “Kaplan–Meier estimates exceeded
the CIF at each time point.” McCaw et al. [14] remarked that
“the corresponding Kaplan–Meier curve for the end point of
interest is uninterpretable.” Haque et al. [15] noted that “A clear
overestimation of the CIF function over time was observed under
the K–M estimation technique.” Gaynor et al. [16] indicated that
“one minus Kaplan–Meier approach simply does not represent any
probability in the presence of competing risks and will almost always
produce biased estimates (thus, it should never be used).” Zaino [17]
noted that “KM consistently overestimated cardiovascular mortality
risk compared to CIF.” These studies claim that the Kaplan–Meier
estimate always exceeds the CIF and warn against overestimation.
However, they do not explain the reason why CIF is used as a
standard to assess the performance of the Kaplan–Meier estimate.
The proposition, however, mathematically indicates that the one-
minus Kaplan–Meier estimate is larger than CIF; therefore, their
ﬁndings only conﬁrm the proposition.
Following these studies, some biostatisticians also presented
similar views. Klein and Moershberger [18] also noted that “one
minus the Kaplan–Meier estimator of relapse obtained by treating
occurrences of relapse as events and occurrences of death before
relapse as censored observations. It is the probability of relapse in
a hypothetical world where it is impossible for patients to die in
remission. These are rarely the probabilities of clinical interest and we
cannot recommend the use of this estimator.” Recently, Geskus [19]
observed that “If, additionally, we can assume that the competing
risks are independent, then the Kaplan–Meier is valid for estimating
the marginal distribution” and “The estimate of the cause-speciﬁc
cumulative incidence is never larger than the Kaplan–Meier.”
On the other hand, since the Type-j Kaplan–Meier estimator
estimates Sj(t) and Sj(t) + F∗
j (t)
=
1 holds [10], one minus
Type-j speciﬁc Kaplan–Meier estimator estimates the CCD-
incidence F∗
j (t). It is shown in the following section that F∗
j (t)
is more appropriate than Fj(t) for comparing Type-j incidence
between groups.
As for Sj(t), Kalbﬂeisch and Prentice [20] deﬁned Fj (t) =
exp

−
 t
0 λj (s)ds

with the remark “these functions will not, in
general, have any survivor function interpretation” and assigned no
name to it. In this study, their Fj (t) is Sj (t). Later, Kalbﬂeisch and
Prentice [21] deﬁned the cumulative incidence function as ¯Fj(t) =
 t
0 fj(s)ds, but neither deﬁned nor used Fj(t). Meanwhile, Tsiatis
[22] refers to Sj(t) as the jth net-speciﬁc survival distribution. He
concluded that “Type-j speciﬁc Kaplan–Meier estimator, obtained
from regarding Type-j event as failure and the other type of failure as
censor, of the jth net-speciﬁc survival distribution does not estimate
any interesting or relevant probability without the assumption that
cause j is independent of all the other causes.” Birrer et al. [23]
also note that “Death is, in time to event analysis that assesses
other outcomes rather than overall survival, a competing risk.
The KM estimator, however, is not designed to accommodate for
such competing risks and will produce inaccurate estimates.” These
observations are related to the comment made by Kalbﬂeisch and
Prentice [20], described in the later Section 7, “Censor or failure.”
6 CD-incidence to resolve
inconvenience with CS-incidence
According to Gray [3], a paradoxical relationship between CS-
incidence and CS-hazard was described using two groups and two
types of failure. He deﬁned a latent failure time model [20] such that
λ(1)0 = λ(1)1 = 3, λ(2)0 = 2, and λ(2)1 = 1, where λ(k)j denotes the
Type-j speciﬁc hazard for Group k. Groups 1 and 2 are considered
the control and treatment groups, respectively, and Types 0 and
1 are considered the primary and competing causes, respectively.
According to our interpretation, this treatment reduces the hazard
from 3 to 2 for the primary cause and 3 to 1 for the competing
cause, making it highly eﬀective. Since the failure types are mutually
independent, the competing failures are treated as independent
censoring in calculating the CD-incidence.
Figure 1 (left) depicts Type-1 CCS-incidence for the groups.
Since they cross each other, they fail to represent the treatment
eﬀect properly. This paradoxical phenomenon is caused by the
impact of competing failures on primary failures. On the other
hand, Figure 1 (right) shows that Type-1 CCD-incidence for the
treatment arm is consistently lower than that for the control arm,
which presents the treatment eﬀect properly. Gray’s example, in
eﬀect, demonstrates that the CD-incidence is more reliable than the
CS-incidence.
Kalbﬂeisch and Prentice [21] also describe a paradoxical
example of CCS-incidence. They deﬁne a latent failure time model
such that λ(1)0 = 1, λ(1)1 = t1/2, λ(2)0 = 1, and λ(2)1 = 0.5t1/2.
Treatment aﬀects the competing failures but not the primary
failures. However, CCS-incidence apparently showed a treatment
eﬀect on primary failure because of the change in the competing
risk. On the other hand, Nakamura and Yamada [10] showed that
CCD-incidence was the same for the two groups and therefore
showed no treatment eﬀect on Type-1 failure. The example also
demonstrated that the CD-incidence is more reliable than the CS-
incidence.
Frontiers in Applied Mathematics and Statistics
03
frontiersin.org

````

## PDF page 4; PDF label 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Nakamura et al.
10.3389/fams.2026.1777018
FIGURE 1
The horizontal lines denote time, while the vertical lines denote CCS-incidence (left) and CCD-incidence (right). The control and treatment arms are
denoted by blue and red lines, respectively. They cross in the left but not in the right ﬁgures.
7 Censor or failure
Kalbﬂeisch and Prentice [20] noted that “The likelihood factors
into a separate component for each failure type j=1..., m. Moreover,
the likelihood involving a speciﬁc hazard is precisely that which would
be obtained by regarding all failure types other than j as censored at
the individual failure time.” Although this is exactly true, it does not
mean that the likelihood is obtained by regarding other failure types
as censored independent of the primary failure. To understand
these observations correctly, we follow their likelihood derivation.
as follows:
Without loss of generality, we consider two failure types and
no censoring. Let {t0i}and {t1j} denote Type-0 and Type-1 failure
times, respectively. Then, using S(t) = S0(t)S1(t), the likelihood
factors are deﬁned as follows:
L(λ0, λ1) =

i
f0(t0
i )

j
f1(t1
j )
=

i
λ0(t0
i )S(t0
i )

j
λ1(t1
j )S(t1
j )
=

i
λ0(t0
i )S0(t0
i )S1(t0
i )

j
λ1(t1
j )S1(t1
j )S0(t1
j )
=
⎧
⎨
⎩

i
λ0(t0
i )S0(t0
i )

j
S0(t1
j )
⎫
⎬
⎭
⎧
⎨
⎩

j
λ1(t1
j )S1(t1
j )

i
S1(t0
i )
⎫
⎬
⎭= L0(λ0)L1(λ1),
where
L0(λ0)
=

i
f ∗
0 (t0
i ) 
j
S0(t1
j )
and
L1(λ1)
=

j
f ∗
1 (t1
j ) 
i
S1(t0
i ).
When (T = t, δ = 0) occurs, the likelihood contribution
f0(t)
=
λ0(t)S(t) is used, and when (T = t, δ = 1) occurs,
f1(t) = λ1(t)S(t) is used in the likelihood construction. In both
cases, the other event, or failure type, is simply ignored because it
did not occur. No censoring is involved in the likelihood derivation.
In short, since failure types are events, not random variables, they
cannot be censored. In a latent failure time formulation, their note
is appropriate. Nevertheless, L0(λ0) coincides with the likelihood
obtained as if regarding {t0i} as failures and {t1j} as censoring.
Furthermore, the independence between primary and competing
failures is not assumed in the likelihood derivation. Summarizing
the results from a practical point of view, MLE λ0 maximizing the
likelihood L0(λ0) = 
i
f ∗
0 (t0
i ) 
j
S0(t1
j ), obtained from regarding
{t0i} as failures and {t1j} as censoring, is asymptotically unbiased
and follow a normal distribution, even without assuming that
the competing failure is independent of the primary failure.
Consequently, the Kaplan–Meier estimate is a valid estimate of
S0(t). The results mainly follow from the assumption that λ(t) =
λ0(t) + λ1(t).
The majority of literature dealing with competing risk analysis
misinterprets that the MLE of λ0 is obtained from assuming the
competing failure as censoring independent of the primary failure.
Wolbers et al. [24] observed that “For this naive Kaplan–Meier
estimator, subjects experiencing competing events would be treated as
censored observations at the time of the competing event occurrence.
While frequently used, it is important to note that the logic of this
modiﬁed estimator is ﬂawed.” As described in Section 5, Klein
and Moershberger [18], Geskus [19], and Tsiatis [22] also showed
similar misinterpretation.
Cox [25] and Tsiatis [26] have shown that the data of (T, δ)
are not appropriate to study the interrelation between the failure
types. Therefore, the results of the Type-1 failure analysis should be
interpreted as dependent on the occurrence of Type-2 failure.
8 Subdistribution hazard or
cause-speciﬁc hazard
There is ongoing debate as to whether the subdistribution
hazard or the cause-speciﬁc hazard is more appropriate. Görlich
et al. [27] showed that “subdistribution models are better suited in
analysis contexts which aim at incidence or prediction.” Haque et al.
[28] observed that “The major limitation of using PH (Proportional
hazards model) is that it considers the individuals failing from causes
other than cause of interest as censored observations,” and concluded
Frontiers in Applied Mathematics and Statistics
04
frontiersin.org

````

## PDF page 5; PDF label 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Nakamura et al.
10.3389/fams.2026.1777018
that “The solution of this problem is to apply Fine-Gray regression
model based on CIF which does not ignore the other competing risks
when a speciﬁc cause is of interest.”
As discussed in Section 7, it is statistically valid to consider
individuals failing from the competing cause as censored, even
without assuming that the competing cause is independent of
the primary cause. The subdistribution hazard, or the Fine–Gray
hazard, was introduced as a hazard that corresponds one-to-one to
CCS-incidence, or CIF. However, the risk set of the subdistribution
hazard is unrealistic, since this hazard includes individuals who
have experienced competing causes of death as still being at risk
of the primary cause of death. In addition, it is veriﬁed that the
subdistribution hazard depends on independent censoring even
assuming censoring is complete [10].
Furthermore, as described in Section 6, CIF is severely subject
to the competing survival function, and CIF corresponds one-to-
one to the subdistribution hazard. Therefore, the subdistribution
hazard severely depends on the competing hazard. This explains the
ﬁndings by Haque et al. [29]; “the diﬀerences in the resulting sample
size from the cause-speciﬁc hazard and the subdistribution hazard
approaches depend strongly on the values of the type-2 treatment
eﬀect.” Thus, the solution opted by Haque et al. [28] may also pose
problems. Instead of the Fine–Gray hazard and CIF, λ0(t) and f ∗
0 (t)
might be considered as alternatives.
9 Conclusion
First, this study addressed the confusion in the interpretation
of the Fine–Gray hazard, the cause-speciﬁc incidence, and
the Kaplan–Meier estimate. To resolve the root cause of the
confusion, we ﬁrst demonstrated that the maximum likelihood
estimate of λ0 obtained by treating {t0i} as failures and {t1j}
as censoring is statistically valid and unbiased, even without
assuming independence between the competing and primary
failures. Consequently, the Kaplan–Meier estimate, obtained by
treating competing failures as censoring, is also statistically valid
and an unbiased estimate of the primary survivor function S0(t),
even when the competing failure is not independent of the
primary failure.
Secondly, we presented a proposition to resolve confusion
regarding the Kaplan–Meier estimate and CIF.
Thirdly, we examined the remark by Kalbﬂeisch and Prentice
[20] “Sj(t) will not, in general, have any survivor function
interpretation.” We reviewed their likelihood derivation and
showed that Sj(t) should be interpreted as a survivor function
to consider L0(λ0)
=

i
f ∗
0 (t0
i ) 
j
S1(t1
j ) and L1(λ1)
=

j
f ∗
1 (t1
j ) 
i
S0(t1
i ) as likelihoods for λ0 and λ1, respectively.
Author contributions
TN: Conceptualization, Supervision, Writing – original draft,
Writing – review & editing. TY: Investigation, Resources,
Writing – review & editing. YN: Conceptualization, Investigation,
Supervision, Writing – review & editing.
Funding
The author(s) declared that ﬁnancial support was not received
for this work and/or its publication.
Acknowledgments
The authors wish to thank Dr. Todd Saunders for proofreading
and providing valuable suggestions to improve our article.
Conﬂict of interest
The author(s) declared that this work was conducted in the
absence of any commercial or ﬁnancial relationships that could be
construed as a potential conﬂict of interest.
Generative AI statement
The author(s) declared that generative AI was not used in the
creation of this manuscript.
Any alternative text (alt text) provided alongside ﬁgures in
this article has been generated by Frontiers with the support of
artiﬁcial intelligence and reasonable eﬀorts have been made to
ensure accuracy, including review by the authors wherever possible.
If you identify any issues, please contact us.
Publisher’s note
All claims expressed in this article are solely those of the
authors and do not necessarily represent those of their aﬃliated
organizations, or those of the publisher, the editors and the
reviewers. Any product that may be evaluated in this article, or
claim that may be made by its manufacturer, is not guaranteed or
endorsed by the publisher.
References
1. Tullio A, Magli A, Moretti E, Valenta F. Why we should take care of the
competing risk bias in survival analysis: a phase II trial on the toxicity proﬁle
of radiotherapy for prostate cancer. Rep Pract Oncol Radiother. (2019) 24:511–
9. doi: 10.1016/j.rpor.2019.08.001
Frontiers in Applied Mathematics and Statistics
05
frontiersin.org

````

## PDF page 6; PDF label 6

FORMULA CHECK REQUIRED: original PDF page 6.

````text
Nakamura et al.
10.3389/fams.2026.1777018
2. Li
Y,
Sun
L,
Burstein
DS,
Getz
KD.
Considerations
of
competing
risks
analysis
in
cardio-oncology
studies.
JACC
CardioOncol.
(2022)
4:287–301. doi: 10.1016/j.jaccao.2022.08.002
3. Gray RJ. A class of K-sample tests for comparing the cumulative incidence of a
competing risk. Ann Stat. (1988) 16:1141–54. doi: 10.1214/aos/1176350951
4. Fine
JP,
Gray
RJ.
A
proportional
hazards
model
for
the
subdistribution
of
a
competing
risk.
J
Am
Stat
Assoc.
(1999)
94:496–
509. doi: 10.1080/01621459.1999.10474144
5. Austin PC, Steyerberg EW, Putter H. Fine-gray subdistribution hazard models to
simultaneously estimate the absolute risk of diﬀerent event types: cumulative total
failure probability may exceed 1. Statist Med. (2021) 40:4200–12. doi: 10.1002/sim.9023
6. Rehman H, Chandra N. Inferences on cumulative incidence function for middle
censored survival data with Weibull regression. Jpn J Stat Data Sci. (2022) 5:65–
86. doi: 10.1007/s42081-021-00142-y
7. Koller MT, Raatz H, Steyerberg EW, Wolbers M. Competing risks and
the clinical community: irrelevance or ignorance? Stat Med. (2012) 31:1089–
97. doi: 10.1002/sim.4384
8. Macek P, Biskup M, Terek-Derszniak M, Manczuk M, Krol H, Naszydlowska E, et al.
Competing risks of cancer and non-cancer mortality when accompanied by lifestyle-
related factors—a prospective cohort study in middle-aged and older adults. Front
Oncol. (2020) 10:545078. doi: 10.3389/fonc.2020.545078
9. Putter H, Schumacher M, van Houwelingen HC. On the relation between the cause-
speciﬁc hazard and the subdistribution rate for competing risks data: the ﬁne–gray
model revisited. Biom J. (2020) 62:790–807. doi: 10.1002/bimj.201800274
10. Nakamura
T,
Yamada
T.
On
concerns
with
cause-speciﬁc
incidence
and
subdistribution
hazard.
Jpn
J
Stat
Data
Sci.
(2025)
8:265–
78. doi: 10.1007/s42081-024-00274-x
11. Andersen PK, Geskus RB, de Witte T, Putter, H. Competing risks in epidemiology:
possibilities and pitfalls. Int J Epidemiology. (2012) 41:861–70. doi: 10.1093/ije/
dyr213
12. Schuster NA, Hoogendijk EO, Kok AAL, Twisk JWR, Heymans MW. Ignoring
competing events in the analysis of survival data may lead to biased results: a
nonmathematical illustration of competing risk analysis. J Clin Epidemiol. (2020)
122:42–8. doi: 10.1016/j.jclinepi.2020.03.004
13. Lacny S, Faris P, Bohm E, Woodhouse LJ, Robertsson O, Marshall DA.
Competing risks methods are recommended for estimating the cumulative incidence of
revision arthroplasty for health care planning purposes. Orthopedics. (2021) 44:e549–
55. doi: 10.3928/01477447-20210618-16
14. McCaw ZR, Claggett BL, Tian L, Solomon SD, Berwanger O, Pfeﬀer MA, et al.
Practical recommendations on quantifying and interpreting treatment eﬀects in
the presence of terminal competing risks: a review. JAMA Cardiol. (2022) 7:450–
6. doi: 10.1001/jamacardio.2021.4932
15. Haque
MA,
Cortese
G.
Cumulative
incidence
functions
for
competing
risks
survival
data
from
subjects
with
COVID-19.
Mathematics.
(2023)
11:3772. doi: 10.3390/math11173772
16. Gaynor JJ, Guerra G, Vianna R, Marina M, Tabbara MM, Graell EL, et al.
Competing risks analysis of kidney transplant waitlist outcomes: two important
statistical perspectives. Kidney Int Rep. (2024) 9:1580–9. doi: 10.1016/j.ekir.2024.01.050
17. Zaino M. Overestimation of cardiovascular mortality risk by Kaplan–Meier in
competing risks settings: a web-based calculator and NHANES analysis. Int J Stat Med
Res. (2025) 14:323–36. doi: 10.6000/1929-6029.2025.14.31
18. Klein JP, Moeschberger ML. Survival Analysis: Techniques for Censored and
Truncated Data. New York: Springer-Verlag (1997).
19. Geskus RB. Competing risks: concepts, methods, and software. Annu Rev Stat Appl.
(2024) 11:227–54. doi: 10.1146/annurev-statistics-040522-094556
20. Kalbﬂeisch JD, Prentice RL. The Statistical Analysis of Failure Time Data. 1st ed.
New York, NY: Wiley-Interscience (1980).
21. Kalbﬂeisch JD, Prentice RL. The Statistical Analysis of Failure Time Data. 2nd ed.
New York, NY: Wiley-Interscience (2002). doi: 10.1002/9781118032985
22. Tsiatis A. Competing Risks Encyclopedia of Biostatistics. New York, NY: Wileys
(1998). p. 824–34.
23. Birrer DL, Kuemmerli C, Meuli L. The risk of competing risks in time to event
analysis. Eur J Vasc Endovasc Surg. (2024) 68:6–9. doi: 10.1016/j.ejvs.2024.04.013
24. Wolbers M, Koller MT, Stel VS, Schaer B, Jager KJ, Leﬀondre K, et al.
Competing risks analyses: objectives and approaches. Eur Heart J. (2014) 35:2936–
41. doi: 10.1093/eurheartj/ehu131
25. Cox DR. The analysis of exponentially distributed life-times with two types of
failure. J R Stat Soc B. (1959) 21:311–421. doi: 10.1111/j.2517-6161.1959.tb00349.x
26. Tsiatis A. A nonidentiﬁability aspect of the problem of competing risk. Proc Natl
Acad Sci. (1975) 72:20–2. doi: 10.1073/pnas.72.1.20
27. Görlich D, Lanwer L, Sauerland C, Krug U, Faldum A. Characterizing overall
survival of patients with acute myeloid leukemia: a competing risk analysis of SEER
data covering 46 years. Cancers. (2025) 17:3735. doi: 10.3390/cancers17233735
28. Haque N, Haque MA, Sadikeen SS, Uddin MJ. A hierarchical competing risks
survival model in the study of child mortality in Bangladesh. Sci Rep. (2025)
15:44812. doi: 10.1038/s41598-025-28584-4
29. Haque MA, Cortese G. Sample size for competing risks survival analysis
in ﬁxed and group-sequential designs. Stat Methods Appl. (2025) 34:1095–
121. doi: 10.1007/s10260-025-00811-2
Frontiers in Applied Mathematics and Statistics
06
frontiersin.org

````

