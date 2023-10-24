#!/usr/bin/node

const request = require('request')
const fs = require('fs')

const apiUrl = process.argv[2]
const file = process.argv[3]

request(apiUrl, (err, res, data) => {
  if (err) {
    console.log(err)
    return
  }

  // parse data to javascript object
  const allContent = data

  // write data to the file
  fs.writeFile(file, allContent, 'utf-8', (err) => {
    if (err) {
      console.error(err)
    }
  })
})
