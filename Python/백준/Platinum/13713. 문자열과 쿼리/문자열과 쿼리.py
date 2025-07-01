import sys; input = lambda: sys.stdin.readline().rstrip()


def get_z_arr(word):
    word = word[::-1]

    length = len(word)
    z = [0]
    left, right = 0,0
    for i in range(1, length):
        x = min(right - i + 1, z[i-left]) if i <= right else 0
        while i+x < length and word[x] == word[i+x]:
            x += 1
        if i + x - 1 > right:
            left,right = i , i+x-1
        z.append(x)
    z[0] = length
    return z


z = get_z_arr(input())
for _ in range(int(input())):
    print(z[-int(input())])