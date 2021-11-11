import os
import pandas as pd
import numpy as np

def premodel(currency: str, date: str, d_matrix: str, predictor: str, target: str, timestemp: str, time_ahead: str) -> None:
    time_ahead = check_time_ahead(int(time_ahead))
    timestemp = int(timestemp)
    path = f'./data/indicator/{currency}/data.csv'
    df = pd.read_csv(path, index_col='Date')
    df = df.loc[:, predictor.split(',')]
    target = df.loc[:, target].drop(columns='Date')
    
    for i in ['pred', 'train']:
        x, y = np.array(df), np.array(target)
        if (i == 'train'): x, y = x[100: -(time_ahead)], y[(100 + time_ahead):]
        else: x, y = x[100:], y[100:]
        if (d_matrix == '3'): x = matrix_3d(x, timestemp)
        save(x, y, df.iloc[100: -(time_ahead), :], target.iloc[(100 + time_ahead):], currency, d_matrix, i, time_ahead)

def matrix_3d(x: np.array, timestemp: int) -> list:
    reshaped_x = []
    for i in range(timestemp, x.shape[0] + 1):
        reshaped_x.append(x[i - timestemp:i])
    return np.array(reshaped_x)

def save(x: np.array, y: np.array, df: pd.DataFrame, target: pd.DataFrame, currency: str, d_matrix: str, type_situation: str, time_ahead: str) -> None:
    save_path = f'./data/premodel/{currency}/'
    if (not os.path.exists(save_path)): os.makedirs(save_path)

    np.save(f'{save_path}/x_{d_matrix}d_{type_situation}_{time_ahead}tah', x)

    if (type_situation == 'train'): 
        np.save(f'{save_path}/y_1d_train_{time_ahead}tah', y)
        df.to_csv(f'{save_path}/df_{time_ahead}tah.csv')
        target.to_csv(f'{save_path}/target_{time_ahead}tah.csv')

def check_time_ahead(time_ahead: int):
    print(time_ahead)
    if (time_ahead <= 0): 
        print("time_ahead is not > 0 | time_ahead = 1 now")
        return 1
    return time_ahead