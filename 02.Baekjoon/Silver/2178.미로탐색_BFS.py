import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
min_v = 1e10

def bfs(sr, sc):
    queue = deque()
    queue.append((sr, sc))
    visited = [[False] * M for _ in range(N)]
    d = [[0] * M for _ in range(N)]

    visited[sr][sc] = True

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if visited[nr][nc] or not board[nr][nc]:
                continue
            visited[nr][nc] = True
            d[nr][nc] = d[r][c] + 1
            queue.append((nr, nc))

    return d

D = bfs(0, 0)
print(D[N - 1][M - 1] + 1)