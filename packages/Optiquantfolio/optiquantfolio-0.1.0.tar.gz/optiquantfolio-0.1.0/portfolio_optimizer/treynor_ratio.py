from .data_fetcher import fetch_data

def treynor_ratio(portfolio_return, risk_free_rate, portfolio_beta):
    """Calculate the Treynor ratio."""
    return (portfolio_return - risk_free_rate) / portfolio_beta

def treynor_ratio_analysis(portfolios, risk_free_rate, start_date, end_date):
    """Analyze the Treynor ratio of multiple portfolios."""
    returns = {p['name']: fetch_data(p['tickers'], start_date, end_date).pct_change(fill_method=None).mean() for p in portfolios}
    betas = {p['name']: fetch_data(p['tickers'], start_date, end_date).pct_change(fill_method=None).cov() for p in portfolios}
    return {p['name']: treynor_ratio(returns[p['name']], risk_free_rate, betas[p['name']]) for p in portfolios}
