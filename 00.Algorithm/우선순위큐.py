from heapq import heappush, heappop

queue = []
queue_tuple = []
# 일반 배열
arr = [1, 4, 5, 2, 6, 7, 0, 3, 9, 12, 4]
# 튜플 사용
arr_tuple = [(1, 2), (3,2), (2,3), (2, 5), (3, 1), (2, 2), (4, 4), (4, 2), (4, 1), (1, 1)]
ordered = []
ordered_tuple = []

for num in arr:
    heappush(queue, num)

while len(queue) > 0:
    tmp = heappop(queue)
    ordered.append(tmp)

print(ordered)

for tuple_num in arr_tuple:
    heappush(queue_tuple, tuple_num)

while len(queue_tuple) > 0:
    tmp = heappop(queue_tuple)
    ordered_tuple.append(tmp)

print(ordered_tuple)
