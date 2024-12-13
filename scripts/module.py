import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.dataload import load_data, preprocess_data
from src.data_analysis import get_basic_info, get_unique_counts, split_date_columns, calculate_headline_length
from src.text_processing import clean_headlines, get_common_words, word_frequency_over_years
from src.sentiment_analysis import add_sentiment, get_top_headlines
from src.data_visualization import (
    plot_top_publishers, plot_article_distribution_by_year, 
    plot_sentiment_distribution, plot_top_headlines, plot_word_frequencies_over_years, plot_monthly_publications
)

# Load and preprocess the data
filepath = 'C:\Users\Dagi\Documents\KAIM\Week 1\Financial-News-Sentiment-Stock-Market-Correlation-Analysis\data/raw_analyst_ratings.csv'
data = load_data(filepath)
data = preprocess_data(data)

# Analyze the data
get_basic_info(data)
get_unique_counts(data)
headline_stats = calculate_headline_length(data)
print("Headline length statistics:\n", headline_stats)

# Split date into components
data = split_date_columns(data)

# Clean headlines and analyze text
data = clean_headlines(data)
top_words = get_common_words(data)
years, word_freq_per_year = word_frequency_over_years(data, [word for word, count in top_words])

# Sentiment analysis
data = add_sentiment(data)
plot_sentiment_distribution(data)
positive_headlines = get_top_headlines(data, positive=True)
plot_top_headlines(positive_headlines, 'Top 10 Headlines with the Most Positive Sentiments', 'top_10_headlines_with_positive_sentiment.png')
negative_headlines = get_top_headlines(data, positive=False)
plot_top_headlines(negative_headlines, 'Headlines with the Most Negative Sentiments', 'top_headlines_with_negative_sentiment.png')

# Visualization
publisher_counts = data['publisher'].value_counts()
plot_top_publishers(publisher_counts)
plot_article_distribution_by_year(data)
plot_word_frequencies_over_years(years, word_freq_per_year, [word for word, count in top_words])

# Specify the year of interest
year_of_interest = 2020
plot_monthly_publications(data, year_of_interest)