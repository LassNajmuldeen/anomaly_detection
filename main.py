from preprocessing import load_and_preprocess_data
from models import train_and_evaluate_model

def main():
    print("Starting anomaly detection project")

    # Preprocess data
    file_path = "FinancialMarketData-EWS.csv"
    X_train, X_test, y_train, y_test = load_and_preprocess_data(file_path)

    # Train and evaluate model
    train_and_evaluate_model(X_train, X_test, y_train, y_test)

    print("Anomaly detection process completed.")

if __name__ == "__main__":
    main()
