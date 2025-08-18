import sys; input = sys.stdin.readline


N,L = map(int,input().split())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x:(-x[0],x[1]))

ans = 0
stress = 0
for k,t in arr:
    ans += t
    stress += k*t

    ans += max(stress-L, 0)

    stress -= max(stress-L, 0)

    stress -= min(k*t, 5*k)

    stress = max(stress, 0)

print(ans)
