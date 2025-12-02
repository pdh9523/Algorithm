import sys; input = sys.stdin.readline


for _ in range(int(input())):
    N,M,K = map(int,input().split())
    print("Yuto" if N*M%2 or max(N,M) < K*2 else "Platina")