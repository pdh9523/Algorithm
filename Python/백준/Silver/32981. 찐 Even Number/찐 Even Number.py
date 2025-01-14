import sys; input = sys.stdin.readline


def memo(f):
    cache = dict()
    def wrapper(*args):
        if args not in cache:
            cache[args] = f(*args) % MOD
        return cache[args]
    return wrapper

@memo
def div_conq(num):
    if num == 0: return 1
    if num == 1: return 5

    if num % 2:
        half = div_conq(num//2)
        odd = div_conq(num//2+1)
        return half * odd

    half = div_conq(num//2)
    return half * half


MOD = 10**9+7
for _ in range(int(input())):
    N = int(input())
    if N == 1: 
        print(5)
        continue
    print(4*div_conq(N-1)%MOD)