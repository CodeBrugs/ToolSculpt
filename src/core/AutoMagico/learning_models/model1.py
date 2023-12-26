# Import necessary libraries
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

class Model1:
    def __init__(self):
        # Initialize your model and any required parameters
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        """
        Train the machine learning model.

        Parameters:
        - X_train (numpy.ndarray): Input features for training.
        - y_train (numpy.ndarray): Target labels for training.
        """
        # Split the data into training and validation sets
        X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Make predictions on the validation set
        val_predictions = self.model.predict(X_val)

        # Evaluate the model
        mse = mean_squared_error(y_val, val_predictions)
        print(f'Mean Squared Error on Validation Set: {mse}')

    def predict(self, X_test):
        """
        Make predictions using the trained model.

        Parameters:
        - X_test (numpy.ndarray): Input features for prediction.

        Returns:
        - predictions (numpy.ndarray): Predicted values.
        """
        predictions = self.model.predict(X_test)
        return predictions

    def save_model(self, model_path='model1.pkl'):
        """
        Save the trained model to a file.

        Parameters:
        - model_path (str): File path to save the model.
        """
        # Save the model using your preferred serialization method
        # For example, using joblib for simplicity
        from joblib import dump
        dump(self.model, model_path)

    def load_model(self, model_path='model1.pkl'):
        """
        Load a pre-trained model from a file.

        Parameters:
        - model_path (str): File path to load the model from.
        """
        # Load the model using your preferred deserialization method
        # For example, using joblib for simplicity
        from joblib import load
        self.model = load(model_path)

