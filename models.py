from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_and_evaluate_model(X_train, X_test, y_train, y_test):
    """
    Train and evaluate machine learning models.
    Args:
        X_train, X_test, y_train, y_test: Processed training and test data.
    Returns:
        model: Trained machine learning model.
    """
    # Train logistic regression
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Evaluate model
    y_pred = model.predict(X_test)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

    # Save model
    joblib.dump(model, "anomaly_detection_model.pkl")
    print("Model saved as 'anomaly_detection_model.pkl'.")
    return model
