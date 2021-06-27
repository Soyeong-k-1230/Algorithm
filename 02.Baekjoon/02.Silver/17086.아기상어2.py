import sys
sys.stdin = open('input.txt', 'r')
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

from collections import deque


def bfs(st):
    queue = deque()
    for sr, sc in st:
        queue.append((sr, sc))

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nc < 0 or nc >= M or nr < 0 or nr >= N:
                continue
            if not box[nr][nc]:
                box[nr][nc] = box[r][c] + 1
                queue.append((nr, nc))

start = []
for i in range(N):
    for j in range(M):
        if box[i][j]:
            start.append((i, j))

bfs(start)
print(max(map(max, box)) - 1)