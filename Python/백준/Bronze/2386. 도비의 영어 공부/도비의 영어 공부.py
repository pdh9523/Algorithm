import sys; input = lambda: sys.stdin.readline().rstrip()


while (q:=input()) != "#":
    s, *words = q.split()
    word = "".join(words).lower()
    print(s, word.count(s))