import sys; sys.setrecursionlimit(10**6)


def josephus(n,k):
    def _josephus(n):
        if n == 1: return 0
        if k > n:
            return (_josephus(n-1)+k) % n
        res = _josephus(n - n//k) - n%k
        return res + (n if res < 0 else res // (k-1))
    return n if k == 1 else _josephus(n) + 1

print(josephus(*map(int,input().split())))
