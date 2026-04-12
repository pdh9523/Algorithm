import sys; input = sys.stdin.readline

class Block:
    def __init__(self, up: list, front: list, right: list):
        self.ans = up
        self.front = front
        self.right = right[::-1]
    
    def complete(self):
        for i in range(N):
            for j in range(M):
                if self.ans[i][j]:
                    self.ans[i][j] = min(self.right[i], self.front[j])
        return self.ans

N,M = map(int,input().split())
block = Block(
    [[*map(int,input().split())] for _ in range(N)], 
    [*map(int,input().split())], 
    [*map(int,input().split())])

ans = block.complete()

for i in range(N):
    if max(ans[i]) != block.right[i]:
        exit(print(-1))

for j in range(M):
    if max(ans[i][j] for i in range(N)) != block.front[j]:
        exit(print(-1))

for a in ans:
    print(*a)