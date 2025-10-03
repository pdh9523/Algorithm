import sys; input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def solve():
    q = deque([1])
    visit = [False] * (N+1)
    visit[1] = True

    result = word[1]
    while q:
        nxt_q = deque()
        max_char = ''
        
        for _ in range(len(q)):
            now = q.popleft()
            for nxt in graph[now]:
                if not visit[nxt] and word[nxt] >= max_char:
                    max_char = word[nxt]
                    visit[nxt] = True
                    nxt_q.append(nxt)

        if max_char:
            result += max_char
            while nxt_q:
                tmp = nxt_q.popleft()
                if word[tmp] == max_char: q.append(tmp)
    print(result)

N = int(input())
word = " " + input()

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

if __name__ == "__main__":
    solve()