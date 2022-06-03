# 19) 역순 연결 리스트2
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

def reverse_between(head: ListNode, m: int, n:int) -> ListNode:
    # 예외 처리
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head

    # start, end 지정
    for _ in range(m - 1):
        start = start.next
    end = start.next

    # 반복 하면서 노드 차례대로 뒤집기
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next


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

merge = reverse_between(list_head, 2, 4)
list_print(merge)