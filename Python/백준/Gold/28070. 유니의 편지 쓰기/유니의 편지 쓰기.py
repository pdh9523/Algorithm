import sys; input = sys.stdin.readline


def str_to_int(month: str) -> int:
    year, month = month.split("-")
    return int(year)*100 + int(month)

def int_to_str(month: int) -> str:
    year,month = divmod(month, 100)
    return f"{year}-{month:02}"

arr = [] 
for _ in range(int(input())):
    s,e = map(str_to_int, input().split())
    arr.append((s,-1))
    arr.append((e,1))

arr.sort()

now = 0
max_v = 0
ans = ""
for yyyymm, i in arr:
    now -= i
    if now > max_v:
        ans = yyyymm
        max_v = now

print(int_to_str(ans))