dr = (0,0),(1,0),(0,1),(-1,0),(0,-1)


def light_off(arr):
    cnt = 0
    for x in range(N):
        for y in range(N):
            if x == 0 and not (bit & 1<<y): continue
            if x and not new_arr[x-1][y]: continue

            cnt += 1
            for dx,dy in dr:
                nx,ny = x+dx, y+dy
                if 0 <= nx < N and 0 <= ny < N:
                    arr[nx][ny] = not arr[nx][ny]
    return cnt

N = 10
arr = [[False] * N for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(N):
        arr[i][j] = tmp[j]=="O"

ans = 101
for bit in range(1 << N):
    cnt = light_off(new_arr:=[row[:] for row in arr])
    
    if all(not x for x in new_arr[-1]): ans = min(ans, cnt)

print(ans if ans != 101 else -1)