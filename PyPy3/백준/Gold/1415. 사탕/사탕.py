import sys; input = sys.stdin.readline


SIZE = 500000
def get_primes():
    is_prime = [True] * (SIZE+1)

    for i in range(2, SIZE+1):
        if is_prime[i]:
            for j in range(i*2, SIZE+1, i):
                is_prime[j] = False
    return set(x for x in range(2,SIZE+1) if is_prime[x])

zero = 0
counter = dict()
for _ in range(int(input())):
    x = int(input())
    if x == 0:
        zero += 1
        continue
    counter[x] = counter.get(x, 0) + 1

DP = dict()
DP[0] = 1
for k,v in counter.items():
    tmp = dict()
    for m in range(1,v+1):
        x = k * m
        for kk in DP:
            tmp[kk+x] = tmp.get(kk+x,0)+DP.get(kk)

    for k,v, in tmp.items():
        DP[k] = DP.get(k,0)+v

ans = sum(DP.get(p,0) for p in get_primes())
print(ans * (zero + 1))