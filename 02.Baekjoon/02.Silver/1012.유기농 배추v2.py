import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(100000)
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def dfs(r, c):
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc]:
            continue
        if boards[nr][nc]:
            visited[nr][nc] = True
            dfs(nr, nc)

for tc in range(int(input())):
    M, N, K = map(int, input().split())
    boards = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        c, r = map(int, input().split())
        boards[r][c] = 1

    for i in range(N):
        for j in range(M):
            if boards[i][j] and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j)
                cnt += 1
    print(cnt)
