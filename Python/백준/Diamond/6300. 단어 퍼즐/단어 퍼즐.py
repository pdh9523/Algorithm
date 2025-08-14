import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


class Node:
    def __init__(self,key=""):
        self.key = key
        self.children = dict()
        self.is_end = False
        self.fail = None


class AhoCorasick:
    def __init__(self, patterns):
        self.root = Node()
        for pattern in patterns:
            self.insert(pattern)
        self.connect()
    
    def insert(self, pattern):
        now = self.root

        for char in pattern:
            now = now.children.setdefault(char, Node(char))
        now.is_end = pattern
    
    def connect(self):
        q = deque([self.root])
        while q:
            now = q.popleft()
            for char in now.children:
                nxt = now.children[char]
                if now is self.root:
                    nxt.fail = self.root
                
                else:
                    dst = now.fail
                    while dst is not self.root and char not in dst.children:
                        dst = dst.fail
                    
                    if char in dst.children:
                        dst = dst.children[char]
                    
                    nxt.fail = dst

                if nxt.fail.is_end: nxt.is_end = nxt.fail.is_end

                q.append(nxt)
    
    @staticmethod
    def is_in_range(x,y):
        return 0 <= x < N and 0 <= y < M

    def search(self, x, y, d):
        now = self.root

        dx,dy = dr[d]
        nx,ny = x,y
        while self.is_in_range(nx,ny):
            char = arr[nx][ny]
            while now is not self.root and char not in now.children:
                now = now.fail
            
            if char in now.children:
                now = now.children[char]
            
            if now.is_end:
                pattern_len = len(now.is_end)
                start_x = nx - dx * (pattern_len - 1)
                start_y = ny - dy * (pattern_len - 1)
                ans[now.is_end] = min(ans[now.is_end],(start_x, start_y, d))
            
            nx,ny = nx + dx, ny + dy

        
dr = {
    "A": (-1,0),
    "B": (-1,1),
    "C": (0,1),
    "D": (1,1),
    "E": (1,0),
    "F": (1,-1),
    "G": (0,-1),
    "H": (-1,-1)
}

N,M,K = map(int,input().split())
arr = [input() for _ in range(N)]
patterns = [input() for _ in range(K)]
ac = AhoCorasick(patterns)

ans = {k: (float('inf'),float('inf'), "Z") for k in patterns}
for i in range(N):
    for d in "B", "C", "D":
        ac.search(i, 0, d)

    for d in "F", "G", "H":
        ac.search(i, M-1, d)

for i in range(M):
    for d in "D", "E", "F":
        ac.search(0, i, d)

    for d in "A", "B", "H":
        ac.search(N-1, i, d)

for pattern in patterns:
    print(*ans[pattern])