N = int(input())
if N == 1: exit(print(1))
arr = [*map(int,input().split())]
res = [0] * (N-1)
for i in range(N-1):
    comp = arr[i] - arr[i+1]

    if comp > 0:
        if i > 0 and res[i-1] > 0:
            res[i] = res[i-1] + 1
        else:
            res[i] = 1
    elif comp < 0:
        if i > 0 and res[i-1] < 0:
            res[i] = res[i-1] - 1
        else:
            res[i] = -1
    else:
        res[i] = res[i-1]

print(max(abs(x) + 1 for x in res))
