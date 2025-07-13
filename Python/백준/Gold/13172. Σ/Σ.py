import sys; input = sys.stdin.readline


MOD = 10**9+7

def calc(N,M):
    if M == 1: return N
    
    res = calc(N, M//2)
    if M % 2:
        return res*res*N%MOD
    return res*res%MOD

ans = 0
for _ in range(int(input())):
    N,M = map(int,input().split())

    ans += calc(N,MOD-2)*M
    ans %= MOD
print(ans)