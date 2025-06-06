import sys; input = sys.stdin.readline


def backtrack(now=""):
    if 0 < len(now) < 10:
        nums.append(int(now))
        if len(now) == 9: return
    
    for i in range(1,10):
        if str(i) in now: continue
        backtrack(now+(str(i)))

def solve():
    N = int(input())
    ans = 0
    left, right = 0, len(nums)
    while left < right:
        
        mid = (left+right) // 2
        if nums[mid] > N:
            ans = nums[mid]
            right = mid
        else:
            left = mid + 1

    return print(ans)

nums = []
backtrack()
nums.sort()
while True:
    try: solve()
    except: break
