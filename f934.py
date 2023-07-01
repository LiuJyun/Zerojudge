def calculate_max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        current_price = prices[i]
        if current_price < min_price:
            min_price = current_price
        elif current_price - min_price > max_profit:
            max_profit = current_price - min_price

    return max_profit


prices = list(map(int, input().split()))
max_profit = calculate_max_profit(prices)
print(max_profit)