import os
from datetime import datetime

def contructor(currency: str) -> dict:
    path_data = f'./data/indicator/{currency}/'
    if (not os.path.exists(path_data)): os.makedirs(path_data)
    path_variable_data = f'{path_data}data.csv'

    return {
        "currency": f'{currency}',
        "path_variable_data": path_variable_data,
        "columns": ["Open", "Close", "High", "Low", "Volume"]
    }