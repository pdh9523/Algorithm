                                                                            
N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            ans += 2

for i in range(N):
    prev = 0
    for j in range(M):
        ans += abs(arr[i][j] - prev)
        prev = arr[i][j]
    ans += prev

for j in range(M):
    prev = 0
    for i in range(N):
        ans += abs(arr[i][j] - prev)
        prev = arr[i][j]
    ans += prev
print(ans)