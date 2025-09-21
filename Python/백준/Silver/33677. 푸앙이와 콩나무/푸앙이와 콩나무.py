import sys; input = sys.stdin.readline
from collections import deque


N = int(input())
visit = [0] * (N+1)
water = [float('inf')] * (N+1)
q = deque([0])
visit[0] = 1
water[0] = 0
while q:
    now = q.popleft()

    for f,w in (lambda x: x+1, 1), (lambda x: x*3, 3), (lambda x: x**2, 5):
        nxt = f(now)
        if nxt > N: continue
        if not visit[nxt] or visit[nxt] == visit[now] + 1:

            visit[nxt] = visit[now] + 1
            if water[nxt] > water[now] + w:
                water[nxt] = water[now] + w
                q.append(nxt)
        
print(visit[-1]-1, water[-1])