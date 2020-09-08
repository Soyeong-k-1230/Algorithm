def dfs(n, total):
    global min_v

    if n == N:
        if total >= B:
            min_v = min(min_v, total)
        return

    dfs(n + 1, total + H[n])
    dfs(n + 1, total)


for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_v = 1e10

    dfs(0, 0)

    print('#{} {}'.format(tc, min_v - B))

