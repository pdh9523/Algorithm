import sys; input = lambda: sys.stdin.readline().rstrip()


data = dict()
# while True:
#     try:
#         word = input()
#         k = tuple(sorted(word))
#         data.setdefault(k, list()).append(word)
#     except: break

for word in sys.stdin.read().splitlines():
    k = tuple(sorted(word))
    data.setdefault(k, list()).append(word)

ans = dict()
for v in data.values():
    ans.setdefault(len(v), list()).append(sorted(v))

idx = 0
for k in sorted(ans.keys(), reverse=True):
    ans[k].sort(key=lambda x:x[0])
    for x in ans[k]:
        print(f"Group of size {k}: {" ".join(sorted(set(x)))} .")
        idx += 1
        if idx == 5: exit()
