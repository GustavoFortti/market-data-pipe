import os
import pandas as pd
import numpy as np

def premodel(currency: str,
            date: str,
            d_matrix: str,
            variables: dict,
            variables_set: str,
            timestemp: str,
            time_ahead: str,
            data_name=str) -> None:

    time_ahead = check_time_ahead(int(time_ahead))
    timestemp = int(timestemp)
    path = f'./data/indicator/{currency}/{data_name}.csv'
    df = pd.read_csv(path, index_col='Date')
    if (variables['predictor'][0] == 'all'): variables['predictor'] = df.columns
    df = df.loc[:, variables['predictor']]
    target = df.loc[:, variables['target']].drop(columns='Date')
    
    for i in ['pred', 'train']:
        x, y = np.array(df), np.array(target)
        if (i == 'train'): x, y = x[100: -(time_ahead)], y[(100 + time_ahead):]
        else: x, y = x[100:], y[100:]
        if (d_matrix == '3'): x = matrix_3d(x, timestemp)
        save(x=x,
             y=y,
             df=df.iloc[100: -(time_ahead), :],
             target=target.iloc[(100 + time_ahead):],
             currency=currency,
             d_matrix=d_matrix,
             type_situation=i,
             time_ahead=time_ahead,
             variables_set=variables_set,
             data_name=data_name)

def matrix_3d(x: np.array, timestemp: int) -> list:
    reshaped_x = []
    for i in range(timestemp, x.shape[0] + 1):
        reshaped_x.append(x[i - timestemp:i])
    return np.array(reshaped_x)

def save(x: np.array,
        y: np.array,
        df: pd.DataFrame,
        target: pd.DataFrame,
        currency: str,
        d_matrix: str,
        type_situation: str,
        time_ahead: str,
        variables_set: str,
        data_name: str) -> None:

    save_path = f'./data/premodel/{currency}/{variables_set}/time_ahead_{time_ahead}/{data_name}/'
    if (not os.path.exists(save_path)): os.makedirs(save_path)

    np.save(f'{save_path}/x_{d_matrix}d_{type_situation}', x)
    # np.savez_compressed(f'{save_path}/x_{d_matrix}d_{type_situation}', x)

    if (type_situation == 'train'): 
        np.save(f'{save_path}/y_1d_train', y)
        # np.savez_compressed(f'{save_path}/y_1d_train', y)
        # np.load(f'{save_path}/y_1d_train', mmap_mode='r+')
        df.to_csv(f'{save_path}/df.csv')
        target.to_csv(f'{save_path}/target.csv')
    
def check_time_ahead(time_ahead: int):
    if (time_ahead <= 0): 
        print("time_ahead is not > 0 | time_ahead = 1 now")
        return 1
    return time_ahead