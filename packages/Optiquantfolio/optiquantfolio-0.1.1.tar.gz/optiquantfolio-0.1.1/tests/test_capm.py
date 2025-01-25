import unittest
from optiquantfolio.capm import capm_portfolio_return

class TestCAPM(unittest.TestCase):
    def test_capm_portfolio_return(self):
        tickers = ['AAPL', 'MSFT']
        risk_free_rate = 0.01
        market_ticker = '^GSPC'
        start_date = '2020-01-01'
        end_date = '2023-01-01'
        portfolio_return = capm_portfolio_return(tickers, risk_free_rate, market_ticker, start_date, end_date)
        self.assertIsNotNone(portfolio_return)

if __name__ == '__main__':
    unittest.main()
