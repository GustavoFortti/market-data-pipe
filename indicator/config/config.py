import sys
import os 
from datetime import datetime
import pandas as pd

def create_path(path_data: str, name: str):
    if (not os.path.exists(path_data)): os.makedirs(path_data)
    path_data += name
    return path_data

def config(currency: str) -> dict:
    path_variable_data = create_path(f'./data/indicator/{currency}/', 'data.csv')

    return {
        "currency": f'{currency}',
        "path_variable_data": path_variable_data,
        "columns": ["Open", "Close", "High", "Low", "Volume"]
    }

def save_data(df: pd.DataFrame, path: str):
    try: 
        df.to_csv(path)
        print(f'save data - {path}')
    except:
        print(f'error to save data - {path}')