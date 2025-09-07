def calc(arr):
    arr = [0]+arr
    
    for i in range(1,N+1):
        if arr[i] == i:
            continue
        idx = arr.index(i)
        
        arr = arr[:i] + arr[i:idx+1][::-1] + arr[idx+1:]
        ans.append((i,idx))
    if len(ans) == 0: ans.append((1,1))
    if len(ans) == 1: 
        ans.append((N,N))

def calc_reversed(arr):
    arr = [0] + arr

    for i in range(N, 0, -1):
        if arr[i] == i: continue
        idx = arr.index(i)
        arr = arr[:idx] + arr[idx:i+1][::-1] + arr[i+1:]
        ans.append((idx,i))
    if len(ans) == 0: ans.append((1,1))
    if len(ans) == 1: 
        ans.append((N,N))

N = int(input())
arr = [*map(int,input().split())]
ans = []
calc(arr)
if len(ans) > 2:
    ans = [(1,N)]
    calc(arr[::-1])
if len(ans) > 2:
    ans = []
    calc_reversed(arr)
for a in ans: print(*a)