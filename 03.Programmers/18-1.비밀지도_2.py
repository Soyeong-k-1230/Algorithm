def solution(n, arr1, arr2):
    answer = [[' '] * n for _ in range(n)]
    arr1 = list(map(bin, arr1))
    arr2 = list(map(bin, arr2))

    for i in range(n):
        number1 = arr1[i][2:]
        if len(number1) < n:
            number1 = '0' * (n - len(number1)) + number1
        number2 = arr2[i][2:]
        if len(number2) < n:
            number2 = '0' * (n - len(number2)) + number2
        for j in range(n):
            if number1[j] == '1' or number2[j] == '1':
                answer[i][j] = '#'

    for idx in range(n):
        answer[idx] = ''.join(answer[idx])

    return answer


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))