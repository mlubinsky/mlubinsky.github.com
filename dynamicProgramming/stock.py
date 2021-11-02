# If number transactions =1 (1 buy and 1 sell)

prices = [100, 10, 200, 85, 500, 63]

profit = 0
min_price = prices[0]
for i in range(1, len(prices)):
    min_price = min(min_price, prices[i])
    profit = max (profit, prices[i] - min_price)

print profit


# What if we can complete most K transactions
