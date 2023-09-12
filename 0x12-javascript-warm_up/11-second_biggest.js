#!/usr/bin/node

const { argv } = require('process')

if (argv.length <= 3) {
  console.log('0')
} else {
  let largest = parseInt(argv[2])
  let secondLargest = parseInt(argv[3])

  if (secondLargest > largest) {
    [largest, secondLargest] = [secondLargest, largest]
  }

  for (let i = 4; i < argv.length; i++) {
    const current = parseInt(argv[i])

    if (current > largest) {
      secondLargest = largest
      largest = current
    } else if (current > secondLargest && current !== largest) {
      secondLargest = current
    }
  }

  console.log(secondLargest)
}
