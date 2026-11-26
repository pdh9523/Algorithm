import sys; input = sys.stdin.readline


N,K = map(int,input().split())

DP = [-float('inf')] * (K+1)
DP[0] = 0

for i in range(N):
    ax,ay, bx,by = map(int,input().split())
    tmp = [-float('inf')] * (K+1)
    for x,y in (ax,ay), (bx,by):
        for j in range(K+1-x):
            tmp[j+x] = max(tmp[j+x], DP[j] + y)
    DP = tmp[:]
print(max(DP))