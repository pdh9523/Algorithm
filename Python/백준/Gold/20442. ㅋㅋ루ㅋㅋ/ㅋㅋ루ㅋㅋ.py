word = input()

left, right = [], []
cnt = 0
for c in word:
    if c == 'K':
        cnt += 1
    else:
        left.append(cnt)

cnt = 0
for c in word[::-1]:
    if c == 'K':
        cnt += 1
    else:
        right.append(cnt)

right.reverse()
l, r = 0, len(left) - 1
ans = 0
while l <= r:
    ans = max(ans, (r-l+1) + 2*min(left[l], right[r]))

    if left[l] < right[r]:
        l += 1
    else:
        r -= 1

print(ans)