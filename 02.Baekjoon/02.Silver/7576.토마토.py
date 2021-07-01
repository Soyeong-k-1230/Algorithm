import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
M, N = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def bfs(start):
    queue = deque(start)

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if not boards[nr][nc]:
                boards[nr][nc] = boards[r][c] + 1
                queue.append((nr, nc))

st = []
for i in range(N):
    for j in range(M):
        if boards[i][j] == 1:
            st.append((i, j))

bfs(st)
max_v = -1
for i in range(N):
    for j in range(M):
        if boards[i][j] == 0:
            print(-1)
            exit()
        max_v = max(max_v, boards[i][j])

if max_v == 1:
    print(0)
else:
    print(max_v - 1)

