import unittest
from optiquantfolio.stochastic_control import stochastic_control_optimization

class TestStochasticControl(unittest.TestCase):
    def test_stochastic_control_optimization(self):
        tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
        start_date = '2020-01-01'
        end_date = '2023-01-01'
        optimization_result = stochastic_control_optimization(tickers, start_date, end_date)
        self.assertIsNotNone(optimization_result)

if __name__ == '__main__':
    unittest.main()