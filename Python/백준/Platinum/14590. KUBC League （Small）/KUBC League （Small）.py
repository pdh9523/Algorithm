def tsp(now=0, visit=1, route=[1]):
    global ans
    if len(ans) == N:
        return
    if len(route) > len(ans):
        ans = route
    
    if visit == (1<<N)-1:
        return

    if (now, visit) in DP: return
    DP[(now, visit)] = True

    for nxt in range(N):
        if visit & (1<<nxt): continue
        if not arr[now][nxt]: continue

        tsp(nxt, visit | (1<<nxt), route + [nxt+1])

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]
ans = []
DP = dict()
tsp()
print(len(ans))
print(*ans)