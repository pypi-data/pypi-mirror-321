import unittest
from optiquantfolio.minimum_variance import minimum_variance_portfolio

class TestMinimumVariance(unittest.TestCase):
    def test_minimum_variance_portfolio(self):
        tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
        start_date = '2020-01-01'
        end_date = '2023-01-01'
        weights = minimum_variance_portfolio(tickers, start_date, end_date)
        self.assertIsNotNone(weights)
        self.assertEqual(len(weights), len(tickers))

if __name__ == '__main__':
    unittest.main()
