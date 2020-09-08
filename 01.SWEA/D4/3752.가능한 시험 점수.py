for tc in range(1, int(input()) + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    M = 100 ** 2
    check = [0] * M
    check[0] = 1

    for score in scores:
        numbers = []

        for num in range(M):
            if check[num]:
                numbers.append(num)

        for number in numbers:
            if check[number] and not check[number + score]:
                check[number + score] = 1

    print('#{} {}'.format(tc, check.count(1)))


# dfs로 풀면 시간초과남
# check배열에 표시해 나가면서 반복으로 풀어야함.
