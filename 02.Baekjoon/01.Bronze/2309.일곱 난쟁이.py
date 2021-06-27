import sys
sys.stdin = open('../알고리즘 분류/03.백트래킹/input.txt', 'r')
# 값이 1개 이상일 경우 하나의 값만 출력하도록 exit()사용

N = 9
dwarfs = []
visited = [False] * N
p = [0] * 7
for _ in range(N):
    dwarfs.append(int(input()))

def backtrack(n, s, p, total):
    if total > 100:
        return
    if n == 7:
        if total == 100:
            ans = []
            for num in p:
                ans.append(dwarfs[num])
            ans.sort()
            for dwarf in ans:
                print(dwarf)
            exit()
        return
    for i in range(s, N):
        if not visited[i]:
            visited[i] = True
            p[n] = i
            backtrack(n + 1, i, p, total + dwarfs[i])
            visited[i] = False

backtrack(0, 0, p, 0)