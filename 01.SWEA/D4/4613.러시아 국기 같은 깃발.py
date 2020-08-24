# 조합문제 >> 일반적인 조합 문제 보다는 쉽다.
# 선택해야 하는 개수가 정해져 있음 >> 2개
# 반복문으로도 처리가 가능함

# 멱집합 (부분집합)
# 조합
# 순열

def change_color(color, st, ed):
    cnt = 0
    for w in range(st, ed + 1):
        for k in range(M):
            if russia[w][k] != color:
                cnt += 1
    return cnt

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    russia = [input() for _ in range(N)]
    min_v = 1e10

    for i in range(0, N - 2):
        for j in range(i + 1, N - 1):
            tmp = change_color('W', 0, i) + change_color('B', i + 1, j) + change_color('R', j + 1, N - 1)
            min_v = min(min_v, tmp)

    print('#{} {}'.format(tc, min_v))

