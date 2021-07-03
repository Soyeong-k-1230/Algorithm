// 정확성: 40.0
// 효율성: 0.0
// 합계: 40.0 / 100.0

function solution(n) {
    let i = 0
    const arr = ['1', '2', '4']
    let ans = []

    while (true) {
        i += 1
        let flag = true
        let words = i.toString()
        for (let j = 0; j < words.length; j++) {
            if (!arr.includes(words[j])) {
                flag = false
                break
            }
        }

        if (flag) {
            ans.push(i)
        }

        if (n === ans.length) {
            break
        }
    }

    return ans[n - 1].toString()
}