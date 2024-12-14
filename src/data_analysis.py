import pandas as pd

def get_basic_info(data):
    print("Shape of the data:", data.shape)
    data.info()
    print("Number of missing values per column:\n", data.isnull().sum())
    print("Number of duplicate rows:", data.duplicated().sum())

def get_unique_counts(data):
    print("Number of stocks: ", len(data['stock'].unique()))
    print("Number of publishers: ", len(data['publisher'].unique()))
    print("Number of urls: ", len(data['url'].unique()))
    print("Number of dates: ", len(data['date'].unique()))
    print("Number of headlines: ", len(data['headline'].unique()))

def calculate_headline_length(data):
    data['headline_length'] = data['headline'].apply(len)
    return data['headline_length'].describe()

def split_date_columns(data):
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.month
    data['day'] = data['date'].dt.day
    data['hour'] = data['date'].dt.hour
    data['minute'] = data['date'].dt.minute
    data['second'] = data['date'].dt.second
    return data