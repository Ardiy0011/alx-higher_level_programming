#!/usr/bin/node
// script that reads and prints to file

const fs = require('fs');

const path = process.argv[2];

fs.readFile(path, 'utf-8', (err, res) => {
  if (err) {
    console.error(err);
  } else {
    console.log(res);
  }
});
