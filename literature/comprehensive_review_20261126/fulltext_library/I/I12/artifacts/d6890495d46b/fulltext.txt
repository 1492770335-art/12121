# Restricted mean survival time: an alternative to the hazard ratio for the design and analysis of randomized trials with a time-to-event outcome

Source: [original.xml](original.xml).

PAGINATION UNAVAILABLE: this original JATS XML does not supply a verified PDF page map. Sections and original formula markup are preserved; no PDF pages are invented. TeX-math and MathML blocks below are original XML content, not reconstructed equations. Formula images remain unresolved and are flagged.





### Background


Designs and analyses of clinical trials with a time-to-event outcome almost invariably rely on the hazard ratio to estimate the treatment effect and implicitly, therefore, on the proportional hazards assumption. However, the results of some recent trials indicate that there is no guarantee that the assumption will hold. Here, we describe the use of the restricted mean survival time as a possible alternative tool in the design and analysis of these trials.




### Methods


The restricted mean is a measure of average survival from time 0 to a specified time point, and may be estimated as the area under the survival curve up to that point. We consider the design of such trials according to a wide range of possible survival distributions in the control and research arm(s). The distributions are conveniently defined as piecewise exponential distributions and can be specified through piecewise constant hazards and time-fixed or time-dependent hazard ratios. Such designs can embody proportional or non-proportional hazards of the treatment effect.




### Results


We demonstrate the use of restricted mean survival time and a test of the difference in restricted means as an alternative measure of treatment effect. We support the approach through the results of simulation studies and in real examples from several cancer trials. We illustrate the required sample size under proportional and non-proportional hazards, also the significance level and power of the proposed test. Values are compared with those from the standard approach which utilizes the logrank test.




### Conclusions


We conclude that the hazard ratio cannot be recommended as a general measure of the treatment effect in a randomized controlled trial, nor is it always appropriate when designing a trial. Restricted mean survival time may provide a practical way forward and deserves greater attention.





### Background


Most randomized controlled trials (RCTs) with a time-to-event outcome are designed and analyzed with a target hazard ratio (HR) for the treatment effect in mind. By convention, the HR is usually taken as the hazard function in the research arm divided by that in the control arm, with values < 1 representing a ‘positive’ treatment effect. In advanced cancers with a mortality outcome, for example, a popular choice of target HR is 0.75. This implies a reduction of 25 percent in the instantaneous mortality rate at all times after randomization. According to a standard sample size calculation based on the logrank test, about 510 events are needed to attain power 90 percent to detect such a treatment effect at a two-sided significance level of 5 percent in a trial with equal allocation to control and research arms.

For a single HR to make scientific sense, we must assume that proportional hazards (PH) of the treatment effect holds, at least approximately. We have argued previously [1] that when the PH assumption fails, it is misleading to report the treatment effect through the estimated HR, since it depends on follow-up time. A simple example of departure from PH occurs when one group is assigned to immediate surgical treatment and the other to medical treatment. Suppose time of randomisation is the origin of the survival time. When surgery increases short-term mortality but confers long-term benefit on the survivors – a reasonable alternative hypothesis – PH does not apply and the HR is a misleading and inappropriate summary.

More technically, we are unconvinced by papers such as Schemper et al [2] where an overall estimate of the HR is regarded as an average of time-dependent HRs over the event times, nor by proposed variants based on different and arbitrary weighting schemes. The main issue is that an average HR is uninterpretable. Under PH, for example, the HR can usefully be applied to the survival function in the control arm to obtain an impression of the survival curve in the research arm. When PH is breached, this property no longer holds. Furthermore, the HR depends on the follow-up time.

It has become apparent in some recently reported trials, e.g. IPASS [3] and ICON7 [4], that gross breaches of the PH assumption can and do occur—even to the extent of observing crossing survival curves, where a local estimate of the log HR changes sign over time. Non-PH may be due to different biological modes of action of the treatments being compared, or as identified in IPASS, to the presence of differentially responsive sub-populations.

As noted before [1], we are dissatisfied with the HR as a universal summary measure. For example, even when PH holds, the HR is not as meaningful clinically as some type of difference in average survival times or proportions at a fixed time-point, obscuring the absolute difference between the treatments and failing to convey the clinical value of a treatment. (By ‘survival time’ we mean generic time to event, for whatever event is of interest.) Furthermore, early stopping rules that assume PH can generate inappropriate decisions if the HR later changes substantially. Also, no single summary of HR or risk difference can adequately describe cases in which the treatment effect changes in direction as follow-up increases.

In our earlier paper [1], we suggested an approach to the analysis of an RCT in which the PH assumption is breached. We proposed to estimate and report the restricted mean survival time (RMST) [5], expressing the treatment effect as the difference in RMST between the randomized arms at a suitable follow-up time, t∗. We constructed confidence intervals through the standard error of the difference in RMST. Further experience with the RMST measure in a larger number of trials has given us the impression that when the PH assumption is approximately satisfied, the test of the null hypothesis based on RMST difference often has operating characteristics similar to the logrank test. Specifically, the significance level and power of the two tests appear to be similar.

An advantage of the RMST is that it is valid under any distribution of the time to event in the treatment groups, of which PH models are a (small) sub-class. Furthermore, it is readily interpretable as the ‘life expectancy’ between randomization (t = 0) and a particular time horizon (t = t∗). Owing to the current dominance of the HR and its presumed time independence, trial reports often ignore the possibility of non-PH and typically place little emphasis on the extent of follow-up, which should be a key aspect of the trial design and analysis. For example, a treatment effect can exhibit PH in the short term but non-PH over a longer period (e.g. the GOG111 trial, see Reference [1]). It is particularly important to ensure sufficient follow-up when there may be good biological or other reasons to expect the effect of a treatment to vary over time. The primary estimate of the RMST is specifically aligned to a chosen t∗ and this must be made explicit. Obviously, though, as part of the analysis, the treatment effect can be explored over a range of alternative t∗ values.

In a previous report [6], we described the implementation of a general method, Assessment of Resources for Trials or ART, for designing a trial allowing for possible non-uniform accrual rates, non-proportional hazards, loss to follow-up and cross-over of patients between treatment arms. With ART, the treatment effect is assessed using the logrank test, irrespective of whether the design assumes PH or not. A central tool in the approach is the realistic representation of the survival function in each trial arm as a piecewise exponential distribution. Recruitment and follow-up time is divided into several ‘periods’ of equal duration. Recruitment is carried out during a subset of these periods, and all recruited patients are followed up for the remaining periods. The accumulated data are analyzed when the necessary numbers of events have accrued. In addition to the usual signficance level and power, the researcher specifies the survival function in the control and research arm at the ends of selected periods. The piecewise constant hazard function is inferred from these values. At its simplest, the method accepts a single exponential distribution in each of the control and research arms, characterized by a single, constant hazard or equivalently by the median time to event. Considerable flexibility is available with a piecewise exponential model, allowing a wide range of survival distributions appropriate to the disease in question to be accommodated.

In this paper, we consider replacing a logrank-based sample size calculation and presentation of results with one based on RMST and its difference between trial arms. The difference in RMST is determined by the survival functions specified in the control and research arms through piecewise exponential distributions, exactly as in ART. Part of the paper is concerned with technical details of the calculation of RMST and its standard error under a piecewise exponential model. The results are needed in the sample size calculations. We report a small simulation study comparing the significance level and power of the logrank and RMST tests under a piecewise exponential model with non-proportional or proportional hazards, incorporating staggered entry of patients and varying length of recruitment and follow-up.

In the section ‘Restricted mean survival time (RMST)’, we describe the RMST and the corresponding standard deviation (RSDST) in general terms and specifically for a piecewise exponential distribution. Section ‘A strategy for design and analysis of clinical trials discusses our proposed strategy for trial design and analysis. We describe how to do a sample size calculation for a trial using the RMST difference. We also consider the choice of suitable values of t∗ at the design and analysis stages. We also suggest an approach to assessing maturity (readiness for analysis) of accumulating trial data according to the RMST method. Section ‘Examples’ includes limited simulation studies of the significance level and power of hypothesis tests based on the RMST difference under non-PH and PH. We provide examples in real trials. Section ‘Further issues’ makes a qualitative comparison between various measures of a treatment effect and describes results of RMST and logrank analyses in four cancer trials. We finish with a discussion and our conclusions.




### Methods




### Restricted mean survival time (RMST)




### 
Definition of RMST



The restricted mean survival time, μ say, of a random variable T is the mean of the survival time X = min(T,t∗) limited to some horizon t∗ > 0. It equals the area under the survival curve S (t) from t = 0 to t = t∗[5,7]: 


(1)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M1" overflow="scroll"><ns0:mo>μ</ns0:mo><ns0:mo>=</ns0:mo><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:mi>E</ns0:mi><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mtext>min</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>T</ns0:mi><ns0:mo>,</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext></ns0:math>
````



When T is years to death, we may think of μ as the ‘ t∗-year life expectancy’. In a two-arm clinical trial with survival functions S0(t) and S1(t) in the control and research arms, respectively, the difference in RMST between arms, Δ, is given by 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M2" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mo>Δ</ns0:mo></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mo>-</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd><ns0:mspace width="2em" /></ns0:mtd></ns0:mtr></ns0:mtable></ns0:math>
````



i.e. Δ is the area between the survival curves.




### 
Restricted standard deviation of survival time (RSDST)



To compute the variance, var (X), of the restricted survival time X, we need E (X2): 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M3" overflow="scroll"><ns0:mrow><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>T</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>|</ns0:mo><ns0:mi>T</ns0:mi><ns0:mo>≤</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mo>Pr</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>T</ns0:mi><ns0:mo>≤</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mo>+</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>Pr</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>T</ns0:mi><ns0:mo>&gt;</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:math>
````



 In terms of the survival function S (t), we have Pr(T ≤ t∗) = 1-S(t∗) and 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M4" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>T</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>|</ns0:mo><ns0:mi>T</ns0:mi><ns0:mo>≤</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mo>Pr</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>T</ns0:mi><ns0:mo>≤</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mi>f</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mspace width="1em" /><ns0:mo>-</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mn>2</ns0:mn><ns0:mi>t</ns0:mi><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````



where f(.) is the density function of T. Hence 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M5" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mspace width="-15.0pt" /><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mo>-</ns0:mo><ns0:mn>2</ns0:mn><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mspace width="0.6em" /><ns0:mi>t</ns0:mi><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mo>+</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>-</ns0:mo><ns0:mn>2</ns0:mn><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mtext mathvariant="italic">tdt</ns0:mtext><ns0:mo>+</ns0:mo><ns0:mn>2</ns0:mn><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mtext mathvariant="italic">tS</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mtext mathvariant="italic">tS</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````



so that 


(2)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M6" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mtext>RSDST</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>=</ns0:mo><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mtext mathvariant="italic">tS</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mspace width="2em" /></ns0:mtd></ns0:mtr></ns0:mtable></ns0:math>
````



The restricted standard deviation (RSDST) is 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M7" overflow="scroll"><ns0:msqrt><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:msqrt></ns0:math>
````
.




### 
RMST and RSDST for the piecewise exponential distribution



Analytic results for RMST and RSDST are available when the survival time has a piecewise exponential distribution. The integrals required in (2) are tractable. Details of the calculations and the results are given in the Appendix: RMST and RSDST for a piecewise exponential distribution.






### A strategy for design and analysis of clinical trials




### The ART approach


The ART approach to trial design [6,8] is based on specifying (log) HRs and testing their difference from zero with the logrank test. It may be used to design a trial with two or more parallel groups and a time-to-event outcome. ART allows the user to specify a recruitment phase with a predefined pattern of staggered patient entry and a follow-up phase at the end of recruitment, a standard feature of sample size calculations for such trials. Furthermore, among other advanced features, ART supports designs with non-proportional hazards, which are specified according to period-specific, time-dependent HRs.

The main design characterstics of ART are as follows: 

1. Power and significance level for a logrank test of the treatment effect (e.g. 0.9 and 0.05);

2. A number K of notional study periods of equal length in suitable units of real (calendar) time, over which the trial is intended to run;

3. Recruitment of patients over the first K1 periods and follow-up of all accrued patients over the remaining K2 periods, with K1 > 0, K2 ≥ 0, such that K = K1 + K2;

4. A relative weight for the number of patients expected to be recruited in each period (since recruitment often starts slowly and picks up as the trial’s existence becomes better known);

5. Control-arm survival function specified at some or all of the K periods. An alternative would be to specify the survival in the research arm at the same time points;

6. Target HR(s) under the alternative hypothesis. Hazard ratios may be specified as a single overall value (proportional hazards assumption) or for individual periods (time-dependent HR). An alternative to specifying HRs would be to provide the survival function in the research arm as well as in the control arm.

The end result is a complete definition of piecewise exponential models for the data expected under the null and alternative hypotheses. The null hypothesis is that the HRs are all equal to 1. The alternative hypothesis is that they are as given (implicitly or explicitly) in step 6 above.

The ART methodology for a two-arm trial assumes that a logrank test of the null hypothesis is to be used even if the trial has been designed with a time-dependent HR. Although not explicit, the implication is that the main trial result would be reported as the HR with a confidence interval (CI). As we have already discussed, we should not necessarily accept a single HR as an adequate trial summary statistic, particularly when the trial was designed with an expectation of non-proportional hazards.

In what follows, we suggest replacing the ART sample size calculation and presentation of results with one based on RMST and testing the RMST difference between arms. Other than the need to define a suitable time horizon t∗ for RMST evaluation, the components of the design are as described above. We present the details in the next section.




### Sample size for RMST difference


The basis of our approach is the familiar comparison of two means using an unpaired t test. Suppose we are sampling at random from the distribution of a positively bound random variable, T. We sample n0 patients from the control arm and n1 patients from the research arm. The total sample size for the trial is n = n0 + n1. Define the allocation ratio as r = n1/n0.

Suppose the means and variances of T in the control and research arms are μ0, 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M8" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:math>
````
 and μ1, 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M9" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:math>
````
, respectively. The null hypothesis is H0 : μ0 = μ1, with 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M10" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:math>
````
 and 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M11" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:math>
````
 unspecified. The alternative hypothesis is H1 : μ0 ≠ μ1. Suppose we wish to test the null hypothesis with power ω at two-sided significance level α. Let Δ = 0 and Δ = μ1 - μ0 ≠ 0 be the difference in RMST under H0 and H1, respectively. Following, for example, Reference [9] (p. 332), the required sample size in the control arm is 


(3)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M12" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mo>α</ns0:mo><ns0:mo>/</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>ω</ns0:mo></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>/</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>+</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msup><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfrac></ns0:math>
````



hence the total sample size is 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M13" overflow="scroll"><ns0:mrow><ns0:mi>n</ns0:mi><ns0:mo>=</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mo>α</ns0:mo><ns0:mo>/</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>ω</ns0:mo></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>/</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>+</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msup><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:math>
````



 where z
p
 = Φ-1 (p) is the inverse standard normal distribution function at probability p. An approximate (typically, conservative) sample size estimate, assuming that 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M14" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>≃</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:math>
````
, is given by 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M15" overflow="scroll"><ns0:mrow><ns0:mi>n</ns0:mi><ns0:mo>≃</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mo>α</ns0:mo><ns0:mo>/</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>ω</ns0:mo></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>/</ns0:mo><ns0:msup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:math>
````



 We see that n is a minimum when r = 1 (equal allocation) and n increases substantially for larger or smaller r (unequal allocation).

The power, ω, is given by 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M16" overflow="scroll"><ns0:mrow><ns0:mo>ω</ns0:mo><ns0:mo>=</ns0:mo><ns0:mo>Φ</ns0:mo><ns0:mfenced open="{" close="}"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>+</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msup><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>/</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mo>α</ns0:mo><ns0:mo>/</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:math>
````



In the standard case, the approach would be to estimate 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M17" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mspace width="2.5em" /><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1"><ns0:mspace width="0.5em" /><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mtext>SE</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac><ns0:mo>+</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````



from the data, and test 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M18" overflow="scroll"><ns0:mrow><ns0:mi>z</ns0:mi><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mtext>SE</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:math>
````



 against a Student’s t or (in large samples) a normal reference distribution. The usual assumption is that the response variable is normally distributed 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M19" overflow="scroll"><ns0:mi>T</ns0:mi><ns0:mo>∼</ns0:mo><ns0:mi>N</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>,</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow></ns0:mfenced></ns0:math>
````
 in arm j (j = 0,1). The RMST context differs from this in the following ways: 

1. The response variable is the restricted time to event, X = min(T,t∗). Due to the right truncation of T, the distribution of X is strongly non-normal;

2. In trials with a time-to-event outcome, T is almost invariably positively skew anyway, sometimes considerably so;

3. Right-censoring of T affects estimation of 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M20" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:math>
````
 and SE
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M21" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
.

Our strategy is to take the standard case described above as our starting point for RMST sample size calculations based on the ART design assumptions, and modify it as necessary. To complete the design, we then addresss the important question of selecting t∗.




### Standard error of RMST in the ART setting


Given the ART workup, the sample size calculation given in eqn. (3) implicitly requires the variance of RMST under the piecewise exponential model around which ART is based. Consider a sample T1,…,T
m
 with no censoring before t∗ (there could be censoring after t∗). The restricted times to event, X
i 
= min(T
i
,t∗) (i = 1,…,m), are an independent, identically distributed sample from some distribution. Notionally, the RMST μ may be estimated as the sample mean 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M22" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>m</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msup><ns0:munderover><ns0:mrow><ns0:mo mathsize="big">∑</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>i</ns0:mi><ns0:mo>=</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>m</ns0:mi></ns0:mrow></ns0:munderover><ns0:msub><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>i</ns0:mi></ns0:mrow></ns0:msub></ns0:math>
````
, and its standard error, SE
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M23" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
, as RSDST/
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M24" overflow="scroll"><ns0:msqrt><ns0:mrow><ns0:mi>m</ns0:mi></ns0:mrow></ns0:msqrt></ns0:math>
````
, where RSDST is the sample standard deviation.

With censoring of some observations before t∗, the RMST is estimated by integration as in (1) and the RSDST as 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M25" overflow="scroll"><ns0:msqrt><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:msqrt></ns0:math>
````
 in (2). We no longer expect RSDST/
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M26" overflow="scroll"><ns0:msqrt><ns0:mrow><ns0:mi>m</ns0:mi></ns0:mrow></ns0:msqrt></ns0:math>
````
 to be an accurate estimate of SE
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M27" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
, since it does not reflect the increased uncertainty associated with censoring.

Consider a restricted sample X1,…,X
m
 with μ = E (X) estimated by integration. (Note that m bears no relation to the number of patients required in a trial.) Write 


(4)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M28" overflow="scroll"><ns0:mtext>SE</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:mo>ϕ</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mtext>RSDST</ns0:mtext></ns0:mrow><ns0:mrow><ns0:msqrt><ns0:mrow><ns0:mi>m</ns0:mi></ns0:mrow></ns0:msqrt></ns0:mrow></ns0:mfrac></ns0:math>
````



where ϕ is some positive scaling factor. Clearly ϕ ≃ 1 for samples without censoring before t∗, but otherwise ϕ is unknown. In exploring simulated trial data with staggered entry of patients and a fixed follow-up time, we found that ϕ was very close to 1 when patients were recruited over a relatively short period and followed up for a reasonably long length of time. However, ϕ could increase substantially when recruitment was over a longer period with shorter follow-up. This finding accords with intuition, since more censoring and hence greater uncertainty is expected in the latter case.

In general, ϕ in (4) must be estimated under a known (hypothesized) piecewise exponential model. We do this by Monte Carlo simulation, as follows. First, we draw a large random sample of m time-to-event observations from the piecewise exponential distribution of interest and determine 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M29" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mo>ϕ</ns0:mo><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msqrt><ns0:mrow><ns0:mi>m</ns0:mi></ns0:mrow></ns0:msqrt><ns0:mtext>SE</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mtext>RSDST</ns0:mtext></ns0:mrow></ns0:mfrac></ns0:mtd></ns0:mtr></ns0:mtable></ns0:math>
````



SE
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M30" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
 is estimated by the delta method within a flexible parametric model [10,11], using the stpm2 program [12] for Stata. Estimation with a flexible parametric model is more stable than directly with a piecewise exponential model, since sparsely populated time intervals between knots can cause fitting difficulties for the latter model. Note that RSDST is a known function of the design parameters (see Appendix: RMST and RSDST for a piecewise exponential distribution) and does not need to be estimated by simulation.

Given estimates of ϕ
j
 (j = 0,1), we can determine the 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M31" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:math>
````
 in eqn. (3) through the expression 


(5)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M32" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>ϕ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mtext>RSDST</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:math>
````



All of ϕ
j
, 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M33" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:math>
````
 and n have ‘Monte Carlo error’ due to the simulation. To quantify Monte Carlo error, the simulation is repeated with M independent samples. In each of the M samples, n is determined from (3) via (5). The SE of n over the M samples is 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M34" overflow="scroll"><ns0:msqrt><ns0:mrow><ns0:mo>(</ns0:mo><ns0:mtext>sample variance of the</ns0:mtext><ns0:mi>n</ns0:mi><ns0:mtext>’s</ns0:mtext><ns0:mo>)</ns0:mo><ns0:mo>/</ns0:mo><ns0:mi>M</ns0:mi></ns0:mrow></ns0:msqrt></ns0:math>
````
. We choose M such that the SE of n is sufficiently small for practical purposes. Following exploration (not reported) with different choices of m and M, we suggest taking m = 10000 and M  =50 as initial defaults, but m and M can be adjusted to suit circumstances.

Note that the only components of the sample size calculation that change with recruitment (K1) and follow-up (K2) times are the ϕ
j
. An illustration of this point is given in the section ‘Examples’.

We next describe the estimation of 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M35" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:math>
````
 and SE
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M36" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
 from trial data.




### Estimation of 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M37" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:math>
````
 and SE 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M38" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
 in trial data


As we discussed in our previous paper [1], several methods of estimating RMST are available, including direct integration of Kaplan-Meier survival curves, a jackknife method, and flexible parametric regression modelling [10,11]. We pointed out that the direct integration of Kaplan-Meier curves may be unreliable. The jackknife method has the advantage of being non-parametric but the drawback of being relatively slow to compute. Its slowness makes it cumbersome when simulation with many replicates is needed. We therefore prefer the third method, flexible parametric modelling, which is fast and efficient.

In the context of a randomized trial, it is essential that the estimation method be predefined, i.e. not requiring the analyst to make data-dependent modelling decisions with the actual trial data. Flexible parametric models are suitable tools for the purpose, because, for example, a cumulative hazards model with 3 d.f. fitted to each treatment arm separately appears to give an adequate fit to a wide variety of survival curves. Proportional hazards is not assumed. This particular model is assumed subsequently in the present paper for both estimation and simulation purposes.

For a given trial dataset, SE
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M39" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:math>
````
 (j = 0,1) may be calculated by the delta method separately in each arm. Hence 


(6)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M40" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub><ns0:mspace width="2em" /></ns0:mtd></ns0:mtr></ns0:mtable></ns0:math>
````




(7)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M41" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mtext>SE</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msqrt><ns0:mrow><ns0:mtext>SE</ns0:mtext><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>+</ns0:mo><ns0:mtext>SE</ns0:mtext><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:msqrt><ns0:mspace width="2em" /></ns0:mtd></ns0:mtr></ns0:mtable></ns0:math>
````



A test the null hypothesis Δ = 0 is made by comparing 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M42" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover><ns0:mo>/</ns0:mo><ns0:mtext mathvariant="italic">SE</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
 with a standard normal distribution.




### Choice of t∗ for the design


In our earlier paper [1], we suggested reporting the RMST and its difference between trial arms, with a CI. For such an analysis, a time (t∗) for calculation of the RMST needs to be specified. The ART-based approach to trial design defines a recruitment time (K1) and minimum follow-up time (K2) sufficient for recruitment of patients and estimation of their group survival curves over the follow-up period of clinical interest. We suggest determining the design value, 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M43" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
, as the t∗ which (approximately) minimizes the required sample size, n, given K1, K2 and the remaining parameters. This may be done by varying t∗ over the range K2 (the shortest follow-up time for any patient) to K1 + K2 (the maximum possible follow-up time of any patient within the design), and computing n by simulation, as described above.




### Choice of t∗ for analysis and assessment of data maturity


When it comes to the analysis of the trial data, for various reasons the precise data structure that is obtained may differ from the design under which 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M44" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 was calculated. For example, the assumed survival distribution may be wrong, or the pattern of recruitment and follow-up may be at variance from that expected. To maximize power, we determine t∗ for the final analysis of the data. We call this value 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M45" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
. We also address the question of how to assess data maturity, i.e. determining when the accumulating data are mature enough for the final analysis of the treatment effect.

In a trial designed under proportional hazards of the treatment effect and analysed using a logrank test, the required total number of events, e, is usually taken as the effective sample size. The reason is because, to a good approximation, var (logHR) is proportional to 1/e, so that e is a measure of the amount of information in the data. The cumulative data in such a trial is ‘ready to analyse’ when the observed number of events reaches e. Monitoring the trial for maturity is then merely a matter of updating the data periodically and counting the number of events.

How should be we apply the principle of monitoring for maturity to trials designed with an RMST outcome? The estimated variance of the treatment effect provides a way forward. Combining (3) with (6), the following relationship holds for a sample size of n under the alternative hypothesis that Δ ≠ 0 is the difference in RMST at some given t∗: 


(8)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M46" overflow="scroll"><ns0:mi>z</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfrac></ns0:math>
````



where zz = z
ω
 + z 1  -α/2. Note that var
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M47" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
 is the variance of the estimated RMST difference at the given t∗, whereas Δ is a design value. The planned power is achieved when var
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M48" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:mo>≤</ns0:mo><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mo>/</ns0:mo><ns0:mi>z</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:math>
````
. To determine if the trial data are mature enough to analyse, we effectively compare the variance of 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M49" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:math>
````
 estimated from the current data with the target value, Δ2/zz2. Let us define the ‘percent maturity’ of the accumulating data as 


(9)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M50" overflow="scroll"><ns0:mtext mathvariant="italic">pmat</ns0:mtext><ns0:mo>=</ns0:mo><ns0:mn>100</ns0:mn><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:mi>z</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfrac></ns0:math>
````



where var
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M51" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:math>
````
 is the estimated variance of the RMST difference in the current data. As more data accumulate, pmat increases; when it reaches 100%, the data are ready for analysis (under the assumptions of the design).

Alternatively, we can invert eqn. (8) and calculate the power, ωcurr, for the current data under the design assumptions as 


(10)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M52" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mo>ω</ns0:mo></ns0:mrow><ns0:mrow><ns0:mtext>curr</ns0:mtext></ns0:mrow></ns0:msub><ns0:mo>=</ns0:mo><ns0:mo>Φ</ns0:mo><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:msqrt><ns0:mrow><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:msqrt><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>z</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:mo>α</ns0:mo><ns0:mo>/</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:math>
````



Sometimes, for reasons of confidentiality of the accumulating trial data, it is desirable to estimate data maturity or power ignoring information on possible treatment effects. In the absence of censoring in (0,t∗), we have 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M53" overflow="scroll"><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac><ns0:mo>+</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:math>
````



 where 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M54" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:math>
````
 is approximately equal to the squared RSDST at t∗ in treatment group j and n
j
 is the sample size (j = 0,1). In the absence of treatment information, we make the simplifying assumption that 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M55" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:math>
````
. This could be regarded as an assumption under the null hypothesis of Δ = 0, since there is then no difference between treatments. We have 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M56" overflow="scroll"><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac><ns0:mo>+</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:math>
````



 By elementary algebra 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M57" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac><ns0:mo>+</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow></ns0:mfrac><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mo>+</ns0:mo><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow></ns0:mfrac><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msqrt><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow></ns0:msqrt><ns0:mo>+</ns0:mo><ns0:msqrt><ns0:mrow><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:msqrt></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````



Hence 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M58" overflow="scroll"><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:mi>n</ns0:mi></ns0:mrow></ns0:mfrac><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msqrt><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow></ns0:msqrt><ns0:mo>+</ns0:mo><ns0:msqrt><ns0:mrow><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:msqrt></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:math>
````



 Taking σ2/n as an estimate of var
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M59" overflow="scroll"><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:mo>,</ns0:mo></ns0:math>
````
 the variance of RMST for the entire dataset, we have 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M60" overflow="scroll"><ns0:mrow><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:mo>≃</ns0:mo><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow></ns0:mfenced><ns0:msup><ns0:mrow><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msqrt><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow></ns0:msqrt><ns0:mo>+</ns0:mo><ns0:msqrt><ns0:mrow><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>r</ns0:mi></ns0:mrow></ns0:mfrac></ns0:mrow></ns0:msqrt></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:math>
````



Finally, to apply the maturity analysis we must find 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M61" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 This is done by varying t∗ over a grid and finding the value that maximizes (9) or (10). If 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M62" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 exceeds tmax, the largest uncensored time to event in the data, to avoid extrapolation of RMST estimates from a flexible parametric model, we suggest limiting it to tmax.





### Results




### Examples




### 
Proportional and non-proportional hazards designs



As a source of illustration, we constructed designs with PH and non-PH treatment effects based on updated data from the GOG111 trial in advanced ovarian cancer [13]. The overall survival probabilities in the control arm at the end of years 1 through 8 post-randomization were estimated to be 0.771, 0.523, 0.342, 0.236, 0.172, 0.130, 0.100, 0.078, respectively, with corresponding control-arm hazards of 0.264, 0.385, 0.425, 0.372, 0.320, 0.280, 0.261, 0.245. The hazard ratios (research arm/control arm) were estimated to be 0.71 under PH and 0.53, 0.66, 0.74, 0.81, 0.87, 0.93, 0.96, 1.00 under non-PH.




### Determining 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M63" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````



We consider determining 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M64" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 for the PH and non-PH designs just described. As an example, suppose K1 = 5 yr, K2 = 3 yr. We vary 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M65" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 in small steps (0.2 yr) over the interval (K2,K1 + K2) = (3,8) yr and compute n according to eqn. (3). Figure 1 shows the resulting sample sizes for both designs. We see that t∗ and the design assumptions (PH or non-PH) both influence the sample size quite markedly. To minimize the sample size, the PH design requires a 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M66" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 close to the maximum available follow-up time (8 yr), whereas the non-PH design needs a much smaller 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M67" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
. The 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M68" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 values are 7.5 and 4.3 yr for the PH and non-PH cases, respectively, with corresponding sample sizes of 461 and 326.
Figure 1

Example of sample sizes as a function of the time horizon t∗ for PH (solid lines) and non-PH (dashed lines) trial designs. The designs assume recruitment over K1 = 5 yr and follow-up over K2 = 3 yr.

[ORIGINAL IMAGE / POSSIBLE FORMULA: 1471-2288-13-152-1.jpg; not reconstructed]
It is apparent that the sample size does not change much for t∗ near 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M69" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
. For example, for t∗ within ±1 yr of 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M70" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
, the sample size is never larger than 9 more than the minimum, which is of no practical importance. This flexibility allows the analyst to select a preferred 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M71" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 within a reasonably wide range without incurring a large sample size penalty.




### 
Comparing RMST and logrank based sample sizes



We turn to a comparison between the RMST and logrank approaches to sample size calculation. We used the ART software [8] for Stata to compute the logrank sample sizes and the numbers of events for both approaches. We used specially written Stata software that, given (K1,K2) and the other ART design parameters, finds 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M72" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 by varying t∗ over a user-defined grid as in the previous section. It calculates the sample size by simulation according to the methods described in sections ‘Sample size for RMST difference’ and ‘Standard error of RMST in the ART setting’. The value of 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M73" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 and the corresponding sample size were determined by smoothing the (t∗,n) relationship using a second degree fractional polynomial and calculating the nadir. In some cases the sample size curve over the range t∗ ∈ (3,8) yr was monotonic decreasing; we then took the optimal sample size to be for 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M74" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup><ns0:mo>=</ns0:mo><ns0:mn>8</ns0:mn></ns0:math>
````
 yr.

We investigated the impact of choices of K1 and K2 on the 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M75" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 and n values, now for K1 = 1(1)7 and K2 = 8 - K1. Table 1 gives the resulting sample sizes and numbers of events for the PH and non-PH designs. For the PH designs, the sample size is similar to that for the logrank test. A 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M76" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 at or near the maximum permissible is needed. For the non-PH designs,
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M77" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 is around 4 yr; a markedly lower sample size is needed with the RMST approach than the logrank.

Table 1

Sample size calculations for hypothetical trials with proportional or non-proportional hazards of the treatment effect

RecruitFollow-upPH designs Non-PH designs   RMSTLogrankRMSTLogrank(
K

1
, yr)(
K

2
, yr)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M78" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi mathvariant="bold">t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext mathvariant="bold">des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo mathvariant="bold">∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````

n
Events
n
Events
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M79" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi mathvariant="bold">t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext mathvariant="bold">des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo mathvariant="bold">∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````

n
Events
n
Events1784243684153594.43242864123642684263634223594.53242814063513584323604313594.43252753993374484403564443594.5325266393322537.54633604623594.3328258389305627.04883594903594.1332245391288716.75323595333603.8351237406273
See the text for further details.





### 
Operating characteristics



We perform a small simulation study to check the power and significance level of the proposed test of RMST difference. The set-up is similar to that described in the section ‘Comparing RMST and logrank based sample sizes’, except that we vary the recruitment period (K1) over 1, 3, 5 and 7 yr, with K2 = 8 - K1. Five thousand replicates are simulated for each combination of recruitment period and null hypothesis (true or false). As before, the times to event are simulated according to a piecewise exponential distribution with staggered entry of patients at a uniform rate and RMST analysis performed with t∗ = K1/2 + K2 yr. The sample size is designed to give the test of the RMST difference power of 90 percent to reject the null hypothesis at the 5 percent level. The power and significance level of the logrank test in the non-PH and PH scenarios are also studied without altering the sample size.

The results are shown in Table 2. Two standard errors of an estimated probability of 90 and 5 percent are 0.85 and 0.62 percent, respectively. The significance levels are close to nominal for the logrank and RMST tests in both scenarios. The RMST test maintains power close to its nominal 90 percent level under both non-PH and PH. As expected from the sample sizes given in Table 1, the logrank test under non-PH is underpowered compared with planned levels. Results in Table 1 suggest that the two tests may have similar power under PH; the logrank test is slightly the more powerful.

Table 2

Operating characteristics of the test of RMST difference

ModelRecruitFollow-up
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M80" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi mathvariant="bold">t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext mathvariant="bold">des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo mathvariant="bold">∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
SampleRMST testLogrank test (
K

1
, yr)(
K

2
, yr) sizePowerSig. levelPowerSig. levelPH17842489.64.690.74.6 35843290.14.690.34.7 537.546390.95.190.74.9 716.753290.55.490.35.1Non-PH174.432489.44.581.24.8 354.432590.05.083.25.2 534.332889.54.384.44.5 713.835191.64.883.55.5
Significance level and power are presented as percentages. Sample size calculations are for hypothetical trials with proportional hazards (PH) or non-proportional hazards (non-PH) of the treatment effect. Results are given for the RMST test and for the logrank test using the RMST designed sample sizes. Details are as given in Table 1.





### 
Examples of design based on the SORCE trial in primary kidney cancer



As a further example,we compare RMST- and logrank-based designs for SORCE, an ongoing trial in primary renal carcinoma coordinated by the MRC Clinical Trials Unit. See http://www.controlled-trials.com/ISRCTN38934710 for a summary of the trial. Only patients with an initial intermediate or poor prognosis according to the Leibovich risk score [14] are eligible. Following surgery for their kidney cancer, patients are randomized into three groups: placebo tablets, one year of treatment with tablets containing the molecular targeted agent sorafenib, or 3 years of sorafenib. We focus on the primary analysis (‘Question 1’) as defined in the trial protocol, namely ‘Does at least one year of treatment with sorafenib increase disease-free survival (DFS) compared with placebo?’.

Patients are randomized in a ratio of 2:3:3 to placebo or to the two sorafenib arms. To answer Question 1, the two sorafenib arms are combined, giving an allocation ratio of r = 6/2 = 3. The sample size calculation was based on the logrank test. It assumed PH with target HR = 0.75, K1 = 5 years’ recruitment with staggered patient entry and K2 = 3 years’ follow-up of all recruited patients. Power was set to ω = 0.9 at a two-sided significance level of α = 0.05. Assuming no dropout, therefore individual patients are followed up for at least 3 years and at most 8 years, depending on when they entered the trial. DFS probabilities at 1, 3, 5, 7, 10 and 13 years after surgery were estimated from values provided by Leibovich et al [14] (see Table 3). The logrank-based sample size for this design is N = 1656 (608 events). The possibility of increasing power by following up patients for up to K2 = 8 years, giving a total trial time of up to K = 13 years, was also envisaged.

Table 3

Design parameters for the SORCE trial

YearTrial planHypothetical DFS prob.HR (PH)HR (non-PH)10.7790.750.6530.6350.750.7550.5760.750.8570.5320.750.9100.4880.751.0130.4540.751.0
“DFS prob.” denotes survival probabilities for the disease-free survival outcome. PH and non-PH refer respectively to designs with (as per protocol) and without (hypothetical) proportional hazards of the treatment effect.


To be clear, we remind the reader that t∗ is measured in analysis time, with each patient’s date of entry as the origin (t = 0). By contrast, K1 and K2 are measured in trial time, i.e. in calendar time whose origins are the dates of randomization of the first and last patient, respectively.

For both logrank and RMST-based sample size calculations, we fix K1 = 5 and illustrate what happens with K2 = 3 yr (as per protocol) and with K2 = 5, 8 yr. We find 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M81" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 as described in the section ‘Determining 

````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M82" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````

’.

We also investigate sample size for an alternative design based on non-PH of the treatment effect. The right-hand column of Table 3 shows a hypothetical but plausible pattern of time-dependent HRs, representing an initially fairly large treatment effect (HR = 0.65) which disappears (HR = 1.0) by t = 10 years. The sample sizes for the PH and non-PH designs are shown in Table 4.

Table 4

Total sample size (
N 
) and 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M83" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi mathvariant="bold">t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext mathvariant="bold">des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo mathvariant="bold">∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 for hypothetical trials based on the design of SORCE

Design
K

1

K

2


````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M84" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi mathvariant="bold">t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext mathvariant="bold">des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo mathvariant="bold">∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````

LogrankRMST (yr)(yr)(yr)
n
Events
n
EventsPH53816566081790658 551015096101627658 581313786121488662non-PH535.416216021280476 556.018037511266528 588.020089341488692
Recruitment (K1) is assumed to be for 5 years in all the designs, whereas follow-up (K2) is varied over 3, 5 and 8 years.


Several features of Table 4 stand out. Not surprisingly, the sample size depends strongly on the assumed magnitude and pattern of the treatment effect. For the PH designs, the sample size is about 8 percent larger with the RMST approach than with the logrank approach. For the non-PH designs, the sample size is 27 to 42 percent larger for the logrank than the RMST approach. The RMST approach has a considerable advantage in the latter case, presumably because as the HR gets closer to 1, the power of the logrank test diminishes.




### 
Example of maturity analysis in the MRC RE04 trial



As an example of determining whether trial data are ready for an analysis of RMST, we consider the MRC RE04 trial in metastatic kidney cancer [15]. Following an increase in planned sample size after the start of the trial, the design involved randomization to two arms with allocation ratio r = 1 and a target hazard ratio of 0.8 for the research arm (triple therapy) compared with the control arm (interferon- α only). The main outcome measure was all-cause mortality (time to death for any reason). Based on a previous kidney cancer trial (MRC RE01), median overall survival time in the control arm was expected to be one year. The sample size required for power 90% at a two-sided signficance level of 5% was set according to ART methodology at 1100 patients and 845 events (i.e. deaths). This assumed the survival curve from the previous trial, and K1 = 4 yr, K2 = 1 yr. The sample size and events for an RMST design based on the same assumptions are 1108 patients and 848 events, with 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M85" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 found to be 4.0 yr.

Accrual of patients was actually stopped when 1006 patients had been recruited. The trial opened for recruitment in April 2001 and closed in August 2006. The data were frozen for final analysis in September 2008, at which point 691 events (deaths) had been recorded.

Since the accrual and follow-up phases were longer than originally planned, for an RMST-based maturity assessment we consider a wider range of candidates for 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M86" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 corresponding to K1 = 2 yr, K2 = 5 yr. We estimate the survival curve from the data, ignoring treatment differences. Figure 2 shows the maturity statistic pmat and the power for t∗ ∈ (2,7) yr. The best choice of 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M87" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 is 5.4 yr, at which time the maturity pmat = 83 percent and the power is about 0.84. The design value, t
des 
n∗ = 4.0 yr, is a little low as a candidate for t
final 
n∗, but may still be a reasonable option.
Figure 2

Percent maturity (pmat) and power curves as a function of t∗ for the RE04 trial. Vertical lines show 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M88" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
.

[ORIGINAL IMAGE / POSSIBLE FORMULA: 1471-2288-13-152-2.jpg; not reconstructed]





### Further issues




### Comparing measures of the treatment effect


Usually, the HR and its CI are reported, and often, the median survival time and/or estimated survival probabilities at fixed time points are also presented. We propose the use of RMST and statistics derived from it, as just discussed. The ‘absolute’ difference in survival (ADS) at a given time point t∗ is defined as 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M89" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:math>
````
, where, 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M90" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>.</ns0:mi></ns0:mrow></ns0:mfenced></ns0:math>
````
 and 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M91" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>.</ns0:mi></ns0:mrow></ns0:mfenced></ns0:math>
````
 are the estimated survival functions in the control and research arms, respectively. How do these four measures compare on several criteria? A list of criteria and our assessments are given in Table 5. The criteria are framed in such a way that we regard ‘yes’ as advantageous and ‘no’ as disadvantageous.

Table 5

Comparison of four measures of the treatment effect in a trial

CriterionMeasure  log HRMedian

a

RMST

a

ADS

a

1. Is easily interpreted noyesyesyes2. Does not assume proportional hazards noyesyesyes3. Reflects entire survival history yesnoyesno4. Is a measure of survival time noyesyesno5. Can be used with all models noyesyesyes6. Can be calculated in any dataset yesnoyesyes7. Does not require a time point to be specified yesyesnono8. Does not change with extended follow-up noyesyesyes9. Is routinely associated with a clinically meaningful time point nonoyesyes
aThe measure is the difference in the given statistic between trial arms. ADS = absolute difference in survival.


In general, difficulties with the HR and with taking the number of events as an index of the ‘maturity’ of the trial data are the following: 

1. In a very large trial, the targeted number of events can occur relatively ‘early’. However, the resulting survival functions may not be a reasonable reflection of the difference between the treatment arms over a clinically relevant time span. In an extreme case, researchers planning trials could use this approach to produce a positive result from early survival experiences, ignoring the possible later evolution of the treatment effect.

2. The same number of events may be seen in a large trial with short follow-up or a small trial with long follow-up. However, these trials are not ‘equivalent’ in the information they bear, nor in the clinical lessons that may be learned from them.

3. There are many examples where results appear to ‘change’ over time. In reality, of course, the change is an illusion caused by ignoring the time element in reporting the results.

In Table 5, RMST emerges favourably since the only ‘box’ that it fails to ‘tick’ is criterion 7. However, it may be argued that the need to define a reference time point is in fact an advantage, since it explicitly incorporates the time dimension of the trial into the results, which is often neglected as just discussed. Neither the median nor the HR do this. This aspect is reinforced in criterion 9.

The absolute difference in survival and the difference in median survival time, although often quoted, are weak because they represent only a ‘snapshot’ of the difference in survival functions. They tell us little about the previous or subsequent survival experiences. For example, the survival curves could cross at the median or at some other t∗ but still show a substantial difference in RMST at 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M92" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
.




### Examples of RMST in analysis of several trials


We compare RMST and Cox/logrank analysis in a further four MRC cancer trials: ASTEC in endometrial cancer [16] (surgery vs. standard therapy randomization), BA06 in advanced bladder cancer [17], ICON4 in ovarian cancer [18] and OE02 in oesophageal cancer [19]. In all cases, the outcome is time to death from any cause (overall survival). We have chosen these particular trials because the estimated treatment effect is approximately the same (around HR = 0.85), yet they have widely varying mortality rates. Note that in the ASTEC trial, mortality in the research arm is actually non-significantly worse than in the control arm. Table 6 presents some results.

Table 6

HR, RMST and derived statistics on survival for four randomized controlled trials in various cancer sites conducted by the Medical Research Council

StatisticASTECBA06ICON4OE02t max (yr)6.86.76.410.8

````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M93" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````

 (yr)6.16.76.310.8S (t∗)0.720.390.0820.11N (events 
a
)1394 (188)962 (483)749 (417)802 (655)Design HR0.750.750.750.75Achieved HR1.160.850.820.85(Cox model)    P-value for HR0.30.070.040.03(logrank test)    P-value for non-PH0.060.70.60.1(G-T test 
b
)    RMST in control5.393.692.462.68arm (
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M94" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub></ns0:math>
````
)    RMST in research5.284.022.793.13arm (
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M95" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:math>
````
)    Diff. 

````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M96" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover><ns0:mo>=</ns0:mo></ns0:math>
````

-0.11 (0.10)0.33 (0.18)0.33 (0.17)0.46 (0.26)

````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M97" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mover accent="false"><ns0:mrow><ns0:mo>μ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msub></ns0:math>
````

 (SE)    P-value for0.30.070.050.08

````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M98" overflow="scroll"><ns0:mover accent="false"><ns0:mrow><ns0:mo>Δ</ns0:mo></ns0:mrow><ns0:mo>^</ns0:mo></ns0:mover></ns0:math>
````

 (RMST test)    P-value for0.070.40.70.04non-PH 
c
    
See text for details.

aEvents occurring in the interval (0,t*).

bGrambsch-Therneau test

cFrom a flexible parametric hazards model with a time-dependent treatment effect.


The logrank and RMST tests of the treatment effect give P-values with a similar interpretation. A possible exception is OE02, for which the RMST test at t∗ = 10.8 yr is not significant at the 5 percent level whereas the Cox test is significant (P = 0.03). However, there is evidence of a non-PH treatment effect in this trial. A hazards model with a time-dependent treatment effect suggests that the hazard ratio is below 1 near t = 0 and tends to approximately 1 over time.

Further insight into the behaviour of the logrank and RMST tests is provided by Figure 3. We varied t∗ in 30 equal-sized steps between 1 and 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M99" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 years. The smooth dashed lines are for the RMST test without truncation (right-censoring) of the data. The corresponding estimates of RMST were obtained at the different values of t∗ from a flexible parametric model applied to the entire dataset. The other two lines are for the data truncated at each value of t∗. The (signed) z-statistic is the log HR divided by its SE from a Cox model, and the RMST difference divided by its SE from the RMST analyses. The z-statistics for the three methods are broadly in agreement in the ASTEC, BA06 and ICON4 trials. For OE02, however, the z-statistic from the Cox model is fairly constant over time, whereas for the RMST tests it diminishes steadily. Presumably the behaviour of the RMST tests is due to the non-PH pattern of the treatment effect in OE02. For the Cox test, the effect of an increasing number of events (effective sample size) may counterbalance the effect of the HR reducing over time.
Figure 3

Evolution over time (
t

∗
) of 
z 
-statistics for RMST (truncated, solid lines; non-truncated, short dashed lines) and Cox (truncated, long dashed lines) tests in four randomized controlled trials in cancer.

[ORIGINAL IMAGE / POSSIBLE FORMULA: 1471-2288-13-152-3.jpg; not reconstructed]
A notable feature of Figure 3 is the instability of the z-statistic (hence P-value) for the tests in the truncated data, which seems greater for the Cox test. The ‘significance’ of the tests is subject to the play of chance.





### Discussion


The main advantages of our proposed method are interpretability of the RMST difference from a clinical perspective as loss of life expectancy (when the outcome of interest is mortality), and robustness of the estimator to the proportional hazards assumption. Perhaps the main disadvantages are the complexity of properly assessing data maturity (readiness for analysis) and the dependence of the test statistic on t∗. One could envisage a temptation to choose t∗ so as to obtain the ‘most significant’ result. An analysis option (not yet explored in detail) to circumvent this problem could be to derive an alternative test statistic as the minimum z-value for the test of RMST difference over a sensible range of values of t∗. The correct significance level of this statistic could be estimated using permutation-test methodology applied to the treatment assignment variable. However, such an analysis would be secondary to the main analysis involving a prespecified t∗.

Sample size calculations are potentially fragile, since they depend strongly on assumptions. This is seen in the SORCE example (Table 3) and in other examples. The problem is not specific to the PH assumption. It is hard to know in advance whether or not PH is a likely feature of the data to come, and if not, what a plausible pattern of time-dependent HRs might look like. In some cases, it may be reasonable to assume that a treatment effect dwindles over time, for example with treatments that are given for a relatively short period after randomization, than for it to remain constant. However, HR patterns between treatments whose modes of action differ (e.g. surgery vs chemotherapy, or targeted agent vs conventional therapy) may be hard to predict. One strategy is to compare the sample sizes arising from different plausible scenarios that include PH and non-PH examples, as we have done for the SORCE example. We would then make an informed choice based on the available evidence and on biological reasoning about the likely treatment effects. Arguably, the easiest way to define a hypothetical treatment-effect pattern is through time-dependent HRs or equivalently through the implied survival curves.

A key element of a discussion of the comparative merits of the HR and the difference in RMST as outcome measures concerns relative versus absolute effects. The HR is a relative measure which indicates neither the time to event nor the survival probability in each trial arm. Under the PH assumption, it is independent of time. The RMST difference measures the effect of treatment on the restricted survival time at some t∗. The values of RMST in each trial arm are absolute measures of survival time. This dual mode of presentation, as both a relative and an absolute measure, is an important advantage of RMST. In our view, the HR’s lack of any absolute component means the HR is incomplete as an outcome measure. It needs to be accompanied by other statistics, such as the estimated median survival times and/or the survival probabilities at specific time(s), or indeed the RMST.

The HR can seem impressively large even when the absolute effect on the time to event is small. Over-stressing the importance of apparently large relative risks has often been criticized in the medical and popular scientific literature as misleading for patients and physicians. For an example in the context of the benefit of breast cancer screening, see Reference [20] pp. 59 – 60. Here, we consider ASTEC vs. OE02 in Table 6. The absolute log HRs are almost identical yet the absolute RMST difference at t∗ = 5 years is some 3.4 times greater in OE02 than in ASTEC (0.29 vs. 0.09 years, i.e. about 3.5 months vs. 1 month). (These results for t∗ = 5 years were calculated separately; they are not given in Table 6.) The reason, of course, is that the 5-year survival probability in ASTEC is much larger than in OE02. The RMST difference of 0.09 years at t∗ = 5 years seen in ASTEC is arguably of little practical importance. In general, statistically significant differences in RMST from randomized trials may appear ‘small’, but they may be more realistic and clinically meaningful than superficially more impressive relative effects on the hazards. See also Royston et al’s [21] proposed graphical comparison of observed and imputed times to event between trial arms, which carries a similar message.

Here we have focused on RMST mainly as a potential design tool, having described the use of RMST in the analysis of trial data in a previous paper [1]. A standard approach to analysis would be to assume PH, test the null hypothesis of no treatment effect using the logrank test, and estimate the HR in a Cox model with randomized treatment as the only covariate. Adjustment for other covariates (e.g. prognostic factors) is readily incorporated. There are many options for extending the model if non-PH is detected. However, any such adaptation is likely to be data-dependent. The Cox model, whether in basic form or extended, does not readily lend itself to estimating the RMST [1]. An alternative may be to fit a piecewise exponential model with the knots used in the trial design. If too many knots are specified, the model can be over-fitted and the parameter estimates correspondingly unstable. This can happen if there are few events between a neighbouring pair of knots.

A more satisfactory analysis strategy is to use flexible parametric survival models [10-12] to estimate RMST. In summary, the PH subclass of these models incorporates a smooth estimate of the baseline log cumulative hazard function as a restricted cubic spline function of log time. The models readily lend themselves to precise estimation of RMST and RSDST and to extensions which accommodate time-dependent treatment effects (i.e. non-PH). An advantage is that their hazard functions are more realistic than those from the piecewise exponential model, since they are smooth functions of time rather than step functions. Parameter estimation by maximum likelihood is straightforward. However, to our knowledge flexible parametric models cannot be used on their own to design a trial. Piecewise exponential models are needed here, since they make it easy to specify the model in terms of survival probabilities and hazards and provide analytic expressions for the RMST and RSDST. Flexible parametric models are unsuitable for exploring hypothetical RMST values associated with a design with given hazard ratio(s) and control arm survival function.

We have described the calculation of two primary values of t∗, namely 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M100" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>des</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 and 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M101" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
. The former is driven by the theoretical structure of the design and the latter by the trial data as recorded. It is important to note that 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M102" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 does not depend on the treatment effect observed in the data, but on the designed difference in RMST and its observed variance as functions of t∗. In particular, 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M103" overflow="scroll"><ns0:msubsup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mtext>final</ns0:mtext></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msubsup></ns0:math>
````
 is not selected to miminize the P-value for the treatment comparison. It is data-driven only with respect to the variance of the RMST difference. However, the value of t∗ at which the definitive analysis is carried out may be motivated more by clinical than statistical concerns. A graph of power or maturity against t∗, as in Figure 2, may be used to decide if the data are adequate for an analysis using some preferred value of t∗. If the data are not sufficient, it may be appropriate to extend the follow-up period and/or recruit more patients. In Figure 2, for example, t
final
nnn∗ = 5.4 yr has power 84 percent and maturity 83 percent under the PH design assumptions, whereas a lower value, say t∗ = 4 yr, might be preferred; this has power and maturity slightly reduced to about 80 and 81 percent, respectively.

An important question is whether the RMST-based sample size calculation we have proposed is robust enough to be put into practice. Tentatively, we believe it is. With designs in which PH is assumed and holds, the logrank- and RMST-based sample size requirements are similar (see Table 1), and the power for a given sample size is correspondingly similar. For designs with severe non-proportional hazards, sample sizes for logrank- and RMST-based tests can differ markedly. As always with trial design, the key assumptions of data structure and relevant parameters critically affect the required sample size, and some kind of informal sensitivity analysis should always done.




### Conclusions


In summary, we conclude that the HR can often be an inappropriate and insufficient general measure of the treatment effect in an RCT, and also that the logrank test may lack power under some patterns of non-proportional hazards. We suggest that wider exploration and use of RMST in the design and analysis of trials with a time-to-event outcome is merited.




### Appendix: RMST and RSDST for a piecewise exponential distribution


Assume that the survival time, T, has a piecewise exponential distribution with k+1 piecewise constant hazards h1,…,h
k
,h
k+1 in a categorization (τ0 = 0,τ1], (τ1,τ2], (τ2,τ3], …, (τ
k
,τ
k+1 = ∞) of the time axis. The time points τ1,…,τ
k
 are known as knots. Suppose that t∗ belongs to interval (τ
k
,τ
k+1), so that t∗ > τ
k
. In the simplest case (k = 0), there are no knots and we have a single exponential distribution with hazard h1, and t∗ > 0.

We wish to calculate the RMST and the RSDST at t∗. For j = 0,1,…,k the interval duration δ
j+1 is 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M104" overflow="scroll"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>=</ns0:mo><ns0:mfenced open="{"><ns0:mrow><ns0:mtable class="array" columnalign="left"><ns0:mtr><ns0:mtd><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>,</ns0:mo></ns0:mtd><ns0:mtd><ns0:mi>j</ns0:mi><ns0:mo>&lt;</ns0:mo><ns0:mi>k</ns0:mi></ns0:mtd></ns0:mtr><ns0:mtr><ns0:mtd><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>k</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>,</ns0:mo></ns0:mtd><ns0:mtd><ns0:mi>j</ns0:mi><ns0:mo>=</ns0:mo><ns0:mi>k</ns0:mi></ns0:mtd></ns0:mtr></ns0:mtable></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:math>
````



 The cumulative hazard function H
j
 = H(τ
j
) at τ
j
 (j = 1,…,k) equals 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M105" overflow="scroll"><ns0:munderover><ns0:mrow><ns0:mo mathsize="big">∑</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>i</ns0:mi><ns0:mo>=</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:munderover><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>i</ns0:mi></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>i</ns0:mi></ns0:mrow></ns0:msub></ns0:math>
````
. Let h0 = H0 = 0. The survival function for t ∈ (τ
j
,τ
j+1] (j = 0,1,…,k) is 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M106" overflow="scroll"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:msup></ns0:mrow></ns0:math>
````



 For example, the survival function for t ∈ (0,τ1] is 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M107" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow></ns0:msup><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi><ns0:mo>-</ns0:mo><ns0:mn>0</ns0:mn></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:msup><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mi>t</ns0:mi></ns0:mrow></ns0:msup></ns0:math>
````
, as expected.

The integrated survival function from 0 to t∗ > τ
k
 (i.e. the RMST) is given by 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M108" overflow="scroll"><ns0:mrow><ns0:mo>μ</ns0:mo><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mo>=</ns0:mo><ns0:munderover accentunder="false" accent="false"><ns0:mrow><ns0:mo mathsize="big">∑</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>=</ns0:mo><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>k</ns0:mi></ns0:mrow></ns0:munderover><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext></ns0:mrow></ns0:math>
````



 Also 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M109" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:msup><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mi>u</ns0:mi></ns0:mrow></ns0:msup><ns0:mtext mathvariant="italic">du</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````



where for j = 0,…,k 


(11)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M110" overflow="scroll"><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfrac></ns0:math>
````



Thus the RMST on (0,t∗) is given by 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M111" overflow="scroll"><ns0:mrow><ns0:mo>μ</ns0:mo><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msubsup><ns0:mi>S</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mo>=</ns0:mo><ns0:munderover accentunder="false" accent="false"><ns0:mrow><ns0:mo mathsize="big">∑</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>=</ns0:mo><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>k</ns0:mi></ns0:mrow></ns0:munderover><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:math>
````



We also need the expectation 
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M112" overflow="scroll"><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow></ns0:mfenced></ns0:math>
````
 of X2 in the interval (τ
j
,τ
j+1] or (τ
k
,t∗], which is 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M113" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:msub><ns0:mrow><ns0:mi>S</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mtext mathvariant="italic">tdt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:mi>t</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:msup><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>t</ns0:mi><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mi>t</ns0:mi></ns0:mrow></ns0:msup><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:mi>t</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mi>t</ns0:mi></ns0:mrow></ns0:msup><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mi>t</ns0:mi></ns0:mrow></ns0:msup><ns0:mtext mathvariant="italic">dt</ns0:mtext></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>A</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````



where B
j+1 is as given in (11) and 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M114" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:msub><ns0:mrow><ns0:mi>A</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mo mathsize="big">∫</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msubsup><ns0:mi>t</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mi>t</ns0:mi></ns0:mrow></ns0:msup><ns0:mtext mathvariant="italic">dt</ns0:mtext><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1" /><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mfrac><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:msubsup><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup></ns0:mrow></ns0:mfrac><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mo>δ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````



Hence 


(12)
````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M115" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:munderover accentunder="false" accent="false"><ns0:mrow><ns0:mo mathsize="big">∑</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>=</ns0:mo><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>k</ns0:mi></ns0:mrow></ns0:munderover><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1"><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:munderover accentunder="false" accent="false"><ns0:mrow><ns0:mo mathsize="big">∑</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>=</ns0:mo><ns0:mn>0</ns0:mn></ns0:mrow><ns0:mrow><ns0:mi>k</ns0:mi></ns0:mrow></ns0:munderover><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>H</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub></ns0:mrow></ns0:msup><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msub><ns0:mrow><ns0:mi>A</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>+</ns0:mo><ns0:msub><ns0:mrow><ns0:mo>τ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi></ns0:mrow></ns0:msub><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mi>j</ns0:mi><ns0:mo>+</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1"><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:msup><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mspace width="2em" /></ns0:mtd></ns0:mtr></ns0:mtable></ns0:math>
````



For a single exponential with hazard h, we have k = 0, τ0 = 0, δ1 = t∗, h1 = h and therefore 



````xml
<ns0:math xmlns:ns0="http://www.w3.org/1998/Math/MathML" id="M116" overflow="scroll"><ns0:mtable columnalign="left"><ns0:mtr><ns0:mtd class="align-1"><ns0:msub><ns0:mrow><ns0:mi>A</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup><ns0:mfenced open="[" close="]"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mi>h</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msup><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>+</ns0:mo><ns0:mi>h</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1"><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>h</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msup><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mn>1</ns0:mn><ns0:mo>-</ns0:mo><ns0:msup><ns0:mrow><ns0:mi>e</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>-</ns0:mo><ns0:mi>h</ns0:mi><ns0:msup><ns0:mrow><ns0:mi>t</ns0:mi></ns0:mrow><ns0:mrow><ns0:mo>∗</ns0:mo></ns0:mrow></ns0:msup></ns0:mrow></ns0:msup></ns0:mrow></ns0:mfenced><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1"><ns0:mo>μ</ns0:mo></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mi>E</ns0:mi><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:msub><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>,</ns0:mo><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr><ns0:mtr><ns0:mtd class="align-1"><ns0:msup><ns0:mrow><ns0:mo>σ</ns0:mo></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msup></ns0:mtd><ns0:mtd class="align-2"><ns0:mo>=</ns0:mo><ns0:mtext>var</ns0:mtext><ns0:mfenced open="(" close=")"><ns0:mrow><ns0:mi>X</ns0:mi></ns0:mrow></ns0:mfenced><ns0:mo>=</ns0:mo><ns0:mn>2</ns0:mn><ns0:msub><ns0:mrow><ns0:mi>A</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow></ns0:msub><ns0:mo>-</ns0:mo><ns0:msubsup><ns0:mrow><ns0:mi>B</ns0:mi></ns0:mrow><ns0:mrow><ns0:mn>1</ns0:mn></ns0:mrow><ns0:mrow><ns0:mn>2</ns0:mn></ns0:mrow></ns0:msubsup><ns0:mspace width="2em" /></ns0:mtd><ns0:mtd /></ns0:mtr></ns0:mtable></ns0:math>
````






### Abbreviations


ART: Assessment of resources for trials; CI: Confidence interval; HR: Hazard ratio; MRC: Medical Research Council; non-PH: Non-proportional hazards; PH: Proportional hazards; RCT: Randomized controlled trial; RMST: Restricted mean survival time; RSDST: Restricted standard deviation of survival time.




### Pre-publication history


The pre-publication history for this paper can be accessed here:

http://www.biomedcentral.com/1471-2288/13/152/prepub





### Acknowledgements


We are grateful to M. Sydes and two reviewers (Y. Wang and S. Wacholder) for helpful comments that have helped us to strengthen the manuscript.


RoystonPParmarMKBThe use of restricted mean survival time to estimate the treatment effect in randomized clinical trials when the proportional hazards assumption is in doubtStat Med2011132409242110.1002/sim.427421611958

SchemperMWakounigSHeinzeGThe estimation of average hazard ratios by weighted Cox regressionStat Med2009132473248910.1002/sim.362319472308

MokTSWuYLThongprasertSYangCHChuDTSaijoNSunpaweravongPHanBMargonoBIchinoseYNishiwakiYOheYYangJJChewaskulyongBJiangHDuffieldELWatkinsCLArmourAAFukuokaMGefitinib or carboplatin - paclitaxel in pulmonary adenocarcinomaN Engl J Med20091394795710.1056/NEJMoa081069919692680

KristensenGPerrenTQianWPfistererJLedermannJAJolyFCareyMSResult of interim analysis of overall survival in the GCIG ICON7 phase III randomized trial of bevacizumab in women with newly diagnosed ovarian cancerJ Clin Oncol201113SLBA5006

AndersenPKPermeMPPseudo-observations in survival analysisStat Methods Med Res201013719910.1177/096228020910502019654170

BarthelFMSBabikerARoystonPParmarMKBEvaluation of sample size and power for multi-arm survival trials allowing for non-uniform accrual, non-proportional hazards, loss to follow-up and cross-overStat Med2006132521254210.1002/sim.251716479563

IrwinJOThe standard error of an estimate of expectation of life, with special reference to expectation of tumourless life in experiments with miceJ Hyg19491318818910.1017/S002217240001444315406758PMC2234920

BarthelFMSRoystonPBabikerAA menu-driven facility for complex sample size calculation in randomized controlled trials with a survival or a binary outcome: updateStat J200513123129

RosnerBFundamentals of Biostatistics2006Belmont, Ca: Duxbury Press

RoystonPParmarMKBFlexible proportional-hazards and proportional-odds models for censored survival data, with application to prognostic modelling and estimation of treatment effectsStat Med2002132175219710.1002/sim.120312210632

RoystonPLambertPCFlexible parametric survival analysis using Stata beyond the Cox model2011College Station, Tx: Stata Press

LambertPCRoystonPFurther development of flexible parametric models for survival analysisStat J200913265290

McGuireWPHoskinsWJBradyMFKuceraPRPartridgeEELookKYClarke-PearsonDLDavidsonMCyclophosphamide and cisplatin compared with paclitaxel and cisplatin in patients with stage III and stage IV ovarian cancerN Engl J Med1996131610.1056/NEJM1996010433401017494563

LeibovichBCBluteMLChevilleJCLohseCMFrankIKwonEDWeaverALParkerASZinckeHPrediction Of progression after radical Nephrectomy for patients with clear cell renal cell carcinomaCancer2003131663177110.1002/cncr.1123412655523

GoreMEGriffinCLHancockBPatelPMPyleLAitchisonMJamesNOliverRTDMardiakJHussainTSylvesterRParmarMKBRoystonPMuldersPFAInterferon alfa-2a versus combination therapy with interferon alfa-2a, interleukin-2, and fluorouracil in patients with untreated metastatic renal cell carcinoma (MRC RE04 / EORTC GU 30012): an open-label randomised trialLancet20101364164810.1016/S0140-6736(09)61921-820153039PMC2835851

KitchenerHSwartAMQianWEfficacy of systematic pelvic lymphadenectomy in endometrial cancer (MRC ASTEC trial): a randomised studyLancet2009131251361907088910.1016/S0140-6736(08)61766-3PMC2646126

International collaboration of trialists on behalf of the Medical Research CouncilAdvanced Bladder Cancer Working PartyNeoadjuvant cisplatin, methotrexate and vinblastine chemotherapy for muscle-invasive bladder cancer: a randomised controlled trialLancet19991353354010470696

ParmarMKLedermannJAColomboNPaclitaxel plus platinum-based chemotherapy versus conventional platinum-based chemotherapy in women with relapsed ovarian cancer: the ICON4/AGO-OVAR-2.2 trialLancet200313209921061282643110.1016/s0140-6736(03)13718-x

Medical ResearchCouncil Oesophageal Cancer Working PartySurgical resection with or without preoperative chemotherapy in oesophageal cancer: a randomised controlled trialLancet200213172717331204986110.1016/S0140-6736(02)08651-8

GigerenzerGReckoning with risk2002London, UK: Allen Lane

RoystonPParmarMKBAltmanDGVisualizing length of survival in time-to-event studies: a complement to Kaplan-Meier plotsJ Natl Cancer Inst200813929710.1093/jnci/djm26518182621
