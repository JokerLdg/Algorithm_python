# 15) 역순 연결 리스트
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

# 재귀 구조로 뒤집기
def reverse_recursion(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode = None):
        if not node:
            return prev
        next, node.next = node.next, prev
        return reverse(next, node)

    return reverse(head)

# 반복 구조로 뒤집기
def reverse_iteration(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev


list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)

list_head = list1
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5

merge = reverse_recursion(list_head)
list_print(merge)

merge = reverse_iteration(merge)
list_print(merge)


