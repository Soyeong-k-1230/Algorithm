1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
let answer = []
function dfs(n, N, start, visited, total, tickets) {
    if(total.length === N + 1) {
        answer.push([...total])
        return
    }
    for(let i = 0; i < N; i++) {
        if(!visited.includes(i) && start === tickets[i][0]) {
            visited.push(i)
            total.push(tickets[i][1])
            dfs(n + 1, N, tickets[i][1], visited, total, tickets)
            visited.pop()
            total.pop()
        }
    }

}

function solution(tickets) {
    const sorted = tickets.sort((a, b) => {
        const wordA = a[1]
        const wordB = b[1]
        if(wordA > wordB) return 1
        else if(wordA < wordB) return -1
        else return 0
    })
    dfs(0, sorted.length, 'ICN', [], ['ICN'], sorted)
    return answer[0]
}