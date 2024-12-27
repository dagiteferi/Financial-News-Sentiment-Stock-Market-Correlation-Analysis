
import matplotlib.pyplot as plt
import seaborn as sns

def plot_daily_returns(daily_df):
    plt.figure(figsize=(14, 7))

    plt.subplot(2, 1, 1)
    plt.plot(daily_df.index, daily_df['Daily Return'], label='Daily Return', color='blue')
    plt.title('Daily Stock Returns')
    plt.xlabel('Date')
    plt.ylabel('Return (%)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(daily_df.index, daily_df['Average Sentiment'], label='Average Sentiment', color='orange')
    plt.title('Average Daily Sentiment')
    plt.xlabel('Date')
    plt.ylabel('Sentiment Score')
    plt.legend()

    plt.tight_layout()
    plt.show()

def scatter_plot(daily_df):
    plt.figure(figsize=(14, 7))
    sns.scatterplot(data=daily_df, x='Average Sentiment', y='Daily Return', alpha=0.5)
    plt.title('Sentiment Score vs. Stock Returns')
    plt.xlabel('Average Sentiment Score')
    plt.ylabel('Daily Return (%)')
    plt.legend()
    plt.show()
