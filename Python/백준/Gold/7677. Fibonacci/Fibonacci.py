f = [0,1]
for i in range(2,15001):
    f.append((f[i-1] + f[i-2]) % 10000)
while (N:=int(input())) >= 0:
    print(f[N%15000])
