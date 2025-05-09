import sys; input = sys.stdin.readline
from math import ceil


def fight(m_atk, m_hp, atk, hp, max_hp):
    user_cnt = ceil(m_hp / atk)
    monster_cnt = ceil(hp / m_atk)

    if user_cnt <= monster_cnt:
        return atk, hp - (m_atk * (user_cnt-1))
    else:
        return atk, 0

def heal(p_atk, p_hp, atk, hp, max_hp):
    return atk + p_atk, min(max_hp, p_hp + hp)

def check(atk, max_hp):
    hp = max_hp
    for q,a,b in arr:
        atk, hp = query[q](a, b, atk, hp, max_hp)
        if hp == 0: return False
    return True

query = {
    1: fight,
    2: heal
}

N,P = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

left,right = 0, N*1000000*1000000

ans = 0
while left <= right:
    mid = (left+right) // 2
    if check(P, mid):
        ans = mid
        right = mid - 1
    else:
        left = mid + 1

print(ans)