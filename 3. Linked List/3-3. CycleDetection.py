# 순환 검출
# 플로이드의 토끼와 거북이 - 2개의 연결리스트 포인터를 운영하면서 해당 포인터의 순환이동속도차를 이용해 순환을 검출
# 순환이 아니라면 빠른 토끼가 연결리스트에 빠르게 도착, 순환이 있다면 빠른 토끼가 느리게 가던 거북이와 만나도록 하는 알고리즘
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''
1. 노드 순회 (시간복잡도 n^2 / 공간복잡도 1)
 - 끝에 도달하거나 연결이 없으면 종료
 - 현재까지 순회 카운터를 기록
 - 노드를 처음부터 순회(순회 카운터만큼)
  > 바깥순회에서 선택된 노드와 비교해 2번 겹치면 순환이 발생
  > 아니라면 순회 종료

  > 외부 순회와 내부 순회가 있음
'''
def hasCycle(head:Node)->bool:
    outer = head

    node_cnt = 0

    while (outer != None and outer.next != None):
        outer = outer.next
        node_cnt += 1

        visit = node_cnt
        inner = head

        matched = 0
        while visit > 0 :
            if outer != inner :
                inner = inner.next
            
            if outer == inner :
                matched += 1

            if matched == 2 :
                return True

            visit -= 1

    return False

'''
해시테이블 이용
1. 노드 순회
 - 각 노드를 set으로 있는지 없는지 확인
 - 있다면 true반환
 - 없으면 set에 추가
'''
def hasCycle(head:Node)->bool:
    curr = head
    node_set = set()

    while curr != None:
        if curr in node_set:
            return True

        node_set.add(curr)
        curr = curr.next

    return False

'''
Two Pointer
1. slow, fast포인터는 head를 가리킴
2. slow는 1번의 이동
3. fast는 2번의 이동
4. fast와 slow가 같아지면 연결리스트는 순환
5. fast나 slow가 가리키는 노드가 None이면 순환이 없음
'''

def hasCycle(head:Node)->bool:
    slow = head
    fast = head

    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
