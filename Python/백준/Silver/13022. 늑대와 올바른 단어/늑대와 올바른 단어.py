def check(word):
    now = "w"
    target = "wolf"
    idx = {t: i for i,t in enumerate(target)}
    visit = [0] * 4
    for char in word:
        if now == char:
            visit[idx[now]] += 1
        elif (nxt:=target[(idx[now]+1)%4]) == char:
            now = nxt
            if now == "w":
                if all(x==visit[0] for x in visit):
                    visit = [0] * 4
                else: return 0
            visit[idx[now]] += 1
        else: return 0

    return int(all(x == visit[0] for x in visit))

print(check(input()))
