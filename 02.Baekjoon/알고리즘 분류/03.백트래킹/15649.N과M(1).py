N, M = map(int, input().split())

def backtrack(n):
    if n == M:
        for num in p:
            print(num, end=" ")
        print()
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            p[n] = i + 1
            backtrack(n + 1)
            visited[i] = False

visited = [False] * N
p = [0] * M
backtrack(0)