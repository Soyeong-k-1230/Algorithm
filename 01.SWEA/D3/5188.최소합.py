import sys
sys.stdin = open('input.txt', 'r')

dirs = [(0, 1), (1, 0)]
def dfs(r, c, total):
    global minV
    if total > minV:
        return
    if r == N - 1 and c == N - 1:
        minV = min(minV, total)
        return

    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        dfs(nr, nc, total + board[nr][nc])

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    minV = 1e10
    dfs(0, 0, board[0][0])

    print('#{} {}'.format(tc, minV))

