import os
import importlib

import pandas as pd
import numpy as np


def model(metrics: dict) -> None:
    data_path = f'./data/premodel/{metrics["currency"]}/{metrics["variables_set"]}/time_ahead_{metrics["time_ahead"]}/'
    np_path = f'{data_path}/x_{metrics["d_matrix"]}d'

    df_prd = pd.read_csv(f'{data_path}df.csv')
    df_tar = pd.read_csv(f'{data_path}target.csv')

    # pred = np.load(f'{np_path}_pred.npy')
    x = np.load(f'{np_path}_train.npy')
    y = np.load(f'{data_path}y_1d_train.npy')
    
    run = importlib.import_module("src.methods.GR1")
    run.method()

    run.predict()