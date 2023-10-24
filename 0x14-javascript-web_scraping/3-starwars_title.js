const request = require('request');

path = process.argv[1]
const apiUrl = "https://swapi-api.alx-tools.com/api/films/:id";

request(apiUrl, (err, res, datas) => {
  if (id == path) {
    //convert to javascriptobject using parse method
    const data = JSON.parse(datas);
    console.log(data);
  } else {
    console.error('Error:', err);
  }
});
