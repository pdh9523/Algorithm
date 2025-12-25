from collections import deque


SIZE = 4
TOTAL = SIZE ** 2
dr = (2,-1),(-1,2),(1,2),(2,1),(1,-2),(-2,1),(-2,-1),(-1,-2)

def move_knight(bit, target_bit):
    res = []
    x,y = target_bit//SIZE, target_bit%SIZE

    tmp = iter(bin(bit)[2:].zfill(TOTAL))
    arr = [[""] * SIZE for _ in range(SIZE)]
    for i in range(SIZE):
        for j in range(SIZE):
            arr[i][j] = next(tmp)
    
    for dx,dy in dr:
        nx,ny = x+dx, y+dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            if arr[nx][ny] == "1": continue

            arr[nx][ny] = "1"
            arr[x][y] = "0"
            res.append(arr_to_bin(arr))
            arr[nx][ny] = "0"
            arr[x][y] = "1"
    return res

def arr_to_bin(arr):
    res = ""
    for i in range(SIZE):
        res += "".join(arr[i])
    return int(res,2)
    
start = arr_to_bin([input().split() for _ in range(SIZE)])
end = arr_to_bin([input().split() for _ in range(SIZE)])

visit = dict()
visit[start] = 0

q = deque([start])
while q:
    now = q.popleft()

    if now == end: break

    for pos in range(TOTAL):
        mask = 1 << (TOTAL - 1 - pos)
        if now & mask:
            nxts = move_knight(now, pos)
            for nxt in nxts:
                if visit.get(nxt) is not None: continue
                visit[nxt] = visit[now] + 1
                q.append(nxt)

print(visit[end])
