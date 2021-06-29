# 배열에서 다수의 요소 찾기
# 정수형배열, 1개 이상의 요소를 가지며 다수의 수는 무조건 하나가 존재

from typing import List

# 시간복잡도 n^2
def majorityElement(nums: List[int]) -> int:
    majority_count = int(len(nums)/2)

    for i, item_i in enumerate(nums):
        count = 0
        for j, item_j in enumerate(nums[i:], start=i):
            if item_i == item_j:
                count += 1
            if count > majority_count:
                return item_i
    return -1

print(majorityElement([2,4,5,1,2,2,2,2,3]))


# 시간복잡도 n
def majorityElement(nums: List[int]) -> int:
    majority_count = int(len(nums)/2)

    hashmap = {}
    for num in nums:
        if hashmap.get(num) != None:
           hashmap[num] = hashmap[num] + 1
        else:
            hashmap[num] = 1

        if hashmap[num] > majority_count:
            return num
    return -1

print(majorityElement([2,4,5,1,2,2,2,2,3]))


# 또다른 방법
def majorityElement(nums: List[int]) -> int:
    return sorted(nums)[int(len(nums)/2)]

print(majorityElement([2,4,5,1,2,2,2,2,3]))
