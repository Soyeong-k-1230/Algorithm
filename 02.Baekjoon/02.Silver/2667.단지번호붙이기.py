import sys
sys.stdin = open('input.txt', 'r')
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(r, c):
    global cnt
    cnt += 1
    visited[r][c] = True
    box[r][c] = 0
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        if not box[nr][nc] or visited[nr][nc]:
            continue
        dfs(nr, nc)

N = int(input())
box = [list(map(int, input())) for _ in range(N)]
ans = []
for i in range(N):
    for j in range(N):
        cnt = 0
        visited = [[False] * N for _ in range(N)]
        if box[i][j]:
            dfs(i, j)
            ans.append(cnt)
ans.sort()
print(len(ans))
for a in ans:
    print(a)
