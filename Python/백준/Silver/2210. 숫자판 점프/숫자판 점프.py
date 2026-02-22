def backtrack(x, y, idx=0, word=""):
    if idx == 6:
        ans.add(word)
        return

    for dx,dy in (1,0),(0,1),(-1,0),(0,-1):
        nx,ny = x+dx, y+dy
        if 0 <= nx < SIZE and 0 <= ny < SIZE:
            backtrack(nx, ny, idx+1, word + arr[nx][ny])

SIZE = 5
arr = [input().split() for _ in range(SIZE)]

ans = set()
for i in range(SIZE):
    for j in range(SIZE):
        backtrack(i,j)
print(len(ans))
