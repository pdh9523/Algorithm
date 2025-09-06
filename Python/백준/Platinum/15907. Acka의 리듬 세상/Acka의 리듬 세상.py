SIZE = 2000001

is_prime = [True] * SIZE
for i in range(2, int(SIZE**0.5)+1):
    if not is_prime[i]: continue
    for j in range(i*i, SIZE, i):
        is_prime[j] = False

N = int(input())
arr = [*map(int,input().split())]

ans = 0
for i in range(2,SIZE):
    if not is_prime[i]: continue
    if ans * i > arr[-1]: break
    data = dict()
    for num in arr:
        tmp = num % i
        data[tmp] = data.get(tmp, 0) + 1
    ans = max(ans, *data.values())

print(ans)