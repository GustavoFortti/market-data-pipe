import os 
from datetime import datetime

def config(currency: str) -> dict:
    date = datetime.today().strftime('%Y%m%d')
    name = f'{date}.csv'
    path = f'./../data/indicator/{currency}'
    if (not os.path.exists(path)): os.makedirs(path)
    path += name
    
    return {
        "currency": f'{currency}',
        "path_data": path,
        "columns": ["Open", "Close", "High", "Low", "Volume"]
    }