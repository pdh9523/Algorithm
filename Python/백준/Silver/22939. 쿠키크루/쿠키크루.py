import sys; input = lambda: sys.stdin.readline().rstrip()


def backtrack(arr, char, now=0, visit=0, res=0):
    if visit == (1<<4)-1:
        res += arr[now][4]
        global min_v, ans
        if min_v > res:
            min_v = res
            ans = data[char]
        return
    
    for i in range(4):
        if visit & 1<<i: continue
        backtrack(arr, char, i, visit | 1<<i, res+arr[now][i])
    

def get_distance(char):
    pos = find("H") + find(char) + find("#")

    dist_arr = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            x1,y1 = pos[i]
            x2,y2 = pos[j]
            dist_arr[i][j] = abs(x1-x2) + abs(y1-y2)
    
    backtrack(dist_arr,char)


def find(char):
    res = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == char:
                res.append((i,j))
    return res

data = {
    "J": "Assassin",
    "C": "Healer",
    "B": "Mage",
    "W": "Tanker"
}

dr = (1,0),(0,1),(-1,0),(0,-1)

N = int(input())
arr = [input() for _ in range(N)]

min_v = float('inf')
ans = ""
for k in data:
    get_distance(k)

print(ans)