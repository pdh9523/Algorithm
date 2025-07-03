import sys; input = sys.stdin.readline


class Student:
    def __init__(self, tier, knowns):
        self.tier = tier
        self.knowns = knowns


N,K,D = map(int,input().split())

students = []
for _ in range(N):
    M,d = map(int,input().split())
    students.append(Student(d, [*map(int,input().split())]))
students.sort(key=lambda x: x.tier)

ans = 0
left,right = 0,0
cnt = [0] * (K+1)
t = 0
while right < N:
    for known in students[right].knowns:
        if cnt[known] == 0: t += 1
        cnt[known] += 1

    while left <= right and students[right].tier - students[left].tier > D:
        for known in students[left].knowns:
            cnt[known] -= 1
            if cnt[known] == 0: t -= 1
        left += 1
    right += 1
    
    e = (t - cnt.count(right-left)) * (right-left)
    ans = max(ans, e)
print(ans)
