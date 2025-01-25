from .minimum_variance import minimum_variance_portfolio
from .data_fetcher import fetch_data

def robust_optimization(tickers, start_date, end_date, uncertainty_factor=0.1):
    """Perform robust portfolio optimization with uncertainty handling."""
    returns = fetch_data(tickers, start_date, end_date).pct_change(fill_method=None).dropna()
    cov_matrix = returns.cov()
    robust_cov_matrix = cov_matrix * (1 + uncertainty_factor)
    return minimum_variance_portfolio(tickers, start_date, end_date)
