import sys; input = sys.stdin.readline


class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = dict()
        self.cnt = 0
        self.end_cnt = 0

class Trie:
    def __init__(self):
        self.root = Node()
        self.data = dict()

    def insert(self, values):
        now = self.root
        for i, v in enumerate(values, start=1):
            now.cnt += 1
            if v not in now.children:
                now.children[v] = Node(v)

            if i >= 2:
                child = now.children[v]
                other_count = now.cnt - 1 - child.cnt - child.end_cnt
                if other_count > 0:
                    self.data[now.value] = self.data.get(now.value, 0) + other_count

            now = now.children[v]
        now.end_cnt += 1

    def get_data(self, x):
        return self.data.get(x, 0)
    
N,Q = map(int,input().split())
trie = Trie()
for _ in range(N):
    a, *q = map(int,input().split())
    trie.insert(q)

for _ in range(Q):
    print(trie.get_data(int(input())))
