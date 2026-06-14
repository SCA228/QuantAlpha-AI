# ====================================================
# PHASE 6
# INVERSE PDE DISCOVERY
# ====================================================

import deepxde as dde
import numpy as np
import pandas as pd
import tensorflow as tf

# ====================================================
# STEP 1
# LOAD PHASE 4 OUTPUT
# ====================================================

alpha_data = pd.read_csv(
    "market_inefficiency_timeseries.csv"
)

alpha_values = (
    alpha_data.iloc[:,1]
    .values
    .reshape(-1,1)
)

# ====================================================
# STEP 2
# TIME GRID
# ====================================================

t = np.linspace(
    0,
    1,
    len(alpha_values)
)

# ====================================================
# STEP 3
# UNKNOWN PDE PARAMETERS
# ====================================================

mu = tf.Variable(
    0.1,
    trainable=True,
    dtype=tf.float32
)

D = tf.Variable(
    0.1,
    trainable=True,
    dtype=tf.float32
)

# ====================================================
# STEP 4
# PDE
# ====================================================

def pde(x,y):

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
        mu*dy_x
        -
        D*dy_xx
    )

# ====================================================
# STEP 5
# DOMAIN
# ====================================================

geom = dde.geometry.Interval(
    0,
    1
)

timedomain = dde.geometry.TimeDomain(
    0,
    1
)

geomtime = dde.geometry.GeometryXTime(
    geom,
    timedomain
)

# ====================================================
# STEP 6
# OBSERVATIONS
# ====================================================

observe_points = np.vstack(
    (
        t,
        np.zeros_like(t)
    )
).T

bc = dde.icbc.PointSetBC(
    observe_points,
    alpha_values,
    component=0
)

# ====================================================
# STEP 7
# DATASET
# ====================================================

data = dde.data.TimePDE(
    geomtime,
    pde,
    [bc],
    num_domain=500,
    num_boundary=100,
    num_test=500
)

# ====================================================
# STEP 8
# NETWORK
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
    lr=1e-3,
    external_trainable_variables=[
        mu,
        D
    ]
)

# ====================================================
# STEP 11
# TRAIN
# ====================================================

losshistory, train_state = model.train(
    iterations=15000
)

# ====================================================
# STEP 12
# EXTRACT PARAMETERS
# ====================================================

mu_estimate = float(
    mu.numpy()
)

D_estimate = float(
    D.numpy()
)

print(
    "Learned Mu:",
    mu_estimate
)

print(
    "Learned D:",
    D_estimate
)

# ====================================================
# STEP 13
# SAVE PARAMETERS
# ====================================================

params = pd.DataFrame({
    "Parameter":[
        "mu",
        "D"
    ],
    "Value":[
        mu_estimate,
        D_estimate
    ]
})

params.to_csv(
    "learned_pde_parameters.csv",
    index=False
)

# ====================================================
# STEP 14
# FORECAST SURFACE
# ====================================================

future_t = np.linspace(
    0,
    1.5,
    200
)

future_x = np.linspace(
    0,
    1,
    200
)

TT,XX = np.meshgrid(
    future_t,
    future_x
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

forecast = pd.DataFrame({
    "time":inputs[:,0],
    "state":inputs[:,1],
    "alpha":predictions.flatten()
})

forecast.to_csv(
    "alpha_forecast.csv",
    index=False
)

# ====================================================
# STEP 15
# SAVE MODEL
# ====================================================

model.save(
    "inverse_pinn_model"
)

print(
    "Inverse PDE Discovery Complete"
)
