# ALPHA FORECASTING & PORTFOLIO CONSTRUCTION
# ====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ====================================================
# STEP 1
# LOAD DATA
# ====================================================

rolling_alpha = pd.read_csv(
    "rolling_alpha_matrix.csv",
    index_col=0,
    parse_dates=True
)

returns = pd.read_csv(
    "stock_returns.csv",
    index_col=0,
    parse_dates=True
)

regimes = pd.read_csv(
    "market_regimes.csv",
    index_col=0,
    parse_dates=True
)

# ====================================================
# STEP 2
# USE LATEST ALPHA ESTIMATES
# ====================================================

latest_alpha = rolling_alpha.iloc[-1]

alpha_rankings = (
    latest_alpha
    .sort_values(
        ascending=False
    )
)

alpha_rankings.to_csv(
    "alpha_rankings.csv"
)

print("Alpha Rankings Created")

# ====================================================
# STEP 3
# SELECT TOP/BOTTOM STOCKS
# ====================================================

TOP_N = 10

long_stocks = (
    alpha_rankings
    .head(TOP_N)
    .index
)

short_stocks = (
    alpha_rankings
    .tail(TOP_N)
    .index
)

print("\nLONG STOCKS")
print(long_stocks)

print("\nSHORT STOCKS")
print(short_stocks)

# ====================================================
# STEP 4
# EQUAL WEIGHT PORTFOLIO
# ====================================================

weights = {}

for stock in long_stocks:

    weights[stock] = 1/TOP_N

for stock in short_stocks:

    weights[stock] = -1/TOP_N

portfolio_weights = pd.DataFrame(
    {
        "Stock":weights.keys(),
        "Weight":weights.values()
    }
)

portfolio_weights.to_csv(
    "portfolio_weights.csv",
    index=False
)

# ====================================================
# STEP 5
# BACKTEST
# ====================================================

returns = returns[
    portfolio_weights["Stock"]
]

weights_vector = (
    portfolio_weights
    .set_index("Stock")
    ["Weight"]
)

portfolio_returns = (
    returns
    * weights_vector
).sum(axis=1)

portfolio_returns = pd.DataFrame(
    {
        "Portfolio_Return":
        portfolio_returns
    }
)

portfolio_returns.to_csv(
    "portfolio_returns.csv"
)

# ====================================================
# STEP 6
# CUMULATIVE RETURNS
# ====================================================

cumulative_returns = (
    1 + portfolio_returns
).cumprod()

# ====================================================
# STEP 7
# SAVE LONG-SHORT PORTFOLIO
# ====================================================

long_short = pd.DataFrame(
    {
        "Long":list(long_stocks),
        "Short":list(short_stocks)
    }
)

long_short.to_csv(
    "long_short_portfolio.csv",
    index=False
)

# ====================================================
# STEP 8
# PLOT PERFORMANCE
# ====================================================

plt.figure(figsize=(14,6))

plt.plot(
    cumulative_returns.index,
    cumulative_returns[
        "Portfolio_Return"
    ],
    linewidth=2
)

plt.title(
    "Long-Short Alpha Portfolio"
)

plt.xlabel("Date")
plt.ylabel("Growth of $1")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "cumulative_returns.png",
    dpi=300
)

plt.show()

# ====================================================
# STEP 9
# PERFORMANCE METRICS
# ====================================================

annual_return = (
    portfolio_returns.mean().iloc[0]
    * 252
)

annual_vol = (
    portfolio_returns.std().iloc[0]
    * np.sqrt(252)
)

sharpe = (
    annual_return
    /
    annual_vol
)

print("\n====================")
print("PERFORMANCE")
print("====================")

print(
    "Annual Return:",
    round(annual_return,4)
)

print(
    "Annual Volatility:",
    round(annual_vol,4)
)

print(
    "Sharpe Ratio:",
    round(sharpe,4)
)

# ====================================================
# STEP 10
# SAVE METRICS
# ====================================================

metrics = pd.DataFrame(
    {
        "Metric":[
            "Annual Return",
            "Annual Volatility",
            "Sharpe Ratio"
        ],
        "Value":[
            annual_return,
            annual_vol,
            sharpe
        ]
    }
)

metrics.to_csv(
    "portfolio_metrics.csv",
    index=False
)

print("\nFiles Saved")

print(
    "alpha_rankings.csv"
)

print(
    "portfolio_weights.csv"
)

print(
    "long_short_portfolio.csv"
)

print(
    "portfolio_returns.csv"
)

print(
    "portfolio_metrics.csv"
)

print(
    "cumulative_returns.png"
)
