import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)
    t = sorted(list(map(int, input().split())), reverse=True)
    ans = 0
    idx = 0
    for i in range(N):
        if idx == M:
            break
        if w[i] <= t[idx]:
            ans += w[i]
            idx += 1
    print('#{} {}'.format(tc, ans))




