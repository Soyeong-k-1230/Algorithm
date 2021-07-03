// 채점 결과
// 정확성: 70.0
// 효율성: 0.0
// 합계: 70.0 / 100.0


let cnt = 0
let ans = []

function find(n, N, p, arr, k) {
    if (n === N) {
        cnt += 1
        ans.push(p)
        return
    }
    for (let i = 0; i < 3; i++) {
        find(n + 1, N, p + arr[i], arr, k)
    }

}

function solution(n) {
    let i = 0
    const arr = ['1', '2', '4']

    while (true) {
        i += 1
        find(0, i, '', arr, n)
        if (cnt >= n) {
            break
        }
    }
    return ans[n - 1]

}
