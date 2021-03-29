function solution(priorities, location) {
  let answer = []
  const n = priorities.length
  let printer = []
  for(let i = 0; i < n; i++) {
      printer.push(i)
  }

  while(true) {
      if(answer.length === n) break

      const current = priorities[printer[0]]
      let maxValue = -1
      printer.slice(1).forEach((ele) => {
          maxValue = Math.max(maxValue, priorities[ele])
      })
      const tmp = printer.shift()
      if(current >= maxValue) answer.push(tmp) 
      else printer.push(tmp)
  }

  return answer.indexOf(location) + 1
}