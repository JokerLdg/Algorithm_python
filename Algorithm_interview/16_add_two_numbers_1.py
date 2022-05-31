# 16) 두 수의 덧셈(자료형 변환)
import collections

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def list_print(node: ListNode):
    while node:
        print(node.val, end="")
        if node.next:
            print("->", end="")
        node = node.next
    print()

# 반복 구조로 연결리스트 뒤집기
def reverse_iteration(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

# 연결리스트를 리스트로 만들기
def to_list(node: ListNode) -> list:
    result_list = []

    while node:
        result_list.append(node.val)
        node = node.next

    return result_list

# 리스트를 연결리스트로 만들기
def to_linkedlist(list_data: str) -> ListNode:
    prev: ListNode = None

    for r in list_data:
        node = ListNode(r)
        node.next = prev
        prev = node

    return node

# 두 연결리스트 덧셈
def add_two_numbers(node1: ListNode, node2: ListNode) -> ListNode:
    a = to_list(reverse_iteration(node1))
    b = to_list(reverse_iteration(node2))

    result = int(''.join(str(e) for e in a)) + \
             int(''.join(str(e) for e in b))

    return to_linkedlist(str(result))

list1 = ListNode(2)
list2 = ListNode(4)
list3 = ListNode(3)

list4 = ListNode(5)
list5 = ListNode(6)
list6 = ListNode(4)

head1 = list1
list1.next = list2
list2.next = list3

head2 = list4
list4.next = list5
list5.next = list6

merge = add_two_numbers(head1, head2)
list_print(merge)

