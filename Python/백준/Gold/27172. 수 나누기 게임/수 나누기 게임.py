N = int(input())
arr = [*map(int,input().split())]
s = set(arr)
max_v = max(arr)

ans = [0] * (max_v+1)
for a in arr:
    for x in range(2*a, max_v+1, a):
        if x in s:
            ans[a] += 1
            ans[x] -= 1

print(*(ans[a] for a in arr))