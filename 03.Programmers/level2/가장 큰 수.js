// 시간 초과
let maxAns = -1
function dfs(n, N, idx, numbers) {
    if(n === N) {
        let ans = ''
        idx.forEach((i) => {
            ans += numbers[i].toString()
        })
        maxAns = Math.max(Number(ans), maxAns)
        return
    }
    for(let num = 0; num < N; num++) {
        if(!idx.includes(num)) {
            idx.push(num)
            dfs(n + 1, N, idx, numbers)
            idx.pop()
        }
    }
}

function solution(numbers) {
    dfs(0, numbers.length, [], numbers)
    return maxAns.toString()
}