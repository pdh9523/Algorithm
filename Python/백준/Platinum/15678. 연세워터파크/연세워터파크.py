from collections import deque


N,D = map(int,input().split())
arr = [*map(int,input().split())]

q = deque([-float('inf')])
DP = [-float('inf')] * D

for left, i in zip(DP,arr):
    now = i + max(0, q[0])
    while q and q[-1] < now:
        q.pop()
    q.append(now)
    DP.append(now)
    if q[0] == left:
        q.popleft()

print(max(DP))