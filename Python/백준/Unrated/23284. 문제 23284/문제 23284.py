def backtrack(idx=0, arr=[], output=[]):
    if idx == N:
        while arr:
            output.append(arr.pop())
        print(*output)
        return
    
    if arr:
        new_arr = arr[:]
        x = new_arr.pop()
        backtrack(idx, new_arr, output + [x])
    
    idx += 1
    backtrack(idx, arr + [idx], output)

N = int(input())
backtrack()