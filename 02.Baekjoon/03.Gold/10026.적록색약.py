import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(100000)
N = int(input())
dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
boards = [list(input()) for _ in range(N)]

def dfs(r, c):
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if visited[nr][nc]:
            continue
        if boards[nr][nc] == boards[r][c]:
            visited[nr][nc] = True
            dfs(nr, nc)

cnt_n = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            cnt_n += 1
cnt_o = 0
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if boards[i][j] == 'G':
            boards[i][j] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            cnt_o += 1

print(cnt_n, cnt_o)

