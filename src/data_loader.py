# src/data_loader.py

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def download_stock_data(ticker, start_date='2018-01-01', end_date=None):
    if not end_date:
        end_date = datetime.today().strftime('%Y-%m-%d')
    df = yf.download(ticker, start=start_date, end=end_date)
    return df

def save_data_to_csv(df, filename):
    df.to_csv(f"data/{filename}.csv")
    print(f"Saved: data/{filename}.csv")

if __name__ == "__main__":
    stocks = {
        'NIFTY_50': '^NSEI',  # Yahoo symbol for NIFTY 50
        'RELIANCE': 'RELIANCE.NS',
        'TCS': 'TCS.NS',
        'HDFCBANK': 'HDFCBANK.NS'
    }

    for name, symbol in stocks.items():
        print(f"Downloading {name}...")
        data = download_stock_data(symbol)
        save_data_to_csv(data, name)
