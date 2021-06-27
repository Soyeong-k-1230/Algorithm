from collections import deque
import sys
sys.stdin = open('../알고리즘 분류/02.큐/input.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    imp = list(map(int, input().split()))
    max_idx = max(imp)
    queue = deque([[i, imp[i]] for i in range(N)])
    print_q = []

    while queue:
        num, p = queue.popleft()
        if p == max_idx:
            print_q.append(num)
            if queue:
                max_idx = max([pr[1] for pr in queue])
        else:
            queue.append([num, p])
    print(print_q.index(M) + 1)
