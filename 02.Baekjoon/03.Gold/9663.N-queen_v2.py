N = int(input())
boards = [[0] * N for _ in range(N)]
visited = [False] * N
cnt = 0
def check(r, c):
    nr, nc_l, nc_r = r, c, c
    while True:
        nr = nr - 1
        nc_l = nc_l - 1
        nc_r = nc_r + 1
        if nr < 0:
            break
        if nc_l >= 0 and boards[nr][nc_l]:
            return False
        if nc_r < N and boards[nr][nc_r]:
            return False

    return True

def n_queen(r):
    global cnt
    if r == N:
        cnt += 1
        return
    for c in range(N):
        if not visited[c] and check(r, c):
            visited[c] = True
            boards[r][c] = 1
            n_queen(r + 1)
            visited[c] = False
            boards[r][c] = 0

n_queen(0)
print(cnt)