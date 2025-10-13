import sys; input = sys.stdin.readline
from collections import deque


def bfs(x):
    if x == 1: return 1

    visited = [False] * x
    parent = [-1] * x
    ans = [-1] * x

    q = deque([1])
    ans[1] = 1
    visited[1] = True

    while q:
        now = q.popleft()

        if now == 0:
            path = []
            temp = 0
            while temp != 1:
                path.append(ans[temp])
                temp = parent[temp]
            path.append(1)    
            return ''.join(map(str, path[::-1]))

        for nxt, check in ((now*10)%x, 0), ((now*10+1)%x, 1):
            if not visited[nxt]:
                visited[nxt] = True
                ans[nxt] = check
                parent[nxt] = now
                q.append(nxt)
    
    return "BRAK"

for _ in range(int(input())):
    print(bfs(int(input())))
