import pandas as pd
import yfinance as yf
from config.config import save_data

def api_market(conf: dict) -> pd.DataFrame:
    df = yf.Ticker(conf['currency']).history(period="max")
    df = df.loc[:, conf['columns']]
    df = df.dropna()
    for i in df.columns: df = df[df[i] != 0]
    save_data(df, conf['path_api_data'])
    return df