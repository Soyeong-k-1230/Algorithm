import sys
import heapq

def dijkstra(s):
    D = [INF] * (V + 1)
    visit = [False] * (V + 1)
    pq = []

    D[s] = 0
    heapq.heappush(pq, [0, s])

    while pq:
        weight, node = heapq.heappop(pq)  # 가중치, 노드
        if weight > D[node]:
            continue
        visit[node] = True
        for v, w in G[node]:
            if not visit[v] and D[v] > D[node] + w:
                D[v] = D[node] + w
                heapq.heappush(pq, [D[v], v])

    return D

INF = float('inf')
V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    G[u].append([v, w])

D = dijkstra(K)
for i in range(1, V + 1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])