import sys
sys.stdin = open('input.txt', 'r')

N = 11

def diamond(n, players, total):
    global max_v
    if n == 11:
        max_v = max(max_v, total)
        return
    for j in range(N):
        if players[n][j] and not visited[j]:
            visited[j] = True
            diamond(n + 1, players, total + players[n][j])
            visited[j] = False


for tc in range(int(input())):
    max_v = -1
    players = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    diamond(0, players, 0)
    print(max_v)





