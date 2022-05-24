data = [-1, 0, 1, 2, -1, -4]


def three_sum_brute_force(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복 값 건너 뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, len(nums)-1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


def three_sum_two_pointer(nums: list[int]) -> list[list[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복값 건너 뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 투포인터 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                # total이 0이면 맞으므로 값 추가
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

    return results


print(three_sum_brute_force(data))
print(three_sum_two_pointer(data))
