import pandas as pd

# Define the RSI strategy function
def rsi_strategy(data):
    # Calculate the RSI indicator
    data['delta'] = data['close'].diff()
    data['gain'] = data['delta'].apply(lambda x: x if x > 0 else 0)
    data['loss'] = data['delta'].apply(lambda x: abs(x) if x < 0 else 0)
    data['avg_gain'] = data['gain'].rolling(window=14).mean()
    data['avg_loss'] = data['loss'].rolling(window=14).mean()
    data['rs'] = data['avg_gain'] / data['avg_loss']
    data['rsi'] = 100 - (100 / (1 + data['rs']))

    # Implement the trading strategy
    data['position'] = 0
    data.loc[data['rsi'] > 70, 'position'] = -1  # Sell signal when RSI > 70
    data.loc[data['rsi'] < 30, 'position'] = 1  # Buy signal when RSI < 30

    # Calculate the returns
    data['return'] = data['position'].shift() * data['close'].pct_change()

    return data

# Load the tabular data
data = pd.read_csv('path_to_your_data.csv')  # Replace 'path_to_your_data.csv' with the actual file path

# Apply the RSI strategy
data = rsi_strategy(data)

# Print the resulting data
print(data)
