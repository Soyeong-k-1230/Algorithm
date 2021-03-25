import sys
sys.stdin = open('input.txt', 'r')

def dfs(n, total, cnt):
    global minV
    if cnt == N:
        minV = min(minV, total)
        return

    for i in range(N):
        if not board[n][i]:
            continue
        if cnt == N - 1 and i == 0:
            dfs(i, total + board[n][i], cnt + 1)
        else:
            if visited[i]:
                continue
            visited[n] = True
            dfs(i, total + board[n][i], cnt + 1)
            visited[n] = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    minV = 1e10
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, minV))

