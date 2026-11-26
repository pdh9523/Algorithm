import sys; input = sys.stdin.readline

dr = None,(-1,0),(1,0),(0,1),(0,-1)

class Shark:
    def __init__(self, speed, dir, size):
        self.speed = speed
        self.dir = dir
        self.size = size
    
    def __gt__(self, other):
        return self.size > other.size

    def move(self, x, y):
        r = N if self.dir in (1,2) else M
        dist = self.speed % ((r - 1) * 2)

        for _ in range(dist):
            if self.dir == 1 and x == 0:
                self.switch()
            elif self.dir == 2 and x == N-1:
                self.switch()
            elif self.dir == 3 and y == M-1:
                self.switch()
            elif self.dir == 4 and y == 0:
                self.switch()

            dx,dy = dr[self.dir]
            x,y = x+dx,y+dy
        return self, x, y

    def switch(self):
        if self.dir <= 2: 
            self.dir = 3 - self.dir
        else: 
            self.dir = 7 - self.dir

def catch(j):
    for i in range(N):
        if arr[i][j]:
            res = arr[i][j].size
            arr[i][j] = None
            return res
    return 0

def move():
    new_arr = [[None]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                s,x,y = arr[i][j].move(i,j)
                if new_arr[x][y]:
                    new_arr[x][y] = max(new_arr[x][y], s)
                else:
                    new_arr[x][y] = s
    return new_arr

N,M,K = map(int,input().split())
arr = [[None] * M for _ in range(N)]
for _ in range(K):
    r,c,s,d,z = map(int,input().split())
    r-=1; c-=1
    arr[r][c] = Shark(s,d,z)

ans = 0
for i in range(M):
    ans += catch(i)
    arr = move()
print(ans)
