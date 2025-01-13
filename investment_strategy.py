def propose_strategy(prediction):
    """
    Proposes general investment advice based on model prediction.

    Args:
        prediction (int): The model's prediction (0 for no crash, 1 for crash).

    Returns:
        str: The proposed investment strategy.
    """
    if prediction == 1:
        strategy = (
            "Market crash predicted! To minimize losses and maximize returns, do the following:\n"
            "1. Shift a significant portion of your portfolio into low-risk, stable assets like government bonds.\n"
            "2. Reduce exposure to high-risk assets (e.g., stocks, commodities).\n"
            "3. Consider hedging strategies (e.g., options, inverse ETFs) to protect against downside risk.\n"
            "4. Diversify into defensive sectors like utilities and consumer staples.\n"
            "5. Maintain liquidity to take advantage of market opportunities when the crash subsides."
        )
    else:
        strategy = (
            "No market crash predicted. To minimize losses and maximize returns, do the following:\n"
            "1. Invest in growth-oriented assets such as stocks, especially in sectors like technology and healthcare.\n"
            "2. Diversify into emerging markets and high-growth industries.\n"
            "3. Increase exposure to riskier, higher-reward assets if your risk tolerance allows.\n"
            "4. Consider leveraging your portfolio with moderate risk exposure (e.g., margin or options) to amplify gains.\n"
            "5. Regularly rebalance your portfolio to capture gains from high-performing sectors."
        )
    return strategy
