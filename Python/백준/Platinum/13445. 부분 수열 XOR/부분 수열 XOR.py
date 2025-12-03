class Node:
    def __init__(self):
        self.cnt = 0
        self.children = [None, None]


class Trie:
    def __init__(self):
        self.root = Node()
        self.BIT = 20
        self.insert(0)

    def insert(self, num):
        now = self.root
        now.cnt += 1
        for i in range(self.BIT, -1, -1):
            bit = (num >> i) & 1
            if not now.children[bit]:
                now.children[bit] = Node()
            now = now.children[bit]
            now.cnt += 1

    def query(self, num, limit):
        now = self.root
        result = 0
        for i in range(self.BIT, -1, -1):
            if not now: break

            n_bit = (num >> i) & 1
            k_bit = (limit >> i) & 1

            if k_bit == 1:
                child = now.children[n_bit]
                if child:
                    result += child.cnt

                now = now.children[1 - n_bit]
            else:
                now = now.children[n_bit]

        return result


N,K = map(int,input().split())
arr = [*map(int,input().split())]

trie = Trie()
xor = 0
ans = 0

for x in arr:
    xor ^= x
    ans += trie.query(xor, K)
    trie.insert(xor)

print(ans)
