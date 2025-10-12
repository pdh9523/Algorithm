N = int(input())
a = [3]+[2*i for i in range(1,N)]
if N%3==2: a[-1] += 4
print(*a)
