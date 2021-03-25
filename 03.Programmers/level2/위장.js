function solution(clothes) {
  let answer = 0
  let spy = {}
  const multiply = ( acc, cur ) => acc * cur
  
  clothes.forEach((ele) => {
      const name = ele[0]
      const type = ele[1]
      if(Object.keys(spy).includes(type)) {
          spy[type].push(name)
      } else {
          spy[type] = [name]
      }
  })

  const clothList = Object.values(spy)
  let clothCnt = clothList.map(x => x.length + 1)
  answer = clothCnt.reduce(multiply) - 1

  return answer
}