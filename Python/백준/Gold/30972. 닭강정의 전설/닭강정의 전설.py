import sys; input = sys.stdin.readline


def set_prefix_sum(arr):
    res = [[0] * (N+1) for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,N+1):
            res[i][j] = res[i][j-1] + res[i-1][j] - res[i-1][j-1] + arr[i-1][j-1]

    return res

def get_prefix_sum(sx,sy,ex,ey):
    return prefix_sum[ex][ey] - prefix_sum[sx-1][ey] - prefix_sum[ex][sy-1] + prefix_sum[sx-1][sy-1]

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]

prefix_sum = set_prefix_sum(arr)
for _ in range(int(input())):
    r1,c1,r2,c2 = map(int,input().split())
    print(2*get_prefix_sum(r1+1,c1+1,r2-1,c2-1)-get_prefix_sum(r1,c1,r2,c2))
