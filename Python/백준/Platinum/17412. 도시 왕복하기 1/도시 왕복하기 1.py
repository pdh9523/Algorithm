'''
도시 왕복하기 1

최대 유량

최대 유량 알고리즘은 네트워크에서 한 노드에서 다른 노드로 보낼 수 있는 최대 유량을 계산한다.
네트워크는 노드와 간선으로 구성되며, 각 간선에는 용량이 할당된다.
현재 문제는 간선의 용량이 모두 1인 경우를 상정하고 있다.
# soruce: 출발점
# sink: 도착점
'''
import sys; input = sys.stdin.readline
from collections import deque


def bfs(source, sink, visit):
    # 출발점 설정
    q = deque([source])

    while q:
        # 도착점에 방문한 상황이면 탈출
        if visit[sink] != -1: break

        now = q.popleft()

        for nxt in graph[now]:
            # 현재 가용 유량을 계산하고
            leftover_flow = capacity[now][nxt] - flow[now][nxt]
            # 방문 하지 않았고, 이 간선에 유량이 남아 있다면
            if visit[nxt] == -1 and leftover_flow > 0:
                # 방문 표시 후 q에 추가
                visit[nxt] = now
                q.append(nxt)
    # 도착지에 방문 했는지 여부를 반환
    return visit[sink] != -1
    

def edmonds_karp(source, sink):
    ans = 0
    
    while True:
        visit = [-1] * (N+1)
        # 종료 조건: 현재 네트워크에서 더 이상 도착지에 방문할 수 없는 경우
        if not bfs(source, sink, visit): break
        
        # 도착지를 j로 두고 출발지에 닿을 때까지 역추적 진행
        j = sink
        while j != source:  # visit 배열의 역추적을 통해 유량 갱신
            i = visit[j]    # 이전 노드 추적
            flow[i][j] += 1 # 순방향 유량 증가
            flow[j][i] -= 1 # 역방향 유량 감소
            j = i           # 다음 노드 이동
        
        ans += 1
    return ans


N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]

capacity = [[0]*(N+1) for _ in range(N+1)]
flow = [[0]*(N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    capacity[a][b] = 1

print(edmonds_karp(1,2))