import sys

class Node:
    def __init__(self):
        self.children = dict()
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        now = self.root
        for char in word:
            now = now.children.setdefault(char, Node())
        now.is_end = True

    def search(self, word):
        now = self.root
        for char in word:
            if char not in now.children:
                return False
            now = now.children[char]
        return now.is_end

    def check(self, word):
        now = self.root
        for idx, char in enumerate(word):
            if char not in now.children:
                return False
            now = now.children[char]
            if now.is_end:
                remaining = word[idx+1:]
                if remaining and self.search(remaining):
                    return True
        return False

trie = Trie()
words = sys.stdin.read().splitlines()

for word in words:
    trie.insert(word)

for word in words:
    if trie.check(word):
        print(word)