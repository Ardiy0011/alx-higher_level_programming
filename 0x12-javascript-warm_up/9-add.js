#!/usr/bin/node

const { argv } = require('process');

const first_phrase = parseFloat(argv[2]);
const second_phrase = parseFloat(argv[3]);

function add (a, b) {
  console.log(a + b);
}
  add(first_phrase, second_phrase);
