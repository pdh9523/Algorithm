import sys; input = sys.stdin.readline

answer = [
    "Not a pangram",
    "Pangram!",
    "Double pangram!!",
    "Triple pangram!!!"
]

for tc in range(1, int(input())+1):
    S = input()
    data = dict()

    for char in S:
        if "A" <= char <= "Z":
            char = char.lower()
        
        if "a" <= char <= "z":
            data[ord(char)] = data.get(ord(char), 0) + 1

    ans = 3
    for i in range(97,123):
        ans = min(ans, data.get(i,0))

    print(f"Case {tc}: {answer[ans]}")