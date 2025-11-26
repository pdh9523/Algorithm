import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def dfs(now=0):
    if not tree[now]: return values[now]
    
    res = 0
    for nxt in tree[now]:
        if (tmp:=dfs(nxt)) > 0: res += tmp
    
    return res + values[now]

N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a].append(b)

values = [*map(int,input().split())]

print(dfs())
