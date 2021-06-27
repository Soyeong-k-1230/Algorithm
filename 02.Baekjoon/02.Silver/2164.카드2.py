from collections import deque
N = int(input())
cards = deque(list(map(int, range(1, N + 1))))
i = 0
while len(cards) > 1:
    tmp = cards.popleft()
    if i % 2:
        cards.append(tmp)
    i += 1
print(cards[0])

