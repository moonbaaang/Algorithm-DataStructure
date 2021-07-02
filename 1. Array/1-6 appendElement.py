from typing import List
# 정렬된 배열의 병합 1
# Constraints
# 주어진 nums1, nums2 요소는 정렬되어있음
# nums1의 요소는 m개, nums2의 요소는 n개
# nums1의 요소 크기는 m+n개 

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    for i,v  in enumerate(nums2):
        nums1[m+i] = v;

    nums1[:] = sorted(nums1)

print("Test Case")
print(f'{merge([1,2,3], 3, [], 0)}')
print(f'{merge([0,0,0], 0, [1,2,3], 3)}')
print(f'{merge([1,2,3,0,0,0], 3, [4,5,6], 3)}')
print(f'{merge([4,5,6,0,0,0], 3, [1,2,3], 3)}')


def merge(nums1: List[int], m: int, nums2: List[int], n:int)-> None:
    i = m-1
    j = n-1
    k = m+n-1

    while i>=0 and j>=0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1

        k -= 1

    while j>=0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1


def merge(nums1: List[int], m:int, nums2: List[int], n:int)->List[int]:
    i = m-1
    j = n-1
    k = m+n-1

    while i>=0 and j>=0:
        if nums1[i]<nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else :
            nums1[k] = nums1[i]
            i -= 1

        k -= 1

    while j>=0:
        nums1[k] = nums2[j]
        k -= 1
        j -= 1

    return nums1

print("Test Case")
print(f'{merge([1,2,3], 3, [], 0)}')
print(f'{merge([0,0,0], 0, [1,2,3], 3)}')
print(f'{merge([1,2,3,0,0,0], 3, [4,5,6], 3)}')
print(f'{merge([4,5,6,0,0,0], 3, [1,2,3], 3)}')
print(f'{merge([1,2,3,5,0,0], 4, [4,6], 2)}')
