# DP
def fibo_dp(n):
    if fibo_memo[n] != -1:
        return fibo_memo[n]
    fibo_memo[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return fibo_memo[n]

N = int(input())
fibo_memo = [0, 1] + [-1] * (N - 1)
print(fibo_dp(N))
