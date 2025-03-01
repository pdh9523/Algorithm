from collections import deque


N = int(input())
q = deque(sorted([*map(int,input().split())]))

ans = 0

while q and q[0]:
    q[0] -= 1
    q.pop()
    if not q: break
    if not q[0]: q.popleft()
    ans += 1

print(ans)