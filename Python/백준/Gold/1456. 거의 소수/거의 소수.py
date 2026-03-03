from bisect import bisect_right

def get_primes(max_v):
    size = int(max_v ** 0.5) + 1

    res = [True] * (size + 1)

    for i in range(2, int(size ** 0.5) + 1):
        if res[i]:
            for j in range(i**2, size+1, i):
                res[j] = False

    primes = []
    for p in range(2, size + 1):
        if res[p]:
            x = p * p
            while x <= max_v:
                primes.append(x)
                x *= p

    primes.sort()
    return primes

A, B = map(int, input().split())
primes = get_primes(B)

print(bisect_right(primes, B) - bisect_right(primes, A - 1))
