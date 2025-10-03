def backtrack(min_v, max_v, idx=0, cnt=1):
    global ans

    if (idx,min_v,max_v) in check: return
    check.add((idx,min_v,max_v))

    if cnt >= ans: return
    if max_v - min_v >= K:
        ans = min(ans,cnt)
        return
    
    if idx+2 < N: backtrack(min(min_v,arr[idx+2]), max(max_v,arr[idx+2]), idx+2, cnt+1)
    if idx+1 < N and (min_v > arr[idx+1] or max_v < arr[idx+1]):
        backtrack(min(min_v,arr[idx+1]), max(max_v,arr[idx+1]), idx+1, cnt+1)

check = set()
N,K = map(int,input().split())
arr = [*map(int,input().split())]
ans = N
if max(arr) - min(arr) >= K:
    backtrack(arr[0],arr[0])
print(ans)
