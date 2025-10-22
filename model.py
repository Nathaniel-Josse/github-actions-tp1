def predict_sentiment(text): 
    '''A simple sentiment analysis function'''
    # Dummy implementation for illustration purposes
    if not text: 
        return "neutral" 
    # Simple keyword-based sentiment prediction
    if "happy" in text.lower() or "good" in text.lower(): 
        return "positive" 
    # Simple keyword-based sentiment prediction
    if "sad" in text.lower() or "bad" in text.lower(): 
        return "negative" 
    return "neutral" 