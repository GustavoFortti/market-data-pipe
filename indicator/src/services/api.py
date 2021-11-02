import os
import sys

import pandas as pd
import yfinance as yf

def Api_market(mode: str, config: dict) -> None:
    currency = config['market']['currency']
    path = config['path']
    request = config['market']['request']

    file = path + currency + '.csv'
    if ((request) | (not os.path.isfile(file)) | (mode == 'pr')):
        data = yf.Ticker(currency)
        data = data.history(period="max")
        data = data.loc[:, config['data']['predict']['columns']]
        data = data.dropna()
        for i in data.columns: 
            data = data[data[i] != 0]
        data.to_csv(file)
    else:
        data = pd.read_csv(file, index_col='Date')