import pytest
import numpy as np
from ml.model import train_model, compute_model_metrics  # Adjust the import based on your structure
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

def test_train_model_return_type():
    # Sample training data
    X_train = np.random.rand(100, 10)  # 100 samples, 10 features
    y_train = np.random.randint(0, 2, size=100)  # Binary labels

    # Train the model
    model = train_model(X_train, y_train)

    # Check that the returned model is of the expected type
    assert isinstance(model, RandomForestClassifier), "The model should be a RandomForestClassifier."


def test_prediction_output_type():
    # Sample training data
    X_train = np.random.rand(100, 10)  # 100 samples, 10 features
    y_train = np.random.randint(0, 2, size=100)  # Binary labels

    # Train the model
    model = train_model(X_train, y_train)

    # Generate some test data
    X_test = np.random.rand(10, 10)  # 10 samples for testing

    # Get predictions
    preds = model.predict(X_test)

    # Check that the predictions are of the expected type
    assert isinstance(preds, np.ndarray), "Predictions should be a NumPy array."


def test_compute_model_metrics():
    #Test that the metrics calculation function returns expected values.
    X_train = np.random.rand(100, 10)  # 100 samples, 10 features
    y_train = np.random.randint(0, 2, size=100)  # Binary labels
    
    model = train_model(X_train, y_train)
    preds = model.predict(X_train)
    precision, recall, fbeta = compute_model_metrics(y_train, preds)
    
    # Check that the metrics are within expected ranges
    assert 0 <= precision <= 1, "Precision should be between 0 and 1."
    assert 0 <= recall <= 1, "Recall should be between 0 and 1."
    assert 0 <= fbeta <= 1, "F-beta score should be between 0 and 1."
"""
import pytest
import numpy as np
from ml.model import train_model, compute_model_metrics  # Adjust the import based on your structure
from sklearn.datasets import make_classification

# Sample data for testing
X, y = make_classification(n_samples=100, n_features=20, random_state=42)

def test_train_model():
    Test that the model can be trained without errors.
    model = train_model(X, y)
    assert model is not None, "The model should not be None after training."

def test_prediction_output_type():
    Test that the model's predictions return the expected type.
    model = train_model(X, y)
    preds = model.predict(X)
    assert isinstance(preds, np.ndarray), "Predictions should be a NumPy array."

def test_compute_model_metrics():
    Test that the metrics calculation function returns expected values.
    model = train_model(X, y)
    preds = model.predict(X)
    precision, recall, fbeta = compute_model_metrics(y, preds)
    
    # Check that the metrics are within expected ranges
    assert 0 <= precision <= 1, "Precision should be between 0 and 1."
    assert 0 <= recall <= 1, "Recall should be between 0 and 1."
    assert 0 <= fbeta <= 1, "F-beta score should be between 0 and 1."
"""