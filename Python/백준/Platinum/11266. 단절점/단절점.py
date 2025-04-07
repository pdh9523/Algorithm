import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def dfs(now, is_root):
    global order

    visit[now] = order
    order += 1
    child_num = 0
    child_order = visit[now]
    for nxt in graph[now]:
        if visit[nxt] != float('inf'): child_order = min(child_order, visit[nxt])
        else:
            child_num += 1
            tmp = dfs(nxt, False)
            if not is_root and tmp >= visit[now]:
                ans.add(now)
            child_order = min(child_order, tmp)
    
    if is_root and child_num >= 2: ans.add(now)
    return child_order

N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = set()
order = 0
visit = [float('inf')] * (N+1)

for i in range(1,N+1):
    if visit[i] == float('inf'):
        dfs(i, True)

print(len(ans))
print(*sorted(ans))