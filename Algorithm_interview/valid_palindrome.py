import sys
import re

read = lambda: sys.stdin.readline().rstrip()

s = read()

s = s.lower()
s = re.sub('[^a-z0-9]', '', s)

print(s == s[::-1])