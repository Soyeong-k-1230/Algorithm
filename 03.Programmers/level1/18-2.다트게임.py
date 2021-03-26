def solution(dartResult):
    answer = 0
    scores = [0] * 3; idx = 0; s_idx = 0

    while s_idx < 3:
        if dartResult[idx + 1] == 'S':
            scores[s_idx] = int(dartResult[idx])
        elif dartResult[idx + 1] == 'D':
            scores[s_idx] = int(dartResult[idx]) ** 2
        else:
            scores[s_idx] = int(dartResult[idx]) ** 3

        if idx + 2 > len(dartResult) - 1:
            break
        if dartResult[idx + 2].isdigit():
            idx += 2; s_idx += 1
        else:
            if dartResult[idx + 2] == '*':
                scores[s_idx] *= 2
                if s_idx > 0: scores[s_idx - 1] *= 2
            elif dartResult[idx + 2] == '#':
                scores[s_idx] *= (-1)
            elif dartResult[idx + 2] == 'S':
                scores[s_idx] = 10
            elif dartResult[idx + 2] == 'D':
                scores[s_idx] = 10 ** 2
            else:
                scores[s_idx] = 10 ** 3
            idx += 3; s_idx += 1
    answer = sum(scores)
    return answer


print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))

