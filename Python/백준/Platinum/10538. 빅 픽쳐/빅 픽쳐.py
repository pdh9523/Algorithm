import sys; input = lambda: sys.stdin.readline().strip()
from collections import deque
sys.setrecursionlimit(10**6)

class Trie:
    def __init__(self):
        self.go = [None, None]  # 'x'=0, 'o'=1
        self.fail = None
        self.terminal = -1  # This position's word index

    def insert(self, word, pos, k):
        if pos == len(word):
            self.terminal = k
            return
        next_node = word[pos]
        if not self.go[next_node]:
            self.go[next_node] = Trie()
        self.go[next_node].insert(word, pos + 1, k)


def construct_fail_functions(root):
    root.fail = root
    queue = deque([root])

    while queue:
        current = queue.popleft()
        for i in range(2):
            next_node = current.go[i]
            if not next_node:
                continue

            if current == root:
                next_node.fail = root
            else:
                dest = current.fail
                while dest != root and not dest.go[i]:
                    dest = dest.fail
                if dest.go[i]:
                    dest = dest.go[i]
                next_node.fail = dest

            if next_node.fail.terminal != -1:
                next_node.terminal = next_node.fail.terminal

            queue.append(next_node)


def main():
    H1, W1, H2, W2 = map(int, input().split())

    P = []
    for _ in range(H1):
        row = input().strip()
        P.append([1 if c == 'o' else 0 for c in row])

    M = []
    for _ in range(H2):
        row = input().strip()
        M.append([1 if c == 'o' else 0 for c in row])

    keys = {}  # Map to store word and their index
    knum = []

    for i, row in enumerate(P):
        row_tuple = tuple(row)
        if row_tuple not in keys:
            keys[row_tuple] = i
        knum.append(keys[row_tuple])

    # Build the Trie using rows of P
    root = Trie()
    for i, row in enumerate(P):
        if knum[i] == i:
            root.insert(row, 0, i)
    construct_fail_functions(root)

    # Perform matching for each row of M
    check = [[-1] * W2 for _ in range(H2)]

    for i in range(H2):
        current = root
        for j in range(W2):
            next_node = M[i][j]
            while current != root and not current.go[next_node]:
                current = current.fail
            if current.go[next_node]:
                current = current.go[next_node]
            if current.terminal != -1:
                check[i][j] = current.terminal

    # Compute the failure array for knum
    pi = [0] * H1
    w = 0
    for i in range(1, H1):
        while w > 0 and knum[i] != knum[w]:
            w = pi[w - 1]
        if knum[i] == knum[w]:
            w += 1
        pi[i] = w

    # Perform KMP on columns of check to find knum pattern
    result = 0
    for j in range(W2):
        w = 0
        for i in range(H2):
            while w > 0 and check[i][j] != knum[w]:
                w = pi[w - 1]
            if check[i][j] == knum[w]:
                if w == H1 - 1:
                    result += 1
                    w = pi[w]
                else:
                    w += 1

    print(result)

if __name__ == "__main__":
    main()
