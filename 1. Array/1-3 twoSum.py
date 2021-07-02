from typing import List

# 두 수의 합 찾기 1(시간복잡도 N^2)
def twoSum(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j]) is target:
                return [i,j]
        return [-1, -1]

#test cases
print(twoSum([2,7,8,11], 9))


#두 수의 합 찾기 2 (시간복잡도 N)
def twoSum(nums: List[int], target: int) -> List[int]:
    hashtable_dict = {}

    for i in range(0, len(nums)):
        value = target - nums[i]

        if hashtable_dict.get(value) is not None \
           and hashtable_dict[value] != i:
            return sorted([i, hashtable_dict[value]])

        hashtable_dict[nums[i]] = i

    return [-1, -1]

#test cases
print(twoSum([2,7,8,11], 9))
print(twoSum([2,5,6,13], 11))
print(twoSum([1,2,7,8,12], 15))
print(twoSum([2,7,8,11], 10))
