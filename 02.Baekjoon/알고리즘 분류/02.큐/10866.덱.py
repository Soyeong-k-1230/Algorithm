from collections import deque
import sys
read = sys.stdin.readline
queue = deque()
for tc in range(int(read())):
    order = list(read().strip().split())
    if order[0] == 'push_back':
        queue.append(order[1])
    elif order[0] == 'push_front':
        queue.appendleft(order[1])
    elif order[0] == 'pop_front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif order[0] == 'pop_back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())
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
            print(queue[len(queue) - 1])




