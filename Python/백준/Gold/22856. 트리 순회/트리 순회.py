import sys; input = sys.stdin.readline


class Node:
    def __init__(self):
        self.parent = -1
        self.left = -1
        self.right = -1

    def set_parent(self, idx):
        self.parent = idx
    
    def set_children(self, left, right):
        self.left = left
        self.right = right

def get_end():
    now = 1
    while True:
        if arr[now].right != -1:
            now = arr[now].right
        else:
            return now

N = int(input())
arr = [None] + [Node() for _ in range(N)]
for _ in range(N):
    a,b,c = map(int,input().split())
    arr[a].set_children(b,c)
    if b != -1:
        arr[b].set_parent(a)
    if c != -1:
        arr[c].set_parent(a)

end = get_end()

now = 1
ans = 0
while True:
    if arr[now].left != -1:
        prev = arr[now]
        now = arr[now].left
        prev.left = -1
        ans += 1
    elif arr[now].right != -1:
        prev = arr[now]
        now = arr[now].right
        prev.right = -1
        ans += 1
    elif now == end: break
    elif arr[now].parent != -1:
        prev = arr[now]
        now = arr[now].parent
        prev.parent = -1
        ans += 1
    else: break

print(ans)
