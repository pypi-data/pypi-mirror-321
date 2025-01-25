import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date, end_date):
    """Fetch historical data for a list of tickers using yfinance."""
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close']

def fetch_market_data(ticker, start_date, end_date):
    """Fetch market data for a single ticker using yfinance."""
    data = yf.download(ticker, start=start_date, end=end_date)
    return data['Adj Close']
