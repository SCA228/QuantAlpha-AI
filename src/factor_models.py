# =========================================================
-----------------------------

        # -----------------------------------------
        # Store p-value
        # ------------------# PHASE 2 — FACTOR PRICING ENGINE
# PINN-Based High-Dimensional Alpha Detection
# =========================================================

# =========================================================
# STEP 1 — IMPORT LIBRARIES
# =========================================================

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

# =========================================================
# STEP 2 — LOAD PHASE 1 DATA
# =========================================================

returns = pd.read_csv(
    "stock_returns.csv",
    index_col=0,
    parse_dates=True
)

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

print("DATA LOADED SUCCESSFULLY")

print("\nReturns Shape:", returns.shape)
print("Excess Returns Shape:", excess_returns.shape)
print("Factors Shape:", factors.shape)

# =========================================================
# STEP 3 — DEFINE FACTOR MODELS
# =========================================================

# CAPM
capm_factors = ["Mkt-RF"]

# Fama-French 3 Factor
ff3_factors = [
    "Mkt-RF",
    "SMB",
    "HML"
]

# Fama-French 5 Factor
ff5_factors = [
    "Mkt-RF",
    "SMB",
    "HML",
    "RMW",
    "CMA"
]

# =========================================================
# STEP 4 — CREATE STORAGE STRUCTURES
# =========================================================

alpha_dict = {}
tstat_dict = {}
pvalue_dict = {}
residuals_dict = {}
beta_dict = {}

# =========================================================
# STEP 5 — SELECT MODEL
# =========================================================

# Choose:
# capm_factors
# ff3_factors
# ff5_factors

selected_factors = ff5_factors

print("\nSelected Model Factors:")
print(selected_factors)

# =========================================================
# STEP 6 — RUN REGRESSION FOR EACH STOCK
# =========================================================

for stock in excess_returns.columns:

    try:

        # -----------------------------------------
        # Dependent Variable
        # -----------------------------------------

        y = excess_returns[stock]

        # -----------------------------------------
        # Independent Variables
        # -----------------------------------------

        X = factors[selected_factors]

        # Add intercept
        X = sm.add_constant(X)

        # -----------------------------------------
        # Run OLS Regression
        # -----------------------------------------

        model = sm.OLS(y, X).fit()

        # -----------------------------------------
        # Store Alpha
        # -----------------------------------------

        alpha_dict[stock] = model.params["const"]

        # -----------------------------------------
        # Store t-statistic
        # ----------------------------------

        pvalue_dict[stock] = model.pvalues["const"]

        # -----------------------------------------
        # Store Residuals
        # -----------------------------------------

        residuals_dict[stock] = model.resid

        # -----------------------------------------
        # Store Betas
        # -----------------------------------------

        beta_dict[stock] = model.params.drop("const")

    except Exception as e:

        print(f"Error processing {stock}: {e}")

# =========================================================
# STEP 7 — CONVERT TO DATAFRAMES
# =========================================================

alpha_df = pd.DataFrame.from_dict(
    alpha_dict,
    orient="index",
    columns=["Alpha"]
)

tstat_df = pd.DataFrame.from_dict(
    tstat_dict,
    orient="index",
    columns=["t_stat"]
)

pvalue_df = pd.DataFrame.from_dict(
    pvalue_dict,
    orient="index",
    columns=["p_value"]
)

residuals_df = pd.DataFrame(residuals_dict)

beta_df = pd.DataFrame(beta_dict).T

# =========================================================
# STEP 8 — DISPLAY RESULTS
# =========================================================

print("\n===================================")
print("ALPHA ESTIMATES")
print("===================================")

print(alpha_df.head())

print("\n===================================")
print("T-STATISTICS")
print("===================================")

print(tstat_df.head())

print("\n===================================")
print("P-VALUES")
print("===================================")

print(pvalue_df.head())

print("\n===================================")
print("BETA ESTIMATES")
print("===================================")

print(beta_df.head())

print("\n===================================")
print("RESIDUAL MATRIX")
print("===================================")

print(residuals_df.head())

# =========================================================
# STEP 9 — COMPUTE SIGNIFICANT ALPHAS
# =========================================================

significant_alphas = pvalue_df[
    pvalue_df["p_value"] < 0.05
]

print("\n===================================")
print("SIGNIFICANT ALPHAS")
print("===================================")

print(significant_alphas)

print(f"\nNumber of Significant Stocks: {len(significant_alphas)}")

# =========================================================
# STEP 10 — VISUALIZE ALPHAS
# =========================================================

plt.figure(figsize=(12,6))

alpha_df["Alpha"].plot(kind="bar")

plt.title("Estimated Alphas")
plt.xlabel("Stocks")
plt.ylabel("Alpha")

plt.grid(True)

plt.show()

# =========================================================
# STEP 11 — VISUALIZE T-STATISTICS
# =========================================================

plt.figure(figsize=(12,6))

tstat_df["t_stat"].plot(kind="bar")

plt.title("Alpha t-Statistics")
plt.xlabel("Stocks")
plt.ylabel("t-statistic")

plt.axhline(2, linestyle="--")
plt.axhline(-2, linestyle="--")

plt.grid(True)

plt.show()

# =========================================================
# STEP 12 — SAVE RESULTS
# =========================================================

alpha_df.to_csv("alpha_matrix.csv")

beta_df.to_csv("beta_matrix.csv")

residuals_df.to_csv("residual_matrix.csv")

tstat_df.to_csv("tstats.csv")

pvalue_df.to_csv("pvalues.csv")

print("\n===================================")
print("FILES SAVED SUCCESSFULLY")
print("===================================")

print("1. alpha_matrix.csv")
print("2. beta_matrix.csv")
print("3. residual_matrix.csv")
print("4. tstats.csv")
print("5. pvalues.csv")

# =========================================================
# STEP 13 — FINAL SUMMARY
# =========================================================

print("\n===================================")
print("PHASE 2 COMPLETED SUCCESSFULLY")
print("===================================")

print(f"\nNumber of Stocks Processed: {len(alpha_df)}")

print(f"\nResidual Matrix Shape: {residuals_df.shape}")

print("\nGenerated Outputs:")
print("- Alpha Estimates")
print("- Beta Estimates")
print("- Residual Matrix")
print("- t-Statistics")
print("- p-Values")
