# 길이 있는지 없는지 판단 => DFS
def dfs(v):
    global adj, N
    if v == 99:
        return 1
    if visited[v] == 1:
        return 0
    visited[v] = 1
    result1 = 0
    result2 = 0

    if adj[0][v] != 0:
        result1 = dfs(adj[0][v])
    if adj[1][v] != 0:
        result2 = dfs(adj[1][v])

    return result1 or result2

for _ in range(1, 11):
    tc, N = map(int, input().split())
    result = 0
    visited = [0] * 100
    path = list(map(int, input().split()))
    adj = [[0] * 100 for _ in range(2)]
    for i in range(0, len(path), 2):
        if adj[0][path[i]] == 0:
            adj[0][path[i]] = path[i + 1]
        else:
            adj[1][path[i]] = path[i + 1]
    result = dfs(0)
    print("#{} {}".format(tc, result))
