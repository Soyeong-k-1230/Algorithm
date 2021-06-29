import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
N = int(input())
boards = [list(map(int, input().split())) for _ in range(N)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def color(r, c, num):
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if boards[nr][nc] == 0:
            continue
        if visited[nr][nc]:
            continue
        visited[nr][nc] = True
        boards[nr][nc] = num
        color(nr, nc, num)

def get_distance(r, c, num):
    global cnt, min_v
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if boards[nr][nc] == num:
            continue
        if boards[nr][nc] == 0 and not visited[nr][nc]:
            visited[nr][nc] = True
            cnt += 1
            get_distance(nr, nc, num)
        if boards[nr][nc] != 0 and boards[nr][nc] != num:
            print('cnt', nr, nc, cnt)
            min_v = min(min_v, cnt)
            return

def bfs(sr, sc, num):
    queue = deque([(sr, sc)])
    d = [[0] * N for _ in range(N)]
    d[sr][sc] = 1

    while queue:
        r, c = queue.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            if boards[nr][nc] == num:
                continue
            if boards[nr][nc] == 0 and not d[nr][nc]:
                d[nr][nc] = d[r][c] + 1
                queue.append((nr, nc))
            if boards[nr][nc] != 0 and boards[nr][nc] != num:
                d[nr][nc] = d[r][c] + 1
                return d[nr][nc] - 2

    return 0



n = 1
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if boards[i][j] == 1:
            n += 1
            visited[i][j] = True
            boards[i][j] = n
            color(i, j, n)

min_v = 1e10

for i in range(N):
    for j in range(N):
        if boards[i][j]:

            D = bfs(i, j, boards[i][j])
            if D:
                min_v = min(min_v, D)
print(min_v)
