import sys
input = sys.stdin.readline
from collections import deque


def get_connected(board, r, c, N, M):
    if board[r][c] == 0:
        return []

    color = board[r][c]
    visited = [[False] * M for _ in range(N)]
    queue = deque([(r, c)])
    visited[r][c] = True
    connected = [(r, c)]

    while queue:
        cr, cc = queue.popleft()

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if board[nr][nc] == color:
                    visited[nr][nc] = True
                    connected.append((nr, nc))
                    queue.append((nr, nc))

    return connected


def apply_gravity(board, N, M):
    for c in range(M):
        items = []
        for r in range(N):
            if board[r][c] != 0:
                items.append(board[r][c])

        for r in range(N - len(items)):
            board[r][c] = 0
        for i, val in enumerate(items):
            board[N - len(items) + i][c] = val


def copy_board(board):
    return [row[:] for row in board]


def dfs(board, clicks_left, N, M):
    if clicks_left == 0:
        return 0

    max_score = 0
    tried_groups = set()

    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                continue

            connected = get_connected(board, r, c, N, M)
            if not connected:
                continue

            group_key = tuple(sorted(connected))
            if group_key in tried_groups:
                continue
            tried_groups.add(group_key)

            score = len(connected) ** 2

            new_board = copy_board(board)
            for pr, pc in connected:
                new_board[pr][pc] = 0

            apply_gravity(new_board, N, M)

            future_score = dfs(new_board, clicks_left - 1, N, M)
            max_score = max(max_score, score + future_score)

    return max_score


M, N = map(int, input().split())
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)

result = dfs(board, 3, N, M)
print(result)
