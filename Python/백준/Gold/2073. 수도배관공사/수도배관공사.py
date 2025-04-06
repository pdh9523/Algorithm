import sys; input = sys.stdin.readline


def sol():
    D,P = map(int,input().split())
    arr = sorted([[*map(int,input().split())] for _ in range(P)], key=lambda x:-x[1])

    DP = [0] * (D+1)
    DP[0] = float('inf')
    for L,C in arr:
        for i in range(D, L-1, -1):
            if DP[i-L]:
                DP[i] = max(DP[i], min(DP[i-L], C)) 
            if DP[-1]: break
    print(DP[D])
sol()