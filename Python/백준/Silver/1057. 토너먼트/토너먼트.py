from math import ceil


N,A,B = map(int,input().split())

cnt = 0
while A!=B:
    A = ceil(A/2)
    B = ceil(B/2)
    cnt += 1
print(cnt)