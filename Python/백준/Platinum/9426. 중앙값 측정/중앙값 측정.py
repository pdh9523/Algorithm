import sys; input = sys.stdin.readline
from heapq import heappop, heappush


class PriorityQueue():
    def __init__(self):
        self.hq = []
        self._deleted = []
    
    def size(self):
        return len(self.hq) - len(self._deleted)

    def top(self):
        return self.hq[0]

    def push(self, v):
        heappush(self.hq, v)
    
    def pop(self):
        p = heappop(self.hq)
        self._gc()
        return p
    
    def delete(self, v):
        heappush(self._deleted, v)
        self._gc()
    
    def _gc(self):
        while self._deleted and self._deleted[0] == self.hq[0]:
            heappop(self.hq)
            heappop(self._deleted)


N,K = map(int,input().split())
arr = [int(input()) for _ in range(N)]
left,right = PriorityQueue(), PriorityQueue()

mid,ans = float('inf'),0

for i, num in enumerate(arr):
    if i >= K:
        target = arr[i-K]
        if target <= mid:
            right.delete(-target)
        else:
            left.delete(target)
    
    if num <= mid:
        right.push(-num)
        while right.size() > left.size() + 1:
            left.push(-right.pop())
    else:
        left.push(num)
        while right.size() < left.size():
            right.push(-left.pop())
    
    mid = -right.top()

    if i >= K - 1:
        ans += mid

print(ans)
