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

    def query(self, beg, end):
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
    
def find_kth(tree, k):
    pos = 1
    size = tree._size

    while pos < size:
        left_child = pos * 2
        left_sum = tree._tree[left_child]

        if k <= left_sum:
            pos = left_child
        else:
            k -= left_sum
            pos = left_child + 1

    return pos - size

N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

MAX_VAL = 65536
tree = SegmentTree([0] * MAX_VAL)

for i in range(K):
    val = arr[i]
    tree.set(val, tree.get(val) + 1)

ans = 0
mid = (K+1)//2

ans += find_kth(tree, mid)

for i in range(K, N):
    old = arr[i - K]
    tree.set(old, tree.get(old) - 1)

    new = arr[i]
    tree.set(new, tree.get(new) + 1)

    ans += find_kth(tree, mid)

print(ans)
