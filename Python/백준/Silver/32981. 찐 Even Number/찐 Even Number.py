import sys; input = sys.stdin.readline


def div_conq(num):
    if num == 0: return 1
    if num == 1: return 5

    if num % 2:
        return div_conq(num//2)**2 * 5 % MOD
    return div_conq(num//2) ** 2 % MOD


MOD = 10**9+7
for _ in range(int(input())):
    N = int(input())
    if N == 1: 
        print(5)
        continue
    print(4*div_conq(N-1)%MOD)