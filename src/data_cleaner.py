import pandas as pd

def clean_data(df, date_column):
    # Check if the column name needs to be renamed to 'date'
    if date_column in df.columns:
        df.rename(columns={date_column: 'date'}, inplace=True)
    
    # Convert the date column to datetime and remove timezone information
    df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.tz_localize(None)
    
    # Drop rows with any missing values
    df.dropna(inplace=True)
    
    return df

def drop_first_column(df):

    df = df.drop(df.columns[0], axis=1)
    return df

def format_date_column(df, date_column):

    df[date_column] = pd.to_datetime(df[date_column], errors='coerce').dt.strftime('%Y-%m-%d')
    return df