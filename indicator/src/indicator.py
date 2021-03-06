import sys
from copy import Error, deepcopy

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

from config.contructor import contructor
from src.services.api import api_market

import ta
from src.indicators_analysis.generate_labels import Genlabels
from src.indicators_analysis.poly_interpolation import PolyInter
from src.indicators_analysis.fibonacci import Fibonacci
from src.indicators_analysis.sar_parabolic import Parabolic_sar
from src.indicators_analysis.macd import Ema

def indicator(currency: str) -> None:
    conf = contructor(currency)
    df = api_market(conf)

    # indicators_columns, indicators = prepare_indicatores()
    # df = add_indicators(df, indicators)
    # df = col_greater_then(df, indicators_columns)
    # df = col_parabolic_sar(df, [['High_Ema_5', 'Low_Ema_5'], ['High_Ema_9', 'Low_Ema_9'], ['High_Ema_12', 'Low_Ema_12'], ['High', 'Low']])
    # df = ta.add_all_ta_features(df=df, close="Close", high='High', low='Low', open="Open", volume="Volume", fillna=True)
    # df = cols_diff(df)
    df = df.loc[:, ['Close']]

    print(df)
    save_data(df, conf['path_variable_data'])

    scaler = StandardScaler()
    scaler.fit(df)
    df_scaler = pd.DataFrame(scaler.transform(df), columns=df.columns, index=df.index)
    print(df_scaler)
    save_data(df_scaler, conf['path_variable_data_scaler'])

def cols_diff(df: pd.DataFrame) -> pd.DataFrame:
    df = deepcopy(df)
    def diff(df, col):
        df[f'{col}_diff'] = df[col].diff()

    [diff(df, i) for i in df.columns]
    return df

def add_indicators(df: pd.DataFrame, indicators: list) -> pd.DataFrame:
    df = deepcopy(df)
    for i in indicators:
        for j in i['columns']:
            df[(j + '_' + i['name'])] = i['method'](df[j], i['params']).get_values()
    return df

def col_parabolic_sar(df: pd.DataFrame, cols: list, params: dict={"af":0.02, "amax":0.2}, name: str='parabolic_sar') -> pd.DataFrame:
    df = deepcopy(df)
    for i in cols:
        df[f'{name}_{i[0]}_{i[1]}'] = Parabolic_sar(df.loc[:, i], params, i[0], i[1]).values
    return df

def col_greater_then(df: pd.DataFrame, cols: list) -> pd.DataFrame:
    df = deepcopy(df)
    for i in cols:
        try: df[f'{i}_ge'] = (df[i].ge(df[i].shift())).astype(int)
        except: print(f'column: {i} not exist')
    return df

def prepare_indicatores() -> list:
    default_columns = ['Close', 'High', 'Low', 'Open']

    Ema_columns = [
        'Close_Ema_5', 'High_Ema_5', 'Low_Ema_5', 'Open_Ema_5', 
        'Close_Ema_9', 'High_Ema_9', 'Low_Ema_9', 'Open_Ema_9', 
        'Close_Ema_12', 'High_Ema_12', 'Low_Ema_12', 'Open_Ema_12'
    ]

    indicators_columns = np.append(default_columns, Ema_columns)
    indicators = [
        {"name": "Ema_5", "columns": default_columns, "method": Ema, "params": {"period":5}},
        {"name": "Ema_9", "columns": default_columns, "method": Ema, "params": {"period":9}},
        {"name": "Ema_12", "columns": default_columns, "method": Ema, "params": {"period":12}},
        {"name": "labels", "columns": indicators_columns, "method": Genlabels, "params": {"window": 29, "polyorder": 3}},
        {"name": "PolyInter", "columns": indicators_columns, "method": PolyInter, "params": {"degree":4, "pd":20, "plot":False, "progress_bar":True}},
    ]

    return [indicators_columns, indicators]

def save_data(df: pd.DataFrame, path: str) -> None:
    try: 
        df.to_csv(path)
        print(f'save data - {path}')
    except Exception as error:
        print(f'error to save data - {path}\n')
        print(error)