function solution(genres, plays) {
  let answer = []
  let songs = {}
  let sum = {}
  
  for (let i = 0; i < genres.length; i++) {
      const genre = genres[i]
      if(!songs[genre]) {
          songs[genre] = {}
          sum[genre] = plays[i]
      } else {
          sum[genre] += plays[i]
      }
      songs[genre][i] = plays[i]
  }
  const genreSorted = Object.keys(sum).sort((a, b) => { return sum[b] - sum[a] })
  
  genreSorted.forEach((genre) => {
      const list = songs[genre]
      const sorted = Object.keys(list).sort((a, b) => { return list[b] - list[a] })
      answer = answer.concat(sorted.slice(0, 2))
  })

  return answer.map(x => Number(x))
}