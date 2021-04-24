let answer = []

// 소수 구하기 O(√n)
function isPrime(number) {
    if(number < 2)  return false
    for(let i = 2; i * i <= number; i++) {
        if(number % i === 0) return false 
    }
    return true
}

function search(n, N, numbers, total, visited) {

    const number = Number(total)
    if(isPrime(number) && !answer.includes(number)) {
        answer.push(number)
    }

    if(n === N) return
    
    for(let i = 0; i < N; i++) {
        const num = numbers[i]
        if(!visited.includes(i)) {
            visited.push(i)
            search(n + 1, N, numbers, total + num, visited)
            visited.pop()
        }
    }
}

function solution(numbers) {
    const numbersList = numbers.split('')
    search(0, numbersList.length, numbersList, '', [])
    return answer.length
}