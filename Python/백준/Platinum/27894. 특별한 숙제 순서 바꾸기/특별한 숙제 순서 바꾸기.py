def check(arr, brr):
    if arr == brr: return True
    for i in range(N-2):
        if brr[i] < brr[i+1] < brr[i+2] or brr[i] > brr[i+1] > brr[i+2]: return True
    return False

N = int(input())
print("POSSIBLE" if check([*map(int,input().split())], [*map(int,input().split())]) else "IMPOSSIBLE")