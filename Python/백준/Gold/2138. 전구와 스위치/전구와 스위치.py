def change(arr, idx):
    if idx > 0: arr[idx-1] = 1-arr[idx-1]
    arr[idx] = 1-arr[idx]
    if idx < N-1: arr[idx+1] = 1-arr[idx+1]

N = int(input())
a = [*map(int, list(input()))]
brr = [*map(int, list(input()))]

a1 = a[:]
a2 = a[:]

change(a2, 0)
ans = float('inf')
for x, arr in enumerate((a1, a2)):
    cnt = x
    for i in range(1, N):
        if arr[i-1] != brr[i-1]:
            change(arr, i)
            cnt += 1
    if arr == brr: ans = min(ans, cnt)
print(ans if ans != float('inf') else -1)
