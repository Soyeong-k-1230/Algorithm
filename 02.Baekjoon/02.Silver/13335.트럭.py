from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

n, w, L = map(int, input().split())
truck = deque(list(map(int, input().split())))
cnt = 0
arrive = []
queue = [0] * w

while len(arrive) != n:
    cnt += 1
    # 다리 건너기
    if queue[0]:
        arrive.append(queue[0])
    # 이동
    for i in range(w):
        if i - 1 >= 0:
            queue[i - 1] = queue[i]
        if i == w - 1:
            queue[i] = 0

    total = sum(queue)
    if len(truck):
        total += truck[0]
    if total <= L:
        if len(truck):
            queue[w - 1] = truck.popleft()

print(cnt)





