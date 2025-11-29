import sys; input = sys.stdin.readline


def merge(a,b):
    return a+b


class SegmentTree:
    def __init__(self, arr, merge=merge):
        _arr = list(arr)
        self._size = len(_arr)
        self._tree = _arr * 2
        self._merge = merge
        for i in range(self._size - 1, 0, -1):
            self._tree[i] = merge(self._tree[i * 2], self._tree[i * 2 + 1])

    def set(self, pos, value):
        i = pos + self._size
        while i:
            self._tree[i] = value
            value = (self._merge(self._tree[i - 1], value) if i % 2
                     else self._merge(value, self._tree[i + 1]))
            i >>= 1

    def get(self, pos):
        return self._tree[pos + self._size]

    def query(self, beg: int, end: int):
        if end == beg + 1:
            return self._tree[beg + self._size]
        l, r = beg + self._size + 1, end + self._size - 2
        ret_l, ret_r = self._tree[l - 1], self._tree[r + 1]
        while l <= r:
            if l % 2:
                ret_l = self._merge(ret_l, self._tree[l])
            if not r % 2:
                ret_r = self._merge(self._tree[r], ret_r)
            l, r = (l + 1) >> 1, (r - 1) >> 1
        return self._merge(ret_l, ret_r)


N = int(input())
tree = SegmentTree([0]*N)

arr = [*map(int,input().split())]
brr = [*map(int,input().split())]

loc = {arr[i]: i+1 for i in range(N)}
ans = 0
for x in brr:
    idx = loc[x] - 1
    if idx + 1 <= N-1:
        ans += tree.query(idx+1, N)
    tree.set(idx, 1)

print(ans)