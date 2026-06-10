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













        







