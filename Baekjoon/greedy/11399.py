import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())
P = list(map(int, read().split()))

P.sort()

answer = P[0]

for i in range(1, len(P)):
    P[i] = P[i-1] + P[i]
    answer += P[i]

print(answer)