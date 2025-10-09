N,M = map(int,input().split())

tmp = []
for i in range(N):
    tmp.append((i,0))

for i in range(1,M-1):
    tmp.append((N-1,i))

if len(tmp)%2==0:
    tmp.append((N-2, M-2))

tmp.append((N-1,M-1))

ans = []
for i in range(0, len(tmp), 2):
    ans.extend([tmp[i], tmp[i+1]] * 2)

print(len(ans))
for a in ans:
    print(*a)
