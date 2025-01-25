from deap import base, creator, tools, algorithms
import random
import numpy as np
from .data_fetcher import fetch_data

def portfolio_variance(weights, cov_matrix):
    """Calculate portfolio variance."""
    variance = np.dot(weights, np.dot(cov_matrix, weights))
    return (variance,)  # Return a tuple

def genetic_algorithm_optimization(tickers, start_date, end_date, generations=50, population_size=20):
    """Apply Genetic Algorithm for portfolio optimization."""
    returns = fetch_data(tickers, start_date, end_date).pct_change(fill_method=None).dropna()
    cov_matrix = returns.cov()

    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("attr_float", random.uniform, 0, 1)
    toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=len(tickers))
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    toolbox.register("mate", tools.cxBlend, alpha=0.5)
    toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.2)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", lambda individual: portfolio_variance(individual, cov_matrix))

    # Initial population and optimization process
    population = toolbox.population(n=population_size)
    algorithms.eaSimple(population, toolbox, cxpb=0.5, mutpb=0.2, ngen=generations, verbose=True)

    # Return the best individual
    best_individual = tools.selBest(population, 1)[0]
    return best_individual
