def factorial(N):
    num = 1
    for i in range(2, N+1):
        num = (num*i) % MOD
    return num

def square(num, k):
    if k == 0:
        return 1
    elif k == 1:
        return num
    
    tmp = square(num, k//2)
    if k % 2:
        return tmp * tmp * num % MOD
    else:
        return tmp * tmp % MOD

N,K = map(int,input().split())
MOD = 1000000007

top = factorial(N)
bot = factorial(N-K) * factorial(K) % MOD

print(top * square(bot, MOD-2) % MOD)