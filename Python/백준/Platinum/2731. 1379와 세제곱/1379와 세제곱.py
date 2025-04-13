def backtrack(num_str, res=""):
    global ans 
    if len(num_str) == len(res):
        ans = res

    if ans: return
    for i in range(10):
        if str(int(str(i) + res)**3)[-len(res)-1:] == num_str[-len(res)-1:]:
            backtrack(num_str, str(i)+res)
            break

for _ in range(int(input())):
    ans = ""
    backtrack(input())
    print(int(ans))