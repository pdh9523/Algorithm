def check(num):
    cnt = M
    for i in range(M):
        cnt += num // arr[i]
    return cnt >= N

N,M = map(int,input().split())
arr = [*map(int,input().split())]
if N<M: exit(print(N))

left, right = 0, 100000000000
ans = 0
while left <= right:
    mid = (left+right) // 2
    if check(mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

cnt = M + sum((ans-1) // arr[i] for i in range(M))
for i in range(M):
    if ans % arr[i] == 0:
        cnt += 1
        if cnt == N: exit(print(i+1))