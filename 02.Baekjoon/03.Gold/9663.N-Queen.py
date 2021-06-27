def backtrack(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if visited[i]:
            continue
        flag_l = flag_r = True
        nr, nc_l = n, i
        while True:
            nr, nc_l = nr - 1, nc_l - 1
            if nr < 0 or nc_l < 0:
                break
            if board[nr][nc_l]:
                flag_l = False
                break
        nr, nc_r = n, i
        while True:
            nr, nc_r = nr - 1, nc_r + 1
            if nr < 0 or nc_r >= N:
                break
            if board[nr][nc_r]:
                flag_r = False
                break
        if flag_l and flag_r:
            board[n][i] = 1; visited[i] = True
            backtrack(n + 1)
            board[n][i] = 0; visited[i] = False

N = int(input())
board = [[0] * N for _ in range(N)]
visited = [False] * N
cnt = 0
backtrack(0)
print(cnt)
