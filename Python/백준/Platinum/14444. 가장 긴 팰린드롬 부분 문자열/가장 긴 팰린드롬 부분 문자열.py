def manacher(word):
    length = len(word:="$#" + "#".join(word) + "#^")
    radius = [0] * length
    center, right = 0,1
    for i in range(length-1):
        if i < right: radius[i] = min(right - i, radius[2*center-i])
        
        while word[i - radius[i] - 1] == word[i + radius[i] + 1]:
            radius[i] += 1
        
        if i + radius[i] > right:
            center = i
            right = radius[i] + i
    
    return max(radius)

print(manacher(input()))