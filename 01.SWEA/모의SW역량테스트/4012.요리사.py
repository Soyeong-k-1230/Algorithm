# 1. 조합을 구한다.
# 2. 구해진 조합으로 점수를 구한다.
# 3. 점수의 차이가 최소인 경우 그 차이를 저장한다.
import sys
sys.stdin = open('input.txt', 'r')

def cook(n, food_a, s):
    global min_v
    if n == N // 2 - 1:
        food_b = []
        for i in range(N):
            if i not in food_a:
                food_b.append(i)
        sum_a = sum_b = 0
        for i in range(N // 2):
            for j in range(i + 1, N // 2):
                ar, ac = food_a[i], food_a[j]
                br, bc = food_b[i], food_b[j]
                sum_a += S[ar][ac] + S[ac][ar]
                sum_b += S[br][bc] + S[bc][br]
        min_v = min(min_v, abs(sum_a - sum_b))
        return

    for i in range(s, N):
        if not selected[i]:
            selected[i] = True
            food_a.append(i)
            cook(n + 1, food_a, i + 1)
            selected[i] = False
            food_a.pop()


for tc in range(1, int(input()) + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]
    selected = [False] * N
    min_v = 1e10
    cook(0, [0], 1)
    print('#{} {}'.format(tc, min_v))
