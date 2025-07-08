'''
case 0:
 1  2  3  4  5  6  7  8
HS YG YG YG YG YG HS YG  

case 1:
 1  2  3  4  5  6  7  8
YG YG YG YG HS HS YG YG
'''
N,K = map(int,input().split())
ans = K%6==1 if N==0 else (K%6==0 or K%6==5)
print("HS" if ans else "YG")