lists = [2, 7, 11, 15]
goal = 9


# 브루트 포스
def two_sum_brute_force(nums: list, target: int) -> list:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)-1):
            if nums[i] + nums[j] == target:
                return [i, j]


# in 탐색
def two_sum_in_search(nums: list, target: int) -> list:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i+1:].index(complement) + (i + 1)]


# 첫번째 수를 뺀 결과 키 조회
def two_sum_exception(nums: list, target: int) -> list:
    nums_map = {}

    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i


# 투 포인터 (정렬이 되어있다는 가정 하에)
def two_sum_two_pointer(nums: list, target: int) -> list:
    left, right = 0, len(nums) - 1

    while not left == right:
        # 합이 타겟보다 작으면 왼쪽을 1 증가
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 크면 오른쪽을 1 감소
        elif nums[left] + nums[right] > target:
            right -=1
        else:
            return [left, right]


print(two_sum_brute_force(lists, goal))
print(two_sum_in_search(lists, goal))
print(two_sum_exception(lists, goal))
print(two_sum_two_pointer(lists, goal))
