function solution(bridge_length, weight, truck_weights) {
  let truck = []
  let truck_time = []
  let passed = []
  let answer = 0
  const reducer = (a, b) => a + b
  const N = truck_weights.length
  
  let i = 0
  let time = 1
  while (true) {

      for(let j = 0; j < truck.length; j++) {
          truck_time[j] += 1
      }
      // 트럭에서 내리기
      if(truck_time[0] > bridge_length) {
          const tmp = truck.shift()
          truck_time.shift()
          passed.push(tmp)
      }
      
      if(passed.length === N) break
      
      // 트럭에 타기
      truck.push(truck_weights[i])
      if(truck.reduce(reducer) <= weight) {
          truck_time.push(1)
          i++
      } else truck.pop()
      time++
  }

  answer = time
  return answer
}