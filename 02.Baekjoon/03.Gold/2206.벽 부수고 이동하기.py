import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
N, M = map(int, input().split())
boards = [list(map(int, input())) for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(sr, sc):
    queue = deque([(sr, sc, 0)])
    d = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    d[sr][sc][0] = 1
    d[sr][sc][1] = 1

    while queue:
        r, c, t = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if t == 0:
                if boards[nr][nc] == 0 and not d[nr][nc][0]:
                    queue.append((nr, nc, 0))
                    d[nr][nc][0] = d[r][c][0] + 1
                if boards[nr][nc] == 1 and not d[nr][nc][1]:
                    queue.append((nr, nc, 1))
                    d[nr][nc][1] = d[r][c][0] + 1
            if t == 1:
                if boards[nr][nc] == 0 and not d[nr][nc][1]:
                    queue.append((nr, nc, 1))
                    d[nr][nc][1] = d[r][c][1] + 1
    return d

D = bfs(0, 0)

min_v = min(D[N - 1][M - 1])
max_v = max(D[N - 1][M - 1])

if min_v == 0:
    if max_v:
        print(max(D[N - 1][M - 1]))
    elif max_v == 0:
        print(-1)
else:
    print(min_v)