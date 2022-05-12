import sys

read = lambda: sys.stdin.readline().rstrip()

"""
-가 온다면 그 데이터 뒤로는 전부 빼준다.
"""

s = read()
isminus = False
num = ""
result = 0

for i in range(len(s)+1):
    if i == len(s) or s[i] == '-' or s[i] == '+':
        if isminus:
            result -= int(num)
            num = ""
        else:
            result += int(num)
            num = ""
    else:
        num += s[i]

    if i != len(s):
        if s[i] == '-':
            isminus = True

print(result)