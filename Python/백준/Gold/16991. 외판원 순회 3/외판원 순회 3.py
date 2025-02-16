def calculate_distance(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2) ** 0.5

def tsp(now=0, bit=1):
    if bit == (1 << N) - 1: return arr[now][0] 
    
    if DP[now][bit]: return DP[now][bit]

    min_v = float('inf')
    for nxt in range(1, N):
        if bit & (1 << nxt): continue

        cost = tsp(nxt, bit | (1 << nxt)) + arr[now][nxt]
        min_v = min(min_v, cost)
    
    DP[now][bit] = min_v
    return min_v

N = int(input())
pos = [tuple(map(int, input().split())) for _ in range(N)]

arr = [[0] * N for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        arr[i][j] = arr[j][i] = calculate_distance(pos[i], pos[j])

DP = [[0] * (1 << N) for _ in range(N)]
print(tsp())
