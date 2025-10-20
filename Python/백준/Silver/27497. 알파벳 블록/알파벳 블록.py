import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def add_front(char):
    q.appendleft(char)
    stack.append(0)

def add_back(char):
    q.append(char)
    stack.append(1)

def remove():
    if not stack: return
    if stack.pop():
        q.pop()
    else:
        q.popleft()

stack = []
q = deque()

cmd = {
    "1": add_back,
    "2": add_front,
    "3": remove
    }

for _ in range(int(input())):
    c, *alphabet = input().split()
    cmd[c](*alphabet)

print("".join(q) if q else 0)