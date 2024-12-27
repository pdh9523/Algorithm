from collections import deque


def in_range(a):
    return 0<=a<=500000

def dfs(N,K):
    if N == K: return 0 
    visit=[[-1,-1] for _ in range(500001)]
    q = deque([N])

    time = 1
    K += time

    while True:
        if not in_range(K): break

        next_q = deque()

        while q:
            now = q.popleft()

            for nxt in [now-1, now+1, now*2]:
                
                if in_range(nxt) and visit[nxt][time%2]==-1:
                    visit[nxt][time%2]=time
                    next_q.append(nxt)

        if visit[K][time%2] != -1: return time

        time += 1
        K += time

        q = next_q

    return -1

N,K=map(int, input().split())

print(dfs(N,K))