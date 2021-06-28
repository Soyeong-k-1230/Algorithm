import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
boards = [list(map(int, input())) for _ in range(N)]
cnt = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ans = []
def dfs(r, c):
    global total
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >=N:
            continue
        if boards[nr][nc]:
            boards[nr][nc] = 0
            total += 1
            dfs(nr, nc)
total = 0
for i in range(N):
    for j in range(N):
        total = 0
        if boards[i][j]:
            cnt += 1
            total += 1
            boards[i][j] = 0
            dfs(i, j)
            ans.append(total)

ans.sort()
print(len(ans))
for num in ans:
    print(num)