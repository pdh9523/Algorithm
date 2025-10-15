import sys; input = sys.stdin.readline


def dfs(now, start):
    visit[now] = True
    nxt = arr[now]
    if visit[nxt] and nxt == start:
        return ans.append(nxt)
    
    if not visit[nxt]: dfs(nxt, start)

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

ans = []
for i in range(1,N+1):
    visit = [False] * (N+1)
    dfs(i,i)

print(len(ans))
print(*sorted(ans), sep="\n")