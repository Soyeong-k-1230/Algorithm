function solution(n, lost, reserve) {
  let answer = 0
  let rest = reserve
  lost.sort()
  for(let i = 1; i < n + 1; i++) {
      if(lost.includes(i)) {
          if(rest.includes(i)) {
              rest = rest.filter(ele => ele !== i)
              answer += 1
          } else {
              for(let j = 0; j < n; j++) {
                  if((rest[j] === i - 1 || rest[j] === i + 1) && !lost.includes(rest[j])){
                      rest = rest.filter(ele => ele !== rest[j])
                      answer += 1
                      break
                  }
              }
          }
      } else {
          answer += 1
      }
  }
  
  return answer
}