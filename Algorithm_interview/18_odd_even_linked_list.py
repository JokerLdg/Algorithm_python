# 18) 홀짝 연결 리스트
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

# 반복 구조로 홀짝 노드 처리
def odd_even_list(head: ListNode) -> ListNode:
    # 예외 처리
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # 반복하면서 홀짝 노드 처리
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 홀수 노드의 마지막을 짝수 헤드로 연결
    odd.next = even_head
    return head



list1 = ListNode(4)
list2 = ListNode(2)
list3 = ListNode(1)
list4 = ListNode(3)
list5 = ListNode(5)

list_head = list1
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5

merge = odd_even_list(list_head)
list_print(merge)
