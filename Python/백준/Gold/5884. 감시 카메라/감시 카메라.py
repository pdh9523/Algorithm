import sys; input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int,input().split())) for _ in range(N)]

px = dict()
py = dict()

cnt_x = [0]*(N + 1)
cnt_y = [0]*(N + 1)

cx,cy = 0,0
for i in range(N):
    x_val = arr[i][0]
    if x_val not in px:
        cx += 1
        px[x_val] = cx
    cnt_x[px[x_val]] += 1

for i in range(N):
    y_val = arr[i][1]
    if y_val not in py:
        cy += 1
        py[y_val] = cy
    cnt_y[py[y_val]] += 1

if cx <= 3 or cy <= 3:
    exit(print(1))

x = [[] for _ in range(cx + 1)]
y = [[] for _ in range(cy + 1)]

for i in range(N):
    xi = px[arr[i][0]]
    yi = py[arr[i][1]]
    x[xi].append(yi)
    y[yi].append(xi)

for i in range(1, cx + 1):
    cnt = 0
    for nxt in x[i]:
        if cnt_y[nxt] == 1:
            cnt += 1
    if cy - cnt <= 2:
        exit(print(1))

for i in range(1, cy + 1):
    cnt = 0
    for nxt in y[i]:
        if cnt_x[nxt] == 1:
            cnt += 1
    if cx - cnt <= 2:
        exit(print(1))

print(0)
