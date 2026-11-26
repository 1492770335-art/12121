# The Sovereign Risk Amplifies ESG Market Extremes: A Quantile-Based Factor Analysis

Original PDF: [original.pdf](original.pdf). SHA256: `f833f68b13564047fccfdbac7d7012fd70beb3cd1e69cf7c62259e0828006158`.

This is an unedited technical text extraction, not a mathematical transcription or translation. Physical PDF page numbers are preserved below. PDF page labels and candidate printed numbers are recorded separately; candidate printed numbers are not verified pagination. Formula glyphs, fractions, superscripts, subscripts, reading order and equation numbers require comparison with the original PDF. No equation has been reconstructed or corrected. Original licensed TeX, where available, takes precedence for formula reading.

## PDF page 1

Technical extraction; compare with original PDF page 1.

````text
Academic Editor: Paolo Giudici
Received: 12 October 2025
Revised: 22 November 2025
Accepted: 1 December 2025
Published: 10 December 2025
Citation: Orozco-Cerón, Oscar
Walduin, Orlando Joaqui-Barandica,
and Diego F. Manotas-Duque. 2025.
The Sovereign Risk Amplifies ESG
Market Extremes: A Quantile-Based
Factor Analysis. Risks 13: 245.
https://doi.org/10.3390/
risks13120245
Copyright: © 2025 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license
(https://creativecommons.org/
licenses/by/4.0/).
Article
The Sovereign Risk Amplifies ESG Market Extremes:
A Quantile-Based Factor Analysis
Oscar Walduin Orozco-Cerón 1,2,*, Orlando Joaqui-Barandica 1
and Diego F. Manotas-Duque 1
1
School of Industrial Engineering, Universidad del Valle, Cali 760001, Colombia;
orlando.joaqui@correounivalle.edu.co (O.J.-B.); diego.manotas@correounivalle.edu.co (D.F.M.-D.)
2
Department of Economics and Finance, Pontificia Universidad Javeriana, Cali 760001, Colombia
*
Correspondence: oscar.w.orozco@correounivalle.edu.co
Abstract
This study examines how sovereign risk shapes the financial performance of sustainable
investments, using the MSCI Emerging Markets ESG Index as a reference. The analysis
covers 24 emerging and frontier economies from Latin America, Asia, the Middle East,
and Eastern Europe during 2016–2025, a period marked by major global disruptions such
as the COVID-19 crisis and post-2022 financial tightening. Sovereign risk dimensions are
extracted through Principal Component Analysis (PCA) applied to sovereign CDS spreads,
identifying a systemic component linked to global shocks and a structural component
associated with domestic fundamentals and governance quality. These factors are inte-
grated into a quantile regression framework alongside control variables—oil prices, interest
rates, and global equity indices—capturing key macro-financial transmission channels.
Results show a nonlinear, quantile-dependent relationship: systemic risk intensifies ESG
losses under adverse conditions, while structural improvements support gains in upper
quantiles. Control variables behave as expected, confirming the macro-financial sensitivity
of ESG performance. The findings reveal that ESG returns are state-dependent and strongly
influenced by sovereign credit dynamics, especially in emerging markets where external
shocks and institutional fragility intersect. Strengthening sovereign governance and inte-
grating risk diagnostics into ESG assessments are essential steps to enhance resilience and
credibility in sustainable finance.
Keywords: sovereign risk; ESG; sustainability; quantile regression; emerging markets
1. Introduction
Sovereign credit risk remains a central source of uncertainty in global financial markets,
influencing investor confidence and capital allocation. A sound and widely accepted
measure of this risk is the sovereign credit default swap (CDS) spread, which reflects
market expectations of default probability and reacts swiftly to macroeconomic shocks,
geopolitical tensions, or fiscal imbalances. Beyond their financial role, CDS spreads provide
a valuable framework for analyzing how market-based risk perceptions interact with
environmental, social, and governance (ESG) factors—an increasingly relevant issue in
sustainable finance.
This study addresses the following research question: to what extent does sovereign
risk affect the financial performance of ESG investments across different market conditions?
Its main objective is to identify and quantify the asymmetric effects of systemic and struc-
tural sovereign risk on ESG returns, assessing their implications for financial stability and
investment resilience.
Risks 2025, 13, 245
https://doi.org/10.3390/risks13120245

````

## PDF page 2

FORMULA CHECK REQUIRED: original PDF page 2.

````text
Risks 2025, 13, 245
2 of 23
Practically, this analysis helps investors and policymakers better understand the
transmission of sovereign risk into ESG markets, offering guidance to strengthen sustainable
investment strategies and align them with macro-financial risk management.
At the firm level, empirical evidence points to a general risk-reducing effect of ESG
performance, though with notable variations. Anthony and Ajay (2024), using a compre-
hensive U.S. CDS database, found that ESG ratings significantly lower perceived credit
risk, although this mitigating effect declines as the maturity of the instruments increases.
Similarly, Caiazza et al. (2023) reported that higher ESG scores are negatively associated
with CDS spreads among S&P 500 firms, even after controlling for contract features and
financial crises. Zhao and Zhu (2024) further demonstrated that firms using CDS as hedging
instruments exhibit better ESG performance, particularly those facing high leverage and
financial constraints.
Nevertheless, the relationship is not homogeneous. Barth et al. 2022, identified a
U-shaped association between ESG scores and CDS spreads, mediated by asset volatility,
suggesting nonlinear effects across different ESG rating levels. Anand et al. (2023), also
highlighted that the influence of ESG ratings on credit spreads varies significantly across
data providers, reflecting inconsistencies and the lack of standardization in sustainability
metrics. Other studies have emphasized the informational and perceptual dimensions of
ESG risk. Tang et al. (2024) found that public perceptions of sustainability—especially
following major policy events such as the Kyoto Protocol—contribute to lower CDS spreads
in East Asia, particularly in contexts of uncertainty. Likewise, Naumer and Yurtoglu (2022)
showed that both the tone and the source of ESG-related news affect credit markets: positive
news can reduce CDS spreads by up to 4%, while negative news can increase financing costs
by around 6%. From a pricing and structural risk perspective, recent approaches based
on contingent claims and market-based risk premia (Michopoulos et al. 2025; Hauch 2025)
reinforce the idea that ESG is embedded within asset valuation mechanisms, transcending
its reputational interpretation.
On the sovereign side, the literature is more limited but points in a similar direction.
Some evidence supports a negative relationship between sovereign ESG ratings and CDS
premiums, suggesting that sustainability can act as a buffer against macro-financial volatil-
ity (Karaman 2022; Hübel 2022; Zhao 2025). However, most of these findings rely on linear
estimation frameworks that overlook potential nonlinearities, asymmetries, and spillover
effects—despite increasing recognition that sovereign risk transmission operates in com-
plex, state-dependent ways (Bajaj et al. 2022). Recent efforts to link ESG and sovereign risk
contagion through VAR or panel models (Zhao 2025; Öcal and Kamil 2021), have improved
understanding of the average interaction but remain limited in capturing tail-risk dynamics
and asymmetric responses.
Furthermore, cross-level analyses combining firm- and country-level ESG data
(Gianfrate et al. 2024; Ballester et al. 2024) highlight the heterogeneity of effects across
geographies and market conditions, with even contradictory results depending on sectoral
and regional contexts.
In view of this fragmented and partly contradictory evidence, this paper contributes
by explicitly modeling the asymmetric response of ESG-based equity returns to sovereign
credit risk, using a quantile-based approach that captures nonlinearities across the entire
conditional distribution. This framework responds to the need for more refined empirical
tools to analyze risk transmission (Barth et al. 2022; Kiesel and Lücke 2019) and provides
new insights into how sovereign risk dynamics shape sustainable investment strategies
under varying market regimes, particularly during periods of heightened financial stress.
This study applies to a quantile regression framework to assess the heterogeneous impact
of sovereign risk on MSCI ESG index returns. Latent risk factors are extracted through

````

## PDF page 3

FORMULA CHECK REQUIRED: original PDF page 3.

````text
Risks 2025, 13, 245
3 of 23
PCA from a wide panel of sovereign CDS data, following Joaqui-Barandica et al. (2023)
in estimating a global risk component. The results reveal that systemic shocks intensify
ESG losses under stress but enhance gains in favorable markets, indicating that ESG
performance is state-dependent and sensitive to sovereign credit dynamics—an insight
relevant for sustainable portfolio management and policy design. Theoretically, sovereign
risk affects ESG returns through both financial and confidence channels. Rising sovereign
spreads signal macro-financial stress, leading to portfolio rebalancing and capital outflows
that depress ESG valuations, particularly in emerging markets. Conversely, during stable
or expansionary periods, improved sovereign credibility enhances investor confidence and
reinforces ESG performance. This asymmetry explains why the impact of sovereign risk is
expected to differ across quantiles of the return distribution.
Taken together, prior findings suggest two state-dependent hypotheses for ESG equity
markets: (i) under adverse conditions (lower quantiles), a global sovereign-risk factor
extracted from CDS should exacerbate downside ESG returns; (ii) under favorable condi-
tions (upper quantiles), improvements in sovereign risk should be associated with stronger
ESG performance. We also expect these effects to be stronger when global risk appetite
dominates idiosyncratic fundamentals, consistent with earlier CDS evidence. The sample
covers the period from June 2016 to July 2025. The inclusion of 2025 reflects the most
recent available data at the time of analysis, updated through mid-year observations. This
ensures that trends are captured without introducing forward-looking bias, and potential
sampling imbalances were checked and found not to affect the robustness of results. A key
empirical challenge is the potential endogeneity between sovereign risk and ESG returns,
as both may respond to shared macroeconomic shocks. This issue is addressed through
the use of lagged variables, PCA-derived orthogonal factors, and robustness checks that
mitigate reverse causality and omitted variable bias. A key empirical challenge is the
potential endogeneity between sovereign risk and ESG returns, as both may respond to
shared macroeconomic shocks. This issue is addressed through the use of lagged variables,
PCA-derived orthogonal factors, and robustness checks that mitigate reverse causality and
omitted variable bias.
Our contribution thus complements sovereign-ESG studies that document average
negative associations between sustainability metrics and sovereign risk by focusing on
distributional effects and tail behavior. It also connects to the growing quantile-based
spillover literature in sustainable finance by linking latent sovereign risk factors to the
conditional distribution of ESG returns—a perspective largely absent from linear, mean-
based designs.
The remainder of the paper is organized as follows: Section 2 presents the materials
and methods used. Section 3 presents the main empirical results and offers a critical
discussion on the implications of the asymmetric behavior of ESG returns in the face of
sovereign risk. Finally, Section 4 summarizes the study’s conclusions.
2. Literature Review
2.1. Sovereign Risk and Systemic Risk
Sovereign risk represents a fundamental component of macro-financial vulnerability,
reflecting a country’s ability to meet its debt obligations and the market’s perception of its
fiscal and institutional soundness. The recent literature highlights that sovereign Credit
Default Swaps (CDS) act as leading indicators of financial stress and latent risk transmission,
especially in globally integrated markets. During periods of turbulence, the CDS market
tends to incorporate new information on sovereign risk faster than the bond market,
capturing both domestic fundamentals and external shocks (Tampakoudis et al. 2020).

````

## PDF page 4

FORMULA CHECK REQUIRED: original PDF page 4.

````text
Risks 2025, 13, 245
4 of 23
Moreover, Hübel (2022) provides evidence that sovereign credit curves increasingly
internalize ESG-related risks, suggesting a gradual shift toward a multidimensional
understanding of sovereign risk where fiscal sustainability interacts with environmen-
tal and governance factors. Corsetti et al.
(2012) further emphasizes that structural
determinants—such as institutional quality, fiscal transparency, and macroeconomic
stability—play a decisive role in shaping sovereign risk perceptions and systemic vul-
nerability across emerging economies.
In essence, the literature converges on the idea that sovereign risk cannot be analyzed
in isolation from global financial interdependence and governance quality, both of which
form the basis for its inclusion as a latent factor in risk–return models.
CDS spreads offer a key advantage by providing real-time signals of sovereign risk and
financial stress, integrating economic, fiscal, and geopolitical information efficiently. Studies
such as Hübel (2022) show that they increasingly reflect ESG dimensions, enriching risk
assessment. However, in emerging markets, limited liquidity and inconsistent ESG data can
distort results, so integrating these factors requires caution to preserve analytical accuracy.
2.2. Sustainable Investments and Financial Performance (ESG)
The financial performance of environmental, social, and governance (ESG) invest-
ments has become a major topic in sustainable finance, yet empirical results remain mixed.
Several recent studies suggest that ESG portfolios exhibit superior resilience during market
downturns. For instance, Aldieri et al. (2023) finds a positive and statistically significant
relationship between corporate ESG scores and risk-adjusted performance, implying that
sustainability factors can mitigate exposure to market shocks. Similarly, Broadstock et al.
(2021) show that firms with stronger ESG profiles experienced lower volatility and smaller
losses during the COVID-19 crisis, supporting the hypothesis that ESG criteria contribute
to systemic resilience.
However, the debate over whether ESG portfolios systematically outperform tradi-
tional assets persists. The comprehensive meta-analysis by Friede et al. (2015)—covering
more than 2000 empirical studies—concludes that while the majority of findings indicate a
non-negative relationship between ESG performance and financial returns, the strength and
direction of the effect depend heavily on regional, temporal, and methodological factors.
Overall, the literature suggests that ESG investing may not always maximize returns,
but it consistently enhances risk management and portfolio stability, particularly under
adverse macroeconomic conditions.
ESG investments have shown greater resilience during market downturns, as studies
like Aldieri et al. (2023) and Broadstock et al. (2021) demonstrate that higher ESG scores
are linked to lower volatility and improved risk-adjusted returns. However, evidence on
consistent outperformance remains mixed. Friede et al. (2015) find that most studies report
a non-negative relationship between ESG and financial performance, though results vary
by region and method. In general, ESG investing strengthens portfolio stability and risk
management, even if it does not always maximize returns.
2.3. Sovereign Risk and ESG Performance
Recent research has increasingly explored how sovereign risk dynamics are shaped
by environmental, social, and governance (ESG) conditions, particularly in emerging
economies where institutional frameworks and policy effectiveness remain uneven. A grow-
ing body of evidence suggests that sovereign creditworthiness is no longer determined
solely by fiscal or macroeconomic fundamentals, but also by the sustainability and gov-
ernance quality underpinning national policies. For example, Naifar (2023) provides
empirical evidence that climate-related vulnerabilities significantly increase sovereign CDS

````

## PDF page 5

FORMULA CHECK REQUIRED: original PDF page 5.

````text
Risks 2025, 13, 245
5 of 23
spreads, indicating that countries more exposed to environmental risk face elevated fi-
nancing costs. Similarly, Capelle-Blancard et al. (2019) show that better sovereign ESG
performance is associated with lower sovereign borrowing costs, particularly within the
OECD context. These studies together emphasize that sustainability and sovereign credit
risk are closely connected, and that integrating macro-financial risk assessment into ESG
investment frameworks is essential to improve resilience, pricing accuracy, and policy
credibility in the context of sustainable finance.
Incorporating ESG factors into sovereign risk analysis allows for a deeper understand-
ing of long-term credit stability by linking financial performance with environmental and
governance quality. This perspective strengthens risk forecasting and aligns investment
decisions with sustainability goals. Nonetheless, its main limitation is the uneven qual-
ity and availability of ESG data across countries, which may distort comparisons and
weaken the reliability of risk assessments, particularly in developing economies with less
transparent institutions.
2.4. PCA in Banking and Finance
Principal Component Analysis (PCA) and related common-factor methodologies have
become central tools in modern banking and financial research, enabling the extraction
of underlying economic forces from high-dimensional datasets. In the context of banking
performance, dynamic factor models reveal that a small number of latent cyclical market
forces explain most of the variation in U.S. banks’ profitability, with household financial
burden, economic activity, income dynamics, and market stress emerging as dominant
drivers (Joaqui-Barandica et al. 2023). This line of research highlights how factor structures
improve interpretability, support the identification of systemic vulnerabilities, and provide
policy-relevant signals for financial-stability monitoring.
Similarly, factor-based panel methods have been applied to macroeconomic puzzles
such as the Feldstein–Horioka correlation between savings and investment. By isolating
idiosyncratic components through common-factor extraction, researchers have shown
that the strength of the puzzle varies across periods and regions, suggesting that global
integration dynamics evolve over time (Bai and Ng 2002). This evidence reinforces the
usefulness of PCA as a tool to decompose aggregate comovements and reassess long-
standing empirical regularities in international macroeconomics.
Advances in the econometric foundations of PCA, particularly those that determine the
number of primitive shocks driving macroeconomic fluctuations, have further strengthened
this methodological framework. Bai and Ng (2007) develop procedures to infer the number
of dynamic factors from large datasets by examining the eigenvalue structure of residual
covariance matrices, formalizing the relationship between static and dynamic factors and
providing a rigorous basis for dimension selection in empirical macro-finance.
The integration of PCA with structural macroeconomic frameworks is exemplified by
factor-augmented VAR (FAVAR) models, which address the limited-information problem
inherent in traditional VARs. By incorporating information from hundreds of economic
indicators into a small set of estimated factors, FAVAR models enhance the identification
of monetary policy shocks and mitigate measurement issues in observed macro variables.
Bernanke et al. (2005) show that FAVAR-based impulse responses provide a richer and
more coherent depiction of the monetary transmission mechanism than standard VARs,
particularly when the central bank and private agents rely on broader information sets.
Across these strands of research, PCA and factor-based methods prove particularly
effective for extracting market-wide forces that drive banking performance, decomposing
aggregate co-movements in macroeconomic puzzles, and incorporating large-scale infor-
mation into policy-relevant models. Their application enables researchers to model latent

````

## PDF page 6

Technical extraction; compare with original PDF page 6.

````text
Risks 2025, 13, 245
6 of 23
financial dynamics, isolate structural sources of variation, and integrate high-dimensional
datasets into empirical frameworks used in banking, macro-finance, and monetary analysis.
3. Materials and Methods
The methodological framework combines Principal Component Analysis (PCA) and
quantile regression (QR) to analyze the link between sovereign risk and ESG returns. The
sample includes emerging and developed economies to capture cross-market heterogeneity,
using the MSCI ESG Index as a benchmark for sustainable investment performance. PCA
is employed because sovereign CDS spreads co-move due to global risk and contagion
effects (Giudici and Pagnottoni 2019), making dimensionality reduction suitable to identify
latent systemic factors. QR is applied to explore asymmetric and tail effects across the
conditional distribution of ESG returns, offering richer insights than mean-based estimators
(Koenker and Xiao 2006; Reboredo and Ugolini 2016; Mensi et al. 2021). The retained
components satisfy the Kaiser criterion and explain over 70% of the variance, ensuring rep-
resentativeness of common variation in CDS spreads. Loadings were stable over time, with
the first component capturing systemic shocks and the second reflecting structural shifts
(Longstaff et al. 2011). To account for external drivers of sovereign and ESG co-movements,
the specification incorporates global control variables such as major commodity prices and
international financial conditions. Although direct proxies of global risk appetite—such as
the VIX or portfolio-flow indicators—are widely used in the literature, the selected controls
already embed the information these measures capture, given their high correlation with
global sentiment and capital-reallocation dynamics. Including additional proxies would
add limited explanatory value while increasing multicollinearity, making the parsimonious
set of controls employed here both economically and econometrically appropriate.
3.1. Data
This study employs two primary data sources: sovereign credit default swaps (CDS)
and the MSCI Emerging Markets SRI Index. The sovereign CDS data consist of daily time
series for 5-year USD-denominated contracts across 24 emerging economies represented
in the MSCI Emerging Markets SRI Index, namely Brazil, Chile, China, Colombia, Czech
Republic, Egypt, Greece, Hungary, India, Indonesia, Korea, Kuwait, Malaysia, Mexico,
Peru, Philippines, Poland, Qatar, Saudi Arabia, South Africa, Taiwan, Thailand, Turkey,
and the United Arab Emirates. The choice of emerging markets is particularly relevant,
as these economies often exhibit greater exposure to global systematic risk factors and
higher sensitivity to shifts in ESG-related performance and governance standards. Their
structural heterogeneity—spanning different stages of economic development, institutional
maturity, and financial depth—offers a unique testing ground to evaluate how sovereign
risk perceptions evolve under varying ESG conditions. Data were extracted from Refinitiv
Workspace, ensuring harmonized frequency and consistent formatting across countries.
Each CDS series captures the spread that reflects the premium demanded by investors to
insure sovereign debt against a five-year credit event. To ensure consistency and mitigate
market microstructure noise, the “Mid” quote was adopted as the benchmark reference for
each contract. All instruments share standardized attributes: sovereign issuer classification,
5-year maturity, USD denomination, senior unsecured status, and inclusion of the Cum-
Restructuring clause as per the 2014 ISDA Protocol. The preferred data sources for each
series were Markit 5Yr Liquid EOD, Refinitiv EOD, and Markit EOD, selected based on
data completeness and reliability.
Due to the absence of a liquid sovereign CDS for Taiwan in Refinitiv’s coverage, we
adopt the CDS of the Bank of Taiwan as a proxy. This financial institution is state-owned and
closely linked to the Taiwanese government, which allows it to partially reflect the country’s

````

## PDF page 7

Technical extraction; compare with original PDF page 7.

````text
Risks 2025, 13, 245
7 of 23
systemic sovereign risk. While this substitution introduces a methodological limitation, its
justification is grounded in institutional linkages, and it may be further complemented by
structural indicators such as sovereign credit ratings in robustness checks.
The second key dataset used in the analysis is the MSCI Emerging Markets SRI Index,
denominated in USD and calculated on a gross return basis. This equity benchmark is
composed of large- and mid-cap companies from emerging markets that demonstrate
superior ESG performance. Constituents are selected using a best-in-class ESG screening
methodology based on MSCI ESG Research, combined with negative filters to exclude firms
involved in controversial business activities such as tobacco, weapons, and other socially
or environmentally detrimental sectors. The index includes companies from 24 emerging
market countries and is weighted by free-float adjusted market capitalization to reflect
investability. Selection is further refined through an assessment of ESG controversy scores
and intra-sectoral ESG ratings.
Geographically, the index exhibits significant concentration in Asia, with Taiwan,
China, and India representing 30.18%, 23.47%, and 11.72% of the total weight, respectively,
(Table 1). This geographic composition makes the index particularly sensitive to systemic
risk events originating in Asia or in other emerging markets. As such, it provides a relevant
benchmark for evaluating the financial performance of ESG-compliant portfolios under
varying macroeconomic and sovereign risk conditions.
Table 1. Country Weights in the MSCI Emerging Markets SRI Index.
Country
Weight (%)
Taiwan
30.18
China
23.47
India
11.72
South Korea
9.77
South Africa
9.18
Other
15.68
Table 2 reports the sectoral composition of the MSCI Emerging Markets SRI Index
based on free-float adjusted market capitalization. Financials and Information Technology
account for over 50% of the index, with 27.13% and 24.54%, respectively, followed by
Consumer Discretionary (14.8%) and Communication Services (11.93%). The index is
notably underexposed to sectors such as Energy (0.11%) and Utilities (0.6%), reflecting its
ESG screening methodology, which tends to exclude high-carbon or controversial industries.
This sectoral allocation influences the index’s sensitivity to both macroeconomic cycles and
ESG-related risks.
Table 2. Sector Weights in the MSCI Emerging Markets SRI Index.
Sector
Weight (%)
Financials
27.13
Information Technology
24.54
Consumer Discretionary
14.8
Communication Services
11.93
Industrials
5.84
Consumer Staples
4.86
Materials
4.55
Health Care
3.95
Real Estate
1.70
Utilities
0.60
Energy
0.11

````

## PDF page 8

FORMULA CHECK REQUIRED: original PDF page 8.

````text
Risks 2025, 13, 245
8 of 23
Systematic risk plays a predominant role in shaping financial outcomes across emerg-
ing markets, as these economies are structurally more sensitive to global liquidity shocks,
interest rate cycles, and capital flow reversals (Bekaert and Harvey 2003). In this context,
the higher degree of external dependence and institutional heterogeneity observed among
emerging economies intensifies the transmission of global financial stress into domestic
markets, particularly through sovereign credit channels.
To capture this systemic influence, the study applies Principal Component Analysis
(PCA) to standardized sovereign CDS spreads, extracting latent factors that represent
shared and structural dimensions of sovereign risk across countries. The first principal
component captures global or time-varying shocks that simultaneously affect multiple
sovereigns, while the second reflects slower-moving structural dynamics associated with
fiscal and institutional fundamentals (Longstaff et al. 2011; Dieckmann and Plank 2012).
The extracted factors are subsequently incorporated into the quantile regression frame-
work, allowing for the identification of heterogeneous sensitivities across the conditional
distribution of ESG-based returns. This methodological design provides a more complete
characterization of how systemic pressures and domestic fundamentals jointly influence the
behavior of sustainable portfolios under different market regimes. By explicitly modeling
these nonlinear interactions, the approach advances the understanding of ESG performance
in contexts where financial stability and sustainability objectives converge, reinforcing
the empirical relevance of emerging markets as an analytical laboratory for sovereign
risk transmission.
In addition, several control variables were incorporated. As indicators of global
conditions, the differenced logarithm of the US dollar exchange rate was used, which acts
as a proxy for exchange rate risk and the strength of the dollar internationally. Likewise, the
variation in the price of Brent crude oil was considered as a measure of commodity price
shocks, given its importance as a key energy input for emerging economies. To capture the
dynamics of international financial markets, the logarithmic variations in the Nasdaq Index
and the MSCI Emerging Markets Index were used, respectively, representing the behavior
of the US technology market and the aggregate performance of emerging stock markets.
The variation in the US 10-year Treasury bond interest rate was also incorporated as a proxy
for monetary policy and the long-term cost of money. Finally, the logarithmic variation in
the S&P 500 Index was included as a general benchmark for the US stock market and its
potential carryover effect on global returns (Long et al. 2022).
3.2. Quantile Regression Approach
This study evaluates the asymmetric effects of sovereign credit risk on the returns of
the MSCI ESG Leaders Index through a quantile regression (QR) framework. The analysis
spans a cross-country panel of sovereign CDS spreads, from which latent risk factors
are extracted using PCA. This methodology allows us to capture the nonlinear and state-
dependent impact of sovereign risk across the full distribution of ESG returns, particularly
under extreme market conditions.
Quantile regression, as proposed by Koenker and Bassett (1978), is a semi-parametric
approach that estimates the conditional quantile function of the dependent variable, mak-
ing it especially suitable for analyzing heterogeneous effects and tail behavior. Unlike
traditional OLS models, QR does not assume constant variance or normality and is robust
to outliers and non-Gaussian errors. Furthermore, it permits the estimation of predictor
effects not only at the mean but at different points (quantiles) of the conditional distribution,
which is critical for understanding downside risk in ESG performance (Ma and Koenker
2006; Koenker 2004; Uribe and Guillen 2020).

````

## PDF page 9

FORMULA CHECK REQUIRED: original PDF page 9.

````text
Risks 2025, 13, 245
9 of 23
Formally, the conditional quantile function for the q-th quantile is defined as
Qq(Yi,t | Xi,t) = X′
i,tβq
i ,
(1)
where Yi,t represents the returns of the MSCI ESG index, Xi,t is a matrix of covariates
including the extracted PCA-based sovereign risk factors, and βq is the vector of coefficients
to be estimated for quantile q ∈(0,1). The parameters βq are obtained by solving the
following minimization problem:
minβq 1
T
T
∑
t=1
[q −I

Yi,t < X′
i,tβq
i

][Yi,t −X′
i,tβq
i ],
(2)
where I (condition) = 1 if the condition is true, 0 otherwise.
The latent risk factors included in Xi,t were derived from a panel of sovereign CDS
spreads using PCA, following standardization. The objective was to reduce dimension-
ality and address multicollinearity, while preserving the principal sources of variation
in sovereign risk. The model was estimated across a range of quantiles (0.05, until 0.95),
allowing us to capture both downside risk amplification and upside gains associated with
varying levels of sovereign credit stress.
ESG returns was transformed to logarithmic differences to ensure stationarity and
interpretability in terms of returns and shocks. This methodological framework enables
a richer characterization of how sovereign risk transmits into sustainable equity markets
under diverse market regimes, from adverse to favorable states.
3.3. The (Regularized) Iterative PCA Algorithm
To estimate the latent sovereign risk factor ˆF, we employ the Regularized Princi-
pal Components method proposed by Josse and Husson (2012). This technique seeks
to identify a reduced-dimensional subspace that minimizes the reconstruction error be-
tween the original observations and their projections within that subspace. Specifically,
it involves computing two matrices FT×S and UN×S of rank S, with S < T, that offer the
best approximation to the original sovereign CDS data matrix XT×N, with T: Time and N:
Countries. The optimization problem is defined in a least-squares framework to capture the
underlying structure of sovereign credit risk dynamics while addressing potential issues of
multicollinearity and overfitting. The minimization criterion is expressed as follows:
ϑ = || X −M −FU′||2 =
T
∑
t=1
N
∑
n=1
 
Xtn −mn −
S
∑
s=1
FtsUns
!2
,
(3)
where M is a matrix of size T × K with each row equal to (m 1, . . . , mN), i.e., the vector
with the mean of each variable. A common technique that deals with missing values in
PCA is to ignore missing values by minimizing the least-squares criterion in Equation (3)
overall non-missing entries. This can be achieved by introducing a weighted matrix W in
the criterion, where Wtn = 0 if Xtn is missing or Wtn = 1 otherwise:
ϑ =
T
∑
t=1
N
∑
n=1
Wtn
 
Xtn −mn −
S
∑
s=1
FtsUns
!2
.
(4)
The iterative (regularized) PCA algorithm minimizes the criterion in Equation (4).
The Regularized PCA methodology (Josse and Husson 2012) inherently addresses the
possibility of incomplete observations in panel structures. Should any missing entries
arise, the weighted reconstruction criterion in Equation (4) relies exclusively on observed

````

## PDF page 10

Technical extraction; compare with original PDF page 10.

````text
Risks 2025, 13, 245
10 of 23
values, ensuring that factor estimation remains consistent without the need for imputation
or listwise deletion. Given the high completeness and quality of the CDS dataset and the
absence of systematic missingness patterns, additional restrictions such as working with a
balanced subsample would not materially affect the extracted latent factor nor enhance the
interpretation of the empirical results.
4. Results
Figure 1 shows the standardized and PCA-imputed sovereign CDS spreads for
30 emerging and frontier economies from 2016 to mid-2025. The data, expressed as
z-scores, enable cross-country comparison of relative risk fluctuations. Common risk
spikes appear around global shocks—most notably during the 2020 COVID-19 crisis and
again in 2022–2023 amid tighter financial conditions and geopolitical tensions—indicating
a systemic component of sovereign risk. Country-specific volatility remains evident, with
Argentina and Turkey showing persistent instability, while Chile, Taiwan, and South Korea
exhibit steadier trajectories. To summarize these intertwined dynamics, a PCA with im-
puted data was applied to extract latent factors representing the main sources of variation in
CDS spreads. These principal components are subsequently used as explanatory variables
in the quantile regression analysis to assess their effect on financial performance under
different macro-financial contexts.
 
Figure 1. Standardized sovereign CDS time series by country (2016–2025).
Figure 2 shows the correlation circle from the PCA, illustrating how sovereign CDS
spreads move together across countries. The direction and proximity of the vectors indicate
shared risk patterns, with most economies showing strong alignment along the main axis,
suggesting a common global risk factor. Countries such as Colombia, Greece, and Chile

````

## PDF page 11

Technical extraction; compare with original PDF page 11.

````text
Risks 2025, 13, 245
11 of 23
exhibit higher sensitivity to global shocks, while others like South Korea and Taiwan display
more independent dynamics.
 
Figure 2. Correlation circle of sovereign CDS spreads across emerging and frontier economies
(PCA results).
Figure 3 illustrates the first two principal components extracted from the panel of
standardized sovereign CDS spreads for 24 emerging market economies. Each compo-
nent captures a latent risk factor that summarizes the co-movements across countries in
sovereign credit risk over time. The first dimension (Dim.1) explains 52% of variability,
depicted in blue, appears to capture a systemic or global risk factor, with sharp increases
during periods of widespread market stress—most notably around the COVID-19 crisis in
2020 and during episodes of financial tightening in 2022–2023. This component reflects the
synchronized reaction of sovereign risk to global shocks and suggests the existence of a
shared vulnerability across the sovereign credit profiles of the countries in the sample.
In contrast, the second dimension (Dim.2) explains 18% of variability, shown in orange,
follows a smoother and more persistent upward trend over time. This factor may be
interpreted as reflecting structural or medium-term shifts in the cross-country configuration
of risk, such as gradual changes in global risk appetite, commodity dependency, or external
financial conditions. Unlike Dim.1, its dynamics do not exhibit pronounced peaks but rather
a slow-moving trend, suggesting that it may absorb regional or long-term latent forces not
directly tied to sudden global events. The decision to retain two principal components was
guided by both statistical and economic criteria. Beyond the Kaiser rule, the interpretability
of these dimensions was central: Dim.1 captures short-term systemic shocks linked to
global contagion, while Dim.2 embodies slower structural adjustments across economies,
consistent with persistent macro-financial and institutional differences. Together, they

````

## PDF page 12

Technical extraction; compare with original PDF page 12.

````text
Risks 2025, 13, 245
12 of 23
represent the dual nature of sovereign risk transmission—between transient market stress
and deeper structural vulnerabilities. Building on this baseline interpretation, a robustness
exercise was conducted using a Robust Principal Component Analysis (RPCA) framework,
which is specifically designed to separate low-rank common structures from idiosyncratic
noise and outliers in high-dimensional financial data. Applying RPCA to the standardized
sovereign CDS panel leads to a substantial improvement in the explanatory power of the
extracted factors: the first robust component accounts for 68.9% of the total variability,
while the second captures 19.5%, yielding a combined explained variance of 88.5%. These
results reinforce the dual-factor structure identified earlier and while demonstrating that the
underlying risk patterns remain highly stable when using a more resilient decomposition
method. The complete results of this robustness test are reported in Appendix E.
 
Figure 3. Estimated common risk dimensions from PCA on sovereign CDS (2016–2025).
The combined behavior of these two components supports the hypothesis that
sovereign CDS spreads can be decomposed into a small number of underlying drivers,
distinguishing between fast-moving global shocks and slower, more persistent structural
trends. The PCA results reveal two economically meaningful dimensions of sovereign risk.
The first component captures a global systemic factor, reflecting how emerging economies
co-move in response to widespread shocks such as tightening global financial conditions,
shifts in risk appetite, or liquidity stress. Countries like Brazil, Chile, Peru, Colombia, and
Greece load heavily on this dimension, indicating that their sovereign spreads are strongly
driven by global market turbulence and therefore highly sensitive to contagion effects. In
contrast, economies such as the United Arab Emirates, the Czech Republic, and Taiwan
exhibit weaker loadings, suggesting greater resilience to systemic pressures. The second
component reflects structural or idiosyncratic risk, distinguishing countries with persistent
domestic vulnerabilities—such as Egypt and Turkey, often characterized by fiscal fragility
or institutional instability—from more structurally robust economies like Qatar and Saudi
Arabia. This dual structure highlights that sovereign credit risk in emerging markets is
shaped both by global financial cycles and by country-specific fundamentals, underscoring
the need to jointly consider systemic exposure and structural strength when assessing
sovereign risk dynamics. These dimensions will be used as key explanatory variables in the

````

## PDF page 13

FORMULA CHECK REQUIRED: original PDF page 13.

````text
Risks 2025, 13, 245
13 of 23
quantile regression analysis that follows, helping to disentangle the heterogeneous effects
of sovereign risk on financial performance across the return distribution.
Table 3 presents the estimated coefficients of the quantile regression model for different
quantile levels, with increments of 0.05. This approach allows for analyzing how the
impact of the explanatory variables on the returns of the MSCI ESG Index varies across its
conditional distribution, capturing potential asymmetries and non-homogeneous effects.
The results show that the effects of the explanatory variables are not constant across the
return distribution, validating the use of the quantile approach instead of classical linear
models. Factors such as emerging markets and the Nasdaq index have persistent and
significant effects, while others such as exchange rates and interest rates have more modest
or non-significant impacts. The evidence also suggests that the sensitivity of the MSCI
index to global factors is asymmetric, being more pronounced at the extreme quantiles,
which has relevant implications for risk management and the design of hedging strategies.
Table 3. Results for the quantile regression model.
Quantile
(Intercept)
Dim.1
Dim.2
Dollar
Index
Brent
Oil
NASDAQ
MSCI
Emerging
US10Y
Trea-
sury
S&P 500
0.05
−0.0164 ***
−0.0008***
0.0000
0.0698
0.0288
0.0680
−0.0703
−0.0005
−0.0174
0.1
−0.0114 ***
−0.0005***
−0.0006***
−0.0182
0.0034
0.1283
*
−0.0884
**
0.0360
−0.1160
0.15
−0.0089 ***
−0.0005***
−0.0006***
−0.0402
−0.0088
0.1119
*
−0.0938
**
−0.0041
−0.1085
0.2
−0.0068 ***
−0.0004***
−0.0006***
−0.0394
−0.0149
0.0620
−0.1004
***
−0.0533
−0.0544
0.25
−0.0052 ***
−0.0003***
−0.0004***
−0.0870
−0.0064
0.0651
−0.0980
***
−0.0451
−0.0586
0.3
−0.0038 ***
−0.0002***
−0.0004***
−0.0327
−0.0037
0.0845
**
−0.0915
***
−0.0270
*** −0.0714
0.35
−0.0027 ***
−0.0002**
−0.0004***
−0.0305
0.0036
0.1043
**
−0.1066
***
−0.0208
−0.1090
**
0.4
−0.0015 ***
−0.0001**
−0.0004***
−0.0158
0.0042
0.1420
***
−0.1178
***
0.0023
−0.1548
***
0.45
−0.0006 ***
−0.0001*
−0.0003***
−0.0085
0.0043
0.1289
***
−0.1308
***
0.0172
−0.1290
***
0.5
0.0006
***
0.0000
−0.0002
−0.0382
0.0014
0.1462
***
−0.1466
***
0.0101
−0.1453
***
0.55
0.0016
***
0.0000
−0.0001
−0.0703
0.0003
0.1762
***
−0.1555
***
−0.0016
−0.1770
***
0.6
0.0026
***
0.0000
−0.0001
−0.0850
0.0038
0.1590
***
−0.1666
***
−0.0100
−0.1523
***
0.65
0.0038
***
0.0000
0.0000
−0.0650
0.0063
0.1654
***
−0.1820
***
−0.0205
−0.1501
***
0.7
0.0051
***
0.0000
0.0001
−0.0863
0.0123
*
0.1485
***
−0.1935
***
−0.0312
−0.1307
***
0.75
0.0065
***
0.0000
0.0002
−0.0711
0.0016
0.0725
***
−0.1832
***
−0.0407
−0.0555
*
0.8
0.0079
***
0.0001
0.0003
**
−0.0487
0.0019
0.0663
−0.2005
***
−0.0491
−0.0519
0.85
0.0100
***
0.0003
***
0.0004
**
−0.0369
0.0109
0.0655
−0.1993
***
−0.0305
−0.0467
0.9
0.0122
***
0.0004
***
0.0005
***
−0.0382
0.0199
*
0.1268
*
−0.2252
***
0.0241
−0.1107
0.95
0.0164
***
0.0005
***
0.0009
***
0.0158
0.0292
**
0.1557
*
−0.2346
***
0.0754
−0.1387
Note: asterisks mark coefficients whose p-value for H0: β = 0 is below the stated level (two-sided tests): *** p < 0.01,
** p < 0.05, * p < 0.10; no star: p ≥0.10.
As shown in Figure 4, the intercept is significant and increasing as the quantiles
increase, moving from a negative value in the low quantiles to a positive value in the
high quantiles, reflecting an asymmetric distribution of returns conditioned by the remain-
ing covariates.
The principal components Dim.1 and Dim.2, which summarize latent factors or struc-
tural correlations in the system, exhibit a negative and significant relationship with returns
in most of the low and middle quantiles. Dim.1 shows a change in sign around the 0.5 quan-
tile, indicating that its negative impact occurs mainly in loss scenarios (lower tails), while
Dim.2 becomes positive and significant only in the high quantiles (0.80 to 0.95), suggesting
a divergent effect depending on the level of return analyzed.
Exchange rate fluctuations are not a significant variable in most quantiles, although
they appear with a persistent negative sign from τ = 0.15 to τ = 0.85. This suggests that their
effect on returns is weak or marginal, although it could be interpreted as slight downward
pressure when the dollar appreciates. The oil price has a weak and nonsignificant impact
in almost all quantiles. Only at the 0.95 quantile does it become positive and significant,
suggesting that in very high-return scenarios, rising oil prices may coincide with improved
returns. The technology market, represented by the Nasdaq, exhibits a positive, increasing,
and significant effect from τ = 0.3, with peaks around τ = 0.55. This confirms the high
sensitivity of the MSCI index to Nasdaq returns, especially in the middle and upper
quantiles, indicating a transmission of optimism in the stock markets.

````

## PDF page 14

FORMULA CHECK REQUIRED: original PDF page 14.

````text
Risks 2025, 13, 245
14 of 23
 
Figure 4. Quantile regression.
The emerging markets index has a significant negative effect across all quantiles from
τ = 0.15 to τ = 0.95, suggesting that losses in emerging markets tend to coincide with
declines in the MSCI index, regardless of the return level analyzed. This denotes a strong
interdependence among emerging markets. Meanwhile, US interest rates are not significant
across most quantiles, although they have moderately negative coefficients at some points.
This could reflect an ambiguous relationship or one mediated by other, more dominant
macroeconomic factors.
The S&P 500, similar to the Nasdaq, has a significant negative effect from the 0.3 quan-
tile onward. This negative relationship could be interpreted as imperfect diversification
between MSCI assets and the S&P 500, where positive movements in the S&P 500 co-
incide with adjustments in other international markets due to portfolio rebalancing or
capital flows.
Taken together, the results provide strong empirical support for the hypothesis
that sovereign risk dynamics—and their latent transmission to sustainable investment
indices—are shaped by a combination of global systemic pressures and structural asymme-
tries across the return distribution. The quantile regression approach reveals heterogeneous
sensitivities, with risk factors exerting differentiated effects depending on the performance
regime of the MSCI ESG Index. The goodness of fit of the quantile regression models was
evaluated using the pseudo R2 statistic, which measures the proportion of variation in
ESG returns explained by the explanatory variables at each quantile level. These values,
which range from 0.01 in the median quantile to approximately 0.70 in the tails, confirm the
model’s capacity to capture asymmetric and nonlinear relationships across the return distri-
bution. The detailed results for all quantiles are presented in Appendix C, where the pseudo
R2 values are reported for each estimated model. In addition, we conduct a robustness test
excluding Taiwan, re-estimating the full quantile framework; the corresponding pseudo R2
values Appendix D, confirm that the results remain highly similar despite the exclusion. To

````

## PDF page 15

FORMULA CHECK REQUIRED: original PDF page 15.

````text
Risks 2025, 13, 245
15 of 23
statistically validate these distributional differences, a quantile ANOVA test was conducted,
confirming that the estimated coefficients vary significantly across quantiles. The detailed
results of this test are reported in Appendix A, further supporting the robustness of the het-
erogeneous effects identified in the main analysis. This asymmetry is particularly relevant
in the context of sustainable finance, where extreme downside events may compromise
the perceived resilience of ESG-linked portfolios. To address potential concerns regarding
collinearity and causal distortion within the quantile regression framework, it is important
to note that the inclusion of PCA-derived dimensions (DIM1 and DIM2) as explanatory
factors was specifically intended to mitigate multicollinearity by transforming correlated
variables into orthogonal latent components. This methodological approach follows the
recommendations of Fan et al. (2017), who emphasize that the PCA–CQR method can
eliminate the multicollinearity among explanatory variables and provide probabilistic
loadings and quantile coefficients.
Davino et al. (2022), demonstrate that principal component regression applied to quan-
tile contexts preserves the information content of predictors while alleviating redundancy
among highly correlated variables
The model specification explicitly incorporates temporal ordering and lagged effects
to strengthen causal interpretation within a non-experimental framework. While causality
remains limited by the observational nature of the data, these design elements enhance
robustness and interpretability of the estimated quantile effects.
The first principal component, associated with global financial shocks, tends to have
a more pronounced negative influence during periods of poor performance (lower quan-
tiles), aligning with the notion that systemic sovereign stress disproportionately affects
sustainable assets when market conditions deteriorate. In contrast, the second component—
interpreted as a structural trend—becomes relevant only in high-return regimes, potentially
reflecting investor reallocation toward ESG assets in contexts of favorable macroeconomic
tailwinds or positive sentiment. This suggests that sustainable investment indices may
benefit from structural shifts in global risk appetite, but remain vulnerable to short-term
sovereign risk spillovers.
The role of emerging markets (as captured by the MSCI Emerging Index) stands out
as a consistently negative and significant driver across the distribution. This not only
highlights the financial fragility of emerging sovereigns but also questions the robustness
of ESG portfolios that include substantial exposure to these markets. It raises important
considerations for sustainability-oriented investors, especially given the trade-off between
ESG impact and exposure to macro-financial instability in the Global South.
Interestingly, classical control variables such as interest rates and exchange rates
exhibit limited explanatory power, except at specific quantiles. This aligns with recent
findings that traditional macroeconomic indicators may be insufficient to capture nonlinear
dynamics in ESG-linked financial performance, especially under stress. The consistent
effect of Nasdaq returns, by contrast, suggests that tech-driven optimism and innovation
narratives continue to influence ESG valuations, reinforcing the hypothesis that sustainable
finance is not insulated from broader speculative cycles.
The observed sensitivity of the MSCI ESG Index to both latent sovereign risk di-
mensions and global equity benchmarks reveals a structural contradiction: while ESG
investments aim to prioritize long-term environmental and social resilience, their short-
term behavior remains closely tied to conventional market risk channels. This finding
challenges the assumption that ESG portfolios inherently offer downside protection or
reduced volatility, and instead points to the need for more robust frameworks to integrate
sovereign and systemic risk assessments into sustainable investment strategies. The re-
sults have clear implications for both investors and policymakers. The negative impact

````

## PDF page 16

Technical extraction; compare with original PDF page 16.

````text
Risks 2025, 13, 245
16 of 23
of the systemic sovereign risk component (Dim.1) on the lower quantiles indicates that
global financial stress disproportionately amplifies losses in ESG portfolios, reinforcing
the need for risk-sensitive portfolio construction and hedging mechanisms that account
for sovereign contagion. Conversely, the structural component (Dim.2) exerts a positive
influence in the upper quantiles, suggesting that improvements in fiscal governance, insti-
tutional strength, and macroeconomic credibility enhance the performance of ESG assets
during favorable conditions. The persistent negative link between the MSCI Emerging
Markets Index and ESG returns reveals a structural vulnerability that limits diversification
benefits and highlights the trade-off between sustainability impact and financial fragility
in emerging economies. These findings underscore the practical need for integrating
sovereign risk assessments and quantile-based stress testing into sustainable investment
frameworks. Overall, this evidence advances current understanding of the nonlinear
dynamics connecting sovereign risk and ESG performance, showing that sustainable port-
folios remain sensitive to global shocks yet benefit from long-term structural resilience. A
robustness test is conducted in this study to validate the stability and consistency of the
main model’s results. This analysis, presented in Appendix B, assesses the sensitivity of
the coefficients to alternative specifications and confirms that the estimated effects retain
their sign, magnitude, and statistical significance, thereby reinforcing the reliability of
the findings.
5. Discussion
The results presented in this study provide a comprehensive understanding of the
heterogeneous influence of sovereign risk dynamics on sustainable investment performance
across different points of the return distribution. By integrating principal component
analysis (PCA) and quantile regression, the empirical framework captures both systemic
and structural dimensions of sovereign risk and their nonlinear transmission to ESG-related
financial indices.
The quantile-based results reveal strong distributional asymmetries. The first princi-
pal component, which reflects systemic global financial stress, exerts a more pronounced
negative impact in the lower quantiles—periods associated with market downturns and
risk aversion. This finding supports the notion that ESG assets are not immune to systemic
contagion, as heightened sovereign stress tends to amplify losses even within sustainability-
oriented portfolios. Conversely, the second component—interpreted as a structural or
long-term factor—shows significance only in higher quantiles, suggesting that favorable
macroeconomic conditions and positive investor sentiment can enhance the relative per-
formance of ESG indices. Together, these results highlight a dual structure in the rela-
tionship between sovereign risk and sustainable returns: one that is highly sensitive to
global shocks and another that evolves more gradually in response to persistent macro-
financial conditions.
Moreover, the role of emerging markets stands out as a consistently negative and
statistically significant driver across most quantiles. This underscores the structural vulner-
ability of these economies and the exposure of ESG portfolios that integrate a substantial
share of emerging market assets. Such patterns call into question the presumed stability of
ESG-linked investments and emphasize the need to differentiate between sustainability nar-
ratives and real financial resilience under stress. Traditional macroeconomic variables such
as interest rates and exchange rates display limited explanatory power, which aligns with
recent evidence that linear macro-financial relationships may fail to capture the nonlinear
dynamics of ESG performance under volatility.
To statistically validate the heterogeneity of these effects, a quantile ANOVA test was
performed, confirming that the estimated coefficients differ significantly across quantiles

````

## PDF page 17

Technical extraction; compare with original PDF page 17.

````text
Risks 2025, 13, 245
17 of 23
(Appendix A). This result reinforces the appropriateness of the quantile regression ap-
proach and provides empirical evidence of asymmetric sensitivities throughout the return
distribution. Furthermore, a robustness test based on bootstrapped standard errors was
conducted to assess the stability of the results under alternative specifications (Appendix B).
The findings indicate that coefficient estimates remain consistent in sign, magnitude, and
statistical significance across replications, thereby supporting the overall reliability of the
model. Overall, these findings underscore a fundamental paradox within sustainable fi-
nance: despite their purported resilience, ESG-linked portfolios remain strongly exposed to
systemic market forces and sovereign risk spillovers. The empirical evidence suggests that
their short-term dynamics are still governed by conventional channels of global financial
transmission, even as they pursue long-term sustainability goals. This tension highlights
the importance of incorporating sovereign and systemic risk diagnostics into the design of
sustainable investment frameworks, ensuring that the transition toward greener finance
does not overlook the vulnerabilities embedded in emerging and interconnected markets.
The robustness checks presented in Appendix B further confirm the stability of these results,
validating both the direction and consistency of the estimated effects across alternative
model specifications. To assess potential endogeneity within the quantile-regression frame-
work, we implemented the IVQR estimator of Chernozhukov and Hansen (2005, 2006),
but the procedure did not converge due to the non-invertibility of the Jacobian matrix—a
known computational limitation (Chernozhukov and Hansen 2005; Machado and Santos
Silva 2019). Given this constraint, we rely on a robust PCA to detect latent common factors
that could generate omitted-variable bias or structural endogeneity. The decomposition
does not reveal underlying confounding patterns, supporting the validity of the baseline
quantile-regression specification.
6. Conclusions
The results presented in this study emphasize an important and nuanced insight: the
relationship between sovereign risk and sustainability is neither static nor homogeneous.
Although ESG-labeled financial instruments are designed to embody environmental, social,
and governance principles, the empirical evidence suggests that the MSCI ESG Index
remains exposed to the broad macro-financial forces that shape global markets. Rather
than being insulated from systemic volatility, ESG assets appear integrated into the same
financial dynamics, contagion channels, and investor reactions that influence conven-
tional portfolios.
The quantile regression estimates reinforce this interpretation. The first principal
component capturing the dominant, systemic dimension of sovereign risk derived from
standardized CDS spreads exhibits a negative and significant association with ESG returns
in lower quantiles. This pattern indicates that under adverse market conditions, such as re-
cessions, geopolitical tensions, or tightening financial cycles, rising sovereign risk coincides
with disproportionately negative outcomes for ESG assets. Rather than exhibiting counter-
cyclical behavior, ESG portfolios tend to be drawn into broader risk-off episodes in which
investors retrench and rebalance exposures independently of sustainability considerations.
In contrast, the second principal component, reflecting slow-moving structural im-
provements in sovereign profiles, becomes relevant only in the upper quantiles of the return
distribution. Under favorable market conditions, countries with stronger institutional qual-
ity, fiscal fundamentals, and long-term creditworthiness tend to see relatively better ESG
performance. This suggests that the credibility and resilience of sustainable finance ulti-
mately depend not only on corporate-level ESG disclosures but also on sovereign-level
macroeconomic and institutional conditions. Strengthening public governance, fiscal trans-

````

## PDF page 18

Technical extraction; compare with original PDF page 18.

````text
Risks 2025, 13, 245
18 of 23
parency, and long-term policy frameworks may therefore indirectly reinforce the appeal
and stability of ESG-linked investments.
A similar pattern emerges when considering exposure to emerging markets. The
consistently negative and significant effect of the MSCI Emerging Markets Index across
quantiles points to structural vulnerabilities among ESG investments concentrated in
developing economies. This reflects a broader tension within sustainable finance: although
emerging markets offer the greatest potential for environmental and social impact, they
also exhibit higher sovereign risk, weaker institutional buffers, and greater exposure to
external shocks. Investors and policymakers therefore face a trade-off between maximizing
sustainability impact and navigating heightened macro-financial fragility.
The performance of traditional control variables such as interest rates and exchange
rates also offers insight. Their limited statistical significance across the return distribu-
tion suggests that conventional macroeconomic indicators may not fully capture the risk
dynamics affecting ESG assets. Instead, the most influential drivers appear to be latent,
market-driven, or structural in nature, including major stock-market indices and composite
risk factors obtained through dimensionality-reduction techniques. This underscores the
importance of considering global financial integration, investor sentiment, and sovereign-
level fundamentals when evaluating ESG portfolios.
Overall, the evidence points to an important conclusion: ESG and sovereign risk are
deeply interconnected. The long-term effectiveness and credibility of sustainable finance
depend not only on firm-level ESG practices but also on macro-level fiscal sustainability,
institutional stability, and sovereign risk management frameworks. The contrast between
emerging and developed economies further illustrates structural asymmetries. Sovereign
risk appears to exert stronger and more persistent effects in emerging markets, where
institutional resilience is lower and financial systems have more limited capacity to absorb
shocks. In developed economies, deeper markets and more robust public institutions
mitigate the impact of volatility, reinforcing the need for context-specific strategies in the
transition toward sustainable finance.
From a practical standpoint, investors can integrate sovereign-risk metrics alongside
ESG criteria when designing portfolios, adjusting exposures according to systemic vulnera-
bilities. Policymakers and regulators can enhance credibility by incorporating sovereign-
level ESG indicators in risk assessments, improving transparency, and designing stress-
testing frameworks that explicitly consider systemic risk transmission into ESG portfolios.
Despite the relevance of these findings, the conclusions should be interpreted with
caution. The empirical design faces several methodological constraints that limit the
strength of causal interpretation and the robustness of the policy implications. First, the
measurement of sovereign risk for Taiwan required the construction of an imputed CDS
series, which may introduce noise and reduce comparability. Second, although control
variables and dimensionality-reduction techniques were employed, the study did not
implement a comprehensive set of robustness or sensitivity checks—such as alternative risk
measures, sub-sample analyses, or model diagnostics. Third, endogeneity concerns remain
only partially addressed, as the analysis did not apply standard instrumental-variable
procedures or identification strategies capable of isolating causal effects. Finally, issues
related to missing data required the use of robust PCA for dimensionality reduction, which,
while effective for handling incomplete panels, may still leave residual uncertainty about
the influence of data imputation on the extracted components. These limitations define the
empirical scope of the study and suggest that the results should be viewed as indicative
rather than definitive.
Ultimately, the evidence challenges the assumption that ESG assets are inherently
insulated from systemic shocks. Instead, the findings point to the importance of inte-

````

## PDF page 19

FORMULA CHECK REQUIRED: original PDF page 19.

````text
Risks 2025, 13, 245
19 of 23
grating sovereign-risk assessment into sustainable investment frameworks to enhance
resilience. Future research would benefit from expanding the analysis to additional asset
classes, implementing more rigorous identification strategies, and exploring how investor
behavior responds to the joint dynamics of sovereign risk and sustainability under varying
financial conditions.
Author Contributions: Conceptualization, O.W.O.-C. and O.J.-B.; methodology, O.W.O.-C., O.J.-B.
and D.F.M.-D.; validation, O.W.O.-C. and O.J.-B.; formal analysis, O.W.O.-C., O.J.-B. and D.F.M.-D.;
investigation, O.W.O.-C. and D.F.M.-D.; data curation, O.W.O.-C.; writing—original draft preparation,
O.W.O.-C. and O.J.-B.; writing—review and editing, O.W.O.-C., O.J.-B. and D.F.M.-D.; visualization,
O.W.O.-C. and O.J.-B. All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding.
Data Availability Statement: Data are contained within paper.
Conflicts of Interest: The authors declare no conflicts of interest.
Abbreviations
The following abbreviations are used in this manuscript:
MSCI
Morgan Stanley Capital International
ESG
Environmental, Social, and Governance
PCA
Principal Component Analysis
CDS
Credit Default Swap
Appendix A
Table A1. Test of equality of coefficients across quantiles (Koenker and Bassett 1978).
Df
Resid Df
F Value
Pr (>F)
144
45,057
2.0175
6.86 × 10−12 ***
Note: The asterisks symbol corresponds to this significance level according to the following scale: *** p < 0.01.
Appendix B
 
Figure A1. Robustness Test Based on Bootstrapped Standard Errors (1000 Replications).

````

## PDF page 20

Technical extraction; compare with original PDF page 20.

````text
Risks 2025, 13, 245
20 of 23
Appendix C
Table A2. Pseudo R2 values by quantile level.
Tau
Pseudo_R2
0.05
0.6837
0.1
0.5074
0.15
0.3738
0.2
0.2693
0.25
0.186
0.3
0.1219
0.35
0.0734
0.4
0.0393
0.45
0.0189
0.5
0.0121
0.55
0.0184
0.6
0.0384
0.65
0.0732
0.7
0.1238
0.75
0.1918
0.8
0.2788
0.85
0.3873
0.9
0.5267
0.95
0.706
Appendix D
Table A3. Pseudo R2 values by quantile level, excluding Taiwan.
Tau
Pseudo_R2
0.05
0.6836
0.1
0.5069
0.15
0.3734
0.2
0.2688
0.25
0.1856
0.3
0.1213
0.35
0.073
0.4
0.0388
0.45
0.0185
0.5
0.012
0.55
0.0184
0.6
0.0384
0.65
0.0732
0.7
0.1238
0.75
0.1917
0.8
0.2785
0.85
0.3872
0.9
0.5259
0.95
0.7048

````

## PDF page 21

Technical extraction; compare with original PDF page 21.

````text
Risks 2025, 13, 245
21 of 23
Appendix E
 
Figure A2. Robust PCA.
References
Aldieri, Luigi, Antonio Amendola, and Vincenzo Candila. 2023. The Impact of ESG Scores on Risk Market Performance. Sustainability
15: 7183. [CrossRef]
Anand, Arsh, Rosanne Vanpée, and Igor Lonˇcarski. 2023. Sustainability and Sovereign Credit Risk. International Review of Financial
Analysis 86: 102494. [CrossRef]
Anthony, Rintu, and Ranjitha Ajay. 2024. Dissecting E, S, and G for Risk Mitigation: Insights from the Term Structure of CDS. Applied
Economics 57: 1–15. [CrossRef]
Bai, Jushan, and Serena Ng. 2002. Determining the Number of Factors in Approximate Factor Models. Econometrica 70: 191–221.
[CrossRef]
Bai, Jushan, and Serena Ng. 2007. Determining the Number of Primitive Shocks in Factor Models. Journal of Business & Economic
Statistics 25: 52–60. [CrossRef]
Bajaj, Vimmy, Pawan Kumar, and Vipul Kumar Singh. 2022. Linkage Dynamics of Sovereign Credit Risk and Financial Markets:
A Bibliometric Analysis. Research in International Business and Finance 59: 101566. [CrossRef]
Ballester, Laura, Ana González-Urteaga, and Long Shen. 2024. Green Bond Issuance and Credit Risk: International Evidence. Journal of
International Financial Markets, Institutions and Money 94: 102013. [CrossRef]
Barth, Florian, Benjamin Hübel, and Hendrik Scholz. 2022. ESG and Corporate Credit Spreads. Journal of Risk Finance 23: 169–90.
[CrossRef]
Bekaert, Geert, and Campbell R. Harvey. 2003. Emerging Markets Finance. Journal of Empirical Finance 10: 3–55. [CrossRef]
Bernanke, Ben S., Jean Boivin, and Piotr Eliasz. 2005. Measuring the Effects of Monetary Policy: A Factor-Augmented Vector
Autoregressive (FAVAR) Approach. The Quarterly Journal of Economics 120: 387–422. [CrossRef]
Broadstock, David C., Kevin Chan, and Xiaowei Wang. 2021. The Role of ESG Performance during Times of Financial Crisis: Evidence
from COVID-19 in China. Finance Research Letters 38: 101716. [CrossRef]
Caiazza, Stefano, Giuseppe Galloppo, and Giovanni la Rosa. 2023. The Mitigation Role of Corporate Sustainability: Evidence from the
CDS Spread. Finance Research Letters 52: 103561. [CrossRef]

````

## PDF page 22

Technical extraction; compare with original PDF page 22.

````text
Risks 2025, 13, 245
22 of 23
Capelle-Blancard, Gunther, Patricia Crifo, Marie-Aude Diaye, Rim Oueghlissi, and Bert Scholtens. 2019. Sovereign Bond Yield Spreads
and Sustainability: An Empirical Analysis of OECD Countries. Journal of Banking & Finance 98: 156–69. [CrossRef]
Chernozhukov, Victor, and Christian Hansen. 2005. An IV Model of Quantile Treatment Effects. Econometrica 73: 245–61. [CrossRef]
Chernozhukov, Victor, and Christian Hansen. 2006. Instrumental quantile regression inference for structural and treatment effect
models. Journal of Econometrics 132: 491–525. [CrossRef]
Corsetti, Giancarlo, Keith Kuester, Andre Meier, and Gernot J. Mueller. 2012. Sovereign Risk, Fiscal Policy, and Macroeconomic Stability.
IMF Working Paper WP/12/33. Washington: International Monetary Fund.
Davino, Cristina, Rosanna Romano, and Domenico Vistocco. 2022. Handling Multicollinearity in Quantile Regression through the Use
of Principal Component Regression. Metron 80: 153–174. [CrossRef]
Dieckmann, Stephan, and Thomas Plank. 2012. Default Risk of Advanced Economies: An Empirical Analysis of Credit Default Swaps
during the Financial Crisis. Review of Finance 16: 903–34. [CrossRef]
Fan, Yurui, Gordon H. Huang, Yongping Li, Xiuquan Wang, Zhong Li, and Lei Jin. 2017. Development of PCA-Based Cluster Quantile
Regression (PCA-CQR) Framework for Streamflow Prediction: Application to the Xiangxi River Watershed, China. Applied Soft
Computing 51: 280–293. [CrossRef]
Friede, Gunnar, Timo Busch, and Alexander Bassen. 2015. ESG and Financial Performance: Aggregated Evidence from More than 2000
Empirical Studies. Journal of Sustainable Finance & Investment 5: 210–33. [CrossRef]
Gianfrate, Gianfranco, Mirco Rubin, Dario Ruzzi, and Mathijs A. van Dijk. 2024. On the Resilience of ESG Firms during the COVID-19
Crisis: Evidence across Countries and Asset Classes. Journal of International Business Studies 55: 1069–84. [CrossRef]
Giudici, Paolo, and Paolo Pagnottoni. 2019. High Frequency Price Change Spillovers in Bitcoin Markets. Risks 7: 111. [CrossRef]
Hauch, Selina. 2025. ESG rating divergence and corporate credit risk. Academy of Management Annual Meeting Proceedings 2025: 11839.
[CrossRef]
Hübel, Benjamin. 2022. Do Markets Value ESG Risks in Sovereign Credit Curves? Quarterly Review of Economics and Finance 85: 134–48.
[CrossRef]
Joaqui-Barandica, Orlando, Andres Oviedo-Gómez, and Diego F. Manotas-Duque. 2023. Directional Predictability between Interest
Rates and the Stoxx 600 Banks Index: A Quantile Approach. Finance Research Letters 58: 104328. [CrossRef]
Josse, Julie, and François Husson. 2012. Handling Missing Values in Exploratory Multivariate Data Analysis Methods. Journal de La
Société Française de Statistique 153: 79–99.
Karaman, Yasemin. 2022. The Effect of Countries’ ESG Ratings on Sovereign Credit Default Swaps: An Empirical Evidence on OECD
Countries (2008–2019). World Journal of Entrepreneurship, Management and Sustainable Development 18: 447–65. [CrossRef]
Kiesel, Florian, and Felix Lücke. 2019. ESG in Credit Ratings and the Impact on Financial Markets. Financial Markets, Institutions and
Instruments 28: 263–90. [CrossRef]
Koenker, Roger. 2004. Quantile Regression for Longitudinal Data. Journal of Multivariate Analysis 91: 74–89. [CrossRef]
Koenker, Roger, and Gilbert Bassett. 1978. Regression Quantiles. Econometrica 46: 33–50. [CrossRef]
Koenker, Roger, and Zhijie Xiao. 2006. Quantile Autoregression. Journal of the American Statistical Association 101: 980–90. [CrossRef]
Long, Shaobo, Hao Tian, and Zixuan Li. 2022. Dynamic Spillovers between Uncertainties and Green Bond Markets in the US, Europe,
and China: Evidence from the Quantile VAR Framework. International Review of Financial Analysis 84: 102416. [CrossRef]
Longstaff, Francis A., Jun Pan, Lasse H. Pedersen, and Kenneth J. Singleton. 2011. How Sovereign Is Sovereign Credit Risk? American
Economic Journal: Macroeconomics 3: 75–103. [CrossRef]
Ma, Lingjie, and Roger Koenker. 2006. Quantile Regression Methods for Recursive Structural Equation Models. Journal of Econometrics
134: 471–506. [CrossRef]
Machado, José A. F., and J. M. C. Santos Silva. 2019. Quantiles via moments. Journal of Econometrics 213: 145–73. [CrossRef]
Mensi, Walid, Abdel Razzaq Al Rababa’a, Xuan Vinh Vo, and Sang Hoon Kang. 2021. Asymmetric Spillover and Network Connected-
ness between Crude Oil, Gold, and Chinese Sector Stock Markets. Energy Economics 98: 105262. [CrossRef]
Michopoulos, Ioannis, Alexandros Bougias, Athanasios Episcopos, and Efstratios Livanis. 2025. Measuring ESG Risk Premia with
Contingent Claims. European Journal of Finance 31: 427–50. [CrossRef]
Naifar, Nader. 2023. Does Climate Change Affect Sovereign Credit Risk? International Evidence. Borsa Istanbul Review 23: S84–S95.
[CrossRef]
Naumer, Hans Jörg, and Burcin Yurtoglu. 2022. It Is Not Only What You Say, but How You Say It: ESG, Corporate News, and the
Impact on CDS Spreads. Global Finance Journal 52: 100571. [CrossRef]
Öcal, Hüseyin, and Anton Abdulbasah Kamil. 2021. The Impact of Risk Indicators on Sustainability (ESG) and Broad-Based Indices: An
Empirical Analysis from Germany, France, Indonesia and Turkey. International Journal of Sustainable Economy 13: 18–54. [CrossRef]
Reboredo, Juan C., and Andrea Ugolini. 2016. Quantile Dependence of Oil Price Movements and Stock Returns. Energy Economics
54: 33–49. [CrossRef]

````

## PDF page 23

Technical extraction; compare with original PDF page 23.

````text
Risks 2025, 13, 245
23 of 23
Tampakoudis, Ioannis, Michail Nerantzidis, Demetres Subeniotis, Apostolos Soutsas, and Nikolaos Kiosses. 2020. Bank Mergers
and Acquisitions in Greece: The Financial Crisis and Its Effect on Shareholder Wealth. International Journal of Managerial Finance
16: 273–296. [CrossRef]
Tang, Ning, Haowen Chang, Chihyung Lin, and Chien Lin Lu. 2024. Public’s Evaluation of ESG and Credit Default Swap: Evidence
from East Asian Countries. Pacific Basin Finance Journal 87: 102512. [CrossRef]
Uribe, Jorge M., and Montserrat Guillen. 2020. Quantile Regression for Cross-Sectional and Time Series Data Applications in Energy Markets
Using R. Cham: Springer.
Zhao, Puhua. 2025. The Impact of ESG on Sovereign Risk Spillover: Evidence from Belt and Road Countries. Applied Economics Letters
1–5. [CrossRef]
Zhao, Ran, and Lu Zhu. 2024. Credit Default Swaps and Corporate ESG Performance. Journal of Banking and Finance 159: 107079.
[CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.

````

