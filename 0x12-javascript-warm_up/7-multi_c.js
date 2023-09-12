#!/usr/bin/node

const { argv } = require('process')
const x = argv[2]

const myVar = 'C is fun'

if (isNaN(x)) {
  console.log('Missing number of occurrences')
}

for (let i = 0; i < x; i++) {
  console.log(myVar)
}
