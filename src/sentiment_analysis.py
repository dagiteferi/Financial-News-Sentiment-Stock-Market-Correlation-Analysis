
import pandas as pd
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def aggregate_sentiments_by_date(df, date_column='date', sentiment_column='sentiment', output_column='Average Sentiment'):
    daily_sentiment = df.groupby(date_column)[sentiment_column].mean().reset_index()
    daily_sentiment.columns = [date_column, output_column]
    return daily_sentiment
