
import matplotlib.pyplot as plt

def plot_moving_averages(data, output_path):
    """Plot stock price and moving averages."""
    plt.figure(figsize=(14, 7))
    plt.plot(data['Close'], label='Close Price', color='blue')
    plt.plot(data['SMA_50'], label='50-Day SMA', color='orange')
    plt.plot(data['SMA_200'], label='200-Day SMA', color='green')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.savefig(output_path)
    plt.close()

def plot_rsi(data, output_path):
    """Plot RSI."""
    plt.figure(figsize=(14, 7))
    plt.plot(data['RSI'], label='RSI', color='purple')
    plt.axhline(70, color='red', linestyle='--')
    plt.axhline(30, color='green', linestyle='--')
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Date')
    plt.ylabel('RSI')
    plt.legend()
    plt.savefig(output_path)
    plt.close()

def plot_macd(data, output_path):
    """Plot MACD."""
    plt.figure(figsize=(14, 7))
    plt.plot(data['MACD'], label='MACD', color='blue')
    plt.plot(data['MACD_signal'], label='MACD Signal', color='orange')
    plt.bar(data.index, data['MACD_hist'], label='MACD Histogram', color='grey', alpha=0.5)
    plt.title('MACD and MACD Signal')
    plt.xlabel('Date')
    plt.ylabel('MACD')
    plt.legend()
    plt.savefig(output_path)
    plt.close()
