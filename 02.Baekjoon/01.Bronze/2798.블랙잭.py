import sys
sys.stdin = open('../알고리즘 분류/03.백트래킹/input.txt', 'r')

ans = -1
N, M = map(int, input().split())
cards = list(map(int, input().split()))
visited = [False] * N

def backtrack(n, s, total):
    global ans
    if total > M:
        return
    if n == 3:
        ans = max(total, ans)
        return
    for i in range(s, N):
        if not visited[i]:
            visited[i] = True
            backtrack(n + 1, i, total + cards[i])
            visited[i] = False

backtrack(0, 0, 0)
print(ans)
