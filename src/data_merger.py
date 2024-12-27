import pandas as pd

def merge_data(news_df, stock_df, on='date'):
    merged_df = pd.merge(news_df, stock_df, on=on)
    return merged_df

def merge_sentiment_with_stock(stock_df, sentiment_df):
    daily_df = pd.merge(stock_df[['date', 'Daily Return']], sentiment_df, on='date', how='inner')
    return daily_df