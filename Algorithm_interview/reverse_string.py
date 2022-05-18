s = ["h", "e", "l", "l", "o"]

## 투포인터 방법
left = 0
right = len(s) - 1

while left < right:
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
print(s)

## reverse
s.reverse()
print(s)

## 슬라이싱
s[:] = s[::-1]
print(s)