import sys
sys.stdin = open('input.txt', 'r')

def lotto(n, s, N, visited, p, nums):
    if n == 6:
        for num in p:
            print(num, end=" ")
        print()
        return
    for i in range(s, N):
        if not visited[i]:
            visited[i] = True
            lotto(n + 1, i, N, visited, p + [nums[i]], nums)
            visited[i] = False

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        exit()
    k = nums[0]
    numbers = nums[1:]
    numbers.sort()
    visited = [False] * k
    lotto(0, 0, k, visited, [], numbers)
    print()

