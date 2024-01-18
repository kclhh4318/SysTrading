# 총 수익률
total_return = data['return'].sum()

# 연간화 수익률
annualized_return = (1 + total_return)**(365.25/data.shape[0]) - 1

# 최대 손실
max_drawdown = (data['return'].cumsum().cummax() - data['return'].cumsum()).max()

# 샤프 비율
sharpe_ratio = data['return'].mean() / data['return'].std()

print(f"Total return: {total_return}")
print(f"Annualized return: {annualized_return}")
print(f"Max drawdown: {max_drawdown}")
print(f"Sharpe ratio: {sharpe_ratio}")