# 25) 원형 큐 디자인
class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k
        self.max_len = k
        self.front_p = 0
        self.rear_p = 0

    # rear 포인터 뒤로 이동
    def en_queue(self, value: int) -> bool:
        if self.q[self.rear_p] is None:
            self.q[self.rear_p] = value
            self.rear_p = (self.rear_p + 1) % self.max_len
            return True
        else:
            return False

    # front 포인터 이동
    def de_queue(self) -> bool:
        if self.q[self.front_p] is None:
            return False
        else:
            self.q[self.front_p] = None
            self.front_p = (self.front_p + 1) % self.max_len
            return True

    def front(self) -> int:
        return -1 if self.q[self.front_p] is None else self.q[self.front_p]

    def rear(self) -> int:
        return -1 if self.q[self.rear_p - 1] is None else self.q[self.rear_p - 1]

    def isempty(self) -> bool:
        return self.front_p == self.rear_p and self.q[self.front_p] is None

    def isfull(self) -> bool:
        return self.front_p == self.rear_p and self.q[self.front_p] is not None

queue = MyCircularQueue(5)
queue.en_queue(10)
queue.en_queue(20)
queue.en_queue(30)

print(queue.front())
print(queue.rear())

queue.de_queue()
print(queue.front())
print(queue.rear())

queue.de_queue()
queue.de_queue()
print(queue.isempty())

queue.en_queue(10)
queue.en_queue(20)
queue.en_queue(30)
queue.en_queue(40)
queue.en_queue(50)
print(queue.isfull())