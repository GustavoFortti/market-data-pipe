import os
import pandas as pd
import numpy as np

def premodel(currency: str, date: str, d_matrix: str, variables: str, timestemp: int=8):
    path = f'./../data/indicator/{currency}/variable/{date}.csv'
    df = pd.read_csv(path, index_col='Date')
    df = df.loc[:, variables['variables']]
    target = df.loc[:, variables['target']].drop(columns='Date')

    x = np.array(df)[100: -1]
    y = np.array(target)[101:]
    if (d_matrix == '3'): x = matrix_3d(x, timestemp)
    save(x, y, df, target, currency)

def matrix_3d(x: np.array, timestemp: int) -> list:
    reshaped_x = []
    for i in range(timestemp, x.shape[0] + 1):
        reshaped_x.append(x[i - timestemp:i])
    return np.array(reshaped_x)

def save(x: np.array, y: np.array, df: pd.DataFrame, target: pd.DataFrame, currency: str) -> None:
    save_path = f'./../data/premodel/{currency}/'
    if (not os.path.exists(save_path)): os.makedirs(save_path)

    np.save(f'{save_path}/x', x)
    np.save(f'{save_path}/y', y)

    df.to_csv(f'{save_path}/df.csv')
    target.to_csv(f'{save_path}/target.csv')