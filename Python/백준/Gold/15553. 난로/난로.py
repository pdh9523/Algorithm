import sys; input = sys.stdin.readline


N,T = map(int,input().split())
arr = [int(input()) for _ in range(N)]
dif = sorted([arr[i+1]-arr[i] for i in range(N-1)])

print(sum(dif[:N-T]) + T)