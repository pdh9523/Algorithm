if (N:=int(input()))<4:exit(print(0))
n = N//4
m = N%4
ans = (2*n**2) - (2*n) + 1
if m: ans += m*n - 1
print(ans)