let answer = 1e10
function search(n, ans, target, words, visited) {
    if(ans === target) {
        answer = Math.min(answer, n)
        return
    }
    for(let i = 0; i < words.length; i++) {
        if(!visited.includes(i)) {
            const next = words[i].split('')
            const cnt = ans.split('').filter((ele, idx) => ele !== next[idx]).length
            if(cnt === 1) {
                visited.push(i)
                search(n + 1, words[i], target, words, visited)
                visited.pop()
            }
        }
    }
}

function solution(begin, target, words) {
    if(!words.includes(target)) return 0
    search(0, begin, target, words, [])
    return answer
}