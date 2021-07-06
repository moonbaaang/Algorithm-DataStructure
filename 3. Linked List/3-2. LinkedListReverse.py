# 연결 리스트 뒤집기

'''
반복 (시간복잡도 n / 공간복잡도 1)
1. prev, curr, next 를 유지운영
2. 현재 노드가 None이 아닐 때 까지
 - 현재의 next를 임시저장
 - 현재의 next를 prev를 가리키도록 업데이트
 - prev를 현재 노드로 이동
 - curr를 임시 저장 후 다음 노드로 이동
''' 
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head:Node)->Node:
    prev = None
    curr = head

    while (curr != None):
        next_temp = curr.next

        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

'''
스택 (시간복잡도 n / 공간복잡도 n, 스택에 모든 노드를 저장)
1. 노드를 저장할 스택 생성
2. 연결 리스트 순회
 - 스택에 현재 노드 추가
 - 마지막 노드는 넣지 않음
3. 스택의 모든 요소를 하나씩 꺼냄
 - 마지막 노드로부터 꺼내진 요소를 next 로 연결
'''
def reverseList(head:Node):
    if head == None:
        return head

    stack = []

    curr = head

    while curr.next != None:
        stack.append(curr)
        curr = curr.next

    # 역전 후 첫 노드를 임시 저장하고 반환
    first = curr

    while stack:
        curr.next = stack.pop()
        curr = curr.next

    curr.next = None

    return first


'''
재귀 (시간복잡도 n / 공간복잡도 n, 재귀도 스택을 사용)
1. 노드를 저장할 스택 생성
2. 연결 리스트 순회
 - 스택에 현재 노드 추가
 - 마지막 노드는 넣지 않음
3. 스택의 모든 요소를 하나씩 꺼냄
 - 마지막 노드로부터 꺼내진 요소를 next 로 연결
'''
def reverseList(head: Node)->Node:
    if head == None or head.next == None:
        return head

    reversed_list = reverseList(head.next)
    head.next.next = head
    head.next = None
    
    return reversed_list