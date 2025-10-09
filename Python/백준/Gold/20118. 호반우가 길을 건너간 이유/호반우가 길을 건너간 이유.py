N,M=map(int,input().split())

a=[]
for i in range(N): a.append((i,0))
for i in range(1,M-1): a.append((N-1,i))
if len(a)%2==0: a.append((N-2, M-2))
a.append((N-1,M-1))

print(len(a)*2)
for i in range(0,len(a),2):
    for _ in range(2):
        print(*a[i])
        print(*a[i+1])