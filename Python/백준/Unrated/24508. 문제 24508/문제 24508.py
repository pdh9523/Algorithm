import sys; input = sys.stdin.readline

def calc():
    left, right = 0, N-1

    x = 0
    while left < right:
        now = arr[left] + arr[right]
        if now >= K:
            x += (K - arr[right])
            arr[left] -= (K - arr[right])
            arr[right] = 0
            right -= 1
        else:
            arr[right] += arr[left]
            x += arr[left]
            arr[left] = 0
            left += 1
        if x > T:
            return False
    return all(x == 0 for x in arr)

N,K,T = map(int,input().split())
arr = sorted(map(int,input().split()))

print("YES" if calc() else "NO")