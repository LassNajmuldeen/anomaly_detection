from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

def train_and_compare_models(X_train, X_test, y_train, y_test):
    """
    Train and compare multiple models.
    Args:
        X_train, X_test, y_train, y_test: Processed training and test data.
    Returns:
        best_model: The best-performing trained model.
    """
    # Define models to compare
    models = {
        "Logistic Regression": LogisticRegression(),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "Gradient Boosting": GradientBoostingClassifier(random_state=42)
    }

    # Train and evaluate each model
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)  # Train the model
        y_pred = model.predict(X_test)  # Predict on test data
        accuracy = accuracy_score(y_test, y_pred)
        results[name] = accuracy

        # Print performance
        print(f"Model: {name}")
        print(f"Accuracy: {accuracy:.2f}")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))
        print("-" * 50)

    # Select the best model
    best_model_name = max(results, key=results.get)
    best_model = models[best_model_name]
    print(f"Best Model: {best_model_name} with Accuracy: {results[best_model_name]:.2f}")

    # Save the best model
    joblib.dump(best_model, "best_model.pkl")
    print("Best model saved as 'best_model.pkl'.")

    return best_model
