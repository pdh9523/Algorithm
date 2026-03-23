import sys; input = sys.stdin.readline
from collections import deque

N,T = map(int,input().split())

data = {(0,0): 0}


graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    a,b = map(int,input().split())
    for x in range(a-2,a+3):
        for y in range(b-2,b+3):
            if (a,b) == (x,y): continue
            if (x,y) in data:
                graph[i].append(data[(x,y)])
                graph[data[(x,y)]].append(i)
    data[(a,b)] = i
rev = {v:k for k,v in data.items()}

q = deque([0])
visit = [0] * (N+1)
while q:
    now = q.popleft()

    if rev[now][1] == T:
        exit(print(visit[now]))

    for nxt in graph[now]:
        if visit[nxt]: continue
        visit[nxt] = visit[now] + 1
        q.append(nxt)
print(-1)
