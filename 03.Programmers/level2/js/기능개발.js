function solution(progresses, speeds) {
  let answer = []
  let days = []
  
  for(let i = 0; i < speeds.length; i++) {
      let day = (100 - progresses[i]) / speeds[i]
      day = Math.ceil(day)
      days.push(day)
  }
  
  for(let i = 0; i < days.length; i++) {
      const prevMax = Math.max(...days.slice(0, i))
      if(days[i] > prevMax) answer.push(1) 
      else answer[answer.length - 1] += 1
  }
  
  return answer
}