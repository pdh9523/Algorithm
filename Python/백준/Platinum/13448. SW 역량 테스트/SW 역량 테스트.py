import sys; input = sys.stdin.readline


N,T = map(int,input().split())
arr = sorted(
    [x for x in zip(*[map(int,input().split()) for _ in range(3)])], 
    key=lambda x: x[2]/x[1]
    )

DP = [0] * (T+1)
for m,p,r in arr:
    for t in range(T, -1, -1):
        if t-r < 0: continue
        DP[t] = max(DP[t], DP[t-r] + (m-(t*p)))

print(max(DP))