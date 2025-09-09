import sys; input = sys.stdin.readline


N = int(input())
arr = sorted([(lambda a,b: a-b)(*map(int,input().split())) for _ in range(N)])
print(1 if N%2 else abs(arr[N//2]-arr[N//2-1]+1))