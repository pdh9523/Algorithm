def backtrack(hp, now=0, drink=0, visit=0):
    global ans
    if ans == l-1:
        return

    if drink and graph[now][0] <= hp:
        ans = max(ans, drink)

    for nxt in range(1, l):
        if not visit & (1<<nxt):
            dist = graph[now][nxt]
            if dist <= hp:
                backtrack(hp - dist + H, nxt, drink + 1, visit | (1<<nxt))

def calc(x1, y1, x2, y2):
    return abs(y1-y2) + abs(x1-x2)

N,M,H = map(int,input().split())
milks = []
ans = 0

for i in range(N):
    tmp = [*map(int,input().split())]
    for j in range(N):
        if tmp[j] == 2:
            milks.append((i, j))
        elif tmp[j] == 1:
            sx,sy = i,j

milks = [(sx, sy)] + milks
l = len(milks)

graph = [[-1] * l for _ in range(l)]
for i in range(l):
    for j in range(l):
        if i == j:
            graph[i][j] = 0
        else:
            graph[i][j] = calc(*milks[i], *milks[j])

backtrack(M)
print(ans)