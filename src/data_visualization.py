import matplotlib.pyplot as plt
import seaborn as sns

def plot_top_publishers(publisher_counts):
    top_10_publishers = publisher_counts.head(10)
    plt.figure(figsize=(10, 6))
    top_10_publishers.plot(kind='bar')
    plt.title('Top 10 Publishers by Number of Articles')
    plt.xlabel('Publisher')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45, ha='right')
    plt.savefig('top_10_publishers_by_number_of_articles.png')
    plt.show()

def plot_article_distribution_by_year(data):
    plt.figure(figsize=(10, 6))
    data['year'].hist(bins=30)
    plt.title('Distribution of Articles Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.xticks(rotation=45)
    plt.grid(False)
    plt.savefig('distribution_of_articles_over_the_years.png')
    plt.show()

def plot_monthly_publications(data, year):
    year_data = data[data['year'] == year]
    monthly_publications = year_data.groupby('month').size()

    plt.figure(figsize=(10, 6))
    monthly_publications.plot(kind='bar', edgecolor='black')
    plt.title(f'Publication Distribution in {year} by Month')
    plt.xlabel('Month')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=0)
    plt.grid(False)
    plt.savefig('Publication_distribution_year_2020.png')
    plt.show()

def plot_sentiment_distribution(data):
    plt.figure(figsize=(10, 6))
    sns.histplot(data['sentiment'], bins=30, color='blue', kde=True)
    plt.title('Distribution of Sentiment Scores')
    plt.xlabel('Sentiment Score')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('distribution_of_sentiment_score.png')
    plt.show()

def plot_top_headlines(headlines, title, filename):
    plt.figure(figsize=(12, 8))
    sns.barplot(x=headlines['sentiment'], y=headlines['headline'], palette='viridis')
    plt.title(title)
    plt.xlabel('Sentiment Score')
    plt.ylabel('Headline')
    plt.xticks(rotation=45, ha='right')
    plt.grid(False)
    plt.savefig(filename)
    plt.show()

def plot_word_frequencies_over_years(years, word_freq_per_year, top_words):
    plt.figure(figsize=(10, 6))
    for word in top_words:
        plt.plot(years, word_freq_per_year[word], label=word)
    plt.title('Top 10 Common Words Repetition Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Word Frequency')
    plt.legend(title="Words")
    plt.grid(True)
    plt.savefig('most_common_words_over_the_years.png')
    plt.show()