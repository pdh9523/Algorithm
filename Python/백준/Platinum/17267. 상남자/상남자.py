import sys; input = sys.stdin.readline
from collections import deque


dy = [0,0,-1,1]; dx = [-1,1,0,0]

def BFS(n,d):
  visited = [[0]*M for i in range(N)]
  dq = deque([(sy,sx,0)])
  while dq:
    y,x,cnt = dq.popleft()
    if visited[y][x]:
      continue
    visited[y][x] = 1
    for i in range(4):
      y1,x1 = y+dy[i],x+dx[i]
      if N>y1>=0 and M>x1>=0 and not visited[y1][x1]|board[y1][x1]:
        if i==d:
          if cnt < n:
            dq.append((y1,x1,cnt+1))
        else:
          dq.appendleft((y1,x1,cnt))
  return visited
      
N,M = map(int,input().split())
L,R = map(int,input().split())

board = [[*map(int,input().strip())] for i in range(N)]

for i in range(N):
  for j in range(M):
    if board[i][j]==2:
      sy,sx = i,j; board[i][j] = 0

visitedL = BFS(L,0); visitedR = BFS(R,1)
print(sum([visitedL[i][j]&visitedR[i][j] for i in range(N) for j in range(M)]))