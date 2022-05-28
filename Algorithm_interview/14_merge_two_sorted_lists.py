# 14) 두 정렬 리스트의 병합
import collections

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

# 재귀 구조로 연결
def merge_two_list_recursion(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = merge_two_list_recursion(l1.next, l2)
    return l1


l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1_head = l1_1
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2_head = l2_1
l2_1.next = l2_2
l2_2.next = l2_3

merge = merge_two_list_recursion(l1_head, l2_head)

while merge:
    print(merge.val, end="")
    if merge.next:
        print("->", end="")
    merge = merge.next

