# Estimating restricted mean survival time and expected life-years lost in the presence of competing risks within flexible parametric survival models

Original PDF: [original.pdf](original.pdf). SHA256: `31ffff349ee4e28d72efca3fc1b7181278c61f343c30d9f8ca15c0602c996114`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
Estimating restricted mean survival time and
expected life-years lost in the presence of
competing risks within §exible parametric survival
models
Sarwar Islam Mozumder  (  sarwar.islam@gmail.com )
University of Leicester https://orcid.org/0000-0001-9644-7525
Mark Rutherford 
University of Leicester College of Medicine Biological Sciences and Psychology
Paul Lambert 
University of Leicester College of Medicine Biological Sciences and Psychology
Research article
Keywords: competing risks, restricted mean survival time, restricted mean life time, ﬂexible parametric
model, life-years lost, survival analysis
Posted Date: January 7th, 2021
DOI: https://doi.org/10.21203/rs.2.23839/v3
License:   This work is licensed under a Creative Commons Attribution 4.0 International License.  
Read Full License
Version of Record: A version of this preprint was published on March 11th, 2021. See the published
version at https://doi.org/10.1186/s12874-021-01213-0.

````

## PDF page 2

Technical extraction; compare with original PDF page 2.

````text
Mozumder et al.
RESEARCH
Estimating restricted mean survival time and
expected life-years lost in the presence of
competing risks within ﬂexible parametric survival
models
Sarwar I Mozumder1*, Mark J Rutherford1 and Paul C Lambert1,2
*Correspondence:
sarwar.mozumder@le.ac.uk
1Biostatistics Research Group,
Department of Health Sciences,
University of Leicester, University
Road, LE1 7RH Leicester, UK
Full list of author information is
available at the end of the article
Abstract
Background: Royston-Parmar ﬂexible parametric survival models (FPMs) can be
ﬁtted on either the cause-speciﬁc hazards or cumulative incidence scale in the
presence of competing risks. An advantage of modelling within this framework for
competing risks data is the ease at which alternative predictions to the
(cause-speciﬁc or subdistribution) hazard ratio can be obtained. Restricted mean
survival time (RMST), or restricted mean failure time (RMFT) on the mortality
scale, is one such measure. This has an attractive interpretation, especially when
the proportionality assumption is violated. Compared to similar measures, fewer
assumptions are required and it does not require extrapolation. Furthermore, one
can easily obtain the expected number of life-years lost, or gained, due to a
particular cause of death, which is a further useful prognostic measure as
introduced by Andersen.
Methods: In the presence of competing risks, prediction of RMFT and the
expected life-years lost due to a cause of death are presented using
Royston-Parmar FPMs. These can be predicted for a speciﬁc covariate pattern to
facilitate interpretation in observational studies at the individual level, or at the
population-level using standardisation to obtain marginal measures. Predictions
are illustrated using English colorectal data and are obtained using the Stata
post-estimation command, standsurv.
Results: Reporting such measures facilitate interpretation of a competing risks
analysis, particularly when the proportional hazards assumption is not
appropriate. Standardisation provides a useful way to obtain marginal estimates
to make absolute comparisons between two covariate groups. Predictions can be
made at various time-points and presented visually for each cause of death to
better understand the overall impact of diﬀerent covariate groups.
Conclusions: We describe estimation of RMFT, and expected life-years lost
partitioned by each competing cause of death after ﬁtting a single FPM on either
the log-cumulative subdistribution, or cause-speciﬁc hazards scale. These can be
used to facilitate interpretation of a competing risks analysis when the
proportionality assumption is in doubt.
Keywords: competing risks; restricted mean survival time; restricted mean life
time; ﬂexible parametric model; life-years lost; survival analysis
1
2
1 Background
3

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
Mozumder et al.
Page 2 of 47
In observational studies of time-to-event data, researchers are often interested in
4
decomposing the overall probability of death into component parts due to the event
5
of interest, and competing, but mutually exclusive outcome events. For example,
6
in cancer studies, it is of interest to partition the overall probability of death into
7
the probability of death due to cancer and the probability of death due to other
8
causes. These are referred to as cause-speciﬁc cumulative incidence functions (CIFs)
9
and are often chosen as the primary estimand of interest. The cause-speciﬁc CIF
10
gives the probability of dying from the cause of interest at a particular time whilst
11
also being at risk of dying from other causes of death [1, 2]. In order to arrive at
12
these quantities and to circumvent bias, methods that appropriately account for the
13
competing nature of the events must be applied. The restricted mean failure time
14
(RMFT) has been proposed as an alternative summary measure that is based on
15
the area under the all-cause probability of death up to a speciﬁc time-point[3]. In
16
an analogous way to the decomposition into cause-speciﬁc CIFs, the RMFT can be
17
further partitioned to give the expected number of life years lost due to a speciﬁc
18
cause before a given time-point. In this paper, we describe how the aforementioned
19
measures can be obtained using a ﬂexible parametric model (FPM) as the estimation
20
approach by modelling covariate eﬀects either using (1) the direct relationship with
21
the cause-speciﬁc CIF on the subdistribution hazards (SDHs) scale, or (2) modelling
22
all cause-speciﬁc hazard functions (CSHs) to obtain each cause-speciﬁc CIF [4,
23
5, 6, 7]. Choosing FPMs as the estimation method allows us to estimate eﬀects
24
conditional on covariates, and eﬀects averaged over speciﬁc covariate distributions.
25
Forming contrasts to compare exposure groups is often a further key focus in many
26
large population-based studies. A common approach would be to report either cause-
27
speciﬁc hazard ratios (HRs), which measures the eﬀect of an exposure group on the
28
rate of dying from a cause of interest, or sub-distribution hazard ratios (SHRs),
29
which measures the eﬀect of an exposure group on the risk of dying from a cause
30

````

## PDF page 4

Technical extraction; compare with original PDF page 4.

````text
Mozumder et al.
Page 3 of 47
of interest, whilst assuming that the cause-speciﬁc HR or SHR was constant over
31
time. However, it is well known, for instance, that the HR for tumor size in cancer
32
studies will vary over time since diagnosis, with stronger relative eﬀects shortly
33
after diagnosis [8, 9, 10]. When non-proportional hazards are present i.e. when the
34
HR is expected to change over time, it has been argued that the HR as the target
35
estimand is not appropriate and there are further issues in making causal inferences
36
using HR measures due to its non-collapsibility as a relative risk measure [11]. As
37
an alternative to the HR, estimation of the diﬀerence in restricted mean survival
38
time (RMST), also known as the restricted mean lifetime (RMLT), as the primary
39
estimand has been proposed [12, 13, 14, 15, 16, 17, 18, 19]. This, in contrast to the
40
HR, is known as a collapsible measure [11, 20]. Furthermore, this single summary
41
measure can still be presented when relaxing the assumption of proportional hazards
42
within the model-building process. These can either be presented as conditional
43
diﬀerences, which is the average covariate eﬀect on the individual, or marginal
44
diﬀerences, which is the average covariate eﬀect on the population [21].
45
In the presence of competing risks, Andersen [3] introduces the analogue to the
46
RMST measure for the CIF which gives the (total) number of years lost before a
47
pre-speciﬁed time, i.e. RMFT, and demonstrates how this can be partitioned to
48
give the expected number of life-years lost due to each cause of death [22]. In his
49
approach, he estimates RMFT and expected number of life-years lost using regres-
50
sion models with pseudo-observations [3, 23]. These models only allow prediction
51
for speciﬁc quantities of interest and only at single time-points. Therefore sepa-
52
rate models must be ﬁtted to estimate, for example, either the cause-speciﬁc CIF
53
or RMFT, when it may be of interest to obtain both and at various time-points.
54
For instance, to allow comparability and to obtain the entire picture of the impact
55
of diﬀerent groups on outcome, it has been suggested that diﬀerences in RMST,
56
RMFT and therefore, expected number of life-years lost, should be reported along-
57

````

## PDF page 5

Technical extraction; compare with original PDF page 5.

````text
Mozumder et al.
Page 4 of 47
side their respective survival, or cumulative incidence functions [24]. Alternatively,
58
the Royston-Parmar FPM approach for estimating RMST, which is extended for
59
competing risks to estimate partitioned RMFT, as introduced in this paper, can
60
be used [25]. In contrast to more popular approaches, such as the Cox model, a
61
parametric estimate of the baseline hazard function is obtained as part of the full
62
likelihood function. This is estimated using restricted cubic splines (RCS), allowing
63
easy prediction of absolute comparisons between key quantities of interest. What’s
64
more, standard errors for predictions can be estimated via the delta method, which
65
oﬀers computational advantages in larger data compared to approaches for non-
66
parametric and semi-parametric methods which use bootstrapping, or jack-knife
67
resampling methods [26]. Further advantages include the easy inclusion of time-
68
dependent eﬀects using interactions with RCS for relaxing the proportional haz-
69
ards assumption. Estimating both the baseline eﬀects, and time-dependent eﬀects
70
to model departures from the baseline using splines allows a uniﬁed approach for
71
estimating all required parameters in order to obtain predictions of all quantities
72
of interest. Therefore, we introduce in this paper how RMFT as the chosen esti-
73
mand can be estimated using FPMs in the presence of competing risks on either the
74
CSHs or cumulative incidence scale as the estimator [7, 5]. This extends on previous
75
work by Royston and Parmar where estimation in the presence of competing risks
76
is not considered [16]. This approach allows the researcher to obtain diﬀerences in
77
eﬀect between exposure groups either conditional on a set of covariates, or averaged
78
over a covariate distribution, also known as marginal estimates. Furthermore, both
79
marginal and conditional estimates can be obtained from the same model where
80
the prediction of marginal estimates using standardisation is proposed [27, 28]. We,
81
therefore, further demonstrate how diﬀerence in marginal estimates of RMFT as
82
the chosen estimand for the comparison between covariate groups can be obtained
83
within FPMs for competing risks.
84

````

## PDF page 6

Technical extraction; compare with original PDF page 6.

````text
Mozumder et al.
Page 5 of 47
We begin with a brief review of competing risks in Section 2.1 and highlight
85
particular interest in the cause-speciﬁc CIF. This is followed by an introduction of
86
the RMFT as the chosen estimand in Section 2.2 along with other useful measure
87
such as expected life-years lost. Section 2.3 details FPM approaches for estimation
88
in the presence of competing risks. In Section 2.4, we show how absolute diﬀerences
89
between RMFT and expected number of life-years lost are calculated to assess the
90
impact of a covariate. We further demonstrate how these models can be used for
91
easily obtaining marginal estimates and associated contrasts using standardisation
92
in Section 2.4.4. For illustration of these various measures, English colorectal cancer
93
data obtained from National Cancer Registration and Analysis Service (NCRAS)
94
is analysed in Section 3 where comparisons between the most and least deprived
95
colorectal cancer patients are made, accompanied by Stata code for estimation in
96
Appendix D. Finally, the paper is concluded with a discussion on the use and
97
estimation of RMST in the presence of competing risks within FPMs. Although
98
we speciﬁcally consider application to cancer studies, where the event of interest is
99
death from cancer, the methods are generalizable to other time-to-event data and
100
therapeutic areas.
101
2 Methods
102
2.1 Overview of competing risks
103
In the presence of competing risks, an individual is at risk of failing from more
104
than one event where the occurrence of one event means that others cannot occur.
105
In the context of a cancer survival study, this is when a patient can die from a
106
multitude of other causes as well as the cancer itself. However, if the patient dies
107
from one of these other causes, it means that the time at which the patient would
108
have died from cancer is never observed. One of the key quantities, and often the
109
chosen estimand of interest within this framework, is the cause-speciﬁc CIF [1].
110

````

## PDF page 7

FORMULA CHECK REQUIRED: original PDF page 7.

````text
Mozumder et al.
Page 6 of 47
2.1.1 Cause-speciﬁc CIF
111
Let T be a non-negative random variable for the time to death from any cause.
112
Furthermore, let D denote the cause of death in the presence of k = 1, . . . , K
113
competing risks, where D = 1, . . . , K. It follows that the estimand, cause-speciﬁc
114
CIF, Fk(t), is deﬁned as,
115
Fk(t) = P(T ≤t, D = k)
(1)
This is interpreted as the probability of dying from cause k by time t whilst also
116
being at risk of dying from other competing causes of death. Note here that the
117
cause-speciﬁc CIF is an improper distribution function since the integral of Fk(t)
118
at inﬁnity is always less than 1 [3].
119
The target estimand, the cause-speciﬁc CIF, can be calculated using either all k
120
CSH functions, or by utilising the one-to-one relationship between the cause-speciﬁc
121
SDH function. These are brieﬂy introduced below.
122
2.1.2 Cause-speciﬁc hazards
123
The CSHs, hcs
k (t), give the instantaneous mortality rate from a particular cause k
124
given that the patient is still alive at time t in the presence of all the other causes
125
of death such that,
126
hcs
k (t) = lim
∆t→0
P[t ≤T < t + ∆t, D = k|T ≥t)
∆t
(2)
It follows that the target estimand, the cause-speciﬁc CIF, can be calculated as a
127
function of all k CSH functions,
128

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
Mozumder et al.
Page 7 of 47
Fk(t) =
Z t
0
S(u)hcs
k (u)du
(3)
where S(t) = exp

−PK
k=1
R t
0 hcs
k (u)du

is the all-cause survival function.
129
2.1.3 Subdistribution hazards
130
Alternatively, Gray [29] introduces the SDH function for cause k, hsd
k (t), which
131
oﬀers a direct one-to-one relationship with the cause-speciﬁc CIF estimand. This
132
has the following mathematical formulation,
133
hsd
k (t) = lim
∆t→0
P[t ≤T < t + ∆t, D = k|T ≥t ∪(T ≤t ∩D̸ = k)
∆t
(4)
which is interpreted as the instantaneous “sub”-rate of failure at time t from
134
cause k amongst those who are still alive, or have died from any of the other K −1
135
competing causes excluding cause k [30].
136
This is not deﬁned as a typical epidemiological rate since the risk-set includes those
137
that are either still alive or have died from a competing cause of death. However,
138
if individuals do not experience the competing event, then the SDH rate and the
139
CSH rate are both equivalent [31]. It should be noted that, due to the nature of the
140
risk-set in the deﬁnition of a SDH, it is very diﬃcult to interpret [32, 30, 33].
141
The cause-speciﬁc CIF estimand can be directly obtained from the SDH for cause
142
k using the standard survival transformation of the cumulative SDH function for
143
cause k, Hsd
k (t), such that,
144
Fk(t) = 1 −exp

−Hsd
k (t)

(5)

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
Mozumder et al.
Page 8 of 47
This shows that a one-to-one correspondence is maintained between the SDH
145
function for a speciﬁc cause of death and the cause-speciﬁc CIF.
146
The choice of which scale to model on depends entirely on the research question
147
to be answered which would relate to other quantities speciﬁc to the modelling
148
approach that may be of interest. For instance, if primary interest is in aetiological
149
outcome, then the estimand of interest would be on the CSH rates. For interest in
150
prognostic outcome, one may wish to quantify eﬀects on the risk of dying from a
151
speciﬁc cause of death. In this case, the estimand of interest would be the cause-
152
speciﬁc CIF, which can be obtained as function of all CSHs, or through the SDH
153
for cause k. Further discussion on this topic is provided elsewhere [34, 4].
154
2.2 Overview of restricted mean survival time for competing risks
155
The RMST measure quantiﬁes the average survival, or time lived, of a patient from
156
time 0 up to a pre-deﬁned time-point, t∗. In the absence of competing risks, the
157
RMST before t = t∗, µ(t∗), of a random variable T is equal to the expectation of
158
min(T, t∗). RMST, in the absence of covariates, can be expressed as the estimand,
159
µ(t∗) = E(min(T, t∗)) =
Z t∗
0
S(u)du
(6)
where S(t) is the all-cause survival function. If time is measured in years, this is
160
the average life-years lived before time t∗. The choice of t∗should be pre-determined
161
and clinically motivated, and will vary by, for example, cancer types [16, 15]. This
162
is also often chosen at maximum follow-up time [13, 35].
163
In addition to this, Andersen [3] proposes calculation of the expected number of
164
years lost before time t∗such that the estimand can be deﬁned as,
165

````

## PDF page 10

FORMULA CHECK REQUIRED: original PDF page 10.

````text
Mozumder et al.
Page 9 of 47
L(0, t∗) = t∗−E(min(T, t∗)) = t∗−
Z t∗
0
S(u)du
(7)
2.2.1 Expected loss in life due to a cause of death
166
In the presence of competing risks, Andersen [3] shows that the (total) number of
167
years lost, L(0, t∗), can be decomposed into the number of years lost due to each
168
cause k [22]. It follows that since,
169
S(t) = 1 −
K
X
k=1
Fk(t)
(8)
then the RMST in Equation 6 can be expressed as a function of each cause-speciﬁc
170
CIF through the following integral,
171
µ(t∗) = E(min(T, t∗)) =
Z t∗
0
S(u)du =
Z t∗
0
1 −
K
X
k=1
Fk(u)du
= t∗−
Z t∗
0
K
X
k=1
Fk(u)du
(9)
Equation 7 can also be written as a sum of the integral of each cause-speciﬁc CIF
172
such that,
173
L(0, t∗) = t∗−
Z t∗
0
S(u)du =
K
X
k=1
Z t∗
0
Fk(u)du
(10)
which may also be referred to as restricted mean failure time (RMFT). It follows
174
that RMFT can be partitioned where we have the estimand,
175

````

## PDF page 11

FORMULA CHECK REQUIRED: original PDF page 11.

````text
Mozumder et al.
Page 10 of 47
Lk(0, t∗) =
Z t∗
0
Fk(u)du
(11)
which gives the expected number of years lost due to cause k before time t∗.
176
2.3 Flexible parametric survival models
177
For competing risks data, many adopt the cause-speciﬁc Cox proportional hazards
178
model, or the Fine & Gray approach as the chosen estimator for the estimands
179
introduced in Sections 2.1 and 2.2. Here, we propose the use of FPMs as the cho-
180
sen estimator in order to obtain the estimand of interest. FPMs are increasing in
181
popularity since the baseline SDH or CSH function is estimated as part of a fully
182
speciﬁed likelihood function and allows the estimation of various estimands from
183
a single model [5, 7]. These models were introduced for standard survival data (in
184
the absence of competing risks) on various scales by Royston and Parmar [9] using
185
a general link function, g(·), to better capture and represent the behaviour of real
186
world data. To increase ﬂexibility and more accurately capture complex shapes of
187
the cumulative hazard function, Royston and Parmar [9] proposed the use of RCS
188
(see Appendix A). Under the assumption of proportional hazards, Rutherford et. al
189
[36] showed in simulations that FPMs more accurately capture complex shapes of
190
hazard functions. They further illustrated that unbiased estimates of the HRs were
191
obtained. Given a vector of M knots, m, and a vector of M −1 parameters, γ, with
192
a RCS function, s(ln(t);γ, m) we have that,
193
η = g(Gk(t | xk)) = sk(ln(t);γk, mk) + xkβT
k
(12)
where, β, is a vector of co-eﬃcient parameters and, x, is a vector of covariates.
194

````

## PDF page 12

FORMULA CHECK REQUIRED: original PDF page 12.

````text
Mozumder et al.
Page 11 of 47
Equation 12 can also be easily extended for time-dependent eﬀects to model non-
195
proportionality by ﬁtting interactions between the associated covariates and the
196
spline functions. Using this interaction, a new set of knots, me, are introduced,
197
which represent the eth time-dependent eﬀect with associated parameters αe. If
198
there are e = 1, · · · , E time-dependent eﬀects, Equation 12 can be extended such
199
that,
200
η = g(Gk(t | x)) = s(ln(t);γ, m0) + xβT +
E
X
l=1
s(ln(t);αl, ml)xl
(13)
Non-proportional hazards are a common occurrence in studies with long follow-
201
up time, or, in the context of cancer studies, when the eﬀect of covariates (e.g
202
tumor size, or treatment) on cancer-related mortality varies over time [9, 10, 8, 19].
203
FPMs, extended for time-dependent eﬀects as in the Equation above, have also
204
been shown to accurately capture complex shapes of the hazard function with time-
205
dependent eﬀects i.e. where there is non-proportionality in the hazards [37]. This
206
result is consistent with what was shown by Rutherford et. al. for FPMs without
207
time-dependent eﬀects i.e. proportional hazards, as mentioned above [36]. Further
208
technical details on FPMs for standard survival data in the absence of competing
209
risks can be found elsewhere [9, 38, 25].
210
The models described in Equations 12 and 13 can be ﬁtted on either CSHs scale
211
[7], where Gk(t | x) = Sk(t | x), or cumulative incidence scale [5, 6], where Gk(t |
212
x) = 1 −Fk(t | x), based on diﬀerent link functions, g(·). The relationship of these
213
with the cause-speciﬁc CIF are deﬁned in Sections 2.1.2 and 2.1.3. Therefore, it
214
follows that, using a complementary log-log link function, the corresponding log-
215
cumulative CSHs FPM (otherwise referred to as a cause-speciﬁc FPM), is,
216

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
Mozumder et al.
Page 12 of 47
ηcs
k = log [−log [Sk (t | xk)]] = log [Hcs
k (t | x)] = sk(ln(t);γk, mk) + xkβT
k (14)
and can be ﬁtted in a similar way to the standard FPM. Alternatively, models for
217
all k causes can be ﬁtted simultaneously by restructuring the data as described by
218
Hinchliﬀe et. al. [7].
219
The log-cumulative SDHs FPM for cause k (also known as the ﬂexible parametric
220
cumulative incidence model, or FPCIM), on the other hand is deﬁned as,
221
ηsd
k = log [−log [1 −Fk (t | xk)]] = log

Hsd
k (t | x)

= sk(ln(t);γk, mk)+xkβT
k (15)
and can be ﬁtted using the approach outlined using either the full likelihood
222
function as described by Mozumder et. al. [5] or by using time-dependent censoring
223
weights, similar to the Fine-Gray model, as detailed by Lambert et. al. [6]. As
224
previously mentioned, alternative link functions are also available for models on
225
either scale. See for example, Lambert et. al. [6].
226
2.4 Estimation
227
2.4.1 Cause-speciﬁc cumulative incidence function
228
If modelling on the cumulative incidence scale using SDHs, after ﬁtting the FPCIM
229
in Equation 15, the cause-speciﬁc CIF is obtained by the following,
230
bFk (t | x) = 1 −exp

−exp
 ˆ
ηsd
k (t | x)

(16)

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
Mozumder et al.
Page 13 of 47
Alternatively, when modelling on the CSHs scale, after ﬁtting the cause-speciﬁc
231
FPM in Equation 14, and as shown in Equation 3, the integral below must be
232
evaluated in order to obtain the cause-speciﬁc CIF,
233
bFk (t | x) =
Z t
0
bS (u | x) bhcs
k (u | x) du
(17)
where the predicted CSH function is,
234
bhcs
k (t | x) = ds (log(t) | γ, m0)
dt
exp (ηcs
k (t))
(18)
and the predicted all-cause survival function is,
235
bS (u | x) =
K
Y
k=1
exp

−
Z t
0
bhcs
k (u | x)du

(19)
However, as the above integral is not of closed form, numerical approximation
236
techniques must be used. Here, the Gauss-Legendre quadrature approximation
237
method is used [39]. Details of this method is provided in Appendix B. Therefore,
238
after ﬁtting the cause-speciﬁc FPM for each k causes, the predicted cause-speciﬁc
239
CIF at t1, · · · , t diﬀerent time-points over an interval [0, t] is approximated by ap-
240
plying Gaussian quadrature rules with W(u) = 1 such that,
241
bFk (t | x) =
Z t
0
f ∗
k(u)du ≈t −0
2
m
X
i=1
w′
if ∗
k
t −0
2
u′
i + t + 0
2
| x

(20)
where, bf ∗
k(t), is the “sub”-density function such that,
242

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
Mozumder et al.
Page 14 of 47
bf ∗
k (t | x) = bS (t | x) bhcs
k (t | x)
(21)
2.4.2 Restricted mean failure time and expected number of life-years lost due to
243
each cause of death
244
If RMFT is the chosen target estimand of interest, this can be predicted as the
245
integral under the all-cause CIF such that,
246
bL (0, t∗) =
Z t∗
0
K
X
j=1
bFj(u)du =
K
X
j=1
Z t∗
0
bFj(u)du
(22)
where the predicted expected number of life-years lost before time t∗due to each
247
cause k is,
248
bLk (0, t∗| x) =
Z t∗
0
bFk(u | x)du
(23)
Again, as above in Equation 17, as the integral is of closed-form, we use the
249
Gauss-Legendre quadrature approximation technique to numerically evaluate,
250
Z t∗
0
bFk(u)du ≈t∗−0
2
m
X
i=1
w′
i bFk
t∗−0
2
u′
i + t∗+ 0
2
| x

(24)
It follows that the RMST can also be obtained by,
251

````

## PDF page 16

FORMULA CHECK REQUIRED: original PDF page 16.

````text
Mozumder et al.
Page 15 of 47
bµ (t∗| x) = t∗−
K
X
j=1
bLj (0, t∗)
(25)
2.4.3 Conditional diﬀerences
252
In population-based studies, i.e. non-randomised studies, it may be of interest to
253
make absolute or relative comparisons between diﬀerent covariate groups. As an
254
alternative summary measure, or estimand, to the HR, we can calculate the diﬀer-
255
ence in RMST between two covariate groups, or the diﬀerence in expected loss in
256
life due to diﬀerent causes [19]. Let X be a binary covariate that denote the group
257
of interest and Z be the set of measured covariates with a speciﬁc covariate pattern
258
zj. To estimate the average number of life years gained in group X = 0 compared
259
to group X = 1, we have that,
260
ˆµ(t∗| X = 1, Z = zj) −ˆµ(t∗| X = 0, Z = zj)
(26)
Alternatively, we can also estimate the expected reduction in the loss (or gain) in
261
life due to cause k by,
262
ˆLk(0, t∗| X = 1, Z = zj) −ˆLk(0, t∗| X = 0, Z = zj)
(27)
Partitioning in this way is particularly useful if covariates act diﬀerently on diﬀer-
263
ent causes of death. For example, those from a particular covariate group may lose
264
(or gain) some life-years due to a speciﬁc cause of death in comparison to another
265
covariate group.
266

````

## PDF page 17

FORMULA CHECK REQUIRED: original PDF page 17.

````text
Mozumder et al.
Page 16 of 47
Absolute measures of gains or losses in years of life are presented above as potential
267
estimates of interest. To obtain relative measures, the ratio between the RMST
268
estimates, or expected loss in life due to cause k for the two covariate groups are
269
calculated. Extension can also be made for comparisons on a unit increase in a
270
continuous covariate Z, and for time-dependent eﬀects.
271
2.4.4 Standardisation for marginal diﬀerences
272
Regression standardisation is part of the estimator that can be used to obtain
273
marginal predictions for diﬀerent covariate groups at each observation given a set
274
of measured confounders [28, 27]. Here, we apply standardisation to RMST and
275
cause-speciﬁc CIFs estimates obtained from a ﬂexible parametric competing risks
276
survival model. In this case, it is of interest to compare the average life-years lived
277
before time t∗between two diﬀerent groups [18, 17]. This is done by obtaining
278
marginal estimates which are calculated as an average over every individual in the
279
observed dataset. This enables comparisons that solely focus on the diﬀerences
280
between the two groups of interest by forcing the same covariate distribution over
281
multiple confounders. If all exposures and confounders are measured at baseline,
282
this is essentially equivalent to the G-formula [40]. For example, to compare males
283
and females, estimates must be standardised by age in order to force the same
284
age distribution for both males and females. Extension can be made for multiple
285
covariates and other potential confounders. This is calculated using an average of
286
RMST estimates for each patient to summarise the risk for a certain covariate group.
287
For instance, let X be an indicator variable that denotes the group of interest and
288
Z be the set of measured covariates. Then the predicted RMST estimate for the ith
289
individual, where i = 1, . . . , N, is,
290
bµi = t∗−
Z t∗
0
K
X
k=1
h
bFk(u | X = x, Z = zi)
i
du
(28)

````

## PDF page 18

FORMULA CHECK REQUIRED: original PDF page 18.

````text
Mozumder et al.
Page 17 of 47
where X is ﬁxed to a speciﬁc value, x, and Z is the observed covariate pattern, zi,
291
for the ith individual. We can then average over the marginal distribution of Z for
292
all the predicted restricted mean life estimates obtained for each individual i such
293
that,
294
E(bµstand | X = x, Z) = 1
N
N
X
i=1
bµi
(29)
This allows us to calculate marginal diﬀerences between covariate groups. For
295
example, between group X = 0 and group X = 1, the marginal diﬀerence in RMST
296
is,
297
E(bµstand | X = 1, Z) −E(bµstand | X = 0, Z)
(30)
In recent literature, some have advocated the use of RMST as a causal measure
298
[41, 42]. For a causal interpretation, the consideration of additional assumptions are
299
required and by adjusting for all appropriate confounders, these measures can be
300
extended and interpreted as causal eﬀects and thus, used as an estimand [21]. This
301
is because, as shown above, they provide marginal comparisons averaged over the
302
same covariate distribution by using standardisation. Standardisation, otherwise
303
referred to as G-computation, has also been highlighted by Gran et al. [43] as an
304
approach for obtaining useful summary causal-eﬀect measures in more complicated
305
multi-state models. However, this is beyond the scope of the paper and estimation
306
of causal eﬀects are not explicitly discussed here. Note also that we only consider
307
time-ﬁxed confounders and that there are additional complexities when considering
308
time-dependent risk-groups [44].
309

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Mozumder et al.
Page 18 of 47
3 Results: Colorectal cancer survival in England
310
3.1 Data
311
Data was obtained from the National Cancer Registration and Analysis Service
312
(NCRAS) to illustrate the estimation of various measures introduced in Section
313
2.2. The data consist of English colorectal (ICD10: C18, C19 and C20) male and
314
female cancer patients aged between 45 and 90 years old. Patients are diagnosed on
315
or after 1998 are included with follow-up restricted to either 10 years or censored at
316
31 Dec 2013, whichever comes ﬁrst. Analysis is further restricted to patients from
317
the most or least deprived groups as deﬁned by the upper and lower quintiles of the
318
English index of multiple deprivation 2010 (IMD 2010). These groups are selected
319
to simplify analysis and to make for easy illustration of presenting diﬀerent metrics
320
to allow comparisons between the two groups. The ﬁnal data consisted a total
321
of 159,022 individuals of which 48,845 die from cancer, 7,987 from cardiovascular
322
disease (CVD) and 32,133 from other causes. In Appendix C, summary statistics
323
on the age distribution, and number of patients in each deprivation and sex groups
324
are provided.
325
3.2 Model
326
For demonstration purposes, predictions are obtained after ﬁtting an FPCIM si-
327
multaneously for all k causes of death and standard errors for conﬁdence intervals
328
(CIs) are obtained using the delta method. However, predictions are also available
329
after ﬁtting cause-speciﬁc FPMs. This paper focusses on the various estimands we
330
can obtain from such models, namely, the RMST measure and expected life-years
331
lost.
332
Models are ﬁtted simultaneously for all k causes of death using the approach
333
of Lambert et al. [6] and Geskus [45]. This ﬁts the model after restructuring the
334
data and applying time-dependent weights that are obtained parametrically to the
335
censoring distribution of the competing causes of death. Alternatively, using the
336

````

## PDF page 20

Technical extraction; compare with original PDF page 20.

````text
Mozumder et al.
Page 19 of 47
approach described by Jeong and Fine [46], models can be ﬁtted on individual-level
337
data using the full likelihood function [47]. Models for each of the causes of death
338
include sex, IMD 2010 deprivation group (upper and lower quintile only) and a
339
non-linear eﬀect of continuous age using RCS with 3 DF centred at 45 years old
340
at diagnosis. Time-dependent eﬀects to relax the proportionality assumptions are
341
included for sex, non-linear age and deprivation group with 2 DF and 3 DF are
342
used for the baseline RCS function. In order to evaluate whether assuming non-
343
proportional (subdistribution) hazards was more sensible, and is more consistent
344
with the data, a likelihood ratio test was performed. This compared the FPCIM
345
with time-dependent eﬀects to relax the proportionality assumption to the one
346
without that assumed proportional SDHs. The likelihood ratio test statistic was
347
752.94 and the associated p-value was less than 0.0001. This shows that relaxing the
348
proportionality assumption leads to a statistically signiﬁcant improvement in model
349
ﬁt. Note that this is an illustrative model and we therefore omit formal evalutation
350
of the model performance. When evaluating the model in practice, we recommend
351
conducting a sensitivity analysis, particularly in the selection of the number of
352
knots. This can be done by comparing the Akaike information criterion and the
353
Bayesian information criterion as an informal guide to selecting the appropriate
354
number of knots and covariates [6].
355
3.3 Analysis of data with conditional estimates
356
3.3.1 Cause-speciﬁc cumulative incidence functions
357
Cause-speciﬁc CIFs are presented in Figure 2 for male colorectal cancer patients.
358
The probability of dying from cancer at 10 years from diagnosis for the most de-
359
prived male patients is approximately 36.5% (95% CI: 35.5%, 37.5%) for those aged
360
50 years old at diagnosis. This slightly increases to approximately 40.5% (95% CI:
361
39.8%, 41.1%) for those aged 80 years old at diagnosis. However, the largest change
362
is in the probability of dying from other causes and CVD which have an increas-
363

````

## PDF page 21

Technical extraction; compare with original PDF page 21.

````text
Mozumder et al.
Page 20 of 47
ing contribution to the probability of dying from any cause for older male patients
364
from the most (and least) deprived groups. For instance, the probability of dying
365
from any cause by 10 years from diagnosis for the most deprived 50 year old male
366
patients at diagnosis is 53.6% of which 17.1% is due to other causes and CVD. In
367
contrast, the all-cause probability of death for the most deprived male patients aged
368
80 years old diagnosis is much higher at 92.5%. However, although the probability
369
of dying due to cancer has only increased from 36.5% to 42.5%, much of the overall
370
probability of dying is due to other causes (38.4%) and CVD (13.6%).
371
Absolute CIF diﬀerences between the most and least deprived male patients aged
372
50, 65 and 80 years old at diagnosis are presented on the third row of Figure 2.
373
This shows that, for 50 year olds, the diﬀerence between CIFs for the most and
374
least deprived groups are similar for deaths due to cancer and other causes. There
375
is very little diﬀerence between the two deprivation groups for deaths due to CVD,
376
however, this is due to a generally very low probability of death due to CVD.
377
On the other hand, for older male patients, the diﬀerence in the probability of
378
dying from other causes and CVD between the most and least deprived is larger
379
and increases over time. This leads to a greater disparity in the probability of
380
dying from other causes and CVD between the most and least deprived patients
381
compared to the diﬀerence in the probability of dying due to cancer. Furthermore,
382
after approximately 1 year from diagnosis for 65 year olds, and 2 years for 80 year
383
olds, the diﬀerence in the probability of dying due to cancer for the most deprived
384
compared to the least deprived patients reduces. This change in diﬀerence between
385
the most and least deprived is greatest for the 80 year old male patients with cancer-
386
speciﬁc CIF diﬀerence reducing from approximately 4.6% (95% CI: 4.2%, 5.0%) at
387
1 year from diagnosis to 3.2% (95% CI: 2.6%, 3.7%) by 10 years from diagnosis.
388

````

## PDF page 22

FORMULA CHECK REQUIRED: original PDF page 22.

````text
Mozumder et al.
Page 21 of 47
3.3.2 Restricted mean failure time and expected number of life-years lost due to a
389
particular cause of death
390
As discussed in Section 6, as a useful summary measure, the RMST estimate can be
391
obtained. This is equivalent to the white area of the associated stacked plot in Figure
392
2 up to t∗for a particular covariate pattern. Conversely, the area of the stacked areas
393
give an estimate of the RMFT. The area of each of the partitioned stacks for each
394
of the respective causes of death yield the expected life years lost due to cancer,
395
CVD and other causes. These are presented for the most and least deprived 50, 65
396
and 80 year old male patients in Figure 3. Each of the stacks represent the average
397
life-years lived in total and life-years lost due to a speciﬁc cause. The plots here
398
present life-years lost and lived before diﬀerent points in time up to 10 years from
399
diagnosis. However, particular interest here is in the life-years lived, or lost, before
400
10 years from diagnosis. For example, total average life-years lived before 10 years
401
from diagnosis for the most deprived 50 year old male patients is 3.99 years (95%
402
CI: 3.84 years, 4.14 years). Of the 6.01 years of the total life-years lost, 2.72 years
403
(95% CI: 2.60 years, 2.85 years) are due to cancer, 0.07 years (95% CI: 0.06 years,
404
0.09 years) are due to CVD and 1.19 (95% CI: 1.11 years, 1.28 years) due to other
405
causes.
406
Table 1 presents diﬀerences in life-years lost due to each cause of death before 10
407
years from diagnosis between the most and least deprived groups for 50, 65 and 80
408
year olds, along with their associated 95% CIs. The absolute estimates of expected
409
life-years lost for the most and least deprived patients at the individual ages are
410
also presented. This provides us with an understanding of how many additional life-
411
years most deprived patients are expected to lose due to a speciﬁc cause of death in
412
comparison to the least deprived patients. For instance, at 10 years from diagnosis,
413
50 year old male patients from the most deprived group lose an additional 0.32
414
(95% CI: 0.28, 0.36) life-years due to cancer, 0.01 (95% CI: 0.01, 0.02) life-years
415

````

## PDF page 23

Technical extraction; compare with original PDF page 23.

````text
Mozumder et al.
Page 22 of 47
due to CVD and 0.33 (95% CI: 0.30, 0.36) life-years due to CVD compared to the
416
least deprived group. For older male patients aged 80 years old, there is a greater
417
disparity in life-years lost due to CVD (0.16 life-years) and other causes (0.76 life-
418
years) between the most and least deprived.
419
3.4 Analysis of data with marginal estimates
420
When interest is in the covariate eﬀects of particular groups, for example, between
421
deprivation groups, it is useful to obtain standardised estimates as described in Sec-
422
tion 2.4.4. By marginalising over the same covariate distribution, fairer comparisons
423
can be made between particular covariate groups of interest. In this example, we
424
standardise by age and sex in order to summarise the diﬀerences in survival between
425
patients from the most and least deprived groups.
426
3.4.1 Cause-speciﬁc probability of death for the most deprived compared to the
427
least deprived
428
Figure 4 illustrates standardised CIFs stacked for each cause of death and Figure 5
429
presents absolute risk diﬀerences for each cause between the least and most deprived
430
patients. As illustrated in Figure 4, patients from the most deprived group have a
431
higher probability of dying from any cause (73.8%) compared to those from the
432
least deprived group (63.3%). However, when partitioned into the diﬀerent causes
433
of death, the diﬀerence in total mortality between the most and least deprived
434
groups is mostly due to other causes and CVD as indicated by the area proportions.
435
The cause-speciﬁc marginal risk diﬀerence between the most and least deprived are
436
presented in Figure 5 along with their respective 95% CIs. As can be seen here,
437
the largest diﬀerence in risk is due to other causes and the largest diﬀerence in risk
438
between the least and most deprived groups is due to other causes at 10 years from
439
diagnosis (6.3%; 95% CI: 5.8%, 6.9%). Generally, the disparity in the probability
440
of dying from other causes or CVD between the most and least deprived patients
441
continues to increase over follow-up time. However, the cancer-speciﬁc risk diﬀerence
442

````

## PDF page 24

FORMULA CHECK REQUIRED: original PDF page 24.

````text
Mozumder et al.
Page 23 of 47
between the most and least deprived increases only for the ﬁrst 2 years. After this
443
point, the disparity in the probability of dying due to cancer between the most and
444
least deprived begins to decrease.
445
3.4.2 Expected number of life-years lost for the most deprived compared to the
446
least deprived
447
In Figure 3, the expected life-years lost and total average life-years lived were pre-
448
sented for each cause of death before various time-points, t∗. By obtaining marginal
449
estimates through standardisation over age and sex, we can focus on speciﬁc com-
450
parisons between the least and most deprived patients. The marginal expected life-
451
years lived for each cause of death and total average life-years lived before each
452
time, t∗, are similarly illustrated in Figure 6. If t∗= 10, then we have that the
453
total average life-years lived before 10 years from diagnosis for the most deprived
454
patients is 4.39 (95% CI: 3.78, 5.00). Of the 5.61 total expected life-years lost, 3.03
455
(95% CI: 2.66, 3.46) years are lost due to cancer, 0.46 (95% CI: 0.27, 0.81) years
456
due to CVD and 2.11 (95% CI: 1.76, 2.53) years due to other causes. By obtaining
457
marginal estimates of expected life-years lost, we are able to directly compare both
458
deprivation groups and determine the additional life-years lost for patients that are
459
the most deprived standardised by age and sex. Thus, where t∗= 10, we have that
460
the additional life-years lost due to cancer, CVD and other causes before 10 years
461
from diagnosis for the most deprived patients is 0.31 (95% CI: 0.25, 0.37), 0.05 (95%
462
CI: 0.02, 0.08) and 0.44 (95% CI: 0.33, 0.54) life-years respectively.
463
4 Discussion
464
This paper presents novel estimation of RMLT and expected life-years lost from
465
within the ﬂexible parametric survival modelling framework in the presence of com-
466
peting risks. This can be done either on the CSHs or cumulative incidence scale
467
and allows easy incorporation of time-dependent eﬀects to relax the proportionality
468
assumption. These also oﬀer additional advantages over the more popular Cox PH
469

````

## PDF page 25

Technical extraction; compare with original PDF page 25.

````text
Mozumder et al.
Page 24 of 47
and Fine and Gray models [7, 5]. In particular, we illustrate how one can easily ob-
470
tain comparative predictions based on the expected number of life-years lost due to
471
a speciﬁc cause of death in addition to other useful estimands, such as absolute dif-
472
ferences in the cumulative incidence functions. A common approach for obtaining
473
marginal estimates uses inverse probability weighted estimating equations. How-
474
ever, diﬀerent estimators need to be calculated subject to whether it is of interest
475
to obtain marginal or non-marginal/conditional estimates [48, 49]. On the other
476
hand, marginal estimates using standardisation are easily obtained in addition to
477
conditional estimates within the FPM approach from a single model.
FPMs in
478
both a standard survival analysis and for competing risks data oﬀer numerous ad-
479
vantages in prediction, speciﬁcally, through its estimation of the baseline hazard
480
function using RCS and easy inclusion of time-dependent eﬀects. In spite of this, it
481
is also important to consider limitations that are often highlighted. One such limita-
482
tion is the problem of choosing the appropriate number of knots for the underlying
483
baseline hazard function using RCS, and for when including time-dependent eﬀects
484
when relaxing the proportional hazards assumption. However, a number of extensive
485
simulation studies have been carried out evaluating how many knots are required in
486
order to accurately capture (both simple and complex i.e. time-dependent) shapes
487
of the baseline hazard function. For instance, Bower et. al. [37] and Syriopoulou
488
et. al. [50] both conclude predictions are not sensitive to the choice in the num-
489
ber of knots, provided that a suﬃcient number of degrees of freedom are used. In
490
other words, too few degrees of freedom may be too simple to accurately capture
491
the eﬀect, and too many will lead to over-ﬁtting. As a guideline, 5 degrees of free-
492
dom to capture baseline eﬀects and 3 degrees of freedom for any time-dependent
493
eﬀects are suggested as a starting point. However, it is further suggested that for
494
each individual study, sensitivity analyses are carried out in order to assess model
495
ﬁt and robustness to the choice in degrees of freedom [37, 50]. Syriopoulou et. al
496

````

## PDF page 26

FORMULA CHECK REQUIRED: original PDF page 26.

````text
Mozumder et al.
Page 25 of 47
[50] also reach similar conclusions with extension to marginal model-based esti-
497
mates when obtaining predictions using standardisation. Alternatively, a penalised
498
approach for choosing the appropriate number of degrees of freedom for RCS can
499
be used [51]. The interpretation of the RMLT measure also has some notable limi-
500
tations. Although communication in terms of changes in life-years lost to clinicians
501
and patients rather than probabilities is attractive, applying an upper bound, t∗,
502
to the time interval may add some diﬃculty in understanding of the measure. This
503
is because, RMLT for an arbitrary choice of t∗can only be used to estimate the
504
average risk within a restricted time period for a group of patients. Furthermore, it
505
should be highlighted that the expected life-years lost makes comparison with an
506
immortal cohort where patients are alive for the whole interval from 0 to time t∗.
507
A similar “unrestricted” measure that do not compare to an immortal cohort can
508
be estimated within the relative survival framework based on extrapolation of the
509
excess hazard rate. This is usually referred to as the number of life years lost, or
510
the loss in expectation of life and is calculated based on a comparison of the life-
511
expectancy of cancer patients to a comparable population group who are assumed
512
to be cancer-free [52, 53, 54]. However, this relies on the assumption that this ex-
513
trapolation is appropriate which is not made for the RMLT estimate. In addition to
514
the above, due to the dependence of the interpretation of RMST on follow-up time,
515
comparison between diﬀerent studies, for example, between countries, becomes dif-
516
ﬁcult. It has also been further shown that the diﬀerence in RMST between two
517
covariate groups depends on the outcome rates within each group. Therefore, it is
518
recommended that diﬀerences in RMST, RMFT and expected number of life-years
519
lost, are reported alongside their respective survival, or cumulative incidence func-
520
tions, in order to allow comparability and to obtain the entire picture of the impact
521
of diﬀerent groups on outcome [24]. This further points to additional advantages of
522

````

## PDF page 27

FORMULA CHECK REQUIRED: original PDF page 27.

````text
Mozumder et al.
Page 26 of 47
estimation of RMFT within the ﬂexible parametric modelling framework, as these
523
additional measures are easily obtained from the same model.
524
5 Conclusions
525
The RMLT measure is presented as a useful summary measure with an attractive
526
interpretation which can aid in the analysis of competing risks data. As discussed by
527
others, it is also useful to present estimated cause-speciﬁc CIFs alongside CSHs [6,
528
34]. We propose FPMs as the chosen estimator as it allows easy estimation of various
529
estimands from a single model providing both conditional and marginal estimates.
530
Note that, although not discussed here, if appropriate confounders are adjusted for,
531
one can also infer causal eﬀects between two groups using standardisation. However,
532
one must also consider the additional complexities and issues in interpretation with
533
the inclusion of time-dependent risk-groups [44]. Furthermore, the RMLT measure
534
can be easily extended for obtaining conditional estimates, for example, the average
535
life-years lived before t∗years given survival to time t0 from diagnosis. Example
536
Stata code for the model and prediction of measures provided in this paper is
537
outlined in Appendix D.
538

````

## PDF page 28

Technical extraction; compare with original PDF page 28.

````text
Mozumder et al.
Page 27 of 47
6 List of Abbreviations
539
CSH
Cause-speciﬁc hazards
CIF
Cumulative incidence function
CI
Conﬁdence interval
CVD
Cardiovascular disease
DF
Degrees of freedom
FPM
Flexible parametric model
FPCIM
Flexible parametric cumulative incidence model
HR
Hazard ratio
LYL
Life-years lost
RCS
Restricted cubic splines
RMFT
Restricted mean failure time
RMLT
Restricted mean lifetime
RMST
Restricted mean survival time
SDH
Subdistribution hazards
SHR
Subdistribution hazard ratio
540
Declarations
541
Ethics approval and consent to participate
542
The study received ethical approval from North West - Greater Manchester East Research Ethics Committee
543
(14/NW/1449).
544
Consent for publication
545
Not applicable.
546
Availability of data and material
547
The data that support the ﬁndings of this study are available from Public Health England
548
(https://www.gov.uk/government/publications/accessing-public-health-england-data/about-the-phe-odr-and-
549
accessing-data), but restrictions apply to the availability of these data, which were used under license for the current
550
study, and so are not publicly available.
551
Competing interests
552
SIM works at Roche 0.5 WTE (working-time-equivalent). All other authors declare that they have no competing
553
interests.
554

````

## PDF page 29

FORMULA CHECK REQUIRED: original PDF page 29.

````text
Mozumder et al.
Page 28 of 47
Funding
555
This project was funded by Cancer Research UK [Grant Number C1483/A18262] and supported the research
556
presented in this article. Cancer Research UK had no role in the methods development, study design, data
557
collection, analysis and interpretation of the data, or in the writing of the article. The article processing charge for
558
open access was funded by Cancer Research UK as a member of the 2020/21 Charity Open Access Fund (COAF).
559
Author’s contributions
560
Contributions of each author to the work detailed in the manuscript are as follows. All authors, SIM, MJR and PCL,
561
equally contributed towards the conception and design, acquisition of data, and interpretation of data. Speciﬁcally,
562
SIM carried out the analysis of the data and prepared the manuscript. PCL and MJR supervised the project and
563
contributed comments and suggestions throughout. All authors were involved in the drafting and submission of this
564
research article.
565
Acknowledgements
566
Not applicable.
567
Author details
568
1Biostatistics Research Group, Department of Health Sciences, University of Leicester, University Road, LE1 7RH
569
Leicester, UK.
2Department of Medical Epidemiology and Biostatistics, Karolinska Institutet, Stockholm, Sweden.
570
References
571
1. Putter, H., Fiocco, M., Geskus, R.B.: Tutorial in biostatistics: competing risks and multi-state models.
572
Statistics in Medicine 26(11), 2389–2430 (2007). doi:10.1002/sim.2712
573
2. Geskus, R.: Data Analysis with Competing Risks and Intermediate States. CRC Press, Boca Raton (2016)
574
3. Andersen, P.K.: Decomposition of number of life years lost according to causes of death. Statistics in Medicine
575
32, 5278–85 (2013). doi:10.1002/sim.5903
576
4. Wolbers, M., Koller, M.T., Stel, V.S., Schaer, B., Jager, K.J., Leﬀondr´e, K., Heinze, G.: Competing risks
577
analyses: objectives and approaches. European Heart Journal 35(42), 2936–2941 (2014).
578
doi:10.1093/eurheartj/ehu131
579
5. Mozumder, S.I., Rutherford, M., Lambert, P.: Direct likelihood inference on the cause-speciﬁc cumulative
580
incidence function: A ﬂexible parametric regression modelling approach. Statistics in Medicine 37(1), 82–97
581
(2017). doi:10.1002/sim.7498
582
6. Lambert, P.C., Wilkes, S.R., Crowther, M.J.: Flexible parametric modelling of the cause-speciﬁc cumulative
583
incidence function. Statistics in Medicine 36(9), 1429–1446 (2016). doi:10.1002/sim.7208
584
7. Hinchliﬀe, S.R., Lambert, P.C.: Flexible parametric modelling of cause-speciﬁc hazards to estimate cumulative
585
incidence functions. BMC Medical Research Methodology 13(1) (2013). doi:10.1186/1471-2288-13-13
586
8. Putter, H., Sasako, M., Hartgrink, H.H., van de Velde, C.J.H., van Houwelingen, J.C.: Long-term survival with
587
non-proportional hazards: results from the Dutch gastric cancer trial. Stat Med 24(18), 2807–2821 (2005).
588
doi:10.1002/sim.2143
589
9. Royston, P., Parmar, M.K.B.: Flexible parametric proportional-hazards and proportional-odds models for
590
censored survival data, with application to prognostic modelling and estimation of treatment eﬀects. Statistics
591
in Medicine 21(15), 2175–2197 (2002). doi:10.1002/sim.1203
592
10. Sauerbrei, W., Royston, P., Look, M.: A new proposal for multivariable modelling of time-varying eﬀects in
593
survival data based on fractional polynomial time-transformation. Biometrical Journal 49(3), 453–473 (2007).
594
doi:10.1002/bimj.200610328. https://onlinelibrary.wiley.com/doi/pdf/10.1002/bimj.200610328
595

````

## PDF page 30

FORMULA CHECK REQUIRED: original PDF page 30.

````text
Mozumder et al.
Page 29 of 47
11. Hern´an, M.A.: The hazards of hazard ratios. Epidemiology 21(1), 13–15 (2010).
596
doi:10.1097/EDE.0b013e3181c1ea43
597
12. Belot, A., Ndiaye, A., Luque-Fernandez, M.-A., Kipourou, D.-K., Maringe, C., Rubio, F.J., Rachet, B.:
598
Summarizing and communicating on survival data according to the audience: a tutorial on diﬀerent measures
599
illustrated with population-based cancer registry data. Clinical Epidemiology Volume 11, 53–65 (2019).
600
doi:10.2147/clep.s173523
601
13. Calkins, K.L., Canan, C.E., Moore, R.D., Lesko, C.R., Lau, B.: An application of restricted mean survival time
602
in a competing risks setting: comparing time to ART initiation by injection drug use. BMC Medical Research
603
Methodology 18(1) (2018). doi:10.1186/s12874-018-0484-z
604
14. Karrison, T.: Restricted mean life with adjustment for covariates. Journal of the American Statistical
605
Association 82(400), 1169–1176 (1987). doi:10.1080/01621459.1987.10478555.
606
https://www.tandfonline.com/doi/pdf/10.1080/01621459.1987.10478555
607
15. Royston, P., Parmar, M.K.B.: The use of restricted mean survival time to estimate the treatment eﬀect in
608
randomized clinical trials when the proportional hazards assumption is in doubt. Satistics in Medicine 30(19),
609
2409–2421 (2011). doi:10.1002/sim.4274
610
16. Royston, P., Parmar, M.K.B.: Restricted mean survival time: an alternative to the hazard ratio for the design
611
and analysis of randomized trials with a time-to-event outcome. BMC Medical Research Methodology 13, 152
612
(2013). doi:10.1186/1471-2288-13-152
613
17. Uno, H., Claggett, B., Tian, L., Inoue, E., Gallo, P., Miyata, T., Schrag, D., Takeuchi, M., Uyama, Y., Zhao,
614
L., Skali, H., Solomon, S., Jacobus, S., Hughes, M., Packer, M., Wei, L.-J.: Moving beyond the hazard ratio in
615
quantifying the between-group diﬀerence in survival analysis. Journal of Clinical Oncology 32(22), 2380–2385
616
(2014). doi:10.1200/JCO.2014.55.2208
617
18. Chen, P.-Y., Tsiatis, A.A.: Causal inference on the diﬀerence of the restricted mean lifetime between two
618
groups. Biometrics 57(4), 1030–1038 (2001). doi:10.1111/j.0006-341x.2001.01030.x
619
19. Dehbi, H.-M., Royston, P., Hackshaw, A.: Life expectancy diﬀerence and life expectancy ratio: two measures of
620
treatment eﬀects in randomised trials with non-proportional hazards. BMJ, 2250 (2017).
621
doi:10.1136/bmj.j2250
622
20. Austin, P.C.: The use of propensity score methods with survival or time-to-event outcomes: reporting measures
623
of eﬀect similar to those used in randomized experiments. Statistics in Medicine 33(7), 1242–1258 (2014).
624
doi:10.1002/sim.5984. https://onlinelibrary.wiley.com/doi/pdf/10.1002/sim.5984
625
21. Austin, P.C.: An introduction to propensity score methods for reducing the eﬀects of confounding in
626
observational studies. Multivariate Behavioral Research 46(3), 399–424 (2011).
627
doi:10.1080/00273171.2011.568786. PMID: 21818162. https://doi.org/10.1080/00273171.2011.568786
628
22. Beltr´an-S´anchez, H., Preston, S.H., Canudas-Romo, V.: An integrated approach to cause-of-death analysis:
629
cause-deleted life tables and decompositions of life expectancy. Demographic Research 19, 1323–1350 (2008).
630
doi:10.4054/demres.2008.19.35
631
23. Andersen, P.K., Perme, M.P.: Pseudo-observations in survival analysis. Statistical Methods in Medical Research
632
19(1), 71–99 (2010). doi:10.1177/0962280209105020
633
24. Kloecker, D.E., Davies, M.J., Khunti, K., Zaccardi, F.: Uses and limitations of the restricted mean survival
634
time: Illustrative examples from cardiovascular outcomes and mortality trials in type 2 diabetes. Annals of
635
Internal Medicine 172(8), 541 (2020). doi:10.7326/m19-3286
636
25. Royston, P.: Flexible Parametric Survival Analysis Using Stata : Beyond the Cox Model. Stata Press, College
637
Station, TX (2011)
638

````

## PDF page 31

FORMULA CHECK REQUIRED: original PDF page 31.

````text
Mozumder et al.
Page 30 of 47
26. Lambert, P.C., Dickman, P.W., Nelson, C.P., Royston, P.: Estimating the crude probability of death due to
639
cancer and other causes using relative survival models. Stat Med 29, 885–895 (2010)
640
27. Rothman, K.: Modern Epidemiology. Wolters Kluwer Health/Lippincott Williams & Wilkins, Philadelphia
641
(2008)
642
28. Sj¨olander, A.: Regression standardization with the r package stdReg. European Journal of Epidemiology 31(6),
643
563–574 (2016). doi:10.1007/s10654-016-0157-3
644
29. Gray, R.J.: A class of k-sample tests for comparing the cumulative incidence of a competing risk. The Annals of
645
Statistics 16, 1141–1154 (1988)
646
30. Andersen, P.K., Keiding, N.: Interpretability and importance of functionals in competing risks and multistate
647
models. Statistics in Medicine 31(11-12), 1074–1088 (2012). doi:10.1002/sim.4385
648
31. Beyersmann, J., Allignol, A., Schumacher, M.: Competing Risks and Multistate Models with R. Springer, New
649
York (2012). doi:10.1007/978-1-4614-2035-4. https://doi.org/10.1007/978-1-4614-2035-4
650
32. Andersen, P.K., Geskus, R.B., de Witte, T., Putter, H.: Competing risks in epidemiology: possibilities and
651
pitfalls. International Journal of Epidemiology 41(3), 861–870 (2012). doi:10.1093/ije/dyr213
652
33. Austin, P.C., Fine, J.P.: Practical recommendations for reporting ﬁne-gray model analyses for competing risk
653
data. Statistics in Medicine 36(27), 4391–4400 (2017). doi:10.1002/sim.7501
654
34. Latouche, A., Allignol, A., Beyersmann, J., Labopin, M., Fine, J.P.: A competing risks analysis should report
655
results on all cause-speciﬁc hazards and cumulative incidence functions. Journal of Clinical Epidemiology 66(6),
656
648–653 (2013). doi:10.1016/j.jclinepi.2012.09.017
657
35. Zhao, L., Claggett, B., Tian, L., Uno, H., Pfeﬀer, M.A., Solomon, S.D., Trippa, L., Wei, L.J.: On the restricted
658
mean survival time curve in survival analysis. Biometrics 72(1), 215–221 (2015). doi:10.1111/biom.12384
659
36. Rutherford, M.J., Abel, G.A., Greenberg, D.C., Lambert, P.C., Lyratzopoulos, G.: The impact of eliminating
660
age inequalities in stage at diagnosis on breast cancer survival for older women. British Journal of Cancer 112
661
Suppl, 124–128 (2015). doi:10.1038/bjc.2015.51
662
37. Bower, H., Crowther, M.J., Rutherford, M.J., Andersson, T.M.-L., Clements, M., Liu, X.-R., Dickman, P.W.,
663
Lambert, P.C.: Capturing simple and complex time-dependent eﬀects using ﬂexible parametric survival models:
664
A simulation study. Communications in Statistics - Simulation and Computation 0(0), 1–17 (2019).
665
doi:10.1080/03610918.2019.1634201. https://doi.org/10.1080/03610918.2019.1634201
666
38. Lambert, P.C., Royston, P.: Further development of ﬂexible parametric models for survival analysis. The Stata
667
Journal: Promoting communications on statistics and Stata 9(2), 265–290 (2009).
668
doi:10.1177/1536867x0900900206
669
39. Crowther, M.J., Lambert, P.C.: A general framework for parametric survival analysis. Stat Med 33(30),
670
5280–5297 (2014). doi:10.1002/sim.6300
671
40. Young, J.G., Stensrud, M.J., Tchetgen, E.J.T., Hernn, M.A.: A causal framework for classical statistical
672
estimands in failure time settings with competing events (2018). 1806.06136
673
41. Stensrud, M.J., Aalen, J.M., Aalen, O.O., Valberg, M.: Limitations of hazard ratios in clinical trials. European
674
Heart Journal 40(17), 1378–1383 (2018). doi:10.1093/eurheartj/ehy770
675
42. Valeri, L., Chen, J.T., Garcia-Albeniz, X., Krieger, N., VanderWeele, T.J., Coull, B.A.: The role of stage at
676
diagnosis in colorectal cancer black-white survival disparities: A counterfactual causal inference approach.
677
Cancer Epidemiology Biomarkers & Prevention 25(1), 83–89 (2015). doi:10.1158/1055-9965.epi-15-0456
678
43. Gran, J.M., Lie, S.A., ˜Ayeﬂaten, I., Borgan, ˜A., Aalen, O.O.: Causal inference in multi-state models-sickness
679
absence and work for 1145 participants after work rehabilitation. BMC Public Health 15, 1082 (2015).
680
doi:10.1186/s12889-015-2408-8
681

````

## PDF page 32

FORMULA CHECK REQUIRED: original PDF page 32.

````text
Mozumder et al.
Page 31 of 47
44. von Cube, M., Schumacher, M., Wolkewitz, M.: Causal inference with multistate models—estimands and
682
estimators of the population attributable fraction. Journal of the Royal Statistical Society: Series A (Statistics
683
in Society) (2019). doi:10.1111/rssa.12486
684
45. Geskus, R.B.: Cause-speciﬁc cumulative incidence estimation and the Fine and Gray model under both left
685
truncation and right censoring. Biometrics 67(1), 39–49 (2011). doi:10.1111/j.1541-0420.2010.01420.x
686
46. Jeong, J.-H., Fine, J.P.: Parametric regression on cumulative incidence function. Biostatistics 8(2), 184–196
687
(2007). doi:10.1093/biostatistics/kxj040
688
47. Mozumder, S.I., Rutherford, M.J., Lambert, P.C.: A ﬂexible parametric competing-risks model using a direct
689
likelihood approach for the cause-speciﬁc cumulative incidence function. The Stata Journal: Promoting
690
communications on statistics and Stata 17(2), 462–489 (2017). doi:10.1177/1536867x1701700212
691
48. Schaubel, D.E., Wei, G.: Double inverse-weighted estimation of cumulative treatment eﬀects under
692
nonproportional hazards and dependent censoring. Biometrics 67(1), 29–38 (2010).
693
doi:10.1111/j.1541-0420.2010.01449.x
694
49. Zhang, M., Schaubel, D.E.: Double-robust semiparametric estimator for diﬀerences in restricted mean lifetimes
695
in observational studies. Biometrics 68(4), 999–1009 (2012)
696
50. Syriopoulou, E., Mozumder, S.I., Rutherford, M.J., Lambert, P.C.: Robustness of individual and marginal
697
model-based estimates: A sensitivity analysis of ﬂexible parametric models. Cancer Epidemiology 58, 17–24
698
(2019). doi:10.1016/j.canep.2018.10.017
699
51. Clements, M., Liu, X.-R.: Rstpm2: Smooth Survival Models, Including Generalized Survival Models. (2019). R
700
package version 1.5.1. https://CRAN.R-project.org/package=rstpm2
701
52. Andersson, T.M.-L., Dickman, P.W., Eloranta, S., Lambe, M., Lambert, P.C.: Estimating the loss in
702
expectation of life due to cancer using ﬂexible parametric survival models. Statistics in Medicine 32(30),
703
5286–5300 (2013). doi:10.1002/sim.5943
704
53. Burnet, N.G., Jeﬀeries, S.J., Benson, R.J., Hunt, D.P., Treasure, F.P.: Years of life lost (YLL) from cancer is an
705
important measure of population burden – and should be considered when allocating research funds. British
706
Journal of Cancer 92(2), 241–245 (2005). doi:10.1038/sj.bjc.6602321
707
54. Chu, P.-C., Wang, J.-D., Hwang, J.-S., Chang, Y.-Y.: Estimation of life expectancy and the expected years of
708
life lost in patients with major cancers: extrapolation of survival curves under high-censored rates. Value Health
709
11(7), 1102–1109 (2008). doi:10.1111/j.1524-4733.2008.00350.x
710
55. Abramowitz, M.: Handbook of Mathematical Functions, with Formulas, Graphs, and Mathematical Tables.
711
Dover Publications, New York (1965)
712
56. Lambert, P.C.: The estimation and modeling of cause-speciﬁc cumulative incidence functions using
713
time-dependent weights. The Stata Journal: Promoting communications on statistics and Stata 17(1), 181–207
714
(2017). doi:10.1177/1536867x1701700110
715
57. Lunn, M., McNeil, D.: Applying Cox regression to competing risks. Biometrics 51(2), 524–532 (1995)
716
Figures
717

````

## PDF page 33

FORMULA CHECK REQUIRED: original PDF page 33.

````text
Mozumder et al.
Page 32 of 47
alive
death
from cause
k = 1
death
from cause
k = 2
hcs
1 (t)
hcs
2 (t)
(a) Transitions described by the cause-
speciﬁc hazard rate. The typical compet-
ing risks scenario.
alive
or
death
from cause
k = 2
alive
or
death
from cause
k = 1
death
from cause
k = 1
death
from cause
k = 2
hsd
1 (t)
hsd
2 (t)
(b) Transitions described by the subdistri-
bution hazard rate.
Figure 1: Schematics of transitions from an initial state to one of K = 2
causes of death.
0.00
0.20
0.40
0.60
0.80
1.00
Probability of death
0
2
4
6
8
10
 
50 year olds
 
0.00
0.20
0.40
0.60
0.80
1.00
 
0
2
4
6
8
10
Years since diagnosis
65 year olds
Most deprived
0.00
0.20
0.40
0.60
0.80
1.00
 
0
2
4
6
8
10
 
80 year olds
 
0.00
0.20
0.40
0.60
0.80
1.00
Probability of death
0
2
4
6
8
10
 
50 year olds
 
0.00
0.20
0.40
0.60
0.80
1.00
 
0
2
4
6
8
10
Years since diagnosis
65 year olds
Least deprived
0.00
0.20
0.40
0.60
0.80
1.00
 
0
2
4
6
8
10
 
80 year olds
 
-0.05
0.00
0.05
0.10
0.15
CIF difference
0
2
4
6
8
10
 
50 year olds
 
-0.05
0.00
0.05
0.10
0.15
 
0
2
4
6
8
10
Years since diagnosis
65 year olds
Most - Least Deprived
-0.05
0.00
0.05
0.10
0.15
 
0
2
4
6
8
10
 
80 year olds
 
Cancer
CVD
Other causes
Figure 2: Stacked cause-speciﬁc CIFs by deprivation group and CIF
diﬀerences for male patients at speciﬁc ages.

````

## PDF page 34

Technical extraction; compare with original PDF page 34.

````text
Mozumder et al.
Page 33 of 47
0
2
4
6
8
10
 
0
2
4
6
8
10
 
0
2
4
6
8
10
 
 
50 year olds
 
0
2
4
6
8
10
 
0
2
4
6
8
10
 
0
2
4
6
8
10
Total years that can be lived
from diagnosis (t*)
65 year olds
Most deprived
0
2
4
6
8
10
Expected life-years lost/lived
0
2
4
6
8
10
 
0
2
4
6
8
10
 
 
80 year olds
 
0
2
4
6
8
10
 
0
2
4
6
8
10
 
0
2
4
6
8
10
 
 
50 year olds
 
0
2
4
6
8
10
 
0
2
4
6
8
10
 
0
2
4
6
8
10
Total years that can be lived
from diagnosis (t*)
65 year olds
Least deprived
0
2
4
6
8
10
Expected life-years lost/lived
0
2
4
6
8
10
 
0
2
4
6
8
10
 
 
80 year olds
 
Average life-years lived
Expected LYL due to other causes
Expected LYL due to CVD
Expected LYL due to cancer
Figure 3: Stacked plots of expected life-years lost partitioned by each
cause of death for male patients.
0.00
0.20
0.40
0.60
0.80
1.00
(Standardised) Probablity of death
0
2
4
6
8
10
 
Most deprived
0.00
0.20
0.40
0.60
0.80
1.00
 
0
2
4
6
8
10
 
Least deprived
Years since diagnosis
Cause-specific CIFs standardised by age and sex
Cancer
CVD
Other causes
Figure 4: Estimated cause-speciﬁc CIFs standardised by age and sex
for each deprivation group.

````

## PDF page 35

Technical extraction; compare with original PDF page 35.

````text
Mozumder et al.
Page 34 of 47
-0.04
0.00
0.04
0.08
0.12
Standardised CIF difference
(most - least deprived)
0 2 4 6 8 10
 
Cancer
-0.04
0.00
0.04
0.08
0.12
 
 
0 2 4 6 8 10
 
CVD
-0.04
0.00
0.04
0.08
0.12
 
 
0 2 4 6 8 10
 
Other causes
-0.04
0.00
0.04
0.08
0.12
 
 
0 2 4 6 8 10
 
All causes
Years since diagnosis
Figure 5: Estimated CIF diﬀerences for each cause of death standard-
ised by age and sex with 95% CIs.
0
2
4
6
8
10
Expected life-years lost/lived
0
2
4
6
8
10
 
0
2
4
6
8
10
Total years that can be lived
from diagnosis (t*)
Most deprived
0
2
4
6
8
10
Expected life-years lost/lived
0
2
4
6
8
10
 
0
2
4
6
8
10
Total years that can be lived
from diagnosis (t*)
Least deprived
Average life-years lived
Expected LYL due to other causes
Expected LYL due to CVD
Expected LYL due to cancer
Figure 6: Stacked plots of expected life-years lost for each cause of death
standardised by age and sex.

````

## PDF page 36

Technical extraction; compare with original PDF page 36.

````text
Mozumder et al.
Page 35 of 47
Tables
718
Table 1: Expected LYL for each cause for males aged 50, 65 and 80 years old at diagnosis.
Most Deprived
Least Deprived
Diﬀerence
LYL
95% LCI
95% UCI
LYL
95% LCI
95% UCI
LYL
95% LCI
95% UCI
50 Yrs Old
Cancer
2.724
[2.604,
2.848]
2.407
[2.299,
2.519]
0.317
[0.277,
0.357]
CVD
0.069
[0.055,
0.088]
0.056
[0.044,
0.071]
0.014
[0.009,
0.018]
Other causes
1.195
[1.113,
1.282]
0.864
[0.804,
0.929]
0.330
[0.300,
0.361]
65 Yrs Old
Cancer
2.654
[2.179,
3.232]
2.340
[1.913,
2.864]
0.313
[0.250,
0.377]
CVD
0.271
[0.149,
0.495]
0.219
[0.120,
0.400]
0.052
[0.019,
0.085]
Other causes
1.662
[1.285,
2.149]
1.212
[0.930,
1.580]
0.449
[0.339,
0.559]
80 Yrs Old
Cancer
3.415
[3.055,
3.818]
3.018
[2.690,
3.386]
0.397
[0.340,
0.454]
CVD
0.840
[0.468,
1.508]
0.681
[0.378,
1.228]
0.159
[0.063,
0.255]
Other causes
2.845
[2.426,
3.337]
2.120
[1.792,
2.508]
0.725
[0.618,
0.833]

````

## PDF page 37

FORMULA CHECK REQUIRED: original PDF page 37.

````text
Mozumder et al.
Page 36 of 47
Appendix A: Restricted cubic spline variables
719
Given a vector of M knots, m and a vector of M −1 parameters, γ, with M −1
degrees of freedom (df), the restricted cubic spline function, s(ln(t);γ, m), is deﬁned
as,
s(ln(t);γ, m) = γ0 + γ1z1 + · · · + γ(M−1)z(M−1)
(31)
Where z1, · · · , z(M−1) are the basis functions of the restricted cubic splines and are
deﬁned as,
z1 = ln(t)
(32)
zj = (ln(t) −mj)3
+ −φj(ln(t) −m1)3
+ −(1 −φj)(ln(t) −mM)3
+,
j = 2, · · · , M −1
where,
φj = mM −mj
mM −m1
(33)
and
(u)+ =









u,
if u > 0
0,
otherwise
(34)
Usually, M knots are placed at equally spaced centiles of the distribution of the
720
uncensored log-survival times including two boundary knots at the 0th and 100th
721
centiles.
722

````

## PDF page 38

FORMULA CHECK REQUIRED: original PDF page 38.

````text
Mozumder et al.
Page 37 of 47
Appendix B: Gaussian quadrature
723
With the general Gaussian quadrature rule, the integral of any polynomial function,
724
g(u), over the interval [−1, 1] can be evaluated. This performs best for integrals that
725
can be approximated by a polynomial function of degree 2m −1, where m is a pre-
726
determined number of points, otherwise known as nodes, or abscissae. Hence, this
727
integral can be evaluated for,
728
Z 1
−1
g(u)du =
Z 1
−1
W(u)g(u)du
(35)
where, W(u), is a known weighting function. Here, the integral, e.g. the cause-
729
speciﬁc cumulative incidence function, is calculated using Gauss-Legendre quadra-
730
ture, with W(u) = 1. With this, based on a set of pre-deﬁned number of nodes,
731
u′
i, and associated Lagrange polynomials of degree m, Pm(u), weights, w′
i, for
732
i = 1, . . . , m, are obtained such that,
733
w
′
i =
2
(1 −u
′2
i ) (P ′m(u′
i))2
(36)
and are provided by Abramowitz and Stegun [55]. Therefore, equation 35 is ap-
734
proximated by,
735
Z 1
−1
g(u)du ≈
m
X
i=1
w′
ig(u′
i)
(37)
However, for survival data, functions are evaluated over an interval [0, t]. There-
736
fore, to apply the Gaussian quadrature rule in equation 35, integrals over the interval
737
[0, t] must be changed to an interval over [−1, 1] such that,
738

````

## PDF page 39

FORMULA CHECK REQUIRED: original PDF page 39.

````text
Mozumder et al.
Page 38 of 47
Table 2: Distribution of data on key covariates included in the analysis for n = 159,022 patients
Females, n(%)
Least deprived, n(%)
Age, mean(sd)
Cancer
21 137 (43.27)
25 084 (51.35)
72.25 (10.57)
CVD
3 158 (39.54)
3 853 (48.24)
76.78 (7.96)
Other Causes
13 716 (42.71)
14 955 (46.57)
74.04 (9.64)
All Causes
38 011 (42.74)
43 892 (49.35)
73.30 (10.13)
Alive/Censored within 10 yrs
30 663 (43.76)
43 079 (61.47)
68.05 (9.97)
Total
68 974 (43.19)
86 971 (54.59)
70.99 (10.39)
Z t
0
g(u)du = t −0
2
Z 1
−1
g
t −0
2
u + t + 0
2

du
(38)
Therefore, a function evaluated at t1, . . . , t diﬀerent time-points over an interval
739
[0, t] is approximated by applying Gaussian quadrature rules with W(u) = 1 such
740
that,
741
Z tω
0
g(u)du ≈t −0
2
m
X
i=1
w′
ig
t −0
2
u′
i + t + 0
2

(39)
742
Appendix C: Additional summary statistics
743
Table 2 provide summary statistics on the distribution of key covariates of interest
744
for inclusion in analysis i.e. sex, deprivation group (least/most deprived) and age,
745
by cause of death, and in total.
746
Figure 7 represents the cause-speciﬁc cumulative incidence functions estimates
747
obtained by the non-parametric Aalen-Johansen estimator. This summarises the
748
probability of dying from each cause of death by sex and deprivation groups.
749

````

## PDF page 40

Technical extraction; compare with original PDF page 40.

````text
Mozumder et al.
Page 39 of 47
0.00
0.10
0.20
0.30
0.40
0.50
Probability of death
0
2
4
6
8
10
Time since diagnosis (years)
Least deprived male patients
0.00
0.10
0.20
0.30
0.40
0.50
Probability of death
0
2
4
6
8
10
Time since diagnosis (years)
Most deprived male patients
0.00
0.10
0.20
0.30
0.40
0.50
Probability of death
0
2
4
6
8
10
Time since diagnosis (years)
Least deprived female patients
0.00
0.10
0.20
0.30
0.40
0.50
Probability of death
0
2
4
6
8
10
Time since diagnosis (years)
Most deprived female patients
Cancer
CVD
Other
Figure 7: Cause-speciﬁc cumulative incidence functions (CIFs)
Aalen-Johansen estimates for each cause of death.
Figure 8 illustrates the all-cause survival probabilities obtained by the non-
750
parametric Kaplan-Meier estimator. This summarises the all-cause probability of
751
survival by sex and deprivation groups.
752
0.00
0.10
0.20
0.30
0.40
0.50
0.60
0.70
0.80
0.90
1.00
Probability of survival
 
 
Males (Most deprived)        
     At-risk
Censored
       Died
Males (Least deprived)      
     At-risk
Censored
       Died
Females (Most deprived)        
     At-risk
Censored
       Died
Females (Least deprived)      
     At-risk
Censored
       Died
0
 
 
41527
0
0
 
50004
0
0
 
31916
0
0
 
37981
0
0
2
 
 
19971
4039
17517
 
27857
6128
16019
 
15390
2871
13655
 
21064
4273
12644
4
 Time since diagnosis (years)
 
12795
6816
21916
 
18349
10776
20879
 
10440
4910
16566
 
14457
7680
15844
6
 
 
8592
8980
23955
 
12485
14352
23167
 
7384
6577
17955
 
10264
10470
17247
8
 
 
5869
10567
25091
 
8582
17012
24410
 
5242
7887
18787
 
7220
12622
18139
10
 
 
3964
11828
25735
 
5580
19231
25193
 
3612
8990
19314
 
4853
14433
18695
Males - Most Deprived
Males - Least Deprived
Females - Most Deprived
Females - Least Deprived
Kaplan-Meier All-cause Survival
Figure 8: All-cause Kaplan-Meier survival probabilities by sex and
deprivation groups.

````

## PDF page 41

FORMULA CHECK REQUIRED: original PDF page 41.

````text
Mozumder et al.
Page 40 of 47
Appendix D: Stata code for obtaining predictions
753
This appendix outlines Stata code used to obtain predictions presented in the paper.
754
Some user-deﬁned Stata commands are required which can be installed from the
755
Boston College Statistical Software Components (SSC) archive by calling,
756
ssc install

command

757
The following must be installed before running the code:
758
• stpm2: To ﬁt the ﬂexible parametric models described in Section 2.3.
759
• rcsgen: To generate the restricted cubic spline functions.
760
• stcrprep: To restructure data and calculate time-dependent censoring
761
weights in order to ﬁt models on the subdistribution hazards scale using
762
standard Stata commands.
763
To obtain marginal (and non-marginal) estimates using standardisation, the
764
standsurv command must be installed. This will be released on SSC soon, however,
765
in the meantime, it can be installed by running,
766
net from https://www.pclambert.net/downloads/standsurv
767
D.0.1 Preparing the data for analysis
768
To prepare the data for a survival analysis in Stata, we must ﬁrst run the stset
769
command. We identify the variable that records survival time (in days), exit2, the
770
indicator variable for cause of death, cod, where death from cancer = 1, CVD = 2
771
and other causes = 3 and ﬁnally the variable for date of diagnosis, dx. The scale
772
option is used to transform the survival time into years from days and we use the
773
exit option to restrict follow-up time to 10 years from diagnosis and censor those
774
still alive at 2014. In order to ensure that the death indicator, d, generated after
775
stset matches the death indicator for cause of death, we create a new cause of
776
death indicator, cod2, so that those who die either after 10 years from diagnosis
777
or 2014 are administratively censored. Finally, to generate restricted cubic spline
778

````

## PDF page 42

FORMULA CHECK REQUIRED: original PDF page 42.

````text
Mozumder et al.
Page 41 of 47
variables for the non-linear eﬀect of age centred at 45 years old at diagnosis, we use
779
rcsgen. For 3 degrees of freedom, 3 new age spline variables are created, rcsage1
780
−rcsage3, and we store knot positions and matrix for orthogonalization which
781
are required for post-estimation predictions at speciﬁc ages.
782
stset exit2, failure(cod=1,2,3) id(id) scale(365.25) origin(dx) ///
783
>
exit(time min(dx + 365.25*10.01,mdy(12,31,2013)))
784
785
//must ensure that those that die after follow-up time
786
//
are administratively censored
787
gen cod2 = cond(_d==0,0,cod)
788
789
//center non-linear age (rcsage) at 45 years old
790
rcsgen age, gen(rcsage) df(3) orthog center(45)
791
//store knot positions in global macro
792
global knots `r(knots)´
793
//save matrix for orthogonalization
794
matrix Rage = r(R)
795
To restructure the data and calculate the time-dependent censoring weights so
796
that we may ﬁt a model on the subdistribution hazards scale, we use stcrprep[56].
797
Here, we specify wtstpm2 to estimate the censoring distribution using a Royston-
798
Parmar ﬂexible parametric model with covariates included in the censcov option.
799
The data is restructured based on the variable failcode, which splits the data
800
according to the cause of interest. This is used to ﬁt identify for which cause the
801
model is to be ﬁtted for. For clarity, we create dummy variables for each of the causes
802
of death from failcode and generate cancer, cvd and other. Another indicator
803
variable, event, is also created to identify at which split time interval, or row, death
804
(from any cause) is observed for that patient. To incorporate the calculated weights
805
from stcrprep, we must stset the data again with tstart and tstop. These are
806
also provided by stcrprep and give the times at which an individual starts and
807
stops being at risk.
808
stcrprep, events(cod2) keep(age mostdep sex rcsage?) trans(1 2 3) ///
809
>
wtstpm2 censcov(mostdep sex rcsage?) every(1)
810
811

````

## PDF page 43

FORMULA CHECK REQUIRED: original PDF page 43.

````text
Mozumder et al.
Page 42 of 47
gen event = cod2 == failcode
812
813
stset tstop [iw=weight_c], failure(event) enter(tstart) noshow
814
815
tab failcode, gen(cause)
816
rename cause1 _cancer
817
rename cause2 _cvd
818
rename cause3 _other
819
D.0.2 Model
820
The model described in Section 2.3 can be ﬁtted in two ways after preparing the
821
data. We can either ﬁt separate models for each of the causes of death, or ﬁt a single
822
model to cancer, CVD and other causes simultaneously. Here, we demonstrate for
823
the latter to make illustration of the code for obtaining predictions post-estimation
824
easier. However, in order to ﬁt the equivalent single model with coeﬃcients com-
825
parable to the models ﬁtted individually to each of the causes of death, the knot
826
locations on the cause-speciﬁc survival time distributions must be stored. These are
827
stored in global macros for each of the causes of death.
828
global knotstvc_opt
829
global bknotstvc_opt
830
831
foreach cause in cancer other cvd {
832
2.
global lnbhknots_`cause´
833
3. }
834
835
foreach cause in cancer other cvd {
836
2.
stpm2 mostdep sex rcsage? if _`cause´==1, df(3) ///
837
>
tvc(mostdep sex rcsage?) dftvc(2) scale(h) eform
838
3.
global bhknots_`cause´ `e(bhknots)´
839
4.
global boundknots_`cause´ `e(boundary_knots)´
840
5.
foreach cov in mostdep sex rcsage1 rcsage2 rcsage3 {
841
6.
global knotstvc_opt ${knotstvc_opt} ///
842
>
`cov´_`cause´ `e(tvcknots_`cov´)´
843
7.
}
844
8.
global knotstvc_opt ${knotstvc_opt} _`cause´ ${bhknots_`cause´}
845
9.
global bknotstvc_opt ${bknotstvc_opt} _`cause´ ${boundknots_`cause´}
846
10. }
847

````

## PDF page 44

Technical extraction; compare with original PDF page 44.

````text
Mozumder et al.
Page 43 of 47
Here we deﬁne a global macro of the list of covariates to be included in the single
848
model. As the data is stacked, interactions need to be created between the covari-
849
ates and the indicator variable for each cause of death. See Lunn and McNeil[57]
850
for further details. The baseline coeﬃcient, i.e. the constant in the cause-speciﬁc
851
model, is calculated in
cancer,
cvd and
other. We therefore ﬁt a model for
852
each of the causes of death simultaneously without a constant using nocons and
853
the baseline splines using rcsbaseoff. Instead, the baseline splines are speciﬁed as
854
time-dependent splines for the coeﬃcient that corresponds to the constant in its
855
respective model for that particular cause of death. These were stored in the global
856
macro bknotstvc opt. Since knots are speciﬁed according to the time scale, rather
857
than the log-time scale, the knscale(time) option is used.
858
global covlist
859
global covlist_tvc
860
861
foreach cause in cancer cvd other {
862
2.
global covlist $covlist _`cause´
863
3.
global covlist_tvc $covlist_tvc _`cause´
864
4.
foreach cov in mostdep sex rcsage1 rcsage2 rcsage3 {
865
5.
gen `cov´_`cause´ = `cov´*_`cause´
866
6.
global covlist $covlist `cov´_`cause´
867
7.
global covlist_tvc $covlist_tvc `cov´_`cause´
868
8.
}
869
9. }
870
871
di "$covlist"
872
_cancer mostdep_cancer sex_cancer rcsage1_cancer rcsage2_cancer rcsage3_cancer
873
_cvd mostdep_cvd sex_cvd rcsage1_cvd rcsage2_cvd rcsage3_cvd
874
_other mostdep_other sex_other rcsage1_other rcsage2_other rcsage3_other
875
876
stpm2 $covlist ///
877
>
, scale(h) tvc($covlist_tvc) knotstvc(${knotstvc_opt}) ///
878
>
bknotstvc(${bknotstvc_opt}) knscale(time) rcsbaseoff eform nocons
879
D.0.3 Predictions
880
Although standsurv was written for obtaining marginalised predictions, it can also
881
be used to obtain non-marginalised estimates. This is done by simply specifying the
882

````

## PDF page 45

FORMULA CHECK REQUIRED: original PDF page 45.

````text
Mozumder et al.
Page 44 of 47
entire covariate pattern so that the predictions are not averaged over any covariate
883
distribution. To obtain predictions at a speciﬁc age, we need to calculate the spline
884
variables at that particular age centred at 45 years old with the same knot locations
885
and projection matrix as before. The spline variables are stored in the local macros
886
c1, c2 and c3. An example is given below when the cause of interest is cancer and
887
we want to make comparisons between the most and least deprived male patients
888
aged either 50, 65, or 80 years old at diagnosis.
889
foreach age in 50 65 80 {
890
2.
rcsgen, scalar(`age´) knots($knots) rmatrix(Rage) gen(c) center(45)
891
892
3.
global cancer_mostdep_`age´_male sex_cancer 0 sex_cvd 0 sex_other 0 ///
893
>
mostdep_cancer 1
mostdep_cvd 0
mostdep_other 0
///
894
>
rcsage1_cancer `=c1´ rcsage2_cancer `=c2´ rcsage3_cancer `=c3´ ///
895
>
rcsage1_other 0 rcsage2_other 0 rcsage3_other 0 ///
896
>
rcsage1_cvd 0 rcsage2_cvd 0 rcsage3_cvd 0 _cancer 1 _cvd 0 _other 0
897
898
4.
global cancer_leastdep_`age´_male sex_cancer 0 sex_cvd 0 sex_other 0 ///
899
>
mostdep_cancer 0 mostdep_cvd 0 mostdep_other 0 ///
900
>
rcsage1_cancer `=c1´ rcsage2_cancer `=c2´ rcsage3_cancer `=c3´ ///
901
>
rcsage1_other 0 rcsage2_other 0 rcsage3_other 0 ///
902
>
rcsage1_cvd 0 rcsage2_cvd 0 rcsage3_cvd 0 _cancer 1 _cvd 0 _other 0
903
5. }
904
As we do not average over each observation, we must tell standsurv to only take
905
the ﬁrst observation in the stacked data to calculate non-marginalised predictions.
906
This is done using if
n == 1. The failure option is used to obtain the cumulative
907
incidence functions that is speciﬁed in each at option. To calculate the diﬀerence
908
between at1 and at2, we use contrast(difference).
909
range tempt 0 10 101
910
911
foreach age in 50 65 80 {
912
2.
foreach cause in cancer other cvd {
913
3.
standsurv if _n==1, at1(${`cause´_leastdep_`age´_male}) ///
914
>
at2(${`cause´_mostdep_`age´_male}) ///
915
>
atvars(Fage`age´_`cause´_male_least CIF_`age´_`cause´_male_most) ///
916
>
contrastvar(CIF_`age´_`cause´_male_diff) ///
917
>
contrast(difference) failure timevar(tempt) ci
918

````

## PDF page 46

Technical extraction; compare with original PDF page 46.

````text
Mozumder et al.
Page 45 of 47
4.
}
919
5. }
920
Since we are making predictions at particular covariate patterns for each of the
921
causes separately, specifying rmft gives us estimates of the expected life-years lost
922
due to a particular cause of death. To calculate RMLT, we need to take the sum
923
of all of the at options, where the expected life-years lost due to cancer, CVD and
924
other causes is speciﬁed in each. We do this by creating our own contrast in a user-
925
deﬁned mata function which can be called in the option userfunction. An example
926
of this is also given below.
927
foreach age in 50 65 80 {
928
2.
foreach cause in cancer cvd other {
929
3.
standsurv if _n==1, at1(${`cause´_leastdep_`age´_male}) ///
930
>
at2(${`cause´_mostdep_`age´_male}) ///
931
>
atvars(LYL_`age´_`cause´_leastdep LYL_`age´_`cause´_mostdep) ///
932
>
contrast(difference) contrastvar(LYL_`cause´`age´_diff) ///
933
>
rmft timevar(tempt) ci
934
4.
}
935
5. }
936
937
mata mata clear
938
mata
939
function RMFT(at) {
940
2.
return((at[1]:+at[2]:+at[3]))
941
3. }
942
943
end
944
945
946
In order to obtain marginalised estimates, in each at option, only the covariate
947
pattern for the group of interest need to be given. For the covariate distribution
948
that we want to average over, as we have created interactions between the covariates
949
and the causes of death, these must be mapped to each covariate e.g. sex cancer
950
= sex. The others are excluded from the at option for the other causes of death. In
951
this case, because we want to average over covariates that we wish to standardise
952
by, we need to identify the row for each patient in the stacked data that corresponds
953

````

## PDF page 47

Technical extraction; compare with original PDF page 47.

````text
Mozumder et al.
Page 46 of 47
to the failure time of that individual. This is done by creating the indicator variable
954
first and using it as an if condition in standsurv. As before, we give an example
955
for specifying macros for use in the at options for deaths due to cancer.
956
global cancer_mostdep_stand sex_cvd 0 sex_other 0 sex_cancer = sex ///
957
>
mostdep_cancer 1
mostdep_cvd 0 mostdep_other 0 ///
958
>
rcsage1_cancer = rcsage1 rcsage2_cancer = rcsage2 rcsage3_cancer = rcsage3 ///
959
>
rcsage1_other 0 rcsage2_other 0 rcsage3_other 0 ///
960
>
rcsage1_cvd 0 rcsage2_cvd 0 rcsage3_cvd 0 ///
961
>
_cancer 1 _cvd 0 _other 1
962
963
global cancer_leastdep_stand sex_cvd 0 sex_other 0 sex_cancer = sex ///
964
>
mostdep_cancer 0
mostdep_cvd 0 mostdep_other 0 ///
965
>
rcsage1_cancer = rcsage1 rcsage2_cancer = rcsage2 rcsage3_cancer = rcsage3 ///
966
>
rcsage1_other 0 rcsage2_other 0 rcsage3_other 0 ///
967
>
rcsage1_cvd 0 rcsage2_cvd 0 rcsage3_cvd 0 ///
968
>
_cancer 1 _cvd 0 _other 1
969
970
bysort failcode id (_t): gen first = _n==1
971
The cause-speciﬁc CIF diﬀerences are thus calculated as follows,
972
foreach cause in cancer other cvd {
973
2.
standsurv if first, at1(${`cause´_leastdep_stand}) ///
974
>
at2(${`cause´_mostdep_stand}) ///
975
>
atvars(Fstand_`cause´_least Fstand_`cause´_most) ///
976
>
contrast(difference) contrastvars(Fdiff_`cause´) ///
977
>
failure timevar(tempt) ci
978
3. }
979
As highlighted above, we can write user-functions to deﬁne our own contrasts.
980
Below is an example for when interest is in calculating the diﬀerence in RMLT
981
between the most and least deprived patients.
982
mata mata clear
983
mata
984
: function RMFTdiff(at) {
985
2.
return((at[1]:+at[2]:+at[3]) :- (at[4]:+at[5]:+at[6]))
986
3. }
987
988
: end
989
990
standsurv if first, at1(${cancer_mostdep_stand}) ///
991

````

## PDF page 48

Technical extraction; compare with original PDF page 48.

````text
Mozumder et al.
Page 47 of 47
>
at2(${cvd_mostdep_stand}) ///
992
>
at3(${other_mostdep_stand}) ///
993
>
at4(${cancer_leastdep_stand}) ///
994
>
at5(${cvd_leastdep_stand}) ///
995
>
at6(${other_leastdep_stand}) ///
996
>
atvars(LYLcancer_stand_mostdep LYLcvd_stand_mostdep ///
997
>
LYLother_stand_mostdep LYLcancer_stand_leastdep ///
998
>
LYLcvd_stand_leastdep LYLother_stand_leastdep) ///
999
>
userfunction(RMFTdiff) userfunctionvar(RMFT_diff) ///
1000
>
failure timevar(tempt) ci
1001

````

## PDF page 49

Technical extraction; compare with original PDF page 49.

````text
Figures
Figure 1
Schematics of transitions from an initial state to one of K = 2 causes of death.

````

## PDF page 50

Technical extraction; compare with original PDF page 50.

````text
Figure 2
Stacked cause-speci c CIFs by deprivation group and CIF dif ferences for male patients at speci c ages.

````

## PDF page 51

Technical extraction; compare with original PDF page 51.

````text
Figure 3
Stacked plots of expected life-years lost partitioned by each cause of death for male patients.

````

## PDF page 52

Technical extraction; compare with original PDF page 52.

````text
Figure 4
Estimated cause-speci c CIFs standardised by age and sex for each deprivation group.

````

## PDF page 53

Technical extraction; compare with original PDF page 53.

````text
Figure 5
Estimated CIF dif frences for each cause of death standard- ised by age and sex with 95% CIs.

````

## PDF page 54

Technical extraction; compare with original PDF page 54.

````text
Figure 6
Stacked plots of expected life-years lost for each cause of death standardised by age and sex.
Supplementary Files
This is a list of supplementary ¦les associated with this preprint. Click to download.
stset.log.tex
stcrprep.log.tex
bmcart.cls
bmcmathphys.bst
rmftstand2.log.tex
stata.sty
model2.log.tex

````

## PDF page 55

Technical extraction; compare with original PDF page 55.

````text
rmftage.log.tex
covstand2.log.tex
model.log.tex
covage.log.tex
cifstand2.log.tex
cifage.log.tex
codeappendix.tex
refs02Feb19.bib

````

