N = int(input())

grundy = [0] * (N+1)
for i in range(2, N+1):
    next_grundy_nums = {
        grundy[j] ^ grundy[i-j-2] for j in range(i//2)
    }
    grundy[i] = next(x for x in range(N) if x not in next_grundy_nums)

print(1 if grundy[N] else 2)
