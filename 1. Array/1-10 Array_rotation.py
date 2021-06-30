from typing import List
# 배열의 회전
# 각 요소를 우측으로 k번 이동 및 회전 (k>=0)

# 각 요소를 한번씩 k번 이동 시간복잡도 N*k
def rotate(nums: List[int], k :int)->List[int]:
    for l in range(k):
        prev = nums[len(nums)-1]
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = prev
            prev = temp
    return nums
print(rotate([1,2,3,4],2))


# 각 요소를 임시 배열에 두고옮기기 시간복잡도 N
def rotate2(nums: List[int], k:int) ->List[int]:
    temp = [0]*len(nums)

    for i, elem in enumerate(temp):
        temp[(i+k)%len(nums)] = nums[i]

    return temp
print(rotate2([1,2,3,4,5,6,7] ,4))


# 다른 방법
def rotate3(nums:List[int], k:int)->List[int]:
    k = k%len(nums)
    nums[:] = nums[::-1]
    nums[0:k] = nums[0:k][::-1]
    nums[k:len(nums)] = nums[k:len(nums)][::-1]

rotate3([1,2,3,4,5],3)
