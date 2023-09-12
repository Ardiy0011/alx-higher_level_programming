#!/usr/bin/node

const { argv } = require('process')
const x = argv[2]

if (isNaN(x)) {
  console.log('Missing size')
}

for (let i = 1; i <= x; i++) {
  for (let j = 0; j < x; j++) {
    process.stdout.write('x')
  }
  console.log()
}
