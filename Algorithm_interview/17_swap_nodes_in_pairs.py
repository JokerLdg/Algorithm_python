# 17) 페어의 노드 스왑
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

# 값만 교환
def swap_pairs_value(head: ListNode) -> ListNode:
    cur = head

    while cur and cur.next:
        # 값만 교환
        cur.val, cur.next.val = cur.next.val, cur.val
        cur = cur.next.next

    return head

# 반복 구조로 스왑
def swap_pairs_iteration(head: ListNode) -> ListNode:
    root = prev = ListNode(None)
    prev.next = head

    while head and head.next:
        # b가 head를 가리키도록 할당
        b = head.next
        head.next = b.next
        b.next = head

        # prev가 b를 가리키도록 할당
        prev.next = b

        # 다음번 비교를 위해 이동
        head = head.next
        prev = prev.next.next

    return root.next

# 재귀 구조로 스왑
def swap_pairs_recursion(head: ListNode) -> ListNode:
    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = swap_pairs_recursion(p.next)
        p.next = head
        return p
    return head


list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(4)
list5 = ListNode(5)
list6 = ListNode(6)

list_head = list1
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5
list5.next = list6

#merge = swap_pairs_value(list_head)
#merge = swap_pairs_iteration(list_head)
merge = swap_pairs_recursion(list_head)
list_print(merge)
