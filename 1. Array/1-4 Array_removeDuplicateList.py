from typing import List

# 정렬된 배열에서 중복 제거
def removeDuplicate(nums:List[int]) -> List[int]:
    if len(nums) <= 0:
        return 0
    
    curr = nums[0]
    cnt = 1

    for i in range(1, len(nums)):
        if curr != nums[i]:
            curr = nums[i]
            nums[cnt] = curr
            cnt += 1
            
    return cnt
# 배열로 받고 싶다면 return nums[:cnt]
        
print(removeDuplicate([0,0,0,1,2,2,2]))
print(removeDuplicate([]))
print(removeDuplicate([1,2,3,4]))

# if elif else 문을 이용한 풀이
def removeDuplicate(nums:List[int]) -> List[int]:
    if len(nums) <= 0:
        return 0
    
    cnt = 0
    removeDuplicateList = []
    for i in range(0, len(nums)):
        if len(removeDuplicateList) == 0:
            removeDuplicateList.append(nums[i])
            cnt = nums[i]
        elif cnt == nums[i]:
            continue
        else:
            removeDuplicateList.append(nums[i])
            cnt = nums[i]
    return removeDuplicateList
        
print(removeDuplicate([0,0,0,1,2,2,2]))


## is 연산자는 값이 같더라도 오브젝트가 다르면 false반환
