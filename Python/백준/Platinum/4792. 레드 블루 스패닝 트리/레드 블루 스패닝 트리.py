import sys; input = lambda: sys.stdin.readline().strip()


class DisjointSet:
    def __init__(self, size):
        self._parent = [-1] * size

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return True
        if self._parent[root_x] > self._parent[root_y]:
            root_x, root_y = root_y, root_x
        self._parent[root_x] += self._parent[root_y]
        self._parent[root_y] = root_x
        return False

    def find(self, x):
        while (p := self._parent[x]) >= 0:
            x, self._parent[x] = p, self._parent[p]
        return x

def mst(size, main, sub):
    dsu = DisjointSet(size)
    res = 0
    for edges, cost in (main, 0), (sub, 1):
        for u,v in edges:
            if dsu.union(u,v):
                continue
            res += cost
            size -= 1
            if size == 1:
                return res

while (tmp:=input())!="0 0 0":
    N,M,K = map(int, tmp.split())

    blues = []
    reds = []

    for _ in range(M):
        a,b,c = input().split()
        b,c = map(lambda x: int(x)-1, (b,c))
        if a == "B": blues.append((b,c))
        else: reds.append((b,c))

    min_blue_cnt = mst(N, reds, blues)
    min_red_cnt = mst(N, blues, reds)
    max_blue_cnt = N-1-min_red_cnt
    
    print(1 if min_blue_cnt <= K <= max_blue_cnt else 0)