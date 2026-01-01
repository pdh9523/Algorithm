import sys; input = sys.stdin.readline


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, size=0):
        self.cnt = 0
        self._arr = [Node(i) for i in range(size+1)]
        self._root_check = [False] * (size+1)
        self.root = None
        self.width = dict()
        self._size = size
    
    def insert(self, nodes):
        for now, left, right in nodes:
            
            if left != -1:
                self._root_check[left] = True
                self._arr[now].left  = self._arr[left]
            if right != -1:
                self._root_check[right] = True
                self._arr[now].right = self._arr[right]
        
        for i in range(1, self._size+1):
            if not self._root_check[i]:
                self.root = self._arr[i]
        
    def get_width(self):
        self._get_width(self.root)
        return self.width

    def _get_width(self, now, depth=1):
        if now.left:
            self._get_width(now.left, depth+1)
        self.width.setdefault(depth, [float('inf'),0])
        self.width[depth][0] = min(self.width[depth][0], self.cnt)
        self.width[depth][1] = max(self.width[depth][1], self.cnt)
        self.cnt += 1

        if now.right:
            self._get_width(now.right, depth+1)


N = int(input())
tree = Tree(N)
tree.insert([[*map(int,input().split())] for _ in range(N)])

res = tree.get_width()

ans = 0
width = 0
for k in sorted(res):
    if width < res[k][1] - res[k][0] + 1:
        width = res[k][1] - res[k][0] + 1
        ans = k

print(ans, width)