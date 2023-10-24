#!/usr/bin/node
// script that prints response status code

const request = require('request');
const url = process.argv[2];

request(url, (err, res) => {
  if (err) {
    console.log('error:', err); 
  } else {
    console.log(`code: ${res.statusCode}`)
    
  }
});
