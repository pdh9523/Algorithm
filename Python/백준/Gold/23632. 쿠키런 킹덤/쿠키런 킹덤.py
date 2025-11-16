import sys; input = sys.stdin.readline
from collections import deque


N,M,T = map(int,input().split())

ans = set(map(int,input().split()))
have = set()

buildings = [None] * (N+1)
for i in range(1,N+1):
    _, *x = map(int,input().split())
    buildings[i] = set(x)
    if i in ans:
        have.update(x)

needs = [None] * (N+1)
rev_needs = [set() for _ in range(N+1)]
indegree = [0] * (N+1)

q = deque()
for _ in range(N-M):
    i, _, *x = map(int,input().split())
    needs[i] = set(x)
    for c in x: rev_needs[c].add(i)
    indegree[i] = len(needs[i] - have)
    if indegree[i] == 0:
        q.append((i,0))

while q:
    now, t = q.popleft()
    if t >= T: continue

    ans.add(now)
    for x in buildings[now] - have:
        for nxt in rev_needs[x]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append((nxt, t+1))

    have.update(buildings[now])

print(len(ans))
print(*sorted(ans))