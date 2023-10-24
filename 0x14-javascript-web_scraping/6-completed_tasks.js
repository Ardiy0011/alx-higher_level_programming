#!/usr/bin/node
// script that tabulates completed tasks

const request = require('request')

const apiUrl = 'https://jsonplaceholder.typicode.com/todos'

request(apiUrl, (err, res, data) => {
  if (err) {
    console.log(err)
    return
  }
  const todos = JSON.parse(data)

  // Create an object to store the total completed tasks per user
  const userTasks = {}

  todos.forEach((todo) => {
    const userId = todo.userId

    if (todo.completed) {
      if (userTasks[userId]) {
        userTasks[userId]++
      } else {
        userTasks[userId] = 1
      }
    }
  })

  const output = JSON.stringify(userTasks, null, 2)
  console.log(output)
})
