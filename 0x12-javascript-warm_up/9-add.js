#!/usr/bin/node

const { argv } = require('process');
const first_phrase = parseInt(argv[2]);
const second_phrase = parseInt(argv[3]);

function add (a, b) {
  console.log(a + b);
}
  add(first_phrase, second_phrase);
