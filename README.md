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

# Core Innovation

Most quantitative finance projects stop at estimating alpha using traditional factor models.

QuantAlpha AI extends this process significantly further by treating alpha as a dynamic and evolving market state rather than a static parameter.

The framework introduces a multi-stage research pipeline that combines econometrics, high-dimensional statistical inference, scientific machine learning, and portfolio analytics to discover, model, and monetize market inefficiencies.

## Key Innovations

### Dynamic Alpha Instead of Static Alpha

Traditional asset-pricing studies estimate a single alpha value over an entire sample period.

QuantAlpha AI estimates:

α(t) through rolling-window regressions, enabling the analysis of how abnormal returns evolve over time and across market conditions.

### Market Inefficiency as a Measurable State Variable

The framework introduces a Market Inefficiency Index constructed from dynamic alpha estimates.

This allows market efficiency to be monitored continuously rather than treated as a binary assumption.

The resulting signal provides a quantitative measure of evolving alpha opportunities.

---

### Physics-Informed Alpha Forecasting

Instead of relying solely on conventional machine learning models, QuantAlpha AI applies Physics-Informed Neural Networks (PINNs) to model alpha dynamics.

The model incorporates both:

* Historical financial data
* Governing dynamic constraints

This enables alpha forecasting while maintaining consistency with underlying market evolution processes.

---

### Inverse PDE Discovery for Financial Markets

Rather than assuming market dynamics are known, the framework learns them directly from observed alpha behavior.

An inverse PINN estimates latent drift and diffusion parameters governing alpha evolution, providing interpretable insights into the mechanisms driving market inefficiency.

This transforms the project from a predictive model into a scientific discovery framework.

---

### Regime-Aware Alpha Research

The platform identifies market regimes using machine learning clustering techniques.

Detected states include:

* Efficient Markets
* Crisis Regimes
* Alpha Opportunity Regimes
* Normalization Regimes

This allows alpha signals to be interpreted within the context of changing market environments.


### End-to-End Economic Validation

Most academic alpha studies stop at statistical significance.

QuantAlpha AI evaluates economic significance by transforming forecast alpha into systematic long-short portfolios and assessing performance through institutional portfolio analytics.

This closes the gap between quantitative research and practical investment implementation.

---

## Research Contribution

QuantAlpha AI combines:

* Factor Investing
* High-Dimensional Statistics
* Scientific Machine Learning
* Inverse PDE Discovery
* Market Regime Detection
* Systematic Portfolio Construction

into a unified quantitative research platform.

The result is a framework capable of detecting, forecasting, and economically validating market inefficiencies through an integrated research pipeline.

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

## Source Code – Key Files

| File                      | Purpose                                                                                                                                                 |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `src/factor_models.py`    | Implements CAPM and Fama-French 5-Factor regressions to estimate alpha, beta exposures, residual returns, t-statistics, and significance metrics.       |
| `src/alpha_testing.py`    | Performs high-dimensional alpha testing, residual dependence analysis, correlation structure estimation, and market-wide alpha significance evaluation. |
| `src/dynamic_alpha.py`    | Computes rolling alpha and beta estimates, constructs the Market Inefficiency Index, and tracks the evolution of abnormal returns through time.         |
| `src/pinn.py`             | Implements Physics-Informed Neural Networks (PINNs) for modeling and forecasting alpha dynamics under PDE-based financial constraints.                  |
| `src/inverse_pde.py`      | Learns latent market dynamics by estimating drift and diffusion parameters governing alpha evolution through inverse PDE discovery.                     |
| `src/regime_detection.py` | Applies machine learning clustering techniques to classify market states into Efficient, Crisis, Alpha Opportunity, and Normalization regimes.          |
| `src/portfolio.py`        | Generates alpha rankings, constructs long-short portfolios, and computes portfolio allocations from forecast alpha signals.                             |
| `src/backtesting.py`      | Evaluates economic significance using annualized return, Sharpe ratio, Sortino ratio, maximum drawdown, win rate, and performance attribution metrics.  |

### Research Pipeline

`factor_models.py`
→ `alpha_testing.py`
→ `dynamic_alpha.py`
→ `pinn.py`
→ `inverse_pde.py`
→ `regime_detection.py`
→ `portfolio.py`
→ `backtesting.py`

This sequence represents the complete alpha discovery, forecasting, and economic validation workflow implemented in QuantAlpha AI.

## Benchmark Evaluation

Strategy performance was evaluated relative to:

* Market Average Portfolio Return
* Risk-Free Rate Baseline
* Equal-Weighted Equity Portfolio
* Static Factor-Based Alpha Strategy

## Key Results Highlights 

| Category | Result |
|-----------|-----------|
| Dataset | 10 U.S. Large-Cap Equities |
| Historical Horizon | 5 Years |
| Asset Pricing Model | Fama-French 5-Factor |
| Alpha Framework | High-Dimensional Alpha Detection |
| Dynamic Modeling | Rolling Alpha Estimation |
| Scientific ML | Physics-Informed Neural Networks (PINNs) |
| Market State Modeling | Regime Detection |
| Strategy Type | Long-Short Alpha Portfolio |
| Annualized Return | 24.3% |
| Win Rate | 56.7% |
| Sharpe Ratio | 0.64 |
| Sortino Ratio | 0.94 |
| Maximum Drawdown | -39.4% |
| Research Areas | Quant Finance, Econometrics, Scientific ML |

<img width="700" height="400" alt="image" src="https://github.com/user-attachments/assets/9cfa39df-b8c5-4d06-9f5c-f79a97da329c" />








        







