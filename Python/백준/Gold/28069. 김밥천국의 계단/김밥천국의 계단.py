from collections import deque

N,K = map(int,input().split())
visit = [-1] * (N+1)
visit[0] = 0

q = deque([0])
while q:
    now = q.popleft()

    for nxt in now + now//2, now+1:
        if nxt > N: continue
        if visit[nxt] != -1: continue
        visit[nxt] = visit[now] + 1
        if nxt == N: break
        q.append(nxt)

print("minigimbob" if visit[N] <= K else "water")
