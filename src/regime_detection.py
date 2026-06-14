# ====================================================
# PHASE 7
# MARKET REGIME DETECTION
# ====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# ====================================================
# STEP 1
# LOAD MARKET INEFFICIENCY
# ====================================================

df = pd.read_csv(
    "market_inefficiency_timeseries.csv",
    index_col=0,
    parse_dates=True
)

# ====================================================
# STEP 2
# CREATE FEATURES
# ====================================================

df["lag1"] = (
    df["Market_Inefficiency"]
    .shift(1)
)

df["rolling_mean"] = (
    df["Market_Inefficiency"]
    .rolling(6)
    .mean()
)

df["rolling_std"] = (
    df["Market_Inefficiency"]
    .rolling(6)
    .std()
)

df = df.dropna()

# ====================================================
# STEP 3
# FEATURE MATRIX
# ====================================================

features = df[
    [
        "Market_Inefficiency",
        "lag1",
        "rolling_mean",
        "rolling_std"
    ]
]

# ====================================================
# STEP 4
# NORMALIZE
# ====================================================

scaler = StandardScaler()

X = scaler.fit_transform(features)

# ====================================================
# STEP 5
# K-MEANS REGIME DETECTION
# ====================================================

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=20
)

df["regime"] = kmeans.fit_predict(X)

# ====================================================
# STEP 6
# REGIME LABELS
# ====================================================

regime_means = (
    df.groupby("regime")
    ["Market_Inefficiency"]
    .mean()
)

sorted_regimes = (
    regime_means
    .sort_values()
    .index
)

mapping = {
    sorted_regimes[0]:
    "Efficient",

    sorted_regimes[1]:
    "Mild_Inefficiency",

    sorted_regimes[2]:
    "Alpha_Opportunity",

    sorted_regimes[3]:
    "Crisis"
}

df["regime_name"] = (
    df["regime"]
    .map(mapping)
)

# ====================================================
# STEP 7
# SAVE REGIMES
# ====================================================

df.to_csv(
    "market_regimes.csv"
)

# ====================================================
# STEP 8
# TRANSITION MATRIX
# ====================================================

transition = pd.crosstab(
    df["regime_name"].shift(1),
    df["regime_name"]
)

transition.to_csv(
    "regime_transition_matrix.csv"
)

# ====================================================
# STEP 9
# PLOT
# ====================================================

plt.figure(figsize=(15,6))

plt.plot(
    df.index,
    df["Market_Inefficiency"],
    linewidth=2
)

colors = {
    "Efficient":"green",
    "Mild_Inefficiency":"yellow",
    "Alpha_Opportunity":"orange",
    "Crisis":"red"
}

for regime in colors:

    subset = df[
        df["regime_name"]
        == regime
    ]

    plt.scatter(
        subset.index,
        subset["Market_Inefficiency"],
        color=colors[regime],
        label=regime,
        alpha=0.7
    )

plt.title(
    "Market Regime Detection"
)

plt.xlabel("Date")
plt.ylabel("Market Inefficiency")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "regime_plot.png",
    dpi=300
)

plt.show()

# ====================================================
# STEP 10
# SUMMARY
# ====================================================

print("\n========================")
print("REGIME COUNTS")
print("========================")

print(
    df["regime_name"]
    .value_counts()
)

print("\nFiles Saved:")
print("market_regimes.csv")
print("regime_transition_matrix.csv")
print("regime_plot.png")

print("\nPHASE 7 COMPLETE")
