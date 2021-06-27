# + - * /
import sys
sys.stdin = open('input.txt', 'r')
N = int(input())
nums = list(map(int, input().split()))
ops = []
ops_input = list(map(int, input().split()))
for i in range(len(ops_input)):
    if ops_input[i]:
        tmp = ''
        if i == 0:
            tmp = '+'
        elif i == 1:
            tmp = '-'
        elif i == 2:
            tmp = '*'
        else:
            tmp = '/'
        for _ in range(ops_input[i]):
            ops.append(tmp)

def calculate(a, b, op):
    res = 0
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b
    if op == '/':
        if a < 0:
            return - ((-a) // b)
        return a // b

def dfs(n, total):
    global min_v, max_v
    if n == N - 1:
        min_v = min(min_v, total)
        max_v = max(max_v, total)
        return
    for i in range(N - 1):
        if not visited[i] and (i == 0 or ops[i - 1] != ops[i] or visited[i - 1]):
            visited[i] = True
            dfs(n + 1, calculate(total, nums[n + 1], ops[i]))
            visited[i] = False

visited = [False] * (N - 1)
min_v = 1e11
max_v = -1e11
dfs(0, nums[0])

print(max_v)
print(min_v)
