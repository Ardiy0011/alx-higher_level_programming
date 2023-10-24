const request = require('request')

const path = process.argv[2]
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${path}`

request(apiUrl, (err, res, datas) => {
  if (err) {
    console.log(err)
  } else {
    console.log(res.statusCode)
  }
  // convert to javascriptobject using parse method
  const data = JSON.parse(datas)
  const star_titles = data.title
  if (path) {
    console.log(star_titles)
  }
})
