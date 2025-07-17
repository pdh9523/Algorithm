N = int(input())
arr = [*map(int,input().split())]

left,right,ans = 0,0,0
check = [False] * 100001
while left <= right < N:
    if not check[arr[right]]:
        check[arr[right]] = True
        right += 1
        ans += right-left
    else:
        while check[arr[right]]:
            check[arr[left]] = False
            left += 1
print(ans)