import importlib
import os

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

def model(metrics: dict) -> None:
    data_path = f'./data/premodel/{metrics["currency"]}/{metrics["variables_set"]}/time_ahead_{metrics["time_ahead"]}/data_scaler/'
    np_path = f'{data_path}/x_{metrics["d_matrix"]}d'

    df_prd = pd.read_csv(f'{data_path}df.csv')
    df_tar = pd.read_csv(f'{data_path}target.csv')

    # pred = np.load(f'{np_path}_pred.npy')
    x = np.load(f'{np_path}_train.npy')
    y = np.load(f'{data_path}y_1d_train.npy')

    size = 100
    X_train, x_test, y_train, y_test = train_test_split(x[:-size], y[:-size], test_size=0.33, random_state=42)

    run = importlib.import_module("src.methods.GR1")
    run.method(X_train, x_test, y_train, y_test, x[-size:], y[-size:])

    # run.predict()
