def check(word):
    for char in "MOBIS":
        if char not in word:
            return False
    return True
print("YES" if check(input()) else "NO")