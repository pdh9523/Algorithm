from collections import deque
from heapq import heappop, heappush
dx,dy = [1,0,-1,0], [0,1,0,-1]

N,M = map(int,input().split())  # N 세로 M 가로
islands = [list(map(int,input().split())) for _ in range(N)]

# bfs로 섬 위치 저장
island = []
visit = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if islands[i][j] == 1 and not visit[i][j]:
            q = deque([(i,j)])
            visit[i][j] = 1
            tmp = [(i,j)]
            while q :
                x,y = q.popleft()
                for dt in range(4):
                    di = x + dx[dt]
                    dj = y + dy[dt]
                    if 0 <= di < N and 0 <= dj < M and not visit[di][dj] and islands[di][dj] == 1:
                        visit[di][dj] = 1
                        q.append((di,dj))
                        tmp.append((di,dj))
            island.append(tmp)

# print(island)

# 각 섬에 대해서 다리를 만들었을 때의 길이 구현 (길이는 2 이상이다.)
length = len(island)

graph = [set() for _ in range(length)]

# islands : 큰 2차원 리스트
# island : 각각 섬 좌표를 담아 둔 리스트

for a in range(length):
    for x,y in island[a]:
        for dt in range(4):
            di = x + dx[dt]
            dj = y + dy[dt]
            cnt = 0
            while 0 <= di < N and 0 <= dj < M and not islands[di][dj] :
                cnt += 1
                di += dx[dt]
                dj += dy[dt]
            if cnt>1 and  0 <= di < N and 0 <= dj < M and islands[di][dj]:
                for b in range(length):
                    if (di,dj) in island[b] :
                        graph[a].add((b,cnt))
                        graph[b].add((a,cnt))
                

# 최소 스패닝 트리

start = 0 
hq =[(0,(start))]

visit = [False] * length
ans = 0
while hq :
    dist_now, now = heappop(hq)

    if not visit[now]:
        visit[now] = True
        ans += dist_now
        for next,cost in graph[now] :
            heappush(hq, (cost,next))
        
if all(visit) :
    print(ans)
else :
    print(-1)