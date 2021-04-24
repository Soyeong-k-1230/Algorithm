function solution(citations) {
  const sorted = citations.sort((a, b) => a - b)
  let answer = 0
  for(let i = 0; i < sorted[citations.length - 1]; i++) {
      const book = i
      for(let j = 0; j < citations.length; j++) {
          const leftCnt = sorted.slice(0, j).length
          const rightCnt = sorted.slice(j).length
          if(sorted[j] >= book && book <= rightCnt && book >= leftCnt) {
              answer = Math.max(book, answer)
          }
      }
  }
  return answer
}