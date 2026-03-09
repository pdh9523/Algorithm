import sys; input = sys.stdin.readline

def get_distance(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve():
    N,M = map(int,input().split())
    arr = [tuple(map(int,input().split())) for _ in range(N)]

    DP = [[float('inf')]*(M+1) for _ in range(N)]
    for i in range(M+1):
        DP[0][i] = 0

    for i in range(1,N):
        for j in range(M+1):
            if i < j: break
            
            for k in range(j, M+1):
                DP[i][k] = min(DP[i][k], DP[i-j-1][k-j] + get_distance(arr[i], arr[i-j-1]))

    print(DP[N-1][M])

if __name__ == "__main__":
    solve()