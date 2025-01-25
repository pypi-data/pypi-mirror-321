import unittest
from optiquantfolio.genetic_algorithm import genetic_algorithm_optimization

class TestGeneticAlgorithm(unittest.TestCase):
    def test_genetic_algorithm_optimization(self):
        tickers = ['AAPL', 'MSFT', 'GOOG', 'AMZN']
        start_date = '2020-01-01'
        end_date = '2023-01-01'
        best_individual = genetic_algorithm_optimization(tickers, start_date, end_date)
        self.assertIsNotNone(best_individual)
        self.assertEqual(len(best_individual), len(tickers))

if __name__ == '__main__':
    unittest.main()
