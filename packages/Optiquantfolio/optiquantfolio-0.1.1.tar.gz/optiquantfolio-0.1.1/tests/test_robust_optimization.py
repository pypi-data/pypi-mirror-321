import unittest
from optiquantfolio.robust_optimization import robust_optimization

class TestRobustOptimization(unittest.TestCase):
    def test_robust_optimization(self):
        tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
        start_date = '2020-01-01'
        end_date = '2023-01-01'
        weights = robust_optimization(tickers, start_date, end_date)
        self.assertIsNotNone(weights)
        self.assertEqual(len(weights), len(tickers))

if __name__ == '__main__':
    unittest.main()