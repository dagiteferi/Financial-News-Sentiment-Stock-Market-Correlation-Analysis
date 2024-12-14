import pandas as pd

def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

def preprocess_data(data):
    data.drop_duplicates(inplace=True)
    data = data.drop(data.columns[0], axis=1)
    data['date'] = pd.to_datetime(data['date'], errors='coerce').dt.tz_localize(None)
    return data