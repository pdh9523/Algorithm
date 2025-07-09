from math import trunc


N,K = map(int,input().split())
print(trunc(N/10**K + 0.5) * 10**K)