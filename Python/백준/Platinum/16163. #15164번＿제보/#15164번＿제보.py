def manacher(word):
    word = "#"+"#".join(word)+"#"
    length = len(word)
    radius = [0] * length
    right,mid,res = 0,0,0
    for i in range(length):
        if i <= right:
            radius[i] = min(radius[2*mid-i], right-i)
        while i - radius[i] - 1 >= 0 and i + radius[i] + 1 < length and word[i - radius[i] - 1] == word[i + radius[i] + 1]:
            radius[i] += 1
        if right < i + radius[i]:
            right = i + radius[i]
            mid = i
        res += (radius[i]+1) // 2
    return res

print(manacher(input()))