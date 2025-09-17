import sys; input = sys.stdin.readline
from heapq import heappop, heappush


arr = [[0] * 501 for _ in range(501)]
for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    x1,x2 = min(x1,x2), max(x1,x2)
    y1,y2 = min(y1,y2), max(y1,y2)

    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            arr[x][y] = 1

for _ in range(int(input())):
    x1,y1,x2,y2 = map(int,input().split())
    x1,x2 = min(x1,x2), max(x1,x2)
    y1,y2 = min(y1,y2), max(y1,y2)
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            arr[x][y] = -1

hq = [(0,0,0)]
distance = [[float('inf')] * 501 for _ in range(501)]
distance[0][0] = 0

while hq:
    dist_now, x,y = heappop(hq)
    
    if dist_now > distance[x][y]: continue

    for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
        nx,ny = x+dx, y+dy
        if 0 <= nx < 501 and 0 <= ny < 501:
            if arr[nx][ny] == -1: continue
            if distance[nx][ny] > dist_now + arr[nx][ny]:
                distance[nx][ny] = dist_now + arr[nx][ny]
                heappush(hq, (distance[nx][ny], nx, ny))
print(distance[500][500] if distance[500][500] != float('inf') else -1)
