#!/usr/bin/node

const { argv } = require('process')

const firstPhrase = argv[2]
const secondPhrase = argv[3]

console.log(`${firstPhrase} is ${secondPhrase}`)
