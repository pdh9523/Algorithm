from copy import deepcopy


class Fish:
    def __init__(self, idx, dir):
        self.idx = idx
        self.dir = dir

    def __repr__(self):
        return f"({self.idx}, {self.dir})"

# 백트래킹이 지나간 자리는 상어가 깔끔하게 먹었습니다.
def backtrack(arr, x=0, y=0, dir=-1, total=0):
    # 상어가 먼저 먹고
    arr = deepcopy(arr)
    now = arr[x][y]
    total += now.idx
    dir = now.dir
    # 상어의 위치는 1로 표시한다.
    arr[x][y] = 1
    # 물고기들이 이동한다.
    arr = move_fish(arr)
    # 물고기들이 이동한 후, 상어가 이동한다.
    # 상어가 해당 자리를 비울 것이기 떄문에 0으로 빈자리를 표시한다.
    arr[x][y] = 0
    # 이동은 방향에서 아무대나 갈 수 있으니 방향에 있는 모든 물고기에 대해 백트래킹으로 접근한다.
    nx,ny = x,y
    dx,dy = dr[dir%8]
    while True:
        nx, ny = nx+dx, ny+dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            if type(arr[nx][ny]) == Fish:
                backtrack(arr, nx, ny, dir, total)
        else:
            global ans
            ans = max(ans, total)
            return
    

def move_fish(arr):
    arr = deepcopy(arr)
    cnt = 1
    while cnt <= 16:
        check = False
        for x in range(4):
            if check: break
            for y in range(4):
                if check: break
                if type(arr[x][y]) == Fish and arr[x][y].idx == cnt:
                    for i in range(8):
                        dx,dy = dr[arr[x][y].dir%8]
                        nx,ny = x+dx, y+dy
                        if 0 <= nx < 4 and 0 <= ny < 4 :
                            # 해당 위치가 빈자리거나 다른 물고기인 경우
                            if arr[nx][ny] == 0 or type(arr[nx][ny]) == Fish:
                                arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
                                check = True
                                break
                        
                        arr[x][y].dir += 1
    
        cnt += 1
    return arr

dr = (-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)

arr = [[Fish(idx, dir-1) for idx, dir in zip(*[iter(map(int,input().split()))]*2)] for _ in range(4)]

ans = 0
backtrack(arr)
print(ans)