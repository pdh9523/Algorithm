import sys; input = sys.stdin.readline


N,M,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(N)]
rank = {v[1]:i+1 for i,v in enumerate(sorted(arr, key=lambda x: -x[1]))}

cnt = 0
ans = 0
for a,b in sorted(arr, reverse=True):
    if rank[b] > K and cnt < M:
        cnt += 1
        ans += a
    elif rank[b] <= K:
        ans += a
print(ans)
