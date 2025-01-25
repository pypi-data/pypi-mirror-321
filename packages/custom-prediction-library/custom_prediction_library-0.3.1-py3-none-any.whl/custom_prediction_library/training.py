
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
from typing import Tuple

class ModelTrainer:
    """
    Utility for training and evaluating Scikit-learn models.

    Methods:
        train_model: Train a model and evaluate its performance.
    """

    @staticmethod
    def train_model(
        model, X, y, test_size=0.2, random_state=42, task="classification"
    ) -> Tuple:
        """
        Train a model and evaluate it on a test set.

        Args:
            model: The Scikit-learn model to train.
            X: Features for training and testing.
            y: Target labels for training and testing.
            test_size (float): Proportion of data to use for testing.
            random_state (int): Random state for reproducibility.
            task (str): 'classification' or 'regression'.

        Returns:
            Tuple: Trained model and evaluation metrics.

        Raises:
            ValueError: If the task is invalid.
        """
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

        # Train the model
        model.fit(X_train, y_train)

        # Evaluate the model
        y_pred = model.predict(X_test)
        if task == "classification":
            metrics = {"accuracy": accuracy_score(y_test, y_pred)}
        elif task == "regression":
            metrics = {"mse": mean_squared_error(y_test, y_pred)}
        else:
            raise ValueError("Task must be 'classification' or 'regression'.")

        return model, metrics
        