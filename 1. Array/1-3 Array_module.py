import array as arr

# 배열을 정수형으로 가지도록 초기화
int_array = arr.array('i', [1,2,3])

print("elements in array : ", end = "")
for i in range(0, len(int_array)):
    print(int_array[i], end = " ")
print()

# 1의 위치에 4의 값을추가
int_array.insert(1,4)

print("elements after insertion :", end = " ")
for i in (int_array):
    print(i, end=" ")
print()

# 1값을 찾아서 제거
int_array.remove(1)

print("elements after delete \'1\' in array : ", end = " ")
for i in (int_array):
    print(i, end = " ")
print()


int_list = [1,2,3,4,3,5,6,7,8,9,10, 1]
int_arr = arr.array('i', int_list)
print("elements in array : ")
for i in (int_arr):
    print(i, end=" ")
print()

# 3의 값이 가장 처음 나타나는 배열의 인덱스를 출력
print("The index of 1st occurrence of 3 is : ", end= "")
print(int_arr.index(3))

# 1의 값이 가장 처음 나타나는 배열의 인덱스를 출력
print("The index of 1st occurrence of 1 is : ", end= "")
print(int_arr.index(1))
