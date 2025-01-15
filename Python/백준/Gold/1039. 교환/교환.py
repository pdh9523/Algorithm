from collections import deque


def bfs():
    new_q = set()
    while q:
        now = list(q.popleft())
        
        for i in range(length-1):
            for j in range(i+1, length):
                now[i],now[j] = now[j],now[i]

                if now[0] == "0": 
                    now[i],now[j] = now[j],now[i]
                    continue
                
                new_q.add(tuple(now))
                now[i],now[j] = now[j],now[i]
    return deque(new_q)

def join(arr):
    return "".join(arr)

N,K = input().split()
length = len(N)
K = int(K)
q = deque([list(N)])

for _ in range(K):
    q = bfs()

if not q:
    print(-1)
else:   
    print(max([*map(join,q)]))