
import pandas as pd

def calculate_daily_returns(df, close_column='Close', return_column='Daily Return'):
    df[return_column] = df[close_column].pct_change() * 100
    return df
