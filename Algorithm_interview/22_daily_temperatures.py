# 22) 일일 온도

# 스택으로 진행
def daily_temperatures_stack(temperatures: list) -> list:
    answer = [0] * len(temperatures)
    stack = []

    for i, cur in enumerate(temperatures):
        # 현재 온도가 스택값 보다 높다면 정답 처리
        while stack and cur > temperatures[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer

T = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures_stack(T))

