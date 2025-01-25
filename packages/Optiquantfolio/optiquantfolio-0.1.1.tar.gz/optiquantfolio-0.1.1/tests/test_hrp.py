import unittest
from optiquantfolio.hrp import hierarchical_risk_parity

class TestHRP(unittest.TestCase):
    def test_hierarchical_risk_parity(self):
        tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
        start_date = '2020-01-01'
        end_date = '2023-01-01'
        cluster_order = hierarchical_risk_parity(tickers, start_date, end_date)
        self.assertIsNotNone(cluster_order)
        self.assertEqual(len(cluster_order), len(tickers))

if __name__ == '__main__':
    unittest.main()