N = int(input())
balls = input()
ans = float('inf')

ans = min(ans,
        balls.rstrip("R").count("R"),
        balls.rstrip("B").count("B"),
        balls.lstrip("R").count("R"),
        balls.lstrip("B").count("B")
        )

print(ans)