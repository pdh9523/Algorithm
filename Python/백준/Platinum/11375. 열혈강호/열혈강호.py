import sys; input = sys.stdin.readline
from collections import deque


MAX_VALUE = float('inf')

def bfs():
    q = deque()
    for i in range(1,N+1):                                          # 전체 노드 중
        if pair_a[i]:                                               # 매칭되어 있다면
            distance[i] = MAX_VALUE                                 # 갱신이 안되도록 처리
        else:
            distance[i] = 0                                         # 매칭이 안된 경우 거리 배열의 값을 초기화 하고 큐에 담음
            q.append(i)
    distance[0] = MAX_VALUE                                         # 가상 싱크 노드도 최대값으로 처리

    while q:
        now = q.popleft()                                           # q를 탐색하면서

        if distance[now] < distance[0]:                             # 현재 노드에 저장된 거리가 최단거리 이내인 경우 (0번에는 최단거리가 담기게 된다)
            for nxt in graph[now]:                                  
                if distance[pair_b[nxt]] == MAX_VALUE:              # 순회하면서, 방문하지 않았다면
                    distance[pair_b[nxt]] = distance[now] + 1       # 방문 체크
                    q.append(pair_b[nxt])
    return distance[0] != MAX_VALUE

def dfs(now):
    if now:
        for nxt in graph[now]:
            if distance[pair_b[nxt]] == distance[now] + 1 and dfs(pair_b[nxt]):             # 거리가 확인되고, 서로 dfs로 접근이 가능한 경우 
                pair_a[now] = nxt                                                           # 매칭
                pair_b[nxt] = now
                return True
        distance[now] = float('inf')                                                        # 그런 경우들이 없다면 방문 처리 해제
        return False
    
    return True                                                                             # 0으로 빠진 경우 매칭이 가능하다는 뜻

N,M = map(int,input().split())

graph = [[]]
for _ in range(N):
    num, *jobs = map(int,input().split())
    graph.append(jobs)

pair_a = [0] * (N+1)
pair_b = [0] * (M+1)
distance = [0] * (N+1)


ans = 0
while bfs():                            # 갈 수 있는 경로가 있다면
    for i in range(1,N+1):
        if not pair_a[i] and dfs(i):    # 현재 직원에 매칭된 일이 없고, 매칭시킬 수 있는 일이 있다면
            ans += 1                    # 매칭 (매칭은 dfs 함수에서 갱신)
print(ans)