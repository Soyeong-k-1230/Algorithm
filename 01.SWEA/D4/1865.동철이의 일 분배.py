import sys
sys.stdin = open('input.txt', 'r')
def backtrack(n, total):
    global max_v
    # 기존의 answer보다 작은 값은 계속 곱해봐야 더 작아질 것이기 때문에 재귀 끊는다.
    if total <= max_v:
        return
    if n == N:
        max_v = max(max_v, total)
        return
    for idx in range(N):
        if not selected[idx]:
            selected[idx] = True
            backtrack(n + 1, total * P[n][idx] / 100)
            selected[idx] = False

for tc in range(1, int(input()) + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    selected = [False] * N
    max_v = -1

    backtrack(0, 100)
    print('#%d' % tc, '%.6f' % max_v)
    # print('#{} {}'.format(tc, round(max_v, 6)))
