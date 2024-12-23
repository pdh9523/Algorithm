'''
puyo puyo

BFS, 구현

BFS를 통해 4개 이상 모여있는 블럭을 찾고, 
한 번의 연쇄 후에 gravity 함수를 통해 블럭을 재정렬
최대 연쇄 수를 cnt에 담아 출력
'''

from collections import deque


def gravity():
    for j in range(M):
        for i in range(N-2, -1, -1):
            x,y = i,j
            while x != N-1:
                if arr[x+1][y] == ".":
                    arr[x+1][y], arr[x][y] = arr[x][y], arr[x+1][y]
                x += 1

def bfs(i,j):
    block = arr[i][j]
    
    q = deque([(i,j)])
    tmp = [(i,j)]
    visit = [[False]*M for _ in range(N)]
    visit[i][j] = True
    while q:
        x,y = q.popleft()
        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0<=di<N and 0<=dj<M and not visit[di][dj]:
                if arr[di][dj] == block:
                    tmp.append((di,dj))
                    visit[di][dj] = True
                    q.append((di,dj))
        
    if len(tmp) >= 4:
        for i,j in tmp:
            arr[i][j] = "."
        return True
    return False

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = 12,6
arr = [list(input()) for _ in range(N)]

check = True
cnt = 0
while check:
    check = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == ".": continue

            if bfs(i,j): check = True
    gravity()
    if check: cnt += 1

print(cnt)