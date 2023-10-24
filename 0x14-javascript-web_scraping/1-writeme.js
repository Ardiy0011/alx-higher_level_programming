#!/usr/bin/nodec
//s cript that writes to file

const fs = require('fs');
const path = process.argv[2];
const string = process.argv[3];

fs.writeFile(path, string, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
