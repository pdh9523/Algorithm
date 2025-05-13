'''
N번 까지의 피보나치 수의 누적합은
N+1 번째 피보나치 수 - 1이다 
'''
def fibonacci(n):
    if n in DP: return DP[n]

    half = n//2

    if n%2:
        left = fibonacci(half)
        right = fibonacci(half+1)
        DP[n] = (left**2 + right**2)%MOD
        return DP[n]
    else :
        left = fibonacci(half-1)
        right = fibonacci(half)
        DP[n] = ((2*left+right)*right)%MOD
        return DP[n]
    
MOD = 1000000000
DP = dict()
DP[1], DP[2] = 1, 1

N,M = map(int,input().split())
ans = (fibonacci(M+2) - fibonacci(N+1))
print(ans % MOD)