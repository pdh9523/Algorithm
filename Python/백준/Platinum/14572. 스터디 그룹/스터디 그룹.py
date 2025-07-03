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
data = dict()
while right < N:
    for known in students[right].knowns:
        data[known] = data.get(known, 0) + 1

    while left <= right and students[right].tier - students[left].tier > D:
        for known in students[left].knowns:
            data[known] -= 1
            if not data[known]: data.pop(known)
        left += 1
    right += 1
    
    length = len(data)
    e = (length - [*data.values()].count(right-left)) * (right-left)
    ans = max(ans, e)
print(ans)
