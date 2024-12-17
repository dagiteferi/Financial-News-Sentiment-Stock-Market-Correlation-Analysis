import sys
import os

# Add src directory to the Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

from data_loader import load_data, load_and_concatenate_stock_data
from data_cleaner import clean_data, drop_first_column, format_date_column
from sentiment_analysis import analyze_sentiment, aggregate_sentiments_by_date
from stock_returns import calculate_daily_returns
from data_merger import merge_data, merge_sentiment_with_stock
from correlation_analysis import calculate_correlation
from visualizationt import plot_daily_returns, scatter_plot


def main():
    # Load data
    news_df = load_data('../data/news.csv')

    # File paths and corresponding company names
    file_paths = [
        '../data/apple.csv',
        '../data/amazon.csv',
        '../data/google.csv',
        '../data/meta.csv',
        '../data/microsoft.csv',
        '../data/nvidia.csv',
        '../data/tesla.csv'
    ]

    company_names = ['Apple', 'Amazon', 'Google', 'Meta', 'Microsoft', 'Nvidia', 'Tesla']

    # Load and concatenate the stock data
    stock_df = load_and_concatenate_stock_data(file_paths, company_names)

    # Drop the first column
    news_df = drop_first_column(news_df)
    
    # Clean data
    stock_df = clean_data(stock_df, 'Date')
    news_df = clean_data(news_df, 'date')
    
    # Format the 'date' columns
    news_df = format_date_column(news_df, 'date')
    stock_df = format_date_column(stock_df, 'date')

    # Merge data
    merged_df = merge_data(news_df, stock_df)
    
    # Analyze sentiment
    merged_df['sentiment'] = merged_df['headline'].apply(analyze_sentiment)
    
    # Calculate daily stock returns
    merged_df = calculate_daily_returns(merged_df)
    
    # Aggregate sentiments by date
    daily_sentiment = aggregate_sentiments_by_date(merged_df)
    
    # Merge sentiment data with stock data
    daily_df = merge_sentiment_with_stock(merged_df, daily_sentiment)

    # Calculate correlation
    correlation = calculate_correlation(daily_df)
    print(f'Pearson correlation coefficient: {correlation}')

    # Visualize
    plot_daily_returns(daily_df)
    scatter_plot(daily_df)

if __name__ == '__main__':
    main()