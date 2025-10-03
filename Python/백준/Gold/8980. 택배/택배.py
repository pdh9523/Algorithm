import sys; input = sys.stdin.readline


N,K = map(int,input().split())
arr = sorted([[*map(int,input().split())] for _ in range(int(input()))], key=lambda x:x[1])

capacity = [K] * N
ans = 0
for a,b,c in arr:
    weight = K
    for i in range(a,b):
        weight = min(capacity[i], weight, c)
    for i in range(a,b):
        capacity[i] -= weight
    ans += weight
print(ans)