def merge_count(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    cnt = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            cnt += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return cnt

def merge_sort_count(arr, temp, left, right):
    cnt = 0
    if left < right:
        mid = (left + right) // 2

        cnt += merge_sort_count(arr, temp, left, mid)
        cnt += merge_sort_count(arr, temp, mid + 1, right)
        cnt += merge_count(arr, temp, left, mid, right)

    return cnt

N = int(input())
arr = [*map(int, input().split())]
temp = [0] * N

result = merge_sort_count(arr, temp, 0, N - 1)
print(result)