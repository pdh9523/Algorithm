def solve(arr):
    for i in range(N-1, 0, -1):
        if arr[i-1] >= arr[i]: continue
        for j in range(N-1, 0, -1):
            if arr[i-1] < arr[j]:
                arr[i-1], arr[j] = arr[j], arr[i-1]
                arr = arr[:i] + sorted(arr[i:])
                return " ".join(map(str, arr))
    return -1

N = int(input())
print(solve([*map(int,input().split())]))