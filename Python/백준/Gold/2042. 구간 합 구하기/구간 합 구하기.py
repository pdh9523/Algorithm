import sys; input = sys.stdin.readline


class FenwickTree:
    def __init__(self, arr):
        self._arr = list(arr)
        self._size = len(self._arr)
        self._tree = self._arr[:]
        for i, num in enumerate(self._tree):
            if i | (i + 1) < self._size:
                self._tree[i | (i + 1)] += num

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
        print(res)

N,M,K = map(int,input().split())
tree = FenwickTree(int(input()) for _ in range(N))
cmd = {
    1: tree.set,
    2: tree.query
}
for _ in range(M+K):
    a,b,c = map(int,input().split())
    cmd[a](b-1,c)