import sys; input = sys.stdin.readline


while True:
    N, *arr = map(int,input().split())
    if N == 0: break

    stack = []
    max_v = 0
    for i in range(N):
        while stack and arr[stack[-1]] > arr[i]:
            h = arr[stack.pop()]
            w = i if not stack else i-stack[-1]-1
            max_v = max(max_v, h*w)

        stack.append(i)
    
    while stack:
        h = arr[stack.pop()]
        w = N if not stack else N-stack[-1]-1
        max_v = max(max_v, h*w)
    
    print(max_v)
