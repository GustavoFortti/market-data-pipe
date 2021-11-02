import sys
from copy import deepcopy

import pandas as pd
import numpy as np

from config.config import config
from src.services.api import api_market

import ta
from src.indicators_analysis.generate_labels import Genlabels
from src.indicators_analysis.poly_interpolation import PolyInter
from src.indicators_analysis.fibonacci import Fibonacci
from src.indicators_analysis.sar_parabolic import Parabolic_sar
from src.indicators_analysis.macd import Ema

def indicator() -> None:
    conf = config("XOM")
    df = api_market(conf)
    df = ta.add_all_ta_features(df=df, close="Close", high='High', low='Low', open="Open", volume="Volume", fillna=True)

    default_columns = ['Close', 'High', 'Low', 'Open']
    Ema_5_columns = [
        'Close_Ema_5', 'High_Ema_5', 'Low_Ema_5', 'Open_Ema_5', 
        'Close_Ema_9', 'High_Ema_9', 'Low_Ema_9', 'Open_Ema_9', 
        'Close_Ema_12', 'High_Ema_12', 'Low_Ema_12', 'Open_Ema_12'
    ]

    indicators = [
        {"name": "Ema_5", "columns": default_columns, "method": Ema, "params": {"period":5}},
        {"name": "Ema_9", "columns": default_columns, "method": Ema, "params": {"period":9}},
        {"name": "Ema_12", "columns": default_columns, "method": Ema, "params": {"period":12}},
        {"name": "labels", "columns": default_columns.append(Ema_5_columns), "method": Genlabels, "params": {"window": 29, "polyorder": 3}},
        {"name": "PolyInter", "columns": default_columns.append(Ema_5_columns), "method": PolyInter, "params": {"degree":4, "pd":20, "plot":False, "progress_bar":True}},
    ]

    df = add_variables(df, indicators)
    df = col_parabolic_sar(df, ['ema_5_High', 'ema_5_Low'])
    print(df)
    # df['Open_ge'] = df.Open.ge(df.Open.shift())

def add_variables(df: pd.DataFrame, indicators: list) -> pd.DataFrame:
    df = deepcopy(df)
    for i in indicators:
        for j in i['columns']:
            df[(j + '_' + i['name'])] = i['method'](df[j], i['params']).get_values()
    return df

def col_parabolic_sar(df: pd.DataFrame, cols: list, params: dict={"af":0.02, "amax":0.2}, name: str='parabolic_sar') -> pd.DataFrame:
    df = deepcopy(df)
    df[name] = Parabolic_sar(df.loc[:, cols], params, cols[0], cols[1]).values
    return df