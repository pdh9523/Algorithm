import sys; input = sys.stdin.readline
import heapq


class BMSSP:
    def __init__(self, N):
        self.N = N
        self.graph = [[] for _ in range(N+1)]
    
    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def bounded_explore(self, sources, bound, dist):
        """
        Bound 내에서 탐색하고 frontier 반환
        핵심: bound를 넘는 노드들을 frontier로 수집
        """
        pq = []
        local_dist = {}
        visited = set()
        frontier = []
        
        # 소스들 초기화
        for s in sources:
            if dist[s] < bound:
                heapq.heappush(pq, (dist[s], s))
                local_dist[s] = dist[s]
        
        while pq:
            d, u = heapq.heappop(pq)
            
            if u in visited or d >= bound:
                continue
                
            visited.add(u)
            
            for v, w in self.graph[u]:
                new_dist = d + w
                
                if new_dist < bound:
                    # Bound 내부: 계속 탐색
                    if v not in visited and (v not in local_dist or new_dist < local_dist[v]):
                        local_dist[v] = new_dist
                        heapq.heappush(pq, (new_dist, v))
                        if new_dist < dist[v]:
                            dist[v] = new_dist
                else:
                    # Bound 경계: frontier에 추가
                    if new_dist < dist[v]:
                        frontier.append((v, new_dist))
        
        return frontier
    
    def bmssp_recursive(self, sources, bound, dist, depth=0):
        """
        재귀적 BMSSP 구현
        1. Bounded exploration
        2. Frontier 수집
        3. Frontier에서 재귀 호출
        """
        if bound <= 0 or depth > 10:  # 재귀 깊이 제한
            return
        
        # Phase 1: Bounded 탐색
        frontier = self.bounded_explore(sources, bound, dist)
        
        if not frontier:
            return
        
        # Phase 2: Frontier 노드들을 그룹화하여 재귀 호출
        # 거리별로 정렬하여 가까운 것부터 처리
        frontier.sort(key=lambda x: x[1])
        
        # 같은 거리의 노드들을 묶어서 처리 (효율성)
        current_dist = -1
        batch = []
        
        for node, dist in frontier:
            if dist != current_dist:
                if batch:
                    # 이전 배치 처리
                    remaining = bound - current_dist
                    if remaining > 0:
                        self.bmssp_recursive(batch, remaining, dist, depth + 1)
                batch = []
                current_dist = dist
            
            if dist < dist[node]:
                dist[node] = dist
                batch.append(node)
        
        # 마지막 배치 처리
        if batch:
            remaining = bound - current_dist
            if remaining > 0:
                self.bmssp_recursive(batch, remaining, depth + 1)
    
    def solve(self, sources, bound=float('inf')):
        """
        BMSSP 실행
        """
        dist = [float('inf')] * (self.N+1)
        # 소스 노드들 초기화
        for s in sources:
            dist[s] = 0
        
        # 재귀적 BMSSP 실행
        self.bmssp_recursive(sources, bound, dist)
        
        # 결과 반환
        return dist


N,M = map(int,input().split())

bmssp = BMSSP(N)
for _ in range(M):
    a,b,c = map(int,input().split())
    bmssp.add_edge(a,b,c)

a,b = map(int,input().split())
dist = bmssp.solve([1])
dist_a = bmssp.solve([a])
dist_b = bmssp.solve([b])

print(-1 if (tmp:=min(dist[a] + dist_a[b] + dist_b[N], dist[b] + dist_b[a] + dist_a[N])) == float('inf') else tmp)