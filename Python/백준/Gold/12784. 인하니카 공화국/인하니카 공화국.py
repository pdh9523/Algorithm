import sys; input = sys.stdin.readline


def solve():
    def dfs(prev=1, now=1):
        res = 0
        for nxt, cost in tree[now]:
            if nxt == prev: continue
            res += min(dfs(now, nxt), cost)
        return res if res else float('inf')


    N,M = map(int,input().split())
    if N == 1: return 0
    tree = [[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c = map(int,input().split())
        tree[a].append((b,c))
        tree[b].append((a,c))
    return dfs()

for _ in range(int(input())):
    print(solve())