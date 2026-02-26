import sys; input = sys.stdin.readline

def calc(num):
    return num if num < N else V-1 + (num-N) % (N-V+1)

N,M,V = map(int,input().split())
arr = [*map(int,input().split())]

for _ in range(M):
    print(arr[calc(int(input()))])
