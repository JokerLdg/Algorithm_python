import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())
count = 0

while True:
    if N % 5 == 0:
        count = count + (N//5)
        break

    N = N - 3
    count += 1

    if N < 0:
        count = -1
        break

print(count)
