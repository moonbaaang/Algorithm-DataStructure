# 연결 리스트의 이해
# 각 자료가 다음 자료에 연결고리를 가진 자료구조
# 각 노드는 연결 리스트로 유지하고자 하는 데이터와 다음 노드를 연결하기 위한 주솟값을 가지고 운영
# 연결 리스트는 정해진 공간 내에 데이터를 넣고 빼는 구조가 아니라 연결 고리만으로 많은 데이터를 넣고 관리할 수 있음
# 배열 > 고정 크기 / 연결리스트 > 동적 크기 > 데이터의 연결고리만 변경해주면 얼마든지 노드를 만들 수 있음
# 단, 연결리스트는 인덱스를 사용 불가능하고, 해당 값에 접근하기 위해 처음부터 순회해야함 
# 연속적인 메모리 공간으로 관리되지 않음

from typing import Any

class Node:
    def __init__(self, data:Any):
        self.data = data
        self.next = None

node = Node(3)
print(f'{node.data}')

node1 = Node(11)
node2 = Node(12)
node3 = Node(13)

node1.next = node2
node2.next = node3