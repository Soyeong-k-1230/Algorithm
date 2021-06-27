N, M = map(int, input().split())
def backtrack(n, p, s):
    if n == M:
        for i in range(M):
            print(p[i], end=' ')
        print()
        return
    for i in range(s, N):
        if not visited[i]:
            p[n] = i + 1; visited[i] = True
            backtrack(n + 1, p, i + 1)
            p[n] = 0; visited[i] = False

p = [0] * M
visited = [False] * N
backtrack(0, p, 0)