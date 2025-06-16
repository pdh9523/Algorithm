import sys; input = sys.stdin.readline


while N:=int(input()):
    s = bin(N-1)[2:][::-1]
    ans = ", ".join([str(3**i) for i in range(len(s)) if s[i] == "1"])
    if ans: print("{",f"{ans}","}")
    else: print("{ }")