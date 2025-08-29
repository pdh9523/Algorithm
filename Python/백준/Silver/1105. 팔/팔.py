length = 10
L,R = map(lambda x: x.zfill(length), input().split())

cnt = 0
for l,r in zip(L,R):
    if l==r=="8": cnt += 1
    elif l!=r: break
print(cnt)