nums = []
max_v = 0


def calculate(opers):
    global nums
    num_list = nums.copy()

    for oper in opers:
        flag = True
        for ele in nums:
            if not ele.isdigit() and ele == oper:
                idx = num_list.index(ele)
                tmp = 0
                if ele == '+':
                    tmp = int(num_list[idx - 1]) + int(num_list[idx + 1])
                elif ele == '-':
                    tmp = int(num_list[idx - 1]) - int(num_list[idx + 1])
                elif ele == '*':
                    tmp = int(num_list[idx - 1]) * int(num_list[idx + 1])

                if len(num_list) != 3:
                    if idx - 1 == 0:
                        num_list = [tmp] + num_list[idx + 2:]
                    elif idx + 1 == len(num_list) - 1:
                        num_list = num_list[:idx - 1] + [tmp]
                    else:
                        num_list = num_list[0:idx - 1] + [tmp] + num_list[idx + 2:]
                else:
                    num_list = [tmp]

    return abs(num_list[0])


def comb(n, N, opers, p):
    global max_v
    if n == N:
        ans = calculate(p)
        max_v = max(ans, max_v)
        return
    for i in range(N):
        if opers[i] not in p:
            comb(n + 1, N, opers, p + [opers[i]])


def solution(expression):
    answer = 0
    global nums, max_v
    opers = []

    num = ''
    for s in expression:
        if s.isdigit():
            num += s
        else:
            nums.append(num)
            num = ''
            nums.append(s)
            if s not in opers:
                opers.append(s)

    nums.append(num)

    if len(nums) == 3:
        if nums[1] == '+':
            max_v = int(nums[0]) + int(nums[2])
        elif nums[1] == '-':
            max_v = int(nums[0]) - int(nums[2])
        elif nums[1] == '*':
            max_v = int(nums[0]) * int(nums[2])
    else:
        comb(0, len(opers), opers, [])

    return float(max_v)