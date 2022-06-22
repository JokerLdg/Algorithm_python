# 27) k개 정렬 리스트 병합
import heapq
from typing import List

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


def merge_k_lists(lists: List[ListNode]) -> ListNode:
    root = result = ListNode(None)
    heap = []

    # 각 연결 리스트의 루트를 힙에 저장
    for i in range(len(lists)):
        if lists[i]:
            print(lists[i].val, i, lists[i])
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

    # 힙 추출 이후는 다음 노드는 다시 저장
    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

        return root.next
