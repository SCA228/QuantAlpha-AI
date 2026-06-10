# QuantAlpha-AI
QuantAlpha AI is an end-to-end quantitative research platform designed to identify, model, and forecast market inefficiencies through a combination of econometrics, factor investing, machine learning, and scientific computing.

Traditional asset pricing models assume that expected returns are fully explained by systematic risk factors. However, persistent abnormal returns (alpha) frequently emerge due to information asymmetry, behavioral biases, and evolving market conditions. This project investigates whether such alpha can be statistically detected, dynamically modeled, and transformed into systematic investment strategies.

This project integrates:

Fama-French 5-Factor Modeling ,
High-Dimensional Alpha Testing ,
Dynamic Alpha Estimation
Physics-Informed Neural Networks (PINNs)
Inverse PDE Discovery
Market Regime Detection
Long-Short Portfolio Construction
Institutional-Style Backtesting

into a unified quantitative research workflow.

## Key Results

| Metric | Result |
|----------|----------|
| Equities Analyzed | 10 U.S. Large-Cap Stocks |
| Data Horizon | 5 Years |
| Factor Model | Fama-French 5-Factor |
| Dynamic Alpha Estimation | Rolling 60-Month Regressions |
| Market Regimes Detected | 4 |
| PINN Framework | Physics-Informed Neural Network |
| Annualized Return | 24.3% |
| Win Rate | 56.7% |
| Sharpe Ratio | 0.64 |
| Sortino Ratio | 0.94 |
| Maximum Drawdown | -39.4% |
| Portfolio Type | Long-Short Alpha Strategy |
| Alpha Forecasting | Enabled |
| Regime Detection | Machine Learning Based |
| PDE Discovery | Drift & Diffusion Parameters Learned |

# System Architecture


                    ┌─────────────────────┐
                    │   Market Data       │
                    │  (Equity Returns)   │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Fama-French Factors │
                    │  MKT, SMB, HML      │
                    │  RMW, CMA           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Factor-Based Alpha  │
                    │     Estimation      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ High-Dimensional    │
                    │  Alpha Testing      │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Dynamic Alpha       │
                    │     Modeling        │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Market Inefficiency │
                    │       Index         │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 ▼                           ▼

      ┌─────────────────────┐    ┌─────────────────────┐
      │ Physics-Informed    │    │ Market Regime       │
      │ Neural Networks     │    │ Detection           │
      │ (PINN)              │    │ (Machine Learning)  │
      └──────────┬──────────┘    └──────────┬──────────┘
                 │                          │
                 ▼                          ▼

      ┌─────────────────────┐    ┌─────────────────────┐
      │ Inverse PDE         │    │ Regime Labels       │
      │ Discovery           │    │ Efficient/Crisis    │
      │ μ, D Parameters     │    │ Alpha Opportunity   │
      └──────────┬──────────┘    └──────────┬──────────┘
                 └────────────┬─────────────┘
                              │
                              ▼

                    ┌─────────────────────┐
                    │ Alpha Forecasting   │
                    └──────────┬──────────┘
                               │
                               ▼

                    ┌─────────────────────┐
                    │ Portfolio           │
                    │ Construction        │
                    │ Long / Short        │
                    └──────────┬──────────┘
                               │
                               ▼

                    ┌─────────────────────┐
                    │ Backtesting &       │
                    │ Performance Metrics │
                    └──────────┬──────────┘
                               │
                               ▼

                    ┌─────────────────────┐
                    │ Research Insights   │
                    │ & Trading Signals   │
                    └─────────────────────┘

  ## Workflow Summary

1. Collect 5 years of equity and factor data.
2. Estimate factor-adjusted alpha using the Fama-French 5-Factor model.
3. Test for statistically significant market inefficiencies.
4. Model dynamic alpha evolution through rolling regressions.
5. Forecast alpha dynamics using Physics-Informed Neural Networks.
6. Learn latent market dynamics through inverse PDE discovery.
7. Detect market regimes using machine learning clustering.
8. Construct long-short portfolios from alpha forecasts.
9. Evaluate economic significance through institutional-style backtesting.

    # Methodology

The QuantAlpha AI framework combines econometric asset pricing models, high-dimensional statistical inference, scientific machine learning, and portfolio analytics into a unified quantitative research pipeline.

---

## 1. Factor-Based Alpha Estimation

The first stage estimates abnormal returns (alpha) using the Fama-French 5-Factor asset pricing model.

### Model Specification

[
R_i - R_f =
\alpha_i
+
\beta_M MKT
+
\beta_S SMB
+
\beta_H HML
+
\beta_R RMW
+
\beta_C CMA
+
\epsilon_i
]

Where:

* (R_i): Asset return
* (R_f): Risk-free rate
* (MKT): Market excess return
* (SMB): Size factor
* (HML): Value factor
* (RMW): Profitability factor
* (CMA): Investment factor
* (\alpha_i): Abnormal return
* (\beta): Factor sensitivities

### Objective

Estimate abnormal returns unexplained by systematic risk exposures.

### Outputs

* Alpha Matrix
* Beta Matrix
* Residual Return Matrix
* Statistical Significance Metrics

---

## 2. High-Dimensional Alpha Detection

Traditional alpha estimation evaluates securities independently.

This framework evaluates alpha collectively across the market.

### Residual Correlation Matrix

[
\Sigma_\epsilon
===============

Cov(\epsilon)
]

where:

[
\epsilon=
[\epsilon_1,\epsilon_2,\ldots,\epsilon_N]
]

### Global Alpha Significance

The framework evaluates whether abnormal returns persist beyond factor explanations by analyzing the dependence structure of residual returns.

### Objective

Determine whether statistically significant market inefficiencies exist after controlling for known risk factors.

### Outputs

* Residual Correlation Structure
* J-Alpha Statistics
* Market-Wide Alpha Significance Measures

---

## 3. Dynamic Alpha Modeling

Static alpha estimation assumes:

[
\alpha_i(t)=constant
]

This assumption is unrealistic in evolving financial markets.

### Rolling Alpha Estimation

Using rolling-window regressions:

[
\alpha_i(t)
]

is estimated through time.

### Market Inefficiency Index

The aggregate level of market inefficiency is measured as:

[
MI_t
====

\frac{1}{N}
\sum_{i=1}^{N}
|\alpha_i(t)|
]

### Interpretation

Large values indicate periods of elevated market inefficiency and increased alpha opportunities.

### Outputs

* Rolling Alpha Matrix
* Rolling Beta Matrix
* Market Inefficiency Time Series

---

## 4. Physics-Informed Neural Networks (PINNs)

Alpha is modeled as a dynamic state variable:

[
\alpha = \alpha(t,x)
]

where:

* (t): Time
* (x): Asset dimension

### Governing Equation

The alpha evolution process is represented using an advection-diffusion PDE:

[
\frac{\partial \alpha}{\partial t}
+
\mu
\frac{\partial \alpha}{\partial x}
----------------------------------

D
\frac{\partial^2 \alpha}{\partial x^2}
======================================

0
]

where:

* (\mu): Alpha drift
* (D): Alpha diffusion

### PINN Objective Function

[
L
=

L_{data}
+
\lambda L_{PDE}
]

The model simultaneously minimizes:

* Data fitting error
* PDE residual error

### Outputs

* Alpha Forecasts
* Alpha Surface Predictions
* Trained PINN Models

---

## 5. Inverse PDE Discovery

Instead of assuming market dynamics are known, the framework learns them directly from data.

### Unknown Parameters

[
\mu
]

Alpha Drift

[
D
]

Alpha Diffusion

### Optimization Objective

[
\min_{\mu,D}
L_{PDE}
]

The inverse PINN estimates latent parameters governing alpha evolution.

### Outputs

* Learned Drift Parameters
* Learned Diffusion Parameters
* Inferred Market Dynamics

---

## 6. Market Regime Detection

Financial markets exhibit regime-dependent behavior.

### Feature Space

Regime classification uses:

* Market Inefficiency Index
* Rolling Alpha
* Rolling Volatility

### Clustering Framework

K-Means clustering partitions observations into:

[
K=4
]

market states.

### Regimes

1. Efficient Regime
2. Crisis Regime
3. Alpha Opportunity Regime
4. Normalization Regime

### Outputs

* Regime Labels
* Regime Transition Matrix

---

## 7. Systematic Portfolio Construction

Alpha forecasts are transformed into investment decisions.

### Ranking Function

Assets are ranked using:

[
Rank_i
======

\alpha_i
]

### Portfolio Formation

Long Portfolio:

[
Top(\alpha)
]

Short Portfolio:

[
Bottom(\alpha)
]

### Portfolio Return

[
R_{LS}
======

\frac{1}{N_L}
\sum R_L
--------

\frac{1}{N_S}
\sum R_S
]

where:

* (N_L): Number of long positions
* (N_S): Number of short positions

### Outputs

* Portfolio Weights
* Alpha Rankings
* Long-Short Portfolios

---

## 8. Economic Validation and Performance Evaluation

The economic value of alpha is evaluated through institutional portfolio analytics.

### Equity Curve

[
W_t
===

W_{t-1}
(1+R_t)
]

### Annualized Return

[
AR
==

12
\times
\bar R
]

### Annualized Volatility

[
\sigma_A
========

\sqrt{12}
\times
Std(R_t)
]

### Sharpe Ratio

[
Sharpe
======

\frac{
AR-R_f
}
{
\sigma_A
}
]

### Sortino Ratio

[
Sortino
=======

\frac{
AR-R_f
}
{
\sigma_{downside}
}
]

### Maximum Drawdown

[
MDD
===

\frac{
Peak-Trough
}
{
Peak
}
]

### Objective

Determine whether detected alpha translates into economically meaningful and risk-adjusted investment performance.

### Outputs

* Equity Curve
* Drawdown Analysis
* Risk Metrics
* Performance Attribution
* Strategy Validation














        







