import sys; input = sys.stdin.readline


def parse(num):
    return num//M, num%M

def backtrack(idx=0, res=0):
    global ans
    if idx == N*M:
        ans = max(ans, res)
        return
    
    x,y = parse(idx)

    backtrack(idx+1, res)
    for dr in drs:
        for dx,dy in dr:
            nx,ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny]: break
            else:
                break
        else:
            tmp = arr[x][y]
            for dx,dy in dr:
                nx,ny = x+dx, y+dy
                tmp += arr[nx][ny]
                visit[nx][ny] = arr[nx][ny]
                arr[nx][ny] = 0
                
            backtrack(idx+1, res+tmp)
            for dx,dy in dr:
                nx,ny = x+dx, y+dy
                arr[nx][ny] = visit[nx][ny]
                visit[nx][ny] = 0
    

drs = ((0,0),(0,-1),(1,0)), ((0,0),(-1,0),(0,-1)), ((0,0),(-1,0),(0,1)), ((0,0),(0,1),(1,0))

N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

visit = [[0]*M for _ in range(N)]
ans = 0
backtrack()
print(ans)