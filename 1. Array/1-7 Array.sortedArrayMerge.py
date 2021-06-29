# 정렬된 배열의 정합 2
# Constraint
# 추가 배열 공간 할당 없음
# nums1, nums2 크기 제한 없음
# nums1, nums2 요소는 정렬되어있음
# Tim sort 이용 
from typing import List

def merge(nums1: List[int], m: int, nums2:List[int], n:int) -> List[int]:
    for i, nums1_item in enumerate(nums1):
        if nums1_item>nums2[0]:
            nums1[i] = nums2[0]
            nums2[0] = nums1_item

            for k, item in enumerate(nums2[1:], start=1):
                if nums1_item<=item:
                    nums2[k-1] = nums1_item
                    break

                nums2[k-1] = nums2[k]

    return nums1, nums2

print(merge([1,3],2,[2,4],2))
