# END-TO-END STRATEGY BACKTESTING
# QuantAlpha AI
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ==========================================================
# STEP 1
# LOAD DATA
# ==========================================================

returns = pd.read_csv(
    "stock_returns.csv",
    index_col=0,
    parse_dates=True
)

rolling_alpha = pd.read_csv(
    "rolling_alpha_matrix.csv",
    index_col=0,
    parse_dates=True
)

regimes = pd.read_csv(
    "market_regimes.csv",
    index_col=0,
    parse_dates=True
)

# ==========================================================
# STEP 2
# ALIGN DATES
# ==========================================================

common_dates = (
    rolling_alpha.index
    .intersection(returns.index)
)

rolling_alpha = rolling_alpha.loc[common_dates]
returns = returns.loc[common_dates]

# ==========================================================
# STEP 3
# PARAMETERS
# ==========================================================

TOP_N = 3
BOTTOM_N = 3

# ==========================================================
# STEP 4
# MONTHLY REBALANCING
# ==========================================================

portfolio_returns = []

portfolio_dates = []

for date in rolling_alpha.index[:-1]:

    alpha_today = rolling_alpha.loc[date]

    alpha_today = alpha_today.dropna()

    # Long Portfolio
    long_stocks = (
        alpha_today
        .sort_values(ascending=False)
        .head(TOP_N)
        .index
    )

    # Short Portfolio
    short_stocks = (
        alpha_today
        .sort_values()
        .head(BOTTOM_N)
        .index
    )

    next_idx = (
        rolling_alpha.index
        .get_loc(date)
        + 1
    )

    next_date = rolling_alpha.index[next_idx]

    next_returns = returns.loc[next_date]

    long_return = (
        next_returns[long_stocks]
        .mean()
    )

    short_return = (
        next_returns[short_stocks]
        .mean()
    )

    strategy_return = (
        long_return
        -
        short_return
    )

    portfolio_returns.append(
        strategy_return
    )

    portfolio_dates.append(
        next_date
    )

# ==========================================================
# STEP 5
# CREATE RETURN SERIES
# ==========================================================

portfolio_returns = pd.DataFrame(
    {
        "Return":
        portfolio_returns
    },
    index=portfolio_dates
)

# ==========================================================
# STEP 6
# EQUITY CURVE
# ==========================================================

equity_curve = (
    1 +
    portfolio_returns["Return"]
).cumprod()

# ==========================================================
# STEP 7
# ANNUALIZED RETURN
# ==========================================================

annual_return = (
    portfolio_returns["Return"]
    .mean()
    * 12
)

# ==========================================================
# STEP 8
# VOLATILITY
# ==========================================================

annual_vol = (
    portfolio_returns["Return"]
    .std()
    * np.sqrt(12)
)

# ==========================================================
# STEP 9
# SHARPE RATIO
# ==========================================================

risk_free = 0.02

sharpe = (
    annual_return
    -
    risk_free
) / annual_vol

# ==========================================================
# STEP 10
# SORTINO RATIO
# ==========================================================

downside = (
    portfolio_returns["Return"]
)

downside = downside[
    downside < 0
]

downside_std = (
    downside.std()
    * np.sqrt(12)
)

sortino = (
    annual_return
    -
    risk_free
) / downside_std

# ==========================================================
# STEP 11
# MAXIMUM DRAWDOWN
# ==========================================================

rolling_max = (
    equity_curve
    .cummax()
)

drawdown = (
    equity_curve
    -
    rolling_max
) / rolling_max

max_drawdown = (
    drawdown.min()
)

# ==========================================================
# STEP 12
# WIN RATE
# ==========================================================

win_rate = (
    (
        portfolio_returns["Return"]
        > 0
    ).mean()
)

# ==========================================================
# STEP 13
# INFORMATION RATIO
# ==========================================================

benchmark = (
    returns.mean(axis=1)
)

benchmark = benchmark.loc[
    portfolio_returns.index
]

active_return = (
    portfolio_returns["Return"]
    -
    benchmark
)

information_ratio = (
    active_return.mean()
    /
    active_return.std()
)

# ==========================================================
# STEP 14
# SAVE METRICS
# ==========================================================

metrics = pd.DataFrame({

    "Metric":[

        "Annual Return",
        "Annual Volatility",
        "Sharpe Ratio",
        "Sortino Ratio",
        "Max Drawdown",
        "Win Rate",
        "Information Ratio"

    ],

    "Value":[

        annual_return,
        annual_vol,
        sharpe,
        sortino,
        max_drawdown,
        win_rate,
        information_ratio

    ]

})

metrics.to_csv(
    "backtest_metrics.csv",
    index=False
)

# ==========================================================
# STEP 15
# SAVE RETURNS
# ==========================================================

portfolio_returns.to_csv(
    "portfolio_returns.csv"
)

equity_curve.to_csv(
    "equity_curve.csv"
)

drawdown.to_csv(
    "drawdown_series.csv"
)

# ==========================================================
# STEP 16
# REGIME ANALYSIS
# ==========================================================

regimes = regimes.reindex(
    portfolio_returns.index
)

regime_returns = pd.concat(
    [
        portfolio_returns,
        regimes["regime_name"]
    ],
    axis=1
)

regime_performance = (
    regime_returns
    .groupby("regime_name")
    ["Return"]
    .mean()
)

regime_performance.to_csv(
    "regime_performance.csv"
)

# ==========================================================
# STEP 17
# EQUITY CURVE PLOT
# ==========================================================

plt.figure(figsize=(14,6))

plt.plot(
    equity_curve.index,
    equity_curve.values,
    linewidth=2
)

plt.title(
    "QuantAlpha AI Strategy Equity Curve"
)

plt.xlabel("Date")

plt.ylabel(
    "Growth of $1"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "equity_curve.png",
    dpi=300
)

plt.show()

# ==========================================================
# STEP 18
# DRAWDOWN PLOT
# ==========================================================

plt.figure(figsize=(14,6))

plt.plot(
    drawdown.index,
    drawdown.values
)

plt.title(
    "Strategy Drawdown"
)

plt.xlabel("Date")

plt.ylabel("Drawdown")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "drawdown_plot.png",
    dpi=300
)

plt.show()
