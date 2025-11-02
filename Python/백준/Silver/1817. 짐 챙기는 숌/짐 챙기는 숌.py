N,K=map(int,input().split())
if N==0:exit(print(0))
w,s=0,0
for a in map(int,input().split()):
    if w+a>K:w=0;s+=1
    w+=a
print(s+(w>0))