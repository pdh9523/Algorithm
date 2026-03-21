def backtrack(idx=1, cnt=0, res=set()):
    global ans
    if idx == N+1:
        if len(res) == N:
            ans = min(ans, cnt)
        return

    if cnt >= ans: return

    backtrack(idx+1, cnt+1, res | graph[idx] | {idx})
    backtrack(idx+1, cnt, res)

for _ in range(int(input())):
    N = int(input())
    graph = [set() for _ in range(N+1)]
    for i in range(1,N+1):
        c, *arr = map(int,input().split())
        for a in arr:
            graph[i].add(a)
        
    ans = float('inf')
    backtrack()
    print(ans)
