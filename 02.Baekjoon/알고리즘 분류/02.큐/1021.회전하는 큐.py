from collections import deque
import sys
sys.stdin = open('input.txt', 'r')

N, M = map(int, input().split())
order = list(map(int, input().split()))
queue = deque(list(map(int, range(1, N + 1))))
print(queue)