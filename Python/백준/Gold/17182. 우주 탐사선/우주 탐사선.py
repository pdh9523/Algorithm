import sys; sys.setrecursionlimit(10**6)


def backtrack(visit, now, value=0):
    global ans
    
    if value > ans:
        return
    
    if check.get((visit,now), float('inf')) <= value:
        return
    
    check[(visit,now)] = value
    if visit == (1<<N)-1:
        ans = min(ans, value)
        return

    for nxt in range(N):
        if now==nxt: continue
        backtrack(visit | (1<<nxt), nxt, value + arr[now][nxt])

N,K = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]
check = dict()
ans = sum(sum(a) for a in arr)
backtrack(1<<K, K)
print(ans)