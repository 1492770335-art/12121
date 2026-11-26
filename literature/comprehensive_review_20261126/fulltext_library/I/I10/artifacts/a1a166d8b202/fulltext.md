# Concordance for prognostic models with competing risks

Source: [original.xml](original.xml).

PAGINATION UNAVAILABLE: this original JATS XML does not supply a verified PDF page map. Sections and original formula markup are preserved; no PDF pages are invented. TeX-math and MathML blocks below are original XML content, not reconstructed equations. Formula images remain unresolved and are flagged.



The concordance probability is a widely used measure to assess discrimination of prognostic models with binary and survival endpoints. We formally define the concordance probability for a prognostic model of the absolute risk of an event of interest in the presence of competing risks and relate it to recently proposed time-dependent area under the receiver operating characteristic curve measures. For right-censored data, we investigate inverse probability of censoring weighted (IPCW) estimates of a truncated concordance index based on a working model for the censoring distribution. We demonstrate consistency and asymptotic normality of the IPCW estimate if the working model is correctly specified and derive an explicit formula for the asymptotic variance under independent censoring. The small sample properties of the estimator are assessed in a simulation study also against misspecification of the working model. We further illustrate the methods by computing the concordance probability for a prognostic model of coronary heart disease (CHD) events in the presence of the competing risk of non-CHD death.


1.

### Introduction


Clinical decision-making and cost-effectiveness analyses often rely on prognostic models that quantify a subject's absolute risk of a disease event of interest over time. However, study populations increasingly consist of elderly individuals with varying degrees of co-morbidity who are likely to experience one of several disease endpoints other than the endpoint of main interest (Koller, Raatz and others, 2012). As an example, prediction of coronary heart disease (CHD) events in elderly subjects is complicated by the fact that subjects may die from other causes prior to the observation of the disease event of interest (Wolbers and others, 2009; Koller, Leening and others, 2012).

It is well known that the naive application of standard survival analysis leads to bias and risk over-estimation if competing risks are present and that specialized methods are needed (Grunkemeier and others, 2007; Putter and others, 2007). A key quantity for medical decision-making in the presence of competing risks is the absolute risk of the event of interest over time as quantified by its (covariate-dependent) cumulative incidence function (Gail and Pfeiffer, 2005; Wolbers and others, 2009). Thus, regression models are particularly attractive when they provide subject-specific estimates of the absolute risks based on a set of covariates (Fine and Gray, 1999; Gerds and others, 2012).

Several measures for quantifying the accuracy of prognostic models have been adapted from the standard survival setting with only one failure cause to competing risks. Measures include prediction error curves (Schoop and others, 2011), time-dependent sensitivity, specificity, and area under the receiver operating characteristic (ROC) curve (AUC) (Saha and Heagerty, 2010), and reclassification methods (Wolbers and others, 2009; Koller, Leening and others, 2012). For survival data, the concordance index (Harrell and others, 1982) is a frequently reported measure of discrimination and we have previously presented a simple adaptation of Harrell's concordance estimator to the competing risks setting (Wolbers and others, 2009).

In the present paper, we motivate and formally define a cause-specific concordance index in the presence of competing risks. Notably, the proposed concordance index depends only on the cumulative incidence function of the event of interest. We clarify the relation of the concordance to time-dependent AUC measures and discuss a possible alternative definition. We then study estimation of a truncated concordance index in the presence of right-censoring. We introduce an inverse probability of censoring weighted (IPCW) estimator and demonstrate its consistency and asymptotic normality if the working model for the censoring distribution is correctly specified. The empirical bias and mean-square error as well as coverage of asymptotic and bootstrap confidence intervals are examined in a simulation study. Finally, we illustrate the methods for an example of coronary risk prediction in older woman using data from the Rotterdam Study (Hofman and others, 2011).


2.

### Definition of concordance


2.1

### Definition for a simple prognostic score without censoring


Competing risks data without censoring are given by pairs 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T,D)$\end{document}
````
 of data where 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T$\end{document}
````
 is the time to the event and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D$\end{document}
````
 is the event type. For the purpose of discussing the definition and estimation of the cause-specific concordance index it is sufficient to assume that there are only two competing events. Thus, for simplicity of presentation we let 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=1$\end{document}
````
 denote the event of interest and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=2$\end{document}
````
 the occurrence of any competing event. In applications, it may be important to model all competing events separately.

The concordance index is defined for any prognostic score 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde M(X)$\end{document}
````
 depending on baseline variables 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X$\end{document}
````
 which can be used to order subjects with respect to the risk of an event of type 1. For example, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde M(X)$\end{document}
````
 could be a single baseline marker or the linear predictor of a regression model for the event of interest derived on a training data set. We assume that higher values of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde M(X)$\end{document}
````
 are associated with higher risks of the event of interest.

To motivate our definition with an example, assume that 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T$\end{document}
````
 is the time to death and that a specific treatment were available which prevented death due to the event of interest (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=1$\end{document}
````
) but would not affect death from other causes (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=2$\end{document}
````
). The immediate benefit from such a treatment would be greatest for subject with a high risk of dying from the event of interest early, less for individuals dying from the event of interest late, and negligible for subjects with a low risk of experiencing the event of interest at all (i.e. those likely to die from competing causes). Consequently, for a random pair of subjects 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(X_i,T_i,D_i)$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(X_j,T_j,D_j)$\end{document}
````
, the first subject would be in greater need of treatment than the second subject if they experienced the event of interest (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_i=1$\end{document}
````
) and the second subject experienced the event of interest later (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_i<T_j$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_j=1$\end{document}
````
) or not at all (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_j=2$\end{document}
````
). In these cases, the ranking of the risk marker for the pair of subjects is concordant if 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde M(X_i)>\tilde M(X_j)$\end{document}
````
. Pairs of individuals where both experience the competing event are not comparable as neither of them would be in need of treatment.

To formally define the concordance probability for the event of interest, we assume an independent test set of i.i.d. realizations of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(X_i,T_i,D_i)$\end{document}
````
 from the joint distribution of the marker and the competing risks outcome and define

(2.1)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq2.1} \tilde{\mathcal C}_1=P(\tilde M(X_i)>\tilde M(X_j)\mid D_i=1 \mbox{ and } (T_i<T_j \mbox{ or } D_j=2)), \end{equation*}\end{document}
````


for any randomly chosen pair of subjects 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$i,j$\end{document}
````
 from this distribution. The concordance probability for the competing event, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}_2$\end{document}
````
, is defined analogously.

Define the cumulative incidence function for the event of interest as 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_1(t\mid X)=P(T\leq t,D=1\mid X)$\end{document}
````
 and the improper random variable 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T^*$\end{document}
````
 as 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T^*=I(D=1)\cdot T+I(D\neq 1)\cdot \infty $\end{document}
````
. 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T^*$\end{document}
````
 has a distribution function equal to 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_1(t\mid X)$\end{document}
````
 for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t<\infty $\end{document}
````
 and a point mass of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$1-F_1(\infty \mid X)$\end{document}
````
 at 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\infty $\end{document}
````
 (Fine and Gray, 1999). As an associate editor pointed out, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}_1$\end{document}
````
 can be written in terms of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T^*$\end{document}
````
 leading essentially to the standard definition of concordance for survival data: 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}_1=P(\tilde M(X_i)>\tilde M(X_j)\mid T_1^*<T_j^*)$\end{document}
````
.

We also note that 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$I(\{s<T_j \mbox { or } D_j=2\})=1-I(\{T_j\leq s, D_j=1\})$\end{document}
````
. Thus,


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\[ {\rm P}\{D_i=1 \mbox{ and } (T_i<T_j \mbox{ or } D_j=2)\}= {\rm E}_{X_i,X_j}\int_0^\infty (1-F_1(s\mid X_j))\,{\rm d} F_1(s\mid X_i), \] \end{document}
````


and we can rewrite 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}_1$\end{document}
````
 as

(2.2)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq2.2} \tilde{\mathcal C}_1=\frac{{\mathrm{E}}_{X_i,X_j}(I(\tilde M(X_i)>\tilde M(X_j))\int_0^\infty (1-F_1(s\mid X_j)) \,{\rm d} F_1(s\mid X_i))}{{\rm E}_{X_i,X_j}(\int_0^\infty (1-F_1(s\mid X_j)) \,{\rm d} F_1(s\mid X_i))}. \end{equation*}\end{document}
````


According to (2.2), the cause-specific concordance for event 1 depends on 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_1$\end{document}
````
 and the marginal distribution of the marker but not on the cumulative incidence function 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_2$\end{document}
````
 of the competing event. This feature is not obvious in formula (2.1) but desirable when the aim is to assess the discriminative ability of a marker for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_1$\end{document}
````
.

In Appendix B of supplementary material available at Biostatistics online, we illustrate the properties of the concordance probability for a single marker and competing risks outcomes simulated according to cause-specific proportional hazards models with constant baseline hazards. The illustrations suggest that to achieve a high concordance, the marker needs to be strongly associated with an increased cause-specific hazard of the event of interest but only weakly or, even better, reversely associated with the cause-specific hazard of the competing event. This can be explained by the fact that the overall effect of a covariate on the cumulative incidence function of the event of interest depends on both cause-specific baseline hazards and both cause-specific hazard ratios (Beyersmann and others, 2007; Koller, Raatz and others, 2012).

Finally, it is important to discuss modifications of definition (2.1) for tied data (Yan and Greene, 2008). For example, it may happen that 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X_i=X_j$\end{document}
````
. Depending on the application, it may then be sensible to count such pairs with a weight of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\frac 12$\end{document}
````
:


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{align*} \tilde{\mathcal C}_1&=P(\tilde M(X_i)>\tilde M(X_j)\mid D_i=1 \mbox{ and }(T_i<T_j \mbox{ or } D_j=2))\\ &\quad +\tfrac{1}{2}P(\tilde M(X_i)=\tilde M(X_j)\mid D_i=1 \mbox{ and }(T_i<T_j \mbox{ or } D_j=2)). \end{align*} \end{document}
````


To simplify notation, we use definition (2.1) as the basis for our further developments.


2.2

### An alternative definition of concordance and relation to time-dependent AUC measures


We motivated our definition of concordance with a specific treatment for the event of interest which does not affect the competing event. In this situation, a case subject 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T_i,D_i)$\end{document}
````
 with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_i=1$\end{document}
````
 has a larger immediate benefit from treatment than a control subject 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T_j,D_j)$\end{document}
````
 with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_j>T_i$\end{document}
````
 or 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_j=2$\end{document}
````
 as subjects experiencing a competing event have no benefit from treatment at all. However, in other situations, the treatment may affect both event types and then subjects 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T_i,D_i)$\end{document}
````
 with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_i=1$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T_j,D_j)$\end{document}
````
 with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_j\leq T_i$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_j=2$\end{document}
````
 would not be comparable. Here, it would be more relevant to distinguish cases 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T_i,D_i)$\end{document}
````
 with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D_i=1$\end{document}
````
 from those who haven not had any event up to that time point, i.e. those with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_j>T_i$\end{document}
````
. This leads to an alternative definition of concordance:


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{align*} \tilde{\mathcal C}^*_{1}&=P(\tilde M(X_i)>\tilde M(X_j)\mid D_i=1 \mbox{ and }T_i<T_j)\\ &=\frac{{\mathrm{E}}_{X_i,X_j}(I(\tilde M(X_i)>\tilde M(X_j))\int_0^\infty (1-F_1(s\mid X_j)-F_2(s\mid X_j))\, {\rm d} F_1(s\mid X_i))} {{\rm E}_{X_i,X_j}(\int_0^\infty (1-F_1(s\mid X_j)-F_2(s\mid X_j))\, {\rm d} F_1(s\mid X_i))}. \end{align*} \end{document}
````


Of note, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}^*_{1}$\end{document}
````
 also depends on the cumulative incidence function of the competing event 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_2$\end{document}
````
. Thus, it might be less suitable if the main goal is to assess the relevance of a marker or a prognostic model for predicting the absolute risk of the event of interest alone, and we will not pursue it further. However, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}^*_{1}$\end{document}
````
 could be valuable for assessing joint models for the cumulative incidence of both competing events.

The proposed concordance measures are closely related to measures of the time-dependent AUC which have been proposed to assess discrimination for competing risks data at a fixed time point 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$s$\end{document}
````
 (Saha and Heagerty, 2010; Zheng and others, 2012; Blanche and others, 2013). We review these measures in Appendix C of supplementary material available at Biostatistics online, and show that 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}_1$\end{document}
````
 can be written as a weighted average of one proposed time-dependent AUC measure over time. This is in analogy with a similar result for survival analysis without competing risks (Heagerty and Zheng, 2005) and supports the use of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {\mathcal C}_1$\end{document}
````
 as a global summary measure of performance.


2.3

### Assessing prediction models in right-censored data


We now generalize the concordance index defined in Section 2.1 in two ways. First, we replace the simple prognostic score 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde M(X)$\end{document}
````
 by a more general prediction model 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$M(t,X)$\end{document}
````
 for the risk of event 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$1$\end{document}
````
 until time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
, i.e. estimates of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_1(t\mid X)=P(T\leq t,D=1\mid X)$\end{document}
````
, which can be obtained by combining cause-specific hazards models, by fitting a Fine and Gray regression model or by direct binomial regression (Fine and Gray, 1999; Scheike and others, 2008). Secondly, to include the typical application where individuals have a limited duration of follow-up we define a truncated version of the concordance index. Following Uno and others (2011) and Gerds and others (2013), we define

(2.3)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq2.3} {\mathcal C}_{1}(t):=P(M(t,X_i)>M(t,X_j)\mid D_i=1 \mbox{ and } T_i\leq t \mbox{ and } (T_i<T_j \mbox{ or } D_j=2)). \end{equation*}\end{document}
````


The parameter 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 quantifies the ability of the model to correctly rank events of interest up to time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 and to discriminate them from competing events. The truncation is necessary to enable estimation of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 from right-censored data with a limited follow-up duration.

As before, we can write the truncated concordance (2.2) as a functional of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$F_1$\end{document}
````
 and of the marginal distribution of the predictor values of a pair of individuals 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(X_i,X_j)$\end{document}
````
: If we introduce notation for the order of the predicted risks at time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 for a pair of individuals,


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\[ Q^{ij}(t)=I\{M(t,X_i)>M(t,X_j)\}, \] \end{document}
````


then

(2.4)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq2.4} {\mathcal C}_1(t)=\frac{{\mathrm{E}}_{X_i,X_j}(Q^{ij}(t)\int_0^t (1-F_1(s\mid X_j))\, {\rm d} F_1(s\mid X_i))}{{\rm E}_{X_i,X_j}(\int_0^t (1-F_1(s\mid X_j))\, {\rm d} F_1(s\mid X_i))}. \end{equation*}\end{document}
````






3.

### Estimation of concordance in the presence of right-censoring


3.1

### Right-censored data


To indicate the end of follow-up for subject 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$i,$\end{document}
````
 we introduce a subject-specific censoring time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$C_i$\end{document}
````
. Thus, we observe only 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(X_i,\tilde T_i, \tilde D_i,\Delta _i)$\end{document}
````


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(i=1\cdots n)$\end{document}
````
 where 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {T_i}=\min (T_i,C_i)$\end{document}
````
, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\Delta _i=I\{T_i\le C_i\}$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde {D_i}=\Delta _i D_i$\end{document}
````
. We also use the following notation:


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{align*} \tilde{N}^1_i(t)&=I\{\tilde{T}_i\leq t, \tilde D_i=1 \}, \quad {N}^1_i(t)=I\{T_i\leq t, D_i=1 \},\\ \tilde{N}^2_i(t)&=I\{\tilde{T}_i\leq t, \tilde D_i=2 \}, \quad {N}^2_i(t)=I\{T_i\leq t, D_i=2 \},\\ \tilde{A}_{ij}&=I\{\tilde{T}_i<\tilde{T}_j\}, \quad A_{ij}=I\{T_i<T_j\},\\ \tilde{B}_{ij}&=I\{\tilde{T}_i\geq \tilde{T}_j \mbox{ and } \tilde{D_j}=2\}, \quad B_{ij}=I\{T_i\geq T_j \mbox{ and } D_j=2\}. \end{align*} \end{document}
````


The event-free survival probability conditional on the covariate 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X_i$\end{document}
````
 is then given by


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\[ S(t\mid X_i)=1-{\rm E}(N_i^1(t)\mid X_i) - {\rm E}(N_i^2(t)\mid X_i)=1-F_1(t\mid X_i)-F_2(t\mid X_i). \] \end{document}
````


We allow the censoring distribution to depend on the covariates 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X_i$\end{document}
````
 but assume throughout that 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$C_i$\end{document}
````
 is conditionally independent of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T_i,D_i)$\end{document}
````
 given 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X_i$\end{document}
````
. This implies

(3.1)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq3.1} {\mathrm{P}}(\tilde T_i>t\mid X_i)=G(t\mid X_i)S(t\mid X_i), \end{equation*}\end{document}
````


where 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$G(t\mid X_i)=P(C_i>t\mid X_i)$\end{document}
````
 is the conditional probability of being uncensored at time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
. Noting 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$G(t-| X_i)=P(C_i\ge t\mid X_i)$\end{document}
````
 we also have for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$k=1,2$\end{document}
````
:

(3.2)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq3.2} {\mathrm{E}}(\tilde N_i^k(t)\mid X_i)= {\rm E}(\Delta_i N_i^k(t)\mid X_i) = \int_0^t {\rm E}(C_i\ge s\mid X_i)\,{\rm E}({\rm d} N^k_i(s)\mid X_i) = \int_0^t G(s-|X_i)\, {\rm d} F_k(s\mid X_i). \end{equation*}\end{document}
````





3.2

### Ignoring non-evaluable pairs


An asymptotically biased estimate of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 is given by


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\[ \hat{\mathcal C}_{1,{\rm naive}}(t)= \frac{\sum_{i=1}^n\sum_{j=1}^n (\tilde{A}_{ij}+\tilde{B}_{ij}) Q^{ij}(t) \tilde{N}^1_i(t)} {\sum_{i=1}^n\sum_{j=1}^n (\tilde{A}_{ij}+\tilde{B}_{ij}) \tilde{N}^1_i(t)}, \] \end{document}
````


where 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$Q^{ij}(t)=I\{M(t,X_i)>M(t,X_j)\}$\end{document}
````
 is an indicator for the order of predicted risks at time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
. This can be interpreted as the proportion of definitely concordant pairs amongst evaluable pairs, i.e. pairs for which one individual experiences the event of interest and concordance can be decided based on the observed (potentially censored) data.

This estimate evaluated at the time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 corresponding to the maximum follow-up duration is a direct adaptation of Harrel's 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}$\end{document}
````
 for survival data (Harrell and others, 1982) to the competing risks context and has been previously defined in Wolbers and others (2009). While simple, a major problem of this estimator is that by ignoring non-evaluable pairs without any correction, bias is introduced. It is well known that Harrel's 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}$\end{document}
````
 depends on the censoring distribution (Uno and others, 2011; Gerds and others, 2013) and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {\mathcal C}_{1,{\mathrm {naive}}}(t)$\end{document}
````
 shares this limitation.


3.3

### IPCW estimate


We derive an IPCW estimate for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 based on a working model

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\mathcal G$\end{document}
````
 for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$G$\end{document}
````
. Let 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tau $\end{document}
````
 be a time point where 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\inf _x G(\tau \mid x)>\epsilon >0.$\end{document}
````
 We assume that the model 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\mathcal G$\end{document}
````
 is correctly specified and that for all 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t<\tau $\end{document}
````
 there exists a uniformly consistent, weakly asymptotically linear estimator sequence 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {G}$\end{document}
````
 with influence function 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\rm IF}_G(t,x;\tilde T_i,\tilde D_i,X_i)$\end{document}
````
. This implies (Bickel and others, 1993):

(3.3)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq3.3} \sqrt n \{\hat{G}(t\mid x)-G(t\mid x)\} = \frac{1}{\sqrt n} \sum_{i=1}^n {\mathrm{IF}}_G(t,x;\tilde T_i,\tilde D_i,X_i) + o_p(1). \end{equation*}\end{document}
````


For example, we can specify a Cox regression model and use the estimate


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\[ \hat G(t\mid X_i)=\exp\left\{-\int_0^t \exp(\hat\gamma^T X_i)\hat\Gamma_0(s) \,{\rm d} s\right\}, \] \end{document}
````


where 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat \Gamma _0$\end{document}
````
 is the Breslow estimator of the baseline hazard function and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat \gamma $\end{document}
````
 the maximum partial likelihood estimator of the regression coefficients. If the censoring is conditionally independent of the competing risks outcome given the predictors and the Cox model correctly specified, then condition (3.3) is satisfied (see, e.g. Cheng and others, 1998). As an alternative, we could assume that the censoring is independent of the competing risks outcome and the predictors. If this assumption is correct, then the Kaplan–Meier estimate for the censoring distribution satisfies (3.3).

Based on 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat G,$\end{document}
````
 we construct the weights


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\[ \hat{W}_{ij,1}=\hat{G}(\tilde{T}_i-|X_i)\hat{G}(\tilde{T}_i|X_j) \hbox{ and } \hat{W}_{ij,2}=\hat{G}(\tilde{T}_i-|X_i)\hat{G}(\tilde{T}_j-|X_j), \] \end{document}
````


and define an IPCW estimate of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
:

(3.4)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq3.4} \hat{\mathcal C}_{1}(t)= \frac{\sum_{i=1}^n\sum_{j=1}^n (\tilde{A}_{ij}\hat{W}_{ij,1}^{-1}+\tilde{B}_{ij}\hat{W}_{ij,2}^{-1}) Q^{ij}(t) \tilde{N}^1_i(t) } {\sum_{i=1}^n\sum_{j=1}^n (\tilde{A}_{ij}\hat{W}_{ij,1}^{-1}+\tilde{B}_{ij}\hat{W}_{ij,2}^{-1}) \tilde{N}^1_i(t)}. \end{equation*}\end{document}
````







### Lemma 3.1


If the working model is correctly specified and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {G}$\end{document}
````
 is a consistent estimator of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$G,$\end{document}
````
 then 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {\mathcal C}_{1}(t)$\end{document}
````
 is a consistent estimator of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 for all 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t<\tau $\end{document}
````
. Furthermore, if (3.3) is satisfied, then 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {\mathcal C}_1(t)$\end{document}
````
 is asymptotically linear and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\sqrt n \{\hat {{\mathcal C}}_1(t)- {\mathcal C}_1(t)\}$\end{document}
````
 converges in distribution to a normal random variable with mean 0.


A proof of the lemma is given in Appendix D of supplementary material available at Biostatistics online. For the case of independent censoring, supplementary material available at Biostatistics online also presents an explicit formula for the influence function and a consistent estimator of the asymptotic variance. The proposed concordance estimator has been implemented with the function cindex of the R package pec (Mogensen and others, 2012). Example code is provided in Appendix A of supplementary material available at Biostatistics online.



4.

### Simulation study


A simulation study was performed to assess bias and root mean square error (RMSE) of the proposed IPCW estimator and coverage of asymptotic and bootstrap confidence intervals. Simulations were for a single prognostic marker 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X$\end{document}
````
 and a parameter-free time-independent model 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$M(X,t)=X$\end{document}
````
. The covariate 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X$\end{document}
````
 was simulated to follow a standard normal distribution.

Conditional on 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$X$\end{document}
````
, uncensored competing risks data 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(T,D)$\end{document}
````
 was assumed to follow cause-specific Cox-exponential models (Bender and others, 2006):

(4.1)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\begin{equation*}\label{eq4.1} \begin{split} \text{Event 1: }\lambda_1(t\mid X)&=\lambda_{01}\exp(\beta_1 X),\\ \text{Event 2: }\lambda_2(t\mid X)&=\lambda_{02}\exp(\beta_2 X). \end{split} \end{equation*}\end{document}
````


This was implemented by simulating latent exponentially distributed event times 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_1$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_2$\end{document}
````
 and then setting 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T=\min (T_1,T_2)$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=1$\end{document}
````
 for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_1<T_2$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=2$\end{document}
````
 for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T_1\ge T_2$\end{document}
````
. We consider two competing risks scenarios. In scenario CR1, we set 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\lambda _{01}(t)=1, \lambda _{02}(t)=2,$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\beta _1= \beta _2=1$\end{document}
````
. In scenario CR2, we set 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\lambda _{01}(t)=1, \lambda _{02}(t)=0.5,$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\beta _1= 2,\beta _2=-1$\end{document}
````
. As truncation time points, we used the median and the 75% quantile 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$q_{75}$\end{document}
````
 of the marginal distribution of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T$\end{document}
````
. The truncation time points and corresponding true values of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 were determined by simulation based on a large uncensored data set of size 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$100\,000$\end{document}
````
.

Censoring times 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$C$\end{document}
````
 were drawn under a third Cox-exponential model:


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}\[ \lambda_{{\rm cens}}(t\mid X)=\lambda_{0,{\rm cens}}\cdot\exp(\gamma_1 X). \] \end{document}
````


The observed time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde T$\end{document}
````
 was obtained as the minimum of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$C$\end{document}
````
 and considered as right-censored if 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$C<T$\end{document}
````
. We repeated the simulations for independent censoring (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\gamma _1=0$\end{document}
````
) and covariate-dependent censoring (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\gamma _1=1$\end{document}
````
). For each truncation time point 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t,$\end{document}
````
 the values of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\lambda _{0,{\mathrm {cens}}}$\end{document}
````
 were found by simulation such that the expected proportion of right-censored event times amongst observations with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde T<t$\end{document}
````
 was 25%, 50%, or 75%, respectively. For each of the scenarios, we report results for sample sizes 250 and 1000 averaged across 1000 simulated data sets.

In each simulated data set, we computed three different estimators of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
: the naive estimator 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {naive}}}(t)$\end{document}
````
, the IPCW estimator based on the marginal Kaplan–Meier estimate of the censoring distribution 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
 and the IPCW estimator based on a Cox regression model for the censoring distribution 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\rm Cox}}(t)$\end{document}
````
.

Bias and root mean squared errors for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 chosen as the 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$75\%$\end{document}
````
-quantile of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T$\end{document}
````
 are shown in Table 1. Table 2 shows the associated coverage of percentile bootstrap (all estimators) and asymptotic Wald-type confidence intervals (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\rm KM}}(t)$\end{document}
````
 only) and contrasts empirical standard errors with average bootstrap and asymptotic standard errors for the estimate 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
. Corresponding results for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 chosen as the median are shown in Appendix E of supplementary material available at Biostatistics online.

Table 1.

Average bias and RMSE for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$3$\end{document}
````
 different estimators of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 averaged over 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$1000$\end{document}
````
 data sets simulated under the 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$2$\end{document}
````
 scenarios CR1 and CR2 for varying sample size 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$N,$\end{document}
````
 independent 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(\gamma _1=0),$\end{document}
````
 or covariate-dependent censoring 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$(\gamma _1=1),$\end{document}
````
 respectively
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$,$\end{document}
````
 and varying censoring rates


````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$N$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\gamma _1$\end{document}
````
Censored before 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 (%)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {naive}}}(t)$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {Cox}}}(t)$\end{document}
````
CR1: 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)=62.1\%, \beta _1=1, \beta _2=1, \lambda _{01}=1, \lambda _{02}=2$\end{document}
````
, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t= q_{75}$\end{document}
````
2500251.5 (4.0)0.1 (3.7)0.1 (3.7)2500503.9 (5.9)0.3 (4.8)0.3 (4.8)2500758.1 (10.0)2.6 (10.1)2.8 (9.5)2501251.0 (4.0)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.1 (3.9)0.1 (3.9)2501502.6 (5.4)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.3 (4.9)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.2 (5.8)2501755.1 (8.4)0.2 (8.2)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
1.9 (10.3)10000251.4 (2.3)0.0 (1.9)0.0 (1.9)10000503.8 (4.3)0.0 (2.3)0.0 (2.3)10000757.9 (8.4)1.0 (6.4)1.2 (6.0)10001250.9 (2.1)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.3 (1.9)0.0 (2.0)10001502.5 (3.3)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.5 (2.3)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.1 (3.4)10001755.0 (5.9)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.4 (3.8)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
1.8 (7.5)CR2: 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)=85.0\%, \beta _1=2, \beta _2=-1, \lambda _{01}=1, \lambda _{02}=0.5$\end{document}
````
, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t= q_{75}$\end{document}
````
2500250.7 (1.8)0.1 (1.7)0.1 (1.7)2500501.5 (2.4)0.2 (2.1)0.2 (2.1)2500752.8 (3.7)0.7 (4.1)0.8 (3.7)2501250.6 (1.9)0.0 (1.8)0.1 (1.7)2501501.3 (2.5)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.1 (2.3)0.1 (2.3)2501752.2 (3.8)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.2 (4.4)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.3 (5.6)10000250.7 (1.1)0.0 (0.8)0.0 (0.8)10000501.4 (1.7)0.0 (1.0)0.0 (1.0)10000752.7 (3.0)0.2 (2.8)0.3 (2.5)10001250.6 (1.0)0.0 (0.9)0.1 (0.8)10001501.3 (1.6)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.2 (1.2)0.1 (1.1)10001752.1 (2.6)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.7 (2.4)
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$-$\end{document}
````
0.7 (4.3)

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 was chosen as the 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$75$\end{document}
````
-quantile of the marginal time-to-event distribution. Column 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$3$\end{document}
````
 shows the expected proportion of right-censored event times amongst observations with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\tilde T<t$\end{document}
````
. Columns 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$4$\end{document}
````
–
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$6$\end{document}
````
 show average bias 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$($\end{document}
````
RMSE
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$)$\end{document}
````
 for the three estimators 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$($\end{document}
````
multiplied by 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$100$\end{document}
````
 for easier readability
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$)$\end{document}
````
.




Table 2.

Coverage of confidence intervals for the same simulation scenarios as in Table 1

Standard error KMCoverage
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$N$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\gamma _1$\end{document}
````
Censored before 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t$\end{document}
````
 (%)EmpiricalAverage asymptoticAverage bootstrapAsymptotic KMBootstrap naiveBootstrap KMCoxCR1: 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)=62.1\%, \beta _1=1, \beta _2=1, \lambda _{01}=1, \lambda _{02}=2$\end{document}
````
, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t= q_{75}$\end{document}
````
2500250.03720.03840.038494.591.694.294.32500500.0480.04730.047893.483.693.693.22500750.09740.07070.07777.867.381.282.12501250.03880.03920.039594.293.494.595.12501500.04860.04790.048693.890.194.193.52501750.08230.06960.073386.481.488.688.410000250.01880.01920.01995.488.995.195.210000500.02340.02380.023895.159.695.395.110000750.06350.04750.049980.723.281.982.610001250.01930.01950.019594.991.694.694.310001500.02290.02390.023995.481.695.593.410001750.03760.03680.03793.964.693.889.2CR2: 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)=85.0\%, \beta _1=2, \beta _2=-1, \lambda _{01}=1, \lambda _{02}=0.5$\end{document}
````
, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t= q_{75}$\end{document}
````
2500250.01680.01730.017495.191.495.095.02500500.02070.02080.02194.384.294.594.42500750.04040.03430.035985.472.588.287.92501250.01810.01830.018695.092.295.395.22501500.02320.02350.02494.687.995.295.92501750.04390.03840.039987.481.288.893.310000250.008310.008590.0085695.386.795.595.610000500.01010.01030.010395.666.795.495.710000750.02770.02180.022487.441.488.889.810001250.008780.009050.0091495.288.795.495.910001500.01160.01180.011995.876.595.995.310001750.02340.0220.022193.767.694.294.0
Columns 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$8$\end{document}
````
–
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$10$\end{document}
````
 display observed coverage of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$95\%$\end{document}
````
 percentile bootstrap confidence intervals for all three estimators
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$,$\end{document}
````
 column 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$7$\end{document}
````
 shows coverage of asymptotic Wald-type confidence intervals for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
. Columns 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$4$\end{document}
````
–
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$6$\end{document}
````
 show the empirical standard error for the 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$1000$\end{document}
````
 estimates and the average asymptotic and bootstrap standard errors of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
.




Based on Tables 1 and 2, we draw the following conclusions.


The naive estimator 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {naive}}}(t)$\end{document}
````
 can be biased and this can lead to insufficient coverage.



The ICPW estimator 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
 can also be biased if the censoring depends on the covariate. In some cases, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {Cox}}}(t)$\end{document}
````
 has a smaller bias but for high rates of censoring it can do worse than 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
 even though the censoring depends on the covariate.



Coverage of confidence intervals for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {Cox}}}(t)$\end{document}
````
 was generally close to the nominal 95% except for some scenarios with high censoring rates of 75%. Both average asymptotic and bootstrap standard errors closely resembled the empirical standard errors of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\hat {{\mathcal C}}_{1,{\mathrm {KM}}}(t)$\end{document}
````
.





5.

### Application to coronary risk prediction


Specialist medical societies recommend initiation of preventive treatment for CHD based on a subjects’ predicted 10-year risk for CHD (NCEP, 2002). To accurately predict the absolute risk of CHD in older people, prognostic models for CHD need to account for the competing risk of non-CHD death (Koller, Leening and others, 2012). In this section, we revisit the example of Wolbers and others (2009) on coronary risk prediction based on data of elderly women from the Rotterdam Study, a prospective, population-based cohort of elderly subjects living in a suburb area of Rotterdam, the Netherlands (Hofman and others, 2011).

We analyzed data from 10 years of follow-up of 4144 women aged between 55 and 90 years who were free of CHD at baseline. During that follow-up period, 389 women experienced a CHD event and 921 women died without prior CHD event. Only 41 women of those event-free had less than 10 years of follow-up. We randomly split the data set into a training data set (2763 women with 249 CHD events) and a validation data set (1381 women with 140 CHD events).

Using the training set, we estimated the parameters of a Fine–Gray regression model which included the “traditional” baseline risk factors for CHD: age, treatment for high blood pressure (yes versus no), systolic blood pressure (separate slopes depending on whether the subject was on blood pressure treatment or not), diabetes mellitus, log-transformed total cholesterol to HDL cholesterol ratio, and smoking status (current versus never or former smoker). All these risk factors were associated with an increased CHD risk and, except for diabetes, all reached conventional significance (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$p<0.05$\end{document}
````
). We also investigated the role of age, the strongest predictor variable, as a simple marker for CHD.

Concordance estimates were obtained for these models in the validation set. The dependence of the censoring distribution on the covariates was investigated with a Cox regression model which yielded no trends and non-significant Wald tests for all variables. Thus, all IPCW estimates of concordance were based on the marginal Kaplan–Meier estimator for the censoring distribution from the validation set.

The left panel of Figure 1 shows the discrimination ability of the two Fine–Gray models for varying time horizons between 1 and 10 years. The model including all risk factors shows higher discriminative ability compared with the model based on age alone. For both models, concordance estimates stabilize after about 2.5 years of follow-up and remain fairly stable though slightly decreasing. The decrease may occur because earlier events are easier to predict than later events.
Fig. 1.

Left panel: IPCW estimates of 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````
 for the multiple Fine and Gray model (solid line) and the model with age as the only covariate (dashed line) for a follow-up duration of 1–10 years in the validation data. Error bars at 2.5, 5, 7.5, and 10 years of follow-up correspond to bootstrap standard errors. Right panel: time-dependent receiver operating characteristic curve at time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t=10$\end{document}
````
 years for the multiple Fine and Gray model (solid line) and the model with age as the only covariate (dashed line) in the validation data. Cases were defined as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T\leq t$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D = 1$\end{document}
````
, controls as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T>t$\end{document}
````
 or 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=2$\end{document}
````
.

[ORIGINAL IMAGE / POSSIBLE FORMULA: kxt05901.jpg; not reconstructed]

The right panel of Figure 1 shows time-dependent ROC curves at time 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t=$\end{document}
````
10 years for the two models. For this graph, cases were defined as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T\leq t$\end{document}
````
 and 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D = 1$\end{document}
````
, controls as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T>t$\end{document}
````
 or 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=2$\end{document}
````
. Estimation was also based on IPCW-weighting as implemented in the R package 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$timeROC$\end{document}
````
 (Blanche and others, 2013).

Table 3 shows the estimated concordance for predicting CHD and non-CHD death, respectively, during the 10 years follow-up in the validation data. The Fine and Gray model for non-CHD death used the same covariates as the model for CHD. Age alone is a strong predictor for non-CHD death in this elderly population but the multiple Fine and Gray model did not substantially improve concordance. This is not surprising as most additional covariates are established CHD-specific risk factors which would not be expected to strongly affect non-CHD death (except for other deaths related to the cardiovascular system).

Table 3.

Estimated concordance and AUC measures in the validation data of the CHD study for both competing risks 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$($\end{document}
````
in 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$\%)$\end{document}
````


CHDNon-CHD death
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_1(t)$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathrm {AUC}}(t)_{1,C1}$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathrm {AUC}}(t)_{1,C2}$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathcal C}_2(t)$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathrm {AUC}}(t)_{2,C1}$\end{document}
````

````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathrm {AUC}}(t)_{2,C2}$\end{document}
````
Age only63.772.364.375.780.878.0Fine–Gray71.679.472.476.281.378.6
Truncation point for concordance is 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t=10$\end{document}
````
 years. AUC measures are also reported at 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t=10$\end{document}
````
 years. Cumulative cases were defined for both AUC measures as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T\leq t$\end{document}
````
 and D = “event type studied” (CHD or non-CHD death, respectively), controls as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T>t$\end{document}
````
 for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\rm AUC}(t)_{\cdot ,C1}$\end{document}
````
 and as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T>t$\end{document}
````
 or D = “other event type” for 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathrm {AUC}}(t)_{\cdot ,C2}$\end{document}
````
.




Table 3 also displays time-dependent AUC measures at 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$t=10$\end{document}
````
 years in the validation data using two different definitions of controls (Blanche and others, 2013). AUCs with controls defined as subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T>t$\end{document}
````
 or 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=\text {``other event type''}$\end{document}
````
 (consistently with our concordance definition) were slightly higher but comparable with the concordance whereas AUCs using only subjects with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T>t$\end{document}
````
 as controls were substantially higher. This could be explained by the fact that age is a strong predictor of both CHD and non-CHD death which hampers discrimination of CHD events from non-CHD deaths.


6.

### Discussion


We have presented a formal definition of the concordance probability for prognostic models in the presence of competing risks. Like the concordance probability for survival or binary data, it provides a simple overall numeric measure of discrimination. To deal with right-censored data, we derived an IPCW estimator of the truncated concordance probability and established consistency and asymptotic normality under mild assumptions. Asymptotic properties of the proposed estimator rely on the assumption that the censoring distribution is correctly specified and conditionally independent of the competing risks process given covariates. In many applications, it will be reasonable to assume that the censoring mechanism does not depend on covariates and then the marginal Kaplan–Meier estimate of the censoring distribution can be used. However, if for some reason the design or conduct of a clinical study introduced a dependence between the follow-up duration and covariates which also affect the competing risks process (any component, including the cause-specific hazards of competing events), then it is recommended to use a working regression model for the censoring distribution in order to avoid biased conclusions.

The fact that we estimate a truncated version of concordance rather than the unconstrained concordance probability should not be seen as a limitation of our approach. Indeed it is impossible to assess the performance of prognostic models beyond the maximum follow-up duration without strong and untestable assumptions. If we assume independent censoring, our estimator is defined if we truncate at any time before or at the largest observed censoring or event time. As for the Kaplan–Meier estimator, the effect of censoring on the variability of the IPCW estimator is increasing with increasing truncation time. However, it is difficult to recommend a general purpose truncation time, in particular because the truncation time point influences the interpretation of the concordance probability. To avoid unstable results in practical applications, we recommend that the analyst develops an appropriate model for the censoring distribution, e.g. the Kaplan–Meier estimator or a Cox model, and then investigates the predicted probabilities of being uncensored at the candidate truncation times. Multiple truncation time points can be evaluated and it can be useful to compare discrimination ability at different truncation time points. A model which is good at discriminating patients with an early failure time (e.g. after surgery) from others may not be good at discriminating subsequent failure times amongst patients who survive a first high risk period.

As discussed in Appendix C of supplementary material available at Biostatistics online, our approach is related to time-dependent sensitivity, specificity, and ROC curves for competing risks (Saha and Heagerty, 2010) and the concordance can be written as a weighted average of the time-dependent 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}${\mathrm {AUC}}(s)$\end{document}
````
 for incident cases (
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T=s$\end{document}
````
, 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=1$\end{document}
````
) and controls defined as observations with 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$T>s$\end{document}
````
 or 
````latex
\documentclass[12pt]{minimal}
\usepackage{amsmath}
\usepackage{wasysym} 
\usepackage{amsfonts} 
\usepackage{amssymb} 
\usepackage{amsbsy}
\usepackage{upgreek}
\usepackage{mathrsfs}
\setlength{\oddsidemargin}{-69pt}
\begin{document}
}{}$D=2$\end{document}
````
. Thus, the concordance serves as an overall summary of discrimination whereas the time-dependent AUC measures discrimination of the event status at one specific time point.

We assumed that the prognostic model was derived on an independent training data set and only in this setting are asymptotic or bootstrap confidence intervals for the truncated concordance readily available. Clearly, independent training data are not always available, and even if they are, a joint analysis of all data will be more efficient. However, some form of internal cross-validation is needed to develop and assess a prognostic model with a single data set (Efron and Tibshirani, 1997; Gerds and others, 2008; Hastie and others, 2009).

It is important to emphasize that our definition of concordance assesses a prognostic model for the absolute risk of the event of interest in the presence of competing risks. In line with earlier work (Gail and Pfeiffer, 2005; Wolbers and others, 2009), we regard this risk as crucial for medical decision-making in the competing risks setting. However, in many instances explicit consideration of competing events will also be important and modeling the entire competing risks multi-state process will provide further insights (Beyersmann and others, 2007). As an example, our illustration of concordance for a single marker (presented in supplementary material available at Biostatistics online) shows that discrimination of prognostic models for the event of interest is hampered if covariates affect both cause-specific hazards with regression coefficients of the same sign, especially if there is a strong association with the competing risk or if the baseline competing hazard is high. This indicates that to achieve high discrimination ability one needs predictors which are only weakly or, even better, reversely associated with the cause-specific hazard of the competing event. Moreover, in settings where all competing events are of similar importance, joint accuracy criteria for the entire competing risks multi-state process are needed and their development is an important area for future research.




### Supplementary material


Supplementary material is available at http://biostatistics.oxfordjournals.org.




### Funding


M.W. was supported by the Wellcome Trust and the Li Ka Shing Foundation—University of Oxford Global Health Programme. Funding to pay the Open Access publication charges for this article was provided by the Wellcome Trust.




### Supplementary Material




### Supplementary Data






### Acknowledgments


Computer time for this study was provided by the computing facilities MCIA (Mésocentre de Calcul Intensif Aquitain) of the Université de Bordeaux and of the Université de Pau et des Pays de l’Adour. Conflict of Interest: None declared.


### References


BenderR.AugustinT.BlettnerM.Generating survival times to simulate Cox proportional hazards modelsStatistics in Medicine200524171317231572423210.1002/sim.2059

BeyersmannJ.DettenkoferM.BertzH.SchumacherM.A competing risks analysis of bloodstream infection after stem-cell transplantation using subdistribution hazards and cause-specific hazardsStatistics in Medicine200726536053691763497410.1002/sim.3006

BickelP. J.KlaassenC. A.RitovY.WellnerJ. A.Efficient and Adaptive Estimation for Semiparametric Models1993BaltimoreJohns Hopkins University Press

BlancheP.DartiguesJ.-F.Jacqmin-GaddaH.Estimating and comparing time-dependent areas under receiver operating characteristic curves for censored event times with competing risksStatistics in Medicine201332538153972402707610.1002/sim.5958

ChengS. C.FineJ. P.WeiL. J.Prediction of cumulative incidence function under the proportional hazards modelBiometrics1998542192289544517

EfronB.TibshiraniR.Improvements on cross-validation: the .632+ bootstrap methodJournal of the American Statistical Association199792548560

FineJ. P.GrayR. J.A proportional hazards model for the subdistribution of a competing riskJournal of the American Statistical Association1999446496509

GailM. H.PfeifferR. M.On criteria for evaluating models of absolute riskBiostatistics200562272391577210210.1093/biostatistics/kxi005

GerdsT. A.CaiT.SchumacherM.The performance of risk prediction modelsBiometrical Journal2008504574791866375710.1002/bimj.200810443

GerdsT. A.KattanM. W.SchumacherM.YuC.Estimating a time-dependent concordance index for survival prediction models with covariate dependent censoringStatistics in Medicine201332217321842317275510.1002/sim.5681

GerdsT. A.ScheikeT. H.AndersenP. K.Absolute risk regression for competing risks: interpretation, link functions, and predictionStatistics in Medicine201231392139302286570610.1002/sim.5459PMC4547456

GrunkemeierG. L.JinR.EijkemansM. J.TakkenbergJ. J.Actual and actuarial probabilities of competing risks: apples and lemonsAnnals of Thoracic Surgery200783158615921746236310.1016/j.athoracsur.2006.11.044

HarrellF. E.CaliffR. M.PryorD. B.LeeK. L.RosatiR. A.Evaluating the yield of medical testsJournal of the American Medical Association1982247254325467069920

HastieT.TibshiraniR.FriedmanJ. H.The Elements of Statistical Learning20092nd editionNew YorkSpringerSpringer Series in Statistics.

HeagertyP. J.ZhengY.Survival model predictive accuracy and ROC curvesBiometrics200561921051573708210.1111/j.0006-341X.2005.030814.x

HofmanA.van DuijnC. M.FrancoO. H.IkramM. A.JanssenH. L.KlaverC. C.KuipersE. J.NijstenT. E.StrickerB. H.TiemeierH.The Rotterdam Study: 2012 objectives and design updateEuropean Journal of Epidemiology201126657686and others2187716310.1007/s10654-011-9610-5PMC3168750

KollerM. T.LeeningM. J.WolbersM.SteyerbergE. W.HuninkM. G.SchoopR.HofmanA.BucherH. C.PsatyB. M.Lloyd-JonesD. M.Development and validation of a coronary risk prediction model for older U.S. and European persons in the cardiovascular health study and the Rotterdam StudyAnnals of Internal Medicine2012157389397and others2298637610.7326/0003-4819-157-6-201209180-00002PMC3644640

KollerM. T.RaatzH.SteyerbergE. W.WolbersM.Competing risks and the clinical community: irrelevance or ignorance?Statistics in Medicine201231108910972195340110.1002/sim.4384PMC3575691

MogensenU. B.IshwaranH.GerdsT. A.Evaluating random forests for survival analysis using prediction error curvesJournal of Statistical Software20125012310.18637/jss.v050.i11PMC419419625317082

NCEPThird Report of the National Cholesterol Education Program (NCEP) Expert Panel on Detection, Evaluation, and Treatment of High Blood Cholesterol in Adults (Adult Treatment Panel III) final reportCirculation20021063143342112485966

PutterH.FioccoM.GeskusR. B.Tutorial in biostatistics: competing risks and multi-state modelsStatistics in Medicine200726238924301703186810.1002/sim.2712

SahaP.HeagertyP. J.Time-dependent predictive accuracy in the presence of competing risksBiometrics20106699910112007029610.1111/j.1541-0420.2009.01375.xPMC4512205

ScheikeT.ZhangM. J.GerdsT. A.Predicting cumulative incidence probability by direct binomial regressionBiometrika200895205220

SchoopR.BeyersmannJ.SchumacherM.BinderH.Quantifying the predictive accuracy of time-to-event models in the presence of competing risksBiometric Journal2011538811210.1002/bimj.20100007321259311

UnoH.CaiT.PencinaM. J.D'AgostinoR. B.WeiL. J.On the C-statistics for evaluating overall adequacy of risk prediction procedures with censored survival dataStatistics in Medicine201130110511172148484810.1002/sim.4154PMC3079915

WolbersM.KollerM. T.WittemanJ. C.SteyerbergE. W.Prognostic models with competing risks: methods and application to coronary risk predictionEpidemiology2009205555611936716710.1097/EDE.0b013e3181a39056

YanG.GreeneT.Investigating the effects of ties on measures of concordanceStatistics in Medicine200827419042061838418710.1002/sim.3257

ZhengY.CaiT.JinY.FengZ.Evaluating prognostic accuracy of biomarkers under competing riskBiometrics2012683883962215057610.1111/j.1541-0420.2011.01671.xPMC3694786
