N = int(input())
arr = sorted(enumerate(map(int,input().split()), start=1), key = lambda x: -x[1])

min_v = float('inf')
max_v = 0
sum_v = 0
now = 0
ans = 0
for i, t in enumerate(arr):
    idx, value = t
    min_v = min(min_v, value)
    max_v = max(max_v, value)
    sum_v += value

    if min_v+max_v+sum_v > now:
        now = min_v+max_v+sum_v
        ans = i

print(ans+1)
for i in range(ans+1):
    print(arr[i][0], end=" ")

