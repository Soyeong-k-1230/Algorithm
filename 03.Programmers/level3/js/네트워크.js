let visited = []

function dfs(n, computers, N) {

    visited.push(n)
    
    for(let i = 0;i < N; i++) {
        if(computers[n][i] && !visited.includes(i)) {
            dfs(i, computers, N)   
        }
    }
}

function solution(n, computers) {
    let cnt = 0
    for(let i = 0; i < n; i++) {
        if(!visited.includes(i)) {
            dfs(i, computers, n)
            cnt += 1
        }
    }

    return cnt
}