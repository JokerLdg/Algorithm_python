# 10) 배열 파티션1

data = [1, 4, 3, 2]

def array_pair_sort(nums: list[int]) -> int:
    total = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        pair.append(n)
        if len(pair) == 2:
            total += min(pair)
            pair = []

    return total

def array_pair_even_number(nums: list[int]) -> int:
    total = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            total += n

    return total

def array_pair_slicing(nums: list[int]):
    return sum(sorted(nums)[::2])


print(array_pair_sort(data))
print(array_pair_even_number(data))
print(array_pair_slicing(data))