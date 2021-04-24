function solution(answers) {
  let answer = []
  let score = [0, 0, 0]
  const pA = [1, 2, 3, 4, 5]
  const pB = [2, 1, 2, 3, 2, 4, 2, 5]
  const pC = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
  
  for(let i = 0; i < answers.length; i++) {
      if(pA[i % pA.length] === answers[i]) {
          score[0] += 1
      }
      if(pB[i % pB.length] === answers[i]) {
          score[1] += 1
      }
      if(pC[i % pC.length] === answers[i]) {
          score[2] += 1
      }
  }
  const maxVal = Math.max(...score)
  score.forEach((ele, idx) => {
      if(ele === maxVal) answer.push(idx + 1)
  })
  
  return answer
}