import numpy as np
from scipy.optimize import minimize
from .data_fetcher import fetch_data

def minimum_variance_portfolio(tickers, start_date, end_date):
    """Calculate the minimum variance portfolio."""
    returns = fetch_data(tickers, start_date, end_date).pct_change(fill_method=None).dropna()
    cov_matrix = returns.cov()
    n_assets = len(tickers)
    initial_guess = np.ones(n_assets) / n_assets
    bounds = [(0, 1)] * n_assets
    constraints = [{'type': 'eq', 'fun': lambda w: np.sum(w) - 1}]
    result = minimize(portfolio_variance, initial_guess, args=(cov_matrix,), bounds=bounds, constraints=constraints)
    return result.x

def portfolio_variance(weights, cov_matrix):
    """Calculate portfolio variance."""
    return np.dot(weights.T, np.dot(cov_matrix, weights))
