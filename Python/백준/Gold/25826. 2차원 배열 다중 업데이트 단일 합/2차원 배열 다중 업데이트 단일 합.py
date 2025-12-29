import sys; input = sys.stdin.readline


def add(x1,y1, x2,y2, n):
    prefix_sum[x1+1][y1+1] += n
    prefix_sum[x2+2][y2+2] += n
    prefix_sum[x2+2][y1+1] -= n
    prefix_sum[x1+1][y2+2] -= n

def sout(x1,y1, x2,y2):
    
    for i in range(1,N+1):
        for j in range(1,N+1):
            prefix_sum[i][j] += prefix_sum[i][j-1]

    for i in range(1,N+1):
        for j in range(1,N+1):
            prefix_sum[i][j] += prefix_sum[i-1][j]
    
    res = 0
    for i in range(x1+1,x2+2):
        for j in range(y1+1,y2+2):
            res += arr[i-1][j-1]
            res += prefix_sum[i][j]
    print(res)

N,Q = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]
prefix_sum = [[0] * (N+2) for _ in range(N+2)]

cmd = {
    1: add,
    2: sout
}
for _ in range(Q):
    c, *q = map(int,input().split())
    cmd[c](*q)
