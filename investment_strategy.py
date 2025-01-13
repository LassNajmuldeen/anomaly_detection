def propose_strategy(prediction):
    """
    Proposes general investment advice based on model prediction.

    Args:
        prediction (int): The model's prediction (0 for no crash, 1 for crash).

    Returns:
        str: The proposed investment strategy.
    """
    if prediction == 1:  # If the model predicts a crash
        return (
            "The model detects a potential market crash. Consider reducing exposure to high-risk assets. "
            "It may be ideal to diversify into safer investments. "
        )
    else:  # If no crash predicted
        return (
            "According to the models, there is no imminent market crash detected. Continue with your current investment strategy. "
            "It is recommended that you look for growth opportunities during this time."
        )
