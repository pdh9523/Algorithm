import sys; input = lambda: sys.stdin.readline().strip()


N = int(input())
arr = [""] + [input() for _ in range(N)]
nxt = [0] * (N+1)
tail = [*range(N+1)]

head = None
for _ in range(N-1):
    a,b = map(int,input().split())
    nxt[tail[a]] = b
    tail[a] = tail[b]
    head = a

ans = []
for _ in range(N):
    ans.append(arr[head])
    head = nxt[head]

print("".join(ans))