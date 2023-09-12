#!/usr/bin/node

const { argv } = require('process');

const firstPhrase = argv[2];

if (isNaN(firstPhrase)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstPhrase}`);
}
