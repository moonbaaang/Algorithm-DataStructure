#피라미드
pyramid = []
for i in range(5):
    column = []
    while i>=0:
        column.append(0)
        i -= 1
    pyramid.append(column)

print(pyramid)

# 파스칼의 삼각형
from typing import List

def generate(numRows: int)->List[List[int]]:
    pascal = []

    if numRows <= 0:
        return pascal

    pascal.append([1])

    for i in range(1, numRows):
        prev_len = len(pascal[i-1])
        curr_list = []

        for j in range(prev_len + 1):
            num = 1
            if j!=0 and j!=prev_len:
                num = pascal[i-1][j-1] + pascal[i-1][j]

            curr_list.append(num)

        pascal.append(curr_list)

    return pascal

print(generate(5))
