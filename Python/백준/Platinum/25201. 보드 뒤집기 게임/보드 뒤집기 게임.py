import sys; input = sys.stdin.readline

SIZE = 10**5

N,M = map(int,input().split())

row = [0] * (SIZE+1)
col = [0] * (SIZE+1)
for _ in range(N+M):
    a,b = map(int,input().split())
    row[a] ^= 1
    col[b] ^= 1

for i in range(1,SIZE+1):
    if row[i] or col[i]:
        print("NO")
        break
else: print("YES")
