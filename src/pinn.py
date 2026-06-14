# ====================================================
# PHASE 5
# PINN FOR DYNAMIC ALPHA EVOLUTION
# ====================================================

!pip install deepxde
import deepxde as dde
import numpy as np
import pandas as pd
import tensorflow as tf

# ====================================================
# STEP 1
# LOAD MARKET INEFFICIENCY SERIES
# ====================================================

alpha_series = pd.read_csv(
    "market_inefficiency_timeseries.csv"
)

# ====================================================
# STEP 2
# CREATE TRAINING DATA
# ====================================================

alpha_values = alpha_series.iloc[:,1].values

t = np.linspace(
    0,
    1,
    len(alpha_values)
)

alpha_values = alpha_values.reshape(-1,1)

# ====================================================
# STEP 3
# PDE PARAMETERS
# ====================================================

MU = 0.2
D = 0.05

# ====================================================
# STEP 4
# DEFINE PDE
# ====================================================

def alpha_pde(x,y):

    dy_t = dde.grad.jacobian(
        y,
        x,
        i=0,
        j=0
    )

    dy_x = dde.grad.jacobian(
        y,
        x,
        i=0,
        j=1
    )

    dy_xx = dde.grad.hessian(
        y,
        x,
        i=0,
        j=1
    )

    return (
        dy_t
        +
        MU*dy_x
        -
        D*dy_xx
    )

# ====================================================
# STEP 5
# DOMAIN
# ====================================================

time_domain = dde.geometry.TimeDomain(
    0,
    1
)

state_domain = dde.geometry.Interval(
    0,
    1
)

geomtime = dde.geometry.GeometryXTime(
    state_domain,
    time_domain
)

# ====================================================
# STEP 6
# OBSERVATION POINTS
# ====================================================

observe_t = np.vstack(
    (
        t,
        np.zeros_like(t)
    )
).T

bc = dde.icbc.PointSetBC(
    observe_t,
    alpha_values,
    component=0
)

# ====================================================
# STEP 7
# CREATE DATA OBJECT
# ====================================================

data = dde.data.TimePDE(
    geomtime,
    alpha_pde,
    [bc],
    num_domain=500,
    num_boundary=50,
    num_test=500
)

# ====================================================
# STEP 8
# PINN NETWORK
# ====================================================

net = dde.nn.FNN(
    [2,64,64,64,64,1],
    "tanh",
    "Glorot normal"
)

# ====================================================
# STEP 9
# MODEL
# ====================================================

model = dde.Model(
    data,
    net
)

# ====================================================
# STEP 10
# COMPILE
# ====================================================

model.compile(
    "adam",
    lr=1e-3
)

# ====================================================
# STEP 11
# TRAIN
# ====================================================

losshistory, train_state = model.train(
    iterations=10000
)

# ====================================================
# STEP 12
# SAVE MODEL
# ====================================================

model.save(
    "alpha_pinn_model"
)

print("PINN Model Saved")

# ====================================================
# STEP 13
# FORECAST ALPHA SURFACE
# ====================================================

t_grid = np.linspace(
    0,
    1,
    100
)

x_grid = np.linspace(
    0,
    1,
    100
)

TT,XX = np.meshgrid(
    t_grid,
    x_grid
)

inputs = np.hstack(
    (
        TT.reshape(-1,1),
        XX.reshape(-1,1)
    )
)

predictions = model.predict(
    inputs
)

# ====================================================
# STEP 14
# SAVE FORECASTS
# ====================================================

forecast_df = pd.DataFrame({
    "t":inputs[:,0],
    "state":inputs[:,1],
    "alpha":predictions.flatten()
})

forecast_df.to_csv(
    "alpha_surface_predictions.csv",
    index=False
)

print(
    "alpha_surface_predictions.csv saved"
)

# ====================================================
# PHASE 5 COMPLETE
# ====================================================


