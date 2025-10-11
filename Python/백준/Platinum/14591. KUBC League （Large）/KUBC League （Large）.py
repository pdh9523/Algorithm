import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)


def dfs(now=0):
    check[now] = 1
    for nxt in range(N):
        if check[nxt]: continue
        if not arr[now][nxt]: continue
        dfs(nxt)
    ans.append(now+1)

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]
check = [0] * (N+1)
ans = []
dfs()
print(len(ans))
print(*reversed(ans))
