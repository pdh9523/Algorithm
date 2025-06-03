N = int(input())

if N==1: print(0)
elif N==2: print(2)
else: print(2 * 3**(N-2) % 1000000009)