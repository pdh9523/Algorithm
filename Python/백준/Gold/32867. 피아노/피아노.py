N,K = map(int,input().split())
arr = iter(map(int,input().split()))

ans = 0
min_v = max_v = next(arr)
for a in arr:
    min_v = min(min_v, a)
    max_v = max(max_v, a)

    if max_v - min_v >= K:
        ans += 1
        min_v = max_v = a

print(ans)