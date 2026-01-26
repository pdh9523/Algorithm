import sys; input = sys.stdin.readline

def dfs(start = 1):
    visit = [False] * (N+1)
    stack = [(start, arr[start])]
    
    max_d = 0
    idx = start

    while stack:
        now, dist = stack.pop()
        
        if visit[now]: continue

        visit[now] = True
        if max_d < dist or (max_d == dist and now < idx):
            idx = now
            max_d = dist
        for nxt in tree[now]:
            stack.append((nxt, dist+arr[nxt]))
    return idx, max_d

N = int(input())
arr = [0]+[*map(int,input().split())]

tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

start, _ = dfs()
end, length = dfs(start)

print(length, min(start, end))
