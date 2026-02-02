ax,ay,bx,by,cx,cy,dx,dy = map(int,input().split())

def get_length(t):
    mx = ax + (bx - ax) * t
    my = ay + (by - ay) * t
    kx = cx + (dx - cx) * t
    ky = cy + (dy - cy) * t
    return ((mx - kx)**2 + (my - ky)**2)**0.5

def ternary_search():
    left, right = 0, 1

    while right - left >= 1e-9:
        left_mid = (left * 2 + right) / 3
        right_mid = (left + right * 2) / 3

        if get_length(left_mid) < get_length(right_mid):
            right = right_mid
        else:
            left = left_mid

    return get_length(left)

print(ternary_search())
