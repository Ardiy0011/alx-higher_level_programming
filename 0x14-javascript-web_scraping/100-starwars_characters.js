#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');
const film = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${film}`;
request(url, (err, res, data) => {
  if (!err) {
    const characters = JSON.parse(data).characters;
    characters.forEach((character) => {
      request(character, function (err, res, data) {
        if (!err) {
          console.log(JSON.parse(data).name);
        }
      });
    });
  }
});
