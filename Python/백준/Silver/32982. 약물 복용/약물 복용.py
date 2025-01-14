def take_medicine(time):
    for _ in range(N):
        if arr[0] <= time:
            time = min(time, arr[1]) + K
        else:
            return False

        if arr[2] <= time:
            time = min(time, arr[3]) + K
        else:
            return False
        
        if arr[4] <= time:
            time = min(time, arr[5]) + K
        else:
            return False
        
        time = time%day if time >= day else -1
    return True

N,K = map(int,input().split())
arr = [*map(int,input().split())]
day = 1440
print("YES" if take_medicine(arr[1]) else "NO")
