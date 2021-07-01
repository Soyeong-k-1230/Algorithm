import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
dirs = [(0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1)]
M, N, H = map(int, input().split())
boards = [0] * H
for k in range(H):
    boards[k] = [list(map(int, input().split())) for _ in range(N)]

def bfs(start):
    queue = deque(start)

    while queue:
        h, r, c = queue.popleft()
        for dh, dr, dc in dirs:
            nh, nr, nc = h + dh, r + dr, c + dc
            if nh < 0 or nh >= H or nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not boards[nh][nr][nc]:
                boards[nh][nr][nc] = boards[h][r][c] + 1
                queue.append((nh, nr, nc))

st = []
for k in range(H):
    for i in range(N):
        for j in range(M):
            if boards[k][i][j] == 1:
                st.append((k, i, j))

bfs(st)
max_v = -1
for k in range(H):
    for i in range(N):
        for j in range(M):
            if not boards[k][i][j]:
                print(-1)
                exit()
            max_v = max(max_v, boards[k][i][j])

if max_v == 1:
    print(0)
else:
    print(max_v - 1)