import sys

read = lambda: sys.stdin.readline().rstrip()

N = 1000 - int(read())
coins = [500, 100, 50, 10, 5, 1]
result = 0

for coin in coins:
    result += N // coin
    N = N % coin

print(result)