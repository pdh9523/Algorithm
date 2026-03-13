from collections import deque

N,K = map(int,input().split())

q = deque([1])
while q:
    now = q.popleft()

    for _ in range(K - (now!=1)):
        q.append(N)
        
        print(now, N)
        if (N:=N-1)==1: exit()