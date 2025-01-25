
# Custom Prediction Library

A Python library for:

- Simplified model creation using Scikit-learn.
- Automated hyperparameter tuning with Optuna and Bayesian Optimization.
- Time series forecasting using Exponential Smoothing.
- Interactive visualisation with Bokeh.

## Installation

Install via pip:

```bash
pip install custom_prediction_lib
```

## Features

- **Model Factory**: Create classification and regression models with minimal setup.
- **Hyperparameter Tuning**: Includes GridSearch, RandomizedSearch, and advanced tuning with Optuna.
- **Time Series**: Exponential smoothing for forecasting.
- **Visualisation**: Interactive plots for predictions and forecasts.

## Usage

### Example 1: Model Factory

```python
from custom_prediction_lib.model_creation import ModelFactory

# Create a Random Forest classifier
model = ModelFactory.create_model(
    task="classification", 
    model_type="random_forest", 
    n_estimators=100
)
```

### Example 2: Hyperparameter Tuning

```python
from custom_prediction_lib.tuning import HyperparameterTuner
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_samples=500, n_features=10, random_state=42)

model = RandomForestClassifier(random_state=42)
param_distributions = {
    "n_estimators": (50, 200),
    "max_depth": (5, 20),
}

best_model, best_params = HyperparameterTuner.optuna_search(
    model, X, y, param_distributions, n_trials=30, visualise=True
)
```

### Example 3: Time Series Forecasting

```python
from custom_prediction_lib.time_series import ExponentialSmoothingModel

# Example time series data
data = [100, 120, 130, 125, 135, 140, 145]

# Fit and forecast using exponential smoothing
model = ExponentialSmoothingModel(trend="add", seasonal="mul", seasonal_periods=4)
model.fit(data)
forecast = model.forecast(steps=3)
model.plot(data, forecast_steps=3)
```

## License

This project is licensed under the MIT License.
