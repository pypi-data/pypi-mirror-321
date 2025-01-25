
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import numpy as np
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource

class ExponentialSmoothingModel:
    """
    A class for time series forecasting using exponential smoothing.

    Methods:
        fit: Fit the exponential smoothing model to data.
        forecast: Forecast future values.
        plot: Visualise original data and forecasted values.
    """

    def __init__(self, trend: str = None, seasonal: str = None, seasonal_periods: int = None):
        """
        Initialize the Exponential Smoothing model.

        Args:
            trend (str): The type of trend component ("add", "mul", or None).
            seasonal (str): The type of seasonal component ("add", "mul", or None).
            seasonal_periods (int): Number of periods in a season (for seasonal models).
        """
        self.trend = trend
        self.seasonal = seasonal
        self.seasonal_periods = seasonal_periods
        self.model = None
        self.fitted_model = None

    def fit(self, data: np.ndarray):
        """
        Fit the Exponential Smoothing model to the data.

        Args:
            data (np.ndarray): The time series data.
        """
        self.model = ExponentialSmoothing(data, trend=self.trend, seasonal=self.seasonal, seasonal_periods=self.seasonal_periods)
        self.fitted_model = self.model.fit()

    def forecast(self, steps: int) -> np.ndarray:
        """
        Forecast future values.

        Args:
            steps (int): Number of future steps to forecast.

        Returns:
            np.ndarray: Forecasted values.

        Raises:
            ValueError: If the model is not fitted before forecasting.
        """
        if self.fitted_model is None:
            raise ValueError("Model must be fitted before forecasting.")
        return self.fitted_model.forecast(steps)

    def plot(self, data: np.ndarray, forecast_steps: int):
        """
        Plot the original data and forecasted values.

        Args:
            data (np.ndarray): The original time series data.
            forecast_steps (int): Number of future steps to forecast.
        """
        forecast = self.forecast(forecast_steps)
        extended_data = np.concatenate([data, forecast])

        source = ColumnDataSource(data=dict(
            x=list(range(len(extended_data))),
            y=extended_data,
            type=["Observed"] * len(data) + ["Forecast"] * forecast_steps
        ))

        p = figure(title="Exponential Smoothing Forecast", x_axis_label="Time", y_axis_label="Value", plot_height=400, plot_width=800)
        p.line(x=list(range(len(data))), y=data, line_width=2, legend_label="Observed", color="blue")
        p.line(x=list(range(len(data), len(extended_data))), y=forecast, line_width=2, legend_label="Forecast", color="orange")
        show(p)
        