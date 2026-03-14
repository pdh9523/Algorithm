import sys; input = sys.stdin.readline

def get_prime(SIZE: int) -> list[int]:
    res = [True] * (SIZE+1)

    for now in range(2, int(SIZE**0.5)+1):
        if res[now]:
            for nxt in range(now**2, SIZE+1, now):
                res[nxt] = False
    return [x for x in range(2, SIZE+1) if res[x]]

def find(num):
    for i in range(length):
        for j in range(i,length):
            for k in range(j,length):
                if primes[i] + primes[j] + primes[k] == num:
                    return primes[i],primes[j],primes[k]
    
SIZE = 1000
primes = get_prime(SIZE)
length = len(primes)

for _ in range(int(input())):
    print(*find(int(input())))
