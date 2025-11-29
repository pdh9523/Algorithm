import sys; input = sys.stdin.readline


class FenwickTree:
    def __init__(self, arr):
        self._arr = list(arr)
        self._size = len(self._arr)
        self._tree = self._arr[:]
        for i, num in enumerate(self._tree):
            if (t:=i|(i+1)) < self._size:
                self._tree[t] += num

    def update(self, pos, num):
        self._arr[pos] += num
        while pos < self._size:
            self._tree[pos] += num
            pos |= pos + 1

    def set(self, pos, num):
        self.update(pos, num - self._arr[pos])

    def query(self, beg, end):
        res = 0
        i = end - 1
        while i >= 0:
            res += self._tree[i]
            i = (i & (i + 1)) - 1
        i = beg - 1
        while i >= 0:
            res -= self._tree[i]
            i = (i & (i + 1)) - 1
        return res
    

N,Q = map(int,input().split())
tree = FenwickTree([*map(int,input().split())])

for _ in range(Q):
    x,y,a,b = map(int,input().split())
    x,y = min(x,y), max(x,y)
    print(tree.query(x-1,y))
    tree.set(a-1,b)