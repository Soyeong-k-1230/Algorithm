import sys
sys.stdin = open('input.txt', 'r')
sys.setrecursionlimit(1000000)

M, N, K = map(int, input().split())
boards = [[0] * N for _ in range(M)]
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for _ in range(K):
    a, b, c, d = map(int, input().split())
    # A(M - d, a), B(M - b - 1, c - 1)
    for i in range(M - d, M - b):
        for j in range(a, c):
            boards[i][j] = 1

ans = []
cnt = 0

def dfs(r, c):
    global cnt

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= M or nc < 0 or nc >= N:
            continue
        if not boards[nr][nc]:
            boards[nr][nc] = 1
            cnt += 1
            dfs(nr, nc)

for i in range(M):
    for j in range(N):
        if not boards[i][j]:
            boards[i][j] = 1
            cnt += 1
            dfs(i, j)
            ans.append(cnt)
            cnt = 0
            
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i], end=" ")
