import sys; input = sys.stdin.readline

def solve():
    DP = [float('inf')] * 100001
    DP[0] = 0    
    N = int(input())
    arr = [[*map(int,input().split())] for _ in range(N)]

    total = 0
    for a,b in arr:
        total += a

        for i in range(total, -1, -1):
            if i >= a:
                DP[i] = min(DP[i-a], DP[i] + b)
            else: DP[i] += b
    print(min(max(i, DP[i]) for i in range(100001)))

for _ in range(int(input())):
    solve()
