import sys; input = sys.stdin.readline


arr = dict()
for _ in range(int(input())):
    a,b = map(int,input().split())

    arr[a] = arr.get(a, 0) + 1
    if arr[a] == 0: arr.pop(a)
    arr[b] = arr.get(b, 0) - 1
    if arr[b] == 0: arr.pop(b)

ans = 0
now = 0
check = False
start, end = -1, -1
for k in sorted(arr):
    v = arr[k]
    now += v

    if now > ans:
        ans = now
        if v > 0:
            start = k
        check = True
    if check and v < 0:
        check = False
        end = k

print(ans)
print(start, end)