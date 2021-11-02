import pandas as pd
import yfinance as yf

def api_market(conf: dict) -> pd.DataFrame:
    df = yf.Ticker(conf['currency']).history(period="max")
    df = df.loc[:, conf['columns']]
    df = df.dropna()
    for i in df.columns: df = df[df[i] != 0]
    df.to_csv(conf['path_data'])

    return df