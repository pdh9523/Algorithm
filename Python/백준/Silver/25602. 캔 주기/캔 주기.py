def backtrack(check, i=0, value=0):
    global ans
    if i >= M:
        ans = max(ans, value)
        return
    
    for j in range(N):
        for k in range(N):
            if check[j] >= cans[j] or check[k] >= cans[k]: continue
            if j==k and check[j] + 1 >= cans[j]: continue

            check[j] += 1
            check[k] += 1
            backtrack(check, i+1, value+arr[i][j]+brr[i][k])
            check[j] -= 1
            check[k] -= 1

N,M = map(int,input().split())
cans = [*map(int,input().split())]
arr = [[*map(int,input().split())] for _ in range(M)]
brr = [[*map(int,input().split())] for _ in range(M)]

ans = 0
check = [0]*N
backtrack(check)
print(ans)