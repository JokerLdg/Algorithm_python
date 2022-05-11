import sys

read = lambda: sys.stdin.readline().rstrip()

N, K = map(int, read().split())

A = [int(read()) for _ in range(N)]
i = N-1
count = 0

while K != 0:
    count += K // A[i]
    K = K % A[i]
    i -= 1

print(count)