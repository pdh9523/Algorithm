import sys; input = lambda: sys.stdin.readline().rstrip()

def calc(x):
    match x:
        case "1/4": return 0
        case "1/2": return 1
        case "3/4": return 2

arr = [0] * 3
for _ in range(int(input())):
    arr[calc(input())] += 1

ans = 0

ans += arr[2]
arr[0] -= min(arr[0], arr[2])

ans += arr[1] // 2

if arr[1] % 2:
    ans += 1
    arr[0] -= min(arr[0], 2)

ans += (arr[0] - 1) // 4 + 1

print(ans)
