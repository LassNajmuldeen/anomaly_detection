import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path):
    """
    Load and preprocess the dataset.
    Args:
        file_path (str): Path to the dataset file.
    Returns:
        tuple: Scaled features and target split into training and test sets.
    """
    # Load dataset
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully.")

    # Separate features and target
    features = df.drop(columns=["Y", "Data"])
    target = df["Y"]

    # Handle missing values
    features = features.fillna(features.mean())

    # Normalize features
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        features_scaled, target, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test
