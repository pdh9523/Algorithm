def calc(N):
    res = 0
    k = 1

    while (1 << (k-1)) <= N:
        count = (N >> (k-1)) - (N >> k)
        res += k * count
        k += 1
    return res

print(calc(int(input())))