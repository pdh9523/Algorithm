import sys; input = sys.stdin.readline

def ccw(a,b,c):
    return (a[0] * b[1] + b[0] * c[1] + c[0] * a[1]) - (a[1] * b[0] + b[1] * c[0] + c[1] * a[0]) >= 0

def solve():
    N, *tmp = map(int,input().split())
    arr = sorted([(tmp[i*2], tmp[i*2+1], i) for i in range(N)])
    
    visit = [False] * N
    stack = []
    for i in range(N):
        while len(stack) > 1:
            if ccw(stack[-2], stack[-1], arr[i]):
                break
            visit[stack.pop()[2]] = False
        
        stack.append(arr[i])
        visit[arr[i][2]] = True

    ans = []
    for _,_,i in arr:
        if not visit[i]:
            ans.append(i)

    while stack:
        ans.append(stack.pop()[2])
    
    print(*ans)

for _ in range(int(input())):
    solve()
