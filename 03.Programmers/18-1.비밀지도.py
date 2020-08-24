def change_binary(ans, arr, N):
    arr = list(map(bin, arr))
    for i in range(N):
        number = arr[i][1:].replace('b', '')
        if len(number) < N:
            number = '0' * (N - len(number)) + number
        for j in range(N):
            if number[j] == '1':
                ans[i][j] = '#'
    return ans

def solution(n, arr1, arr2):
    answer = [[' '] * n for _ in range(n)]
    answer = change_binary(answer, arr1, n)
    answer = change_binary(answer, arr2, n)

    for idx in range(n):
        answer[idx] = ''.join(answer[idx])

    return answer


print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))





