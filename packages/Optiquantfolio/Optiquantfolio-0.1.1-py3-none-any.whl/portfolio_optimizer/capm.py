from .data_fetcher import fetch_data, fetch_market_data

def capm_expected_return(risk_free_rate, beta, market_return):
    """Calculate the expected return based on the CAPM formula."""
    return risk_free_rate + beta * (market_return - risk_free_rate)

def capm_portfolio_return(tickers, risk_free_rate, market_ticker, start_date, end_date):
    """Calculate the expected return for a portfolio of assets."""
    market_data = fetch_market_data(market_ticker, start_date, end_date)
    market_return = market_data.pct_change(fill_method=None).mean()
    assets_data = fetch_data(tickers, start_date, end_date)
    betas = assets_data.pct_change(fill_method=None).cov() / market_data.pct_change(fill_method=None).var()
    returns = [capm_expected_return(risk_free_rate, betas[ticker], market_return) for ticker in tickers]
    return sum(returns)
