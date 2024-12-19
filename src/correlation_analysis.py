
import pandas as pd

def calculate_correlation(df, column1='Average Sentiment', column2='Daily Return'):
    correlation = df[[column1, column2]].corr().iloc[0, 1]
    return correlation
