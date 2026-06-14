
# PHASE 3 — HIGH-DIMENSIONAL ALPHA TESTING
# Pesaran-Yamagata J_alpha Test
# ====================================================

import numpy as np
import pandas as pd
from scipy.stats import norm

# ====================================================
# STEP 1 — LOAD PHASE 2 RESULTS
# ====================================================

alphas = pd.read_csv(
    "alpha_matrix.csv",
    index_col=0
)

tstats = pd.read_csv(
    "tstats.csv",
    index_col=0
)

residuals = pd.read_csv(
    "residual_matrix.csv",
    index_col=0
)

print("Data Loaded")

# ====================================================
# STEP 2 — BASIC DIMENSIONS
# ====================================================

N = residuals.shape[1]
T = residuals.shape[0]

print("N =", N)
print("T =", T)

# ====================================================
# STEP 3 — COMPUTE RESIDUAL CORRELATION MATRIX
# ====================================================

R = residuals.corr()

print("\nCorrelation Matrix Shape:")
print(R.shape)

# ====================================================
# STEP 4 — SPARSE THRESHOLDING
# ====================================================

# Simple threshold version

threshold = 0.10

R_sparse = R.copy()

R_sparse[np.abs(R_sparse) < threshold] = 0

print("\nSparse Correlation Matrix Created")

# ====================================================
# STEP 5 — COMPUTE q_N^2
# ====================================================

upper_triangle = np.triu(
    R_sparse.values,
    k=1
)

qN_squared = (
    2
    *
    np.sum(upper_triangle**2)
    /
    (N*(N-1))
)

print("\nqN^2 =", qN_squared)

# ====================================================
# STEP 6 — LOAD T-STATISTICS
# ====================================================

t_values = tstats["t_stat"].values

# ====================================================
# STEP 7 — DEGREES OF FREEDOM
# ====================================================

# FF5

m = 5

v = T - m - 1

print("Degrees of Freedom =", v)

# ====================================================
# STEP 8 — COMPUTE SUM OF t_i^2
# ====================================================

sum_t_squared = np.sum(
    t_values**2
)

print("\nSum(t_i^2) =", sum_t_squared)

# ====================================================
# STEP 9 — NUMERATOR
# ====================================================

numerator = (
    (1/np.sqrt(N))
    *
    (
        sum_t_squared
        -
        (v/(v-2))
    )
)

# ====================================================
# STEP 10 — DENOMINATOR
# ====================================================

denominator = (
    (v/(v-2))
    *
    np.sqrt(
        (
            2*(v-1)
            /
            (v-4)
        )
        *
        (
            1
            +
            (N-1)*qN_squared
        )
    )
)

# ====================================================
# STEP 11 — J_ALPHA TEST
# ====================================================

J_alpha = numerator / denominator

print("\n================================")
print("J_ALPHA TEST")
print("================================")
print(J_alpha)

# ====================================================
# STEP 12 — P-VALUE
# ====================================================

p_value = 2 * (
    1 - norm.cdf(abs(J_alpha))
)

print("\nP-VALUE")
print(p_value)

# ====================================================
# STEP 13 — DECISION
# ====================================================

alpha_level = 0.05

if p_value < alpha_level:

    print("\nRESULT:")
    print("Reject H0")

    print(
        "Factor model fails "
        "to explain returns."
    )

else:

    print("\nRESULT:")
    print("Fail to Reject H0")

    print(
        "Factor model explains "
        "returns adequately."
    )

# ====================================================
# STEP 14 — SAVE RESULTS
# ====================================================

results = pd.DataFrame({
    "J_alpha":[J_alpha],
    "p_value":[p_value],
    "N":[N],
    "T":[T]
})

results.to_csv(
    "J_alpha_results.csv",
    index=False
)

print("\nSaved:")
print("J_alpha_results.csv")

# ====================================================
# STEP 15 — MARKET INEFFICIENCY SCORE
# ====================================================

market_inefficiency = abs(J_alpha)

print("\nMarket Inefficiency Score:")
print(market_inefficiency)

# ====================================================
# PHASE 3 COMPLETE
# ====================================================

print("\n================================")
print("PHASE 3 COMPLETED")
print("================================")

print("Outputs:")
print("- Sparse Correlation Matrix")
print("- qN_squared")
print("- J_alpha")
print("- p-value")
print("- Market Inefficiency Score")

