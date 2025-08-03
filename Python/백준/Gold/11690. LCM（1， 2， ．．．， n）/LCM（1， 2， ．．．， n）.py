def get_primes(num):
    if num < 2:
        return []
    sieve_size = (num + 1) // 2
    is_prime = bytearray([1] * sieve_size)
    is_prime[0] = 0
    
    limit = int(num ** 0.5)
    for i in range(1, (limit + 1) // 2):
        if is_prime[i]:
            p = 2 * i + 1
            start = 2 * i * (i + 1)
            is_prime[start::p] = bytearray([0] * len(is_prime[start::p]))
    
    res = [2] if num >= 2 else []
    for i in range(1, sieve_size):
        if is_prime[i]:
            res.append(2 * i + 1)
    
    return res

def get_log(base, num):
    if num == 0:
        return -1
    cnt = 0
    while num >= base:
        num //= base
        cnt += 1
    return cnt

N = int(input())
primes = get_primes(N)
ans = 1
for p in primes:
    ans = ans * p**get_log(p, N) % 2**32

print(ans)