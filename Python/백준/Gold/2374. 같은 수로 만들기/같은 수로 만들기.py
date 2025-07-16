import sys; input = sys.stdin.readline


N = int(input())
arr = [float('inf')]
data = dict()

for i in range(N):
    num = int(input())
    data.setdefault(num, set()).add(i+1)
    arr.append(num)

arr.append(float('inf'))
ans = 0
visit = [False] * (N+2)
for k in sorted(data):
    
    for i in data[k]:
        if visit[i]: continue

        prev = i
        while arr[prev] <= k:
            visit[prev] = True
            prev -= 1
        
        nxt = i
        while arr[nxt] <= k:
            visit[nxt] = True
            nxt += 1
        
        if (value:= min(arr[nxt], arr[prev])) == float('inf'): break
        ans += value - k

print(ans)