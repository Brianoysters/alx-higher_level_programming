#!/usr/bin/node
//computes the number of tasks completed by user id

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const tasks_Completed = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!tasks_Completed[todo.userId]) {
        tasks_Completed[todo.userId] = 1;
      } else {
        tasks_Completed[todo.userId] += 1;
      }
    }
  });
  console.log(tasks_Completed);
});

