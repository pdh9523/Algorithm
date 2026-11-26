import sys; input = sys.stdin.readline; sys.setrecursionlimit(10**6)

def calc(fail=0, idx=0, combo=0):
    if visit[fail][idx][combo]:
        return DP[fail][idx][combo]

    visit[fail][idx][combo] = True

    if idx == N:
        return 0

    DP[fail][idx][combo] = calc(0, idx+1, combo+1) + (combo+1) * arr[idx]
    if fail < 2:
        DP[fail][idx][combo] = max(DP[fail][idx][combo], calc(fail+1, idx+1, 0))
    return DP[fail][idx][combo]

N = int(input())
arr = [*map(int,input().split())]

DP = [[[0]*(N+1) for _ in range(N+1)] for _ in range(3)]
visit = [[[False]*(N+1) for _ in range(N+1)] for _ in range(3)]

print(max(0, calc()))
