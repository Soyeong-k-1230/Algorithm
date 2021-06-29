import sys
sys.stdin = open('input.txt', 'r')

N = 5
maps = [[False] * N for _ in range(N)]
boards = [list(map(int, input().split())) for _ in range(N)]
orders = [list(map(int, input().split())) for _ in range(N)]
l_cross = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]
r_cross = [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)]
cnt = 0
ans = 0

def check_h(r):
    for i in range(N):
        if not maps[r][i]:
            return False
    return True

def check_v(c):
    for i in range(N):
        if not maps[i][c]:
            return False
    return True

def check_cross(cross):
    for r, c in cross:
        if not maps[r][c]:
            return False
    return True

def find_position(num):
    for i in range(N):
        for j in range(N):
            if boards[i][j] == num:
                return [i, j]

for i in range(N):
    for j in range(N):
        cnt += 1
        r, c = find_position(orders[i][j])
        maps[r][c] = True
        if check_v(c):
            ans += 1
        if check_h(r):
            ans += 1
        if (r, c) in l_cross:
            if check_cross(l_cross):
                ans += 1
        if (r, c) in r_cross:
            if check_cross(r_cross):
                ans += 1

        if ans >= 3:
            print(cnt)
            exit()






