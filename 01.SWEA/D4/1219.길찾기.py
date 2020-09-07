def dfs(v):
    global ans
    if v == 99:
        ans = 1
        return
    if visited[v]:
        ans = 0
        return
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfs(w)

for _ in range(1, 11):
    ans = 0
    tc, N = map(int, input().split())
    arr = list(map(int, input().split()))
    visited = [False] * 100
    G = [[] for _ in range(N)]
    for i in range(0, N * 2, 2):
        G[arr[i]].append(arr[i + 1])
    dfs(0)
    print('#{} {}'.format(tc, ans))
