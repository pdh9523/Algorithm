N,M,K = map(int,input().split())
arr = iter(sorted(enumerate(map(int,input().split()), start=1), key=lambda x: x[1]))

ans = [-1] * K

idx,cnt = next(arr)
for i in range(K):
    cnt -= 1
    if cnt == 0: 
        ans[i] = idx
        idx,cnt = next(arr, (-1,-1))
    elif M:
        ans[i] = 0
        M -= 1
    else:
        break

print(" ".join(map(str,ans)) if ans[-1] != -1 else -1)