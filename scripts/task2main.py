import sys
import os

# Add src directory to the Python path
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../src'))
sys.path.append(src_path)

import data_preprocessing as dp
import indicators as ind
import visualization as vis

# Example usage
def main():
    file_path = '../data/amazon.csv'
    data = dp.load_data(file_path)
    data = ind.calculate_indicators(data)
    vis.plot_moving_averages(data, 'Stock_price_moving_average.png')
    vis.plot_rsi(data, 'relative_strength_index.png')
    vis.plot_macd(data, 'macd_signals.png')

if __name__ == '__main__':
    main()