def is_sub_string(N,M):
    idx=0
    for i in range(len(M)):
        if N[idx] == M[i]:
            idx += 1 
            if idx == len(N): return True
    return False

while True:
    try:
        N,M = input().split()
        print("Yes" if is_sub_string(N,M) else "No")    
    except:
        break