def gcd(a,b):
    if b == 0: 
        return a
    return gcd(b, a%b)

N,M = map(int,input().split())

x = M // N
for i in range(int(x**0.5) + 1, 0, -1):
    if x % i == 0 and gcd(i, x//i) == 1:
            exit(print(*sorted((i * N, x//i * N))))
