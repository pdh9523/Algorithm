class Node:
    def __init__(self):
        self.cnt = 0
        self.children = dict()
    
class Trie:
    def __init__(self, patterns):
        self.root = Node()
        for pattern in patterns:
            self.insert(pattern)

    def insert(self, pattern):
        now = self.root
        for char in pattern:
            now = now.children.setdefault(char, Node())
            now.cnt += 1


def backtrack(now, idx=0, res=""):
    if 0 < now.cnt <= K:
        global cnt
        global ans
        if cnt > idx:
            cnt = idx
            ans = res
    
    if idx > cnt: return
    for x in "RSP":
        if x in now.children: backtrack(now.children[x], idx + 1, res + x)
        

N,M,K = map(int,input().split())
trie = Trie([input() for _ in range(N)])

cnt = float('inf')
ans = ""
backtrack(trie.root)

if cnt != float('inf'):
    print(cnt)
    rev_replaces = {
        "S": "P",
        "P": "R",
        "R": "S"
    }
    for i in range(cnt):
        print(rev_replaces[ans[i]], end="")
else:
    print(-1)