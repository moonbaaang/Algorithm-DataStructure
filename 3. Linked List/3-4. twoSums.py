# 두 수 더하기
'''
정수를 연결 리스트로 표현해 해당 노드를 접근 및 숫자를 인식하고 다른 연결 리스트의 같은 자리와 합 연산을 하여 새로운 연결 리스트를 만들어 반환

Constraint : 
1. 연결 리스트는 양의 정수로 표현
2. 1번째 노드는 가장 높은 자리의 숫자
3. 주어진 두 연결리스트는 무조건 값이 있음
4. 0을 제외하고 0으로 시작하는 숫자는 없음
'''

class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = next
'''
아이디어
(1) 스택 (시간복잡도 n, 공간복잡도 2n)
1. 스택 2개 생성
2. 각 연결 리스트를 각각 순회하면서 노드값을 스택에 넣음
3. 스택의 값을 하나씩 꺼내 자리수를 더해나감
 - 더해진 각 값을 새로운 연결리스트의 노드로 연결
'''
def addTwoNumbers(l1:Node, l2:Node)->Node:
    st1 = []
    st2 = []

    l1_curr = l1
    l2_curr = l2

    head = None
    while l1_curr != None:
        st1.append(l1_curr.val)
        l1_curr = l1_curr.next

    while l2_curr != None:
        st2.append(l2_curr.val)
        l2_curr = l2_curr.next

    carry = 0

    while st1 or st2:
        num1 = st1.pop() if st1 else 0
        num2 = st2.pop() if st2 else 0

        carry, num = divmod(num1 + num2 +carry, 10)

        node = Node(num)
        if head == None:
            head = node
        else:
            temp = head
            head = node
            node.next = temp

    if carry != 0:
        node = Node(carry)
        temp = head
        head = node
        node.next = temp
    
    return head
    

'''
(2) 연결리스트 뒤집기 (시간복잡도 n, 공간복잡도 1)
1. 2개의 연결리스트를 뒤집음
2. 뒤집은 연결리스트를 순회하며 각 자리수를 더함,  각자리숫자를 더하면서 새로운 노드를 생성하고 연결
'''
def addTwoNumbers(l1:Node, l2:Node)->Node:
    def reverse(head):
        prev = None
        curr = head

        while curr != None:
            next_temp = curr.next
            curr.next = prev

            prev = curr
            curr = next_temp
        return prev

    r_l1 = reverse(l1)
    r_l2 = reverse(l2)

    res_head = None

    carry = 0
    while r_l1 != None or r_l2 != None:
        num1 = 0
        num2 = 0

        if r_l1 != None:
            num1 = r_l1.val
            r_l1 = r_l1.next
        if r_l2 != None:
            num2 = r_l2.val
            r_l2 = r_l2.next

        carry, num = divmod(num1+num2+carry, 10)

        node = Node(num)
        if res_head == node:
            res_head = node
        else:
            temp = res_head
            res_head = node
            node.next = temp

    if carry != 0:
        node = Node(carry)
        temp = res_head
        res_head = node
        node.next = temp

    return res_head


'''
(3) 문자열 연산 (시간복잡도 n, 공간복잡도 L+M)
1. 각 연결리스트를 순회하면서 숫자를 문자열로 전환하고 문자열에 숫자를 추가
2. 두 문자열을 int()로 변환
3. 정수를 다시 str()로 변환
4. 각 자리를 접근하면서 연결리스트를 구성
'''

def addTwoNumbers(l1:Node, l2:Node)->Node:
    num1_str = ""
    num2_str = ""

    l1_curr = l1
    l2_curr = l2

    while l1_curr != None:
        num1_str = num1_str + str(l1_curr.val)
        l1_curr = l1_curr.next

    while l2_curr != None:
        num2_str = num1_str + str(l2_curr.val)
        l2_curr = l2_curr.next

    res_num = int(num1_str) + int(num2_str)

    #dummy mode
    head = ListNode(-1)
    curr = head
    for num_ch in str(res_num):
        curr.next = Node(itn(num_ch))
        curr = curr.next

    curr.next = None
    return head.next