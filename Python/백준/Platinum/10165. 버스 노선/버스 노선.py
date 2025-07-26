import sys; input = sys.stdin.readline


N = int(input())
M = int(input())
arr = []
visit = [True] * (M+1)
for i in range(1,M+1):
    a,b = map(int,input().split())
    if a > b :
        arr.append(((a,b+N),i))
        arr.append(((a-N,b),i))
    else:
        arr.append(((a,b),i))

arr.sort(key = lambda x: (x[0][0],-x[0][1]))

start = -float('inf')
end = -float('inf')
for t, idx in arr:
    s,e = t
    if end < s: 
        start,end = s,e
    elif end < e:
        start,end = s,e
    else:
        visit[idx] = False

for i in range(1,M+1):
    if visit[i]: print(i, end=" ")    
