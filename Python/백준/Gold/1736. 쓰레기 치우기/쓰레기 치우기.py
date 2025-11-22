import sys; input = sys.stdin.readline
from collections import deque


N,M = map(int,input().split())
a = [[*map(int,input().split())] for _ in range(N)]

arr = []
for i in range(N):
    for j in range(M):
        if a[i][j]:
            arr.append((i,j))

arr.sort()
q = deque(arr)
new_q = deque()
ans = 0
while q:
    sx,sy = 0,0
    while q:
        x,y = q.popleft()
        
        if sx<=x and sy<=y:
            sx,sy = x,y
        else:
            new_q.append((x,y))
    q = new_q
    new_q = deque()
    ans += 1
print(ans)