import sys; input = lambda: sys.stdin.readline().rstrip()

word = input()
ans = 0
for _ in range(int(input())):
    ring = input() * 2
    ans += word in ring

print(ans)
