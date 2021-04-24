from collections import deque

min_v = 1e10
dirs = [(0, 1, 0), (1, 0, 1), (0, -1, 2), (-1, 0, 3)]


def bfs(sr, sc, N, board):
    queue = deque()
    queue.append((sr, sc, 0))
    queue.append((sr, sc, 1))
    d = [[0] * N for _ in range(N)]

    while queue:
        r, c, w = queue.popleft()
        for dr, dc, dw in dirs:
            nr, nc = r + dr, c + dc

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if board[nr][nc]:
                continue
            if nr == 0 and nc == 0:
                continue

            tmp = 100
            if dw != w:
                tmp += 500

            if not d[nr][nc]:
                d[nr][nc] = d[r][c] + tmp
                queue.append((nr, nc, dw))
                continue

            if d[nr][nc] and d[nr][nc] >= d[r][c] + tmp:
                d[nr][nc] = d[r][c] + tmp
                queue.append((nr, nc, dw))
    return d


def solution(board):
    N = len(board)
    D = bfs(0, 0, N, board)
    return D[N - 1][N - 1]