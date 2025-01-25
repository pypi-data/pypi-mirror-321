from dataclasses import dataclass
from datetime import datetime, timedelta
import logging
import numpy as np
from scipy.optimize import minimize
import pandas as pd
from pybacktestchain.data_module import DataModule, FirstTwoMoments
import os
from pybacktestchain.broker import Broker, RiskModel


def load_sp500_data():
    """
    Load S&P 500 data from a CSV file included in the package.

    Returns:
        tuple: (list of stock names, dict mapping names to tickers)
    """
    try:
        csv_file_path = os.path.join(os.path.dirname(__file__), "../../docs/SP500.csv")
        sp500_data = pd.read_csv(csv_file_path)
        stock_names = sp500_data.iloc[:, 1].tolist()  # Second column for stock names
        stock_tickers = sp500_data.set_index(sp500_data.columns[1])[sp500_data.columns[0]].to_dict()  # Map Name to Ticker

        return stock_names, stock_tickers
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return [], {}


@dataclass
class MaxSharpeRatio(FirstTwoMoments):
    risk_free_rate: float = 0.01  # Annual risk-free rate (e.g., 1%)

    def compute_portfolio(self, t: datetime, information_set):
        try:
            mu = information_set['expected_return']
            Sigma = information_set['covariance_matrix']
            rf = self.risk_free_rate / 252  # Convert annual risk-free rate to daily
            n = len(mu)

            # Define the negative Sharpe Ratio as the objective function
            def sharpe_ratio_neg(weights):
                portfolio_return = weights.dot(mu)
                portfolio_volatility = np.sqrt(weights.dot(Sigma).dot(weights))
                return -(portfolio_return - rf) / portfolio_volatility

            # Constraints: weights sum to 1
            cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
            # Bounds: Long-only portfolio
            bounds = [(0.0, 1.0)] * n
            # Initial guess: equal weights
            x0 = np.ones(n) / n

            # Minimize the negative Sharpe Ratio
            res = minimize(sharpe_ratio_neg, x0, constraints=cons, bounds=bounds)

            # Prepare portfolio dictionary
            portfolio = {k: None for k in information_set['companies']}
            if res.success:
                for i, company in enumerate(information_set['companies']):
                    portfolio[company] = res.x[i]
            else:
                raise Exception("Optimization did not converge")

            return portfolio
        except Exception as e:
            # If an error occurs, return equal weights and log the issue
            logging.warning("Error computing portfolio, returning equal weight portfolio")
            logging.warning(e)
            return {k: 1 / len(information_set['companies']) for k in information_set['companies']}


@dataclass
class MinimumVariancePortfolio(FirstTwoMoments):
    def compute_portfolio(self, t: datetime, information_set):
        try:
            Sigma = information_set['covariance_matrix']
            n = len(Sigma)

            # Define the portfolio variance as the objective function
            def portfolio_variance(weights):
                return weights.dot(Sigma).dot(weights)

            # Constraints: weights must sum to 1
            cons = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
            # Bounds: Long-only portfolio (weights between 0 and 1)
            bounds = [(0.0, 1.0)] * n
            # Initial guess: equal weights
            x0 = np.ones(n) / n

            # Minimize the portfolio variance
            res = minimize(portfolio_variance, x0, constraints=cons, bounds=bounds)

            # Prepare portfolio dictionary
            portfolio = {k: None for k in information_set['companies']}
            if res.success:
                for i, company in enumerate(information_set['companies']):
                    portfolio[company] = res.x[i]
            else:
                raise Exception("Optimization did not converge")

            return portfolio
        except Exception as e:
            # If an error occurs, return equal weights and log the issue
            logging.warning("Error computing portfolio, returning equal weight portfolio")
            logging.warning(e)
            return {k: 1 / len(information_set['companies']) for k in information_set['companies']}

@dataclass
class EqualRiskContributionPortfolio(FirstTwoMoments):
    def compute_portfolio(self, t: datetime, information_set):
        try:
            Sigma = information_set['covariance_matrix']
            n = len(Sigma)

            # Function to compute the risk contributions
            def risk_contributions(weights):
                portfolio_variance = weights.dot(Sigma).dot(weights)
                marginal_risk = Sigma.dot(weights)
                return weights * marginal_risk / portfolio_variance

            # Objective: minimize the squared difference between risk contributions
            def objective(weights):
                rc = risk_contributions(weights)
                avg_rc = np.mean(rc)
                return np.sum((rc - avg_rc) ** 2)

            # Constraints: weights sum to 1
            cons = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})

            # Bounds: Long-only portfolio (weights between 0 and 1)
            bounds = [(0.0, 1.0)] * n

            # Initial guess: equal weights
            x0 = np.ones(n) / n

            # Minimize the objective
            res = minimize(objective, x0, constraints=cons, bounds=bounds)

            # Prepare the portfolio dictionary
            portfolio = {k: None for k in information_set['companies']}
            if res.success:
                for i, company in enumerate(information_set['companies']):
                    portfolio[company] = res.x[i]
            else:
                raise Exception("Optimization did not converge")

            return portfolio
        except Exception as e:
            # If an error occurs, return equal weights and log the issue
            logging.warning("Error computing portfolio, returning equal weight portfolio")
            logging.warning(e)
            return {k: 1 / len(information_set['companies']) for k in information_set['companies']}


@dataclass
class TrailingStop(RiskModel):
    threshold: float = 0.05  # Default trailing stop of 5%

    def trigger_stop_loss(self, t: datetime, portfolio: dict, prices: dict, broker: Broker):
        for ticker, position in broker.positions.items():
            highest_price = broker.highest_prices.get(ticker, broker.entry_prices[ticker])
            current_price = prices.get(ticker)
            if current_price is None:
                continue
            highest_price = max(highest_price, current_price)
            broker.highest_prices[ticker] = highest_price
            trailing_stop_price = highest_price * (1 - self.threshold)
            if current_price < trailing_stop_price:
                broker.sell(ticker, position.quantity, current_price, t)
