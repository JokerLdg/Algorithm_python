# 단어 수학 문제
import sys

read = lambda: sys.stdin.readline().rstrip()

N = int(read())
words = [read() for _ in range(N)]

# 딕셔너리 초기화
dic = {}

for word in words:
    # 길이를 계산하여 10^square_root만큼 넣어주기 위해 계산한다.
    # -1를 하는 이유는 맨뒤는 1의자리이기 때문
    square_root = len(word) - 1

    for ch in word:
        # 딕셔너리에 값이 있다면 값을 더한다.
        if ch in dic:
            dic[ch] += (10 ** square_root)
        else:
            dic[ch] = (10 ** square_root)

        square_root -= 1

# 딕셔너리를 큰 값부터 쓰기 위해 정렬
dic = sorted(dic.values(), reverse=True)

answer, m = 0, 9

for result in dic:
    answer += result * m
    m -= 1

print(answer)