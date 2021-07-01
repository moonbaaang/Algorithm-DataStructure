from typing import List
#주어진 배열에서 가능한 모든 부분집합 반환
def subsets_recursion(nums: List[int],
    res: List[List[int]], sub:List[int], index) -> None:

    if len(sub) > len(nums):
        return

    res.append(sub.copy())
    # sub를 그대로 넣으면 sub의 주소값이 복사됨 

    for i in range(index, len(nums)):
        sub.append(nums[i])
        subsets_recursion(nums, res, sub, i+1)
        sub.pop()

nums = [1,2,3]
res = []
sub = []
subsets_recursion(nums, res, sub, 0)

# 반복 iterative
def subsets(nums:List[int])->List[List[int]]:
    res = []
    nums_len = len(nums)
    nth_bit = 1 << nums_len

    for i in range(2**nums_len):
        bitmask = bin(i|nth_bit)[3:]

        res.append(
            [nums[j] for j in range(nums_len) if bitmask[j] == '1'])
    return res

print(subsets([1,2,3]))

'''
res.append([nums[j] for j in range(nums_len) if bitmask[j] == '1']) 는 아래와 같다

temp = []
for j in range(nums_len):
    if bitmask[j] == '1':
        temp.append(nums[j])
res.append(temp)
'''
