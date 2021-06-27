import sys
sys.stdin = open('input.txt', 'r')

def calculate(a, op, b):
    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    else:
        result = a * b
    return result

def dfs(cnt, total):
    global ans
    if cnt == N // 2:
        ans = max(total, ans)
        return
    # 그냥 계산하기
    result = calculate(total, ops[cnt], nums[cnt + 1])
    # 재귀
    dfs(cnt + 1, result)
    # 괄호 넣어서 계산하기
    if cnt + 1 < N // 2:
        a = calculate(nums[cnt + 1], ops[cnt + 1], nums[cnt + 2])
        b = calculate(total, ops[cnt], a)
        dfs(cnt + 2, b)


N = int(input())
nums = []
ops = []
ans = -999999999999

for word in input():
    if word.isdigit():
        nums.append(int(word))
    else:
        ops.append(word)

dfs(0, nums[0])
print(ans)
