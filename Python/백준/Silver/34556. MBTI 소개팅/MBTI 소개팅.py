def backtrack(value=0,visit=0):
    global ans
    
    if visit == (1 << (N*2)) - 1:
        ans = max(ans,value)
        return
    
    if data.get(visit, -1) >= value: return
    data[visit] = value

    for i in range(N):
        if (1<<i) & visit: continue
        for j in range(N,N*2):
            if (1<<j) & visit: continue
            res = 0
            for a,b in zip(arr[i],arr[j]):
                if a!=b: res+=1
            backtrack(value+res, visit | 1<<i | 1<<j)

N = int(input())
arr = [input() for _ in range(N*2)]
data = dict()
ans = 0
backtrack()
print(ans)