import sys; input = sys.stdin.readline

SIZE = 10**5

N,M = map(int,input().split())

init_row = [0] * (SIZE+1)
init_col = [0] * (SIZE+1)
for _ in range(N):
    a,b = map(int,input().split())
    init_row[a] += 1
    init_col[b] += 1

target_row = [0] * (SIZE+1)
target_col = [0] * (SIZE+1)
for _ in range(M):
    a,b = map(int,input().split())
    target_row[a] += 1
    target_col[b] += 1

for i in range(1,SIZE+1):
    if init_row[i] % 2 != target_row[i] % 2 or init_col[i] % 2 != target_col[i] % 2:
        print("NO")
        break
else: print("YES")
