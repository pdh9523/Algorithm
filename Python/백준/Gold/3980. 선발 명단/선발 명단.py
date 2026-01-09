import sys; input = sys.stdin.readline

size = 11
def solve():
    def backtrack(arr, idx=0, res=0, visit=0):
        if idx == size:
            nonlocal ans
            ans = max(ans, res)
        
        if (size-idx) * 100 + res < ans: return

        for i in range(size):
            if visit & (1<<i): continue
            if arr[idx][i] == 0: continue
            backtrack(arr, idx+1, res+arr[idx][i], visit | (1<<i))
    
    arr = [[*map(int,input().split())] for _ in range(size)]
    ans = 0 
    backtrack(arr)
    print(ans)

for _ in range(int(input())):
    solve()