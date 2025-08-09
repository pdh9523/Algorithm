def swap(x, y):
    hq[x], hq[y] = hq[y], hq[x]

N = int(input())

hq = [0,1]
for i in range(2,N+1):
    hq.append(i)
    swap(i, i-1)
    j = i-1

    while j != 1:
        swap(j, (j:=j//2))

for i in range(1,N+1):
    print(hq[i], end=" ")