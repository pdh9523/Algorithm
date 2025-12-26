n=int(input())
print(n*(n-1)//2 + (0 if n%2 else (n//2)-1))