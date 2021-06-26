import sys
read = sys.stdin.readline
from collections import deque
queue = deque()
for i in range(int(read())):
    order = list(read().strip().split())
    if order[0] == 'push':
        queue.append(order[1])
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif order[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            tmp = queue.popleft()
            print(tmp)



