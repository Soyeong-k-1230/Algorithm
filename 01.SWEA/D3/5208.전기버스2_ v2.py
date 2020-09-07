def dfs(n, remain, cnt):
    global min_v
    if cnt >= min_v:
        return
    if n == N:
        min_v = min(min_v, cnt)
        return

    # 교체 함
    dfs(n + 1, stops[n], cnt + 1)

    # 교체 안함
    if remain - 1 > 0:
        dfs(n + 1, remain - 1, cnt)


for tc in range(1, int(input()) + 1):
    stops = list(map(int, input().split()))
    N = stops[0]
    min_v = 1e10
    dfs(1, 0, 0)
    print('#{} {}'.format(tc, min_v - 1))
