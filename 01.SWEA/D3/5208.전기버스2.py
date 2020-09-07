def backtrack(n, cur, cnt):
    global min_v

    if cnt >= min_v:
        return

    if n == N:
        min_v = min(min_v, cnt)
        return

    # 배터리 갈때
    backtrack(n + 1, cnt + 1, stops[n])
    # 갈지 않았다
    if cur - 1 > 0:
        backtrack(n + 1, cnt, cur - 1)


for tc in range(1, int(input()) + 1):
    stops = list(map(int, input().split()))
    N = stops[0]
    min_v = 10000
    backtrack(1, 0, 0)
