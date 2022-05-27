# 주식을 사고팔기 가장 좋은 시점

import sys

data = [7, 1, 5, 3, 6, 4]

def max_profit_brute_force(prices: list[int]) -> int:
    max_price = 0
    for i, price in enumerate(prices):
        for j in range(i, len(prices)):
            max_price = max(prices[j] - price, max_price)

    return max_price

def max_profit_best(prices: list[int]) -> int:
    profit = 0
    min_price = sys.maxsize

    # 최솟값과 최댓값을 계속 갱신
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)

    return profit

print(max_profit_brute_force(data))
print(max_profit_best(data))