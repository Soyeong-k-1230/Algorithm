let cnt = 0
function dfs(n, N, total, target, numbers) {
    if(n === N) {
        if(total === target) cnt += 1
        return
    }
    dfs(n + 1, N, total + numbers[n], target, numbers)
    dfs(n + 1, N, total - numbers[n], target, numbers)
}

function solution(numbers, target) {
    const answer = 0
    dfs(0, numbers.length, 0, target, numbers)
    return cnt
}