from typing import List
# 1-11 빠진 숫자 찾기

def missingNumber(nums:List[int])->int:
    nums.sort()

    if nums[-1] != len(nums):
        return len(nums)
    if nums[0] != 0:
        return 0

    for i in range(1, len(nums)):
        expected = nums[i-1] + 1
        if expected != nums[i]:
            return expected

    return -1

print(missingNumber([0,3,5,2,7,1,6]))

#set자료구조를 활용한 숫자 찾기
def missingNumber(nums: List[int])->int:
    set_nums = set(nums)

    for i in range(len(nums)-1):
        if i not in set_nums:
            return i

    return -1

print(missingNumber([0,3,5,2,7,1,6]))


# XOR 비트연산을 사용
def missingNumber(nums:List[int])->int:
    missing = len(nums)

    for i in range(len(nums)):
        missing = missing^i^nums[i]

    return missing

print(missingNumber([0,3,5,2,7,1,6]))


# 모든 요소의 합의 차로 빠진 숫자를 찾아내기
def missingNumber(nums:List[int])->int:
    expected_sum = 0
    nums_sum = 0

    for i in range(len(nums)+1):
        expected_sum += i

    for j in nums:
        nums_sum += j

    return expected_sum - nums_sum

print(missingNumber([0,1,2,3,5]))

# 가우스 덧셈 활용
def missingNumber(nums:List[int])->int:
    expected_num = int((len(nums)*(len(nums)+1))/2)
    nums_sum = 0

    for i in nums:
        nums_sum += i

    return expected_num - nums_sum

print(missingNumber([0,1,2,3,5]))

# 가우스덧셈과 sum()함수 활용
def missingNumber(nums:List[int])->int:
    expected_num = int((len(nums)*(len(nums)+1)/2))
    nums_sum = sum(nums)
    return expected_num - nums_sum

print(missingNumber([0,1,2,3,4,6]))
