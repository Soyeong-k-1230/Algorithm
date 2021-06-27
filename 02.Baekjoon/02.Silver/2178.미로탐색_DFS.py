import sys
sys.stdin = open('input.txt', 'r')
# ==> 시간초과!

N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
min_v = 1e10
visited = [[False] * M for _ in range(N)]

def dfs(r, c, cnt):
    global min_v

    if cnt >= min_v:
        return

    if r == N - 1 and c == M - 1:
        min_v = min(cnt, min_v)
        return

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= M:
            continue
        if visited[nr][nc] or not board[nr][nc]:
            continue
        visited[nr][nc] = True
        dfs(nr, nc, cnt + 1)
        visited[nr][nc] = False

visited[0][0] = True
dfs(0, 0, 1)
print(min_v)
