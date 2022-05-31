# 16) 두 수의 덧셈(전가산기)
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

# 두 연결리스트 덧셈
def add_two_numbers(node1: ListNode, node2: ListNode) -> ListNode:
    root = head = ListNode(0)

    carry = 0
    while node1 or node2 or carry:
        total = 0
        # 두 입력값의 합 계산
        if node1:
            total += node1.val
            node1 = node1.next
        if node2:
            total += node2.val
            node2 = node2.next

        # 몫(자리올림수)과 나머지(값) 계산
        carry, val = divmod(total+carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next


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

