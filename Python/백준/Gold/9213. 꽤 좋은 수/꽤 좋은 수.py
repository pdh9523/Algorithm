import sys; input = sys.stdin.readline


SIZE = 1000000

def is_good(num, diff):
    return abs(num-data[num]) <= diff

data = [1] * (SIZE+1)

for s in range(2, SIZE//2+1):
    for t in range(s*2, SIZE+1, s):
        data[t] += s

tc = 0
while True:
    start, end, diff = map(int,input().split())
    if start == 0: break
    
    ans = 0
    for x in range(start, end+1):
        ans += is_good(x, diff)
    
    tc += 1
    print(f"Test {tc}: {ans}")
