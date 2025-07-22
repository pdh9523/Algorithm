import sys; input = sys.stdin.readline


N,M = map(int,input().split())
K = int(input())

cnt = [0] * (N+1)
ans = []
seq = 1
for i in range(1,M+1):
    a,b = map(int,input().split())
    if b == 1:
        if cnt[a] == -1:
            cnt[a] = 0
        else:
            cnt[a] = seq
    else:
        if cnt[a] > 0 and cnt[a] + K <= seq:
            ans.append(a)
        cnt[a] = -1
        seq += 1

for i in range(1,N+1):
    if 0 < cnt[i] <= seq - K:
        ans.append(i)
if ans:
    print(*sorted(ans), sep="\n")
else:
    print(-1)