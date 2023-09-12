#!/usr/bin/node

const { argv } = require('process')

const x = parseInt(argv[2])

function factorial (num) {
  if (num === 0) {
    return 1
  }

  return num * factorial(num - 1)
}

if (isNaN(x)) {
  console.log('1')
} else {
  console.log(`${factorial(x)}`);
}
