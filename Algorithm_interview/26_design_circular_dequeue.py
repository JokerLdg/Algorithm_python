# 26) 원형 데크 디자인
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MyCircularDeQueue:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insert_front(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insert_last(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self.len += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def delete_front(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def delete_last(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)

    def get_front(self) -> int:
        return self.head.right.val if self.len else -1

    def get_rear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isempty(self) -> bool:
        return self.len == 0

    def isfull(self) -> bool:
        return self.len == self.k


queue = MyCircularDeQueue(5)
queue.insert_front(1)
queue.insert_front(2)

print(queue.get_front())
print(queue.get_rear())