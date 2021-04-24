function solution(brown, yellow) {
    const answer = []

    if(yellow === 1) return [3, 3]

    for(let i = yellow; i > 0; i--) {
        if(yellow % i === 0) {
            const width = i
            const height = yellow / i
            if ((width + height) * 2 + 4 === brown){
                return [width + 2, height + 2] 
            } 
        }
    }
    return answer
}