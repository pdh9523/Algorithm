import sys; input = sys.stdin.readline


def solve():
    N = int(input())
    ans = 0
    if N == 1: return 1
    for i in 9,8,7,6,5,4,3,2:
        while N % i == 0:
            N //= i
            ans += 1
        if N == 1: break
    
    return ans if N == 1 else -1


for _ in range(int(input())):
    print(solve())