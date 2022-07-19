# 29) 보석과 돌
# 해시 테이블을 이용한 계산
import collections

def jewels_and_stones_hashtable(jewels: str, stones: str) -> int:
    dic = {}
    count = 0

    # 돌(stones)의 빈도수 계산
    for char in stones:
        if char not in dic:
            dic[char] = 1
        else:
            dic[char] += 1

    # 보석(jewels)의 빈도수 계산
    for char in jewels:
        if char in dic:
            count += dic[char]

    return count

# defaultdic을 이용한 계산
def jewels_and_stones_defaultdic(jewels: str, stones: str) -> int:
    dic = collections.defaultdict(int)
    count = 0

    # 돌의 빈도수 계산
    for char in stones:
        dic[char] += 1

    # 보석의 빈도수 합산
    for char in jewels:
        count += dic[char]

    return count

# Counter를 이용한 계산
def jewels_and_stones_counter(jewels: str, stones: str) -> int:
    dic = collections.Counter(stones)
    count = 0

    for char in jewels:
        count += dic[char]

    return count

# 파이썬 다운 방식
def jewels_and_stones_python(jewels: str, stones: str) -> int:
    return sum(s in jewels for s in stones)


J = 'aA'
S = 'aAAbbbbb'

print(jewels_and_stones_hashtable(J, S))
print(jewels_and_stones_defaultdic(J, S))
print(jewels_and_stones_counter(J, S))
print(jewels_and_stones_python(J, S))