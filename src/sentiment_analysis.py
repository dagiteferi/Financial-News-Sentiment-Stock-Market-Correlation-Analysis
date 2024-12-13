
from textblob import TextBlob

def add_sentiment(data):
    data['sentiment'] = data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return data

def get_top_headlines(data, sentiment_threshold=0.5, top_n=10, positive=True):
    if positive:
        filtered_headlines = data[data['sentiment'] > sentiment_threshold]
    else:
        filtered_headlines = data[data['sentiment'] < sentiment_threshold]
    
    return filtered_headlines.sort_values(by='sentiment', ascending=False).head(top_n)
