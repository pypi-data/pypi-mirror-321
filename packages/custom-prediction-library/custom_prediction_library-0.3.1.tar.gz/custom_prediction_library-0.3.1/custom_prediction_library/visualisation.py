
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
import numpy as np

class PredictionVisualiser:
    """
    A class for visualising model predictions over time periods.

    Methods:
        plot_predictions: Visualise predictions for discrete time periods.
    """

    @staticmethod
    def plot_predictions(y_true, y_pred, period_labels, title="Predictions vs Actuals"):
        """
        Visualise predictions for different time periods.

        Args:
            y_true: True values.
            y_pred: Predicted values.
            period_labels: Labels for the periods (e.g., ["3 months", "6 months"]).
            title (str): Title of the plot.
        """
        data = {"period": period_labels, "actual": y_true, "predicted": y_pred}
        source = ColumnDataSource(data)

        p = figure(x_range=period_labels, title=title, plot_height=400, plot_width=800, toolbar_location=None)
        p.vbar(x="period", top="actual", width=0.4, source=source, color="blue", legend_label="Actual")
        p.vbar(x="period", top="predicted", width=0.2, source=source, color="orange", legend_label="Predicted")

        p.xgrid.grid_line_color = None
        p.y_range.start = 0
        p.legend.title = "Values"
        p.xaxis.axis_label = "Period"
        p.yaxis.axis_label = "Value"

        show(p)
        