from collections import deque
import math

dirs = [(0, 1, 0), (1, 0, 1), (0, -1, 2), (-1, 0, 3)]


def bfs(sr, sc, N, board, sw):
    queue = deque()
    queue.append((sr, sc, sw, 0))
    d = [[math.inf for _ in range(N)] for _ in range(N)]
    d[0][0] = 0

    while queue:
        r, c, w, cost = queue.popleft()
        for dr, dc, dw in dirs:
            nr, nc = r + dr, c + dc
            ncost = cost + 100
            if dw != w:
                ncost += 500

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if board[nr][nc]:
                continue
            if nr == 0 and nc == 0:
                continue

            if d[nr][nc] > ncost:
                d[nr][nc] = ncost
                queue.append((nr, nc, dw, ncost))
    return d


def solution(board):
    N = len(board)
    D1 = bfs(0, 0, N, board, 0)
    D2 = bfs(0, 0, N, board, 1)

    return min(D1[N - 1][N - 1], D2[N - 1][N - 1])