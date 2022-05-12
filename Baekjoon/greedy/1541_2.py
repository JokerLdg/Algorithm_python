import sys

read = lambda: sys.stdin.readline().rstrip()

"""
- 기준으로 나누고, 그 데이터를 다시 +로 나누어서 계산한다.
각 원소에 있는 숫자들을 계산해주고 맨 처음의 원소는 더해주고 나머지는 빼준다.
"""

s = read()
minus_split_data = s.split('-')
result = 0
num_list = []

for minus_data in minus_split_data:
    number = 0
    plus_split_data = minus_data.split('+')

    for plus_data in plus_split_data:
        number += int(plus_data)

    num_list.append(number)

result = num_list[0]
for i in range(1, len(num_list)):
    result -= num_list[i]

print(result)