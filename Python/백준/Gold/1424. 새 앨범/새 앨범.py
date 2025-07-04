N,L,C = int(input()), int(input()), int(input())

capacity = C//(L+1)

tmp = C%(L+1)
if tmp == L: capacity += 1
capacity = min(N, capacity)
if capacity%13 == 0: capacity -= 1
ans = N // capacity
x = N % capacity
tmp = capacity
if x!=0:
    ans += 1
    if x%13 == 0:
        while not (tmp % 13 and x % 13):
            tmp -= 1
            x += 1
        ans += x // capacity
print(ans)