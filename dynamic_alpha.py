 # ==========================================================
# PHASE 4
# DYNAMIC ALPHA MODELING
# QuantAlpha AI
# ==========================================================

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# STEP 1
# LOAD DATA
# ==========================================================

excess_returns = pd.read_csv(
    "excess_returns.csv",
    index_col=0,
    parse_dates=True
)

factors = pd.read_csv(
    "factor_data.csv",
    index_col=0,
    parse_dates=True
)

print("Data Loaded")

# ==========================================================
# STEP 2
# FACTOR MODEL
# ==========================================================

factor_cols = [
    "Mkt-RF",
    "SMB",
    "HML",
    "RMW",
    "CMA"
]

# ==========================================================
# STEP 3
# ROLLING WINDOW
# ==========================================================

WINDOW = 12 # Changed from 60 to 12 to ensure the loop runs

# ==========================================================
# STORAGE
# ==========================================================

rolling_alpha_list = []
rolling_tstat_list = []
rolling_beta_list = []

rolling_dates = []

# ==========================================================
# STEP 4
# ROLLING REGRESSIONS
# ==========================================================

for end_idx in range(WINDOW, len(excess_returns)):

    start_idx = end_idx - WINDOW

    y_window = excess_returns.iloc[start_idx:end_idx]

    factor_window = factors.iloc[start_idx:end_idx]

    date = excess_returns.index[end_idx]

    alpha_snapshot = {}
    tstat_snapshot = {}
    beta_snapshot = {}

    for stock in excess_returns.columns:

        try:

            y = y_window[stock]

            X = factor_window[factor_cols]

            X = sm.add_constant(X)

            model = sm.OLS(y, X).fit()

            alpha_snapshot[stock] = model.params["const"]

            tstat_snapshot[stock] = model.tvalues["const"]

            beta_snapshot[stock] = model.params["Mkt-RF"]

        except:

            alpha_snapshot[stock] = np.nan
            tstat_snapshot[stock] = np.nan
            beta_snapshot[stock] = np.nan

    rolling_alpha_list.append(alpha_snapshot)
    rolling_tstat_list.append(tstat_snapshot)
    rolling_beta_list.append(beta_snapshot)

    rolling_dates.append(date)

# ==========================================================
# STEP 5
# CREATE MATRICES
# ==========================================================

rolling_alpha_df = pd.DataFrame(
    rolling_alpha_list,
    index=rolling_dates
)

rolling_tstat_df = pd.DataFrame(
    rolling_tstat_list,
    index=rolling_dates
)

rolling_beta_df = pd.DataFrame(
    rolling_beta_list,
    index=rolling_dates
)

print("Rolling Matrices Created")

# ==========================================================
# STEP 6
# MARKET INEFFICIENCY INDEX
# ==========================================================

market_inefficiency = (
    rolling_alpha_df
    .abs()
    .mean(axis=1)
)

market_inefficiency = pd.DataFrame({
    "Market_Inefficiency":
    market_inefficiency
})

# ==========================================================
# STEP 7
# SAVE CSV FILES
# ==========================================================

rolling_alpha_df.to_csv(
    "rolling_alpha_matrix.csv"
)

rolling_tstat_df.to_csv(
    "rolling_tstat_matrix.csv"
)

rolling_beta_df.to_csv(
    "rolling_beta_matrix.csv"
)

market_inefficiency.to_csv(
    "market_inefficiency_timeseries.csv"
)

print("CSV Files Saved")

# ==========================================================
# STEP 8
# MARKET INEFFICIENCY PLOT
# ==========================================================

plt.figure(figsize=(14,6))

plt.plot(
    market_inefficiency.index,
    market_inefficiency[
        "Market_Inefficiency"
    ]
)

plt.title(
    "Dynamic Market Inefficiency"
)

plt.xlabel("Date")

plt.ylabel(
    "Average Absolute Alpha"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "market_inefficiency_plot.png",
    dpi=300
)

plt.show()

# ==========================================================
# STEP 9
# TOP ALPHA STOCKS
# ==========================================================

latest_alpha = rolling_alpha_df.iloc[-1]

top_alpha = (
    latest_alpha
    .abs()
    .sort_values(
        ascending=False
    )
    .head(20)
)

top_alpha.to_csv(
    "top_alpha_stocks.csv"
)

print("\nTop Alpha Stocks")
print(top_alpha)

# ==========================================================
# STEP 10
# ALPHA HEATMAP
# ==========================================================

heatmap_data = (
    rolling_alpha_df
    .T
)

plt.figure(
    figsize=(16,10) 
)

sns.heatmap(
    heatmap_data,
    cmap="RdBu_r",
    center=0
)

plt.title(
    "Dynamic Alpha Heatmap"
)

plt.tight_layout()

plt.savefig(
    "alpha_heatmap.png",
    dpi=300
)

plt.show()

# ==========================================================
# STEP 11
# ALPHA DISPERSION
# ==========================================================

alpha_dispersion = (
    rolling_alpha_df
    .std(axis=1)
)

plt.figure(figsize=(14,6))

plt.plot(
    alpha_dispersion.index,
    alpha_dispersion
)

plt.title(
    "Alpha Dispersion Through Time"
)

plt.xlabel("Date")

plt.ylabel(
    "Cross-Sectional Alpha Std"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "alpha_dispersion.png",
    dpi=300
)

plt.show()

# ==========================================================
# STEP 12
# SUMMARY
# ==========================================================

print("\n==============================")
print("PHASE 4 COMPLETED")
print("==============================")

print(
    "\nGenerated Files:"
)

print(
    "rolling_alpha_matrix.csv"
)

print(
    "rolling_tstat_matrix.csv"
)

print(
    "rolling_beta_matrix.csv"
)

print(
    "market_inefficiency_timeseries.csv"
)

print(
    "top_alpha_stocks.csv"
)

print(
    "alpha_heatmap.png"
)

print(
    "market_inefficiency_plot.png"
)

print(
    "alpha_dispersion.png"
)

# ==========================================================

)

print(
    "market_inefficiency_timeseries.csv"
)
