import unittest
from optiquantfolio.treynor_ratio import treynor_ratio_analysis

class TestTreynorRatio(unittest.TestCase):
    def test_treynor_ratio_analysis(self):
        portfolios = [
            {'name': 'Portfolio1', 'tickers': ['AAPL', 'MSFT']},
            {'name': 'Portfolio2', 'tickers': ['GOOG', 'AMZN']}
        ]
        risk_free_rate = 0.01
        start_date = '2020-01-01'
        end_date = '2023-01-01'
        analysis = treynor_ratio_analysis(portfolios, risk_free_rate, start_date, end_date)
        self.assertIsNotNone(analysis)
        self.assertIn('Portfolio1', analysis)
        self.assertIn('Portfolio2', analysis)

if __name__ == '__main__':
    unittest.main()
