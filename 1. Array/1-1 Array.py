# 비어있는 리스트 선언
py_list_empty = []
print(py_list_empty)

#1,2,3,4,5의 요소를 갖는 리스트 선언
py_list = [1,2,3,4,5]
print(py_list)

#0을 10개 가지는 리스트 초기화
py_list_zeros_1 = [0 for i in range(10)]
print(py_list_zeros_1)

py_list_zeros_2 = [0]*10
print(py_list_zeros_2)


# 리스트 요소 추가 및 삭제
# append() / extend() / insert() / remove() / clear()
py_list = [1,2,3,4,5]
py_list.append(6)
print(py_list)

# 리스트에 리스트 추가
py_list1 = [1,2,3]
py_list2 = [4,5,6]
print(py_list1)

py_list1.append(py_list2)
print(py_list1)

# 리스트에 리스트 값을 확정
py_list1.extend(py_list2)
print(py_list1)

# 지정된 인덱스에 요소 추가
py_list = [1,2,3]
py_list.insert(3, 4)
print(py_list)

# 리스트 내부 요소 삭제 > 이때 여러 값 중 가장 앞선 인덱스 요소가 삭제
py_list = [1,2,3,4,2,3]
py_list.remove(2)
print(py_list)

# 모든 요소 삭제
py_list = [1,2,3,4,5]
py_list.clear()
print(py_list)

# 지정된 위치의 요소 삭제
py_list = [1,2,3,4,5]
del py_list[1]
print(py_list)

