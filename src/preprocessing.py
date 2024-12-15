import pandas_ta as ta

def calculate_indicators(data):
    """Calculate technical indicators."""
    data['SMA_50'] = ta.sma(data['Close'], length=50)
    data['SMA_200'] = ta.sma(data['Close'], length=200)
    data['RSI'] = ta.rsi(data['Close'], length=14)
    
    macd = ta.macd(data['Close'], fast=12, slow=26, signal=9)
    data['MACD'] = macd['MACD_12_26_9']
    data['MACD_signal'] = macd['MACDs_12_26_9']
    data['MACD_hist'] = macd['MACDh_12_26_9']
    return data