import sys
sys.stdin = open('input.txt', 'r')
from collections import deque
W, H = map(int, input().split())
K = int(input())
boards = [[0] * W for _ in range(H)]
width = []
height = []
for _ in range(K):
    t, d = map(int, input().split())
    if t == 0:
        height.append(d)
    if t == 1:
        width.append(d)

height.sort(reverse=True)
width.sort(reverse=True)
w = deque([W])
h = deque([H])

for num in height:
    tmp = h.popleft()
    h.appendleft(tmp - num)
    h.appendleft(num)


for num in width:
    tmp = w.popleft()
    w.appendleft(tmp - num)
    w.appendleft(num)

print(max(h)*max(w))
