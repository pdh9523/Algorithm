def get_primes(size):
    primes = [True] * (size+1)

    for i in range(2,size+1):
        if primes[i]:
            for j in range(i*2, size+1, i):
                primes[j] = False
    return [i for i in range(2,size+1) if primes[i]]

N = int(input())
primes = get_primes(N)

DP = [0]*(N+1)
DP[0] = 1
for p in primes:
    for i in range(p, N+1):
        DP[i] = (DP[i-p] + DP[i]) % 123456789

print(DP[N])
