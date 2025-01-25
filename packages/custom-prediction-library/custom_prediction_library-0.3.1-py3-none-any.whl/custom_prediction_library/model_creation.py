
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.linear_model import LogisticRegression, LinearRegression

class ModelFactory:
    """
    Factory for creating pre-configured Scikit-learn models.

    Methods:
        create_model: Create a classification or regression model.
    """

    @staticmethod
    def create_model(task: str, model_type: str, **kwargs):
        """
        Create a Scikit-learn model based on the task and model type.

        Args:
            task (str): 'classification' or 'regression'.
            model_type (str): Type of model (e.g., 'random_forest', 'logistic', 'linear').
            **kwargs: Additional parameters for the model.

        Returns:
            model: Configured Scikit-learn model.

        Raises:
            ValueError: If the task or model_type is invalid.
        """
        if task == "classification":
            if model_type == "random_forest":
                return RandomForestClassifier(**kwargs)
            elif model_type == "logistic":
                return LogisticRegression(**kwargs)
            else:
                raise ValueError("Unsupported model type for classification.")
        elif task == "regression":
            if model_type == "random_forest":
                return RandomForestRegressor(**kwargs)
            elif model_type == "linear":
                return LinearRegression(**kwargs)
            else:
                raise ValueError("Unsupported model type for regression.")
        else:
            raise ValueError("Task must be 'classification' or 'regression'.")
        