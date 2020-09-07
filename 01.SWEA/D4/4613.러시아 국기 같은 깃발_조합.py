def select_row(selected, idx, cnt):
    global result
    if cnt == 2:
        # 깃발을 세 부분으로 나눌 수 있음
        a = -1
        b = -1
        for i in range(N):
            if selected[i] and a == -1:
                a = i
            elif selected[i] and a != -1:
                b = i
        cnt = 0
        for i in range(a + 1):
            for j in range(M):
               if flag[i][j] != 'W':
                   cnt += 1
        for i in range(a + 1, b + 1):
            for j in range(M):
               if flag[i][j] != 'B':
                   cnt += 1
        for i in range(b + 1, N):
            for j in range(M):
               if flag[i][j] != 'R':
                   cnt += 1
        if cnt < result:
            result = cnt

        return 
    if idx >= N - 1:
        return 
    selected[idx] = 1
    select_row(selected, idx + 1, cnt + 1)
    selected[idx] = 0
    select_row(selected, idx + 1, cnt)
    
    
for tc in range(1, int(input()) + 1):
    M, N = map(int, input().split())
    flag = [input() for _ in range(N)]
    result = 2500
    select_row([0] * N)