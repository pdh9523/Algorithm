import sys; input = lambda: sys.stdin.readline().rstrip()

class Node:
    def __init__(self):
        self.children = dict()
        self.visited = ""
        self.visited_index = float('inf')

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word, idx):
        now = self.root
        for char in word:
            now = now.children.setdefault(char, Node())
            now.visited = word
            now.visited_index = idx
    
    def get_prefix(self, word):
        now = self.root
        for i,char in enumerate(word):
            if char not in now.children:
                return i, now.visited, now.visited_index
            now = now.children[char]
        return i+1, now.visited, now.visited_index

trie = Trie()
max_v = 0
min_idx = float('inf')
ans = None
for idx in range(int(input())):
    word = input()
    i,v,id = trie.get_prefix(word)
    if max_v < i or (max_v==i and min_idx > id):
        min_idx = id
        max_v = i
        ans = (v, word)
    trie.insert(word, idx)
print(*ans, sep="\n")
