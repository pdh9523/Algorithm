def solve():
    N = int(input())
    if N == 1:
        return -1

    if N % 2 == 0:
        return "2937" * (N//2)
    
    return "132319" + ("2937" * ((N//2)-1)) 

print(solve())