# 13) 팰린드롬 연결 리스트
import collections

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

# 리스트 변환
def is_palindrome_list(head: ListNode) -> bool:
    q = []

    if not head:
        return True

    node = head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) >= 2:
        if q.pop(0) != q.pop():
            return False

    return True

# 데크 최적화
def is_palindrome_deque(head: ListNode) -> bool:
    q = collections.deque()

    if not head:
        return True

    node = head
    while node is not None:
        q.append(node.val)
        node = node.next

    while len(q) >= 2:
        if q.popleft() != q.pop():
            return False

    return True

# 런너를 이용한 풀이
def is_palindrome_runner(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    """
    런너를 이용하여 역순으로 중간까지의 연결 리스트를 만들고(rev)
    남아있는 slow의 리스트와 역순으로 된 rev의 리스트를 비교해서 동일하면 True이다.
    즉, rev나 slow에 데이터가 None인경우 참
    """

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


list1 = ListNode(1)
list2 = ListNode(2)
list3 = ListNode(3)
list4 = ListNode(2)
list5 = ListNode(1)

list_head = list1
list1.next = list2
list2.next = list3
list3.next = list4
list4.next = list5

print(is_palindrome_list(list_head))
print(is_palindrome_deque(list_head))
print(is_palindrome_runner(list_head))