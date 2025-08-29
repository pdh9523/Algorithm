L,R = input().split()
length = max(len(L),len(R))
L,R = L.zfill(length), R.zfill(length)

cnt = 0
for l,r in zip(L,R):
    if l==r=="8":
        cnt += 1
    elif l!=r: break
print(cnt)