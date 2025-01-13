from preprocessing import load_and_preprocess_data
from models import train_and_compare_models
from investment_strategy import propose_strategy


def main():
    print("Starting anomaly detection project")

    # Preprocess data
    file_path = "FinancialMarketData-EWS.csv"
    X_train, X_test, y_train, y_test = load_and_preprocess_data(file_path)

    # Train and compare models then load best model and make predictions
    best_model = train_and_compare_models(X_train, X_test, y_train, y_test)
    y_pred = best_model.predict(X_test)

    # Prediction based on all models
    prediction = 1 if sum(y_pred) > len(y_pred) / 2 else 0

    # Propose investment strategy based on predictions
    strategy = propose_strategy(prediction)

    # Display the proposed strategy
    print("Investment Strategy Based on Model Prediction:")
    print(strategy)

    print("Anomaly detection process completed.")

if __name__ == "__main__":
    main()
