N, M = map(int, input().split())
def backtrack(n, p, s):
    if n == M:
        for i in range(M):
            print(p[i], end=' ')
        print()
        return
    for i in range(s, N):
        p[n] = i + 1
        backtrack(n + 1, p, i)
        p[n] = 0

p = [0] * M
visited = [False] * N
backtrack(0, p, 0)
