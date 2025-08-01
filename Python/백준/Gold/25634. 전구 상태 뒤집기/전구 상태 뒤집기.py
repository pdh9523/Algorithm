N = int(input())
arr = [x for x in zip(map(int,input().split()), map(int,input().split()))]

on,off,max_v = 0,0,-float('inf')
for i in range(N):
    x, is_on = arr[i]

    if is_on:
        on += x
        off = max(off-x, 0)
        max_v = max(max_v, -1*x)
    else:
        off += x
        max_v = max(max_v, off)

print(on+max_v)
