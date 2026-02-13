import sys; input = sys.stdin.readline

def calc(x, n):
    if n == 1: return x % DIV
    
    h = calc(x, n//2)

    if n % 2:
        return h**2 * x % DIV
    return h**2 % DIV

def get_factorial():
    res = [1] * SIZE

    for i in range(2, SIZE):
        res[i] = res[i-1] * i % DIV
    return res

SIZE = 4000001
DIV = 1000000007

fac = get_factorial()

N = int(input())
for _ in range(N):
    a,p = map(int,input().split())
    print(fac[a] * calc(fac[p] * fac[a-p], DIV-2) % DIV)
