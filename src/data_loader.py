import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def load_and_concatenate_stock_data(file_paths, company_names):
    
    # List to store individual dataframes
    dataframes = []
    
    # Loop through each file path and company name
    for file_path, company_name in zip(file_paths, company_names):
        # Load the CSV file
        df = pd.read_csv(file_path)
        # Add a 'Company' column
        df['Company'] = company_name
        # Append the dataframe to the list
        dataframes.append(df)
    
    # Concatenate all dataframes into one
    stock_df = pd.concat(dataframes)
    
    return stock_df