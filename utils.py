import joblib

def save_model(model, filename):
    """Save a model to a file."""
    joblib.dump(model, filename)
    print(f"Model saved as {filename}")

def load_model(filename):
    """Load a model from a file."""
    try:
        model = joblib.load(filename)
        print(f"Model loaded from {filename}")
        return model
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return None
