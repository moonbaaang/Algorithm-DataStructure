from typing import List

# 배열에서 삽입 위치 찾기
def searchInsert(nums : List[int], target : int)->int:
    index = 0

    while index < len(nums):
        if target <= nums[index]:
            break
        index += 1

    return index

print(searchInsert([2,4,6,8], 10))

#이진탐색으로 삽입 위치 찾기
def searchInsert(nums : List[int], target: int) -> int:
    if len(nums) == 0:
        return None
    low = 0
    high = len(nums) - 1

    while low<=high:
        mid = int((low+high)/2)

        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            low = mid + 1
        else :
            high = mid - 1
    return low

print("Test Case")
print(searchInsert([1,3,5,6], 0))
print(searchInsert([1,3,5,6], 100))















    
