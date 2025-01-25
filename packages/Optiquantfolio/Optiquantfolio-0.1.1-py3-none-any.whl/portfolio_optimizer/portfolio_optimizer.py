from .capm import capm_portfolio_return
from .treynor_ratio import treynor_ratio
from .minimum_variance import minimum_variance_portfolio
from .hrp import hierarchical_risk_parity
from .genetic_algorithm import genetic_algorithm_optimization
from .stochastic_control import stochastic_control_optimization
from .robust_optimization import robust_optimization

def optimize_portfolio(method, **kwargs):
    """Optimize portfolio using different methods (CAPM, HRP, MVO, etc.)."""
    if method == 'CAPM':
        return capm_portfolio_return(**kwargs)
    elif method == 'Treynor':
        return treynor_ratio(**kwargs)
    elif method == 'MVP':
        return minimum_variance_portfolio(**kwargs)
    elif method == 'HRP':
        return hierarchical_risk_parity(**kwargs)
    elif method == 'GA':
        return factor_model_returns(**kwargs)
    elif method == 'Stochastic':
        return stochastic_control_optimization(**kwargs)
    elif method == 'Robust':
        return robust_optimization(**kwargs)
    else:
        raise ValueError(f"Unknown optimization method: {method}")
