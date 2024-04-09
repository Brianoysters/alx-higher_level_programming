#!/usr/bin/node
let no_argument = 0;

exports.logMe = function (item) {
  console.log(no_argument + ': ' + item);
  no_argument++;
};
