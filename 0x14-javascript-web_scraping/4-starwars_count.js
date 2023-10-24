#!/usr/bin/node
// script that counts chraters with name

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, res, datas) => {
  if (err) {
    console.log(err);
    return;
  }

  const filmsData = JSON.parse(datas);
  const films = filmsData.results;

  let Count = 0;
  // iterate through first  and second layers
  films.forEach((film) => {
    film.characters.forEach((Url) => {
      if (Url.endsWith('/18/')) {
        Count++;
      }
    });
  });

  console.log(Count);
});
