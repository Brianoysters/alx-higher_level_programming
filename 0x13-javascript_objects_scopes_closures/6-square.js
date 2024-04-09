#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let letter_p = '';
      for (let j = 0; j < this.width; j++) {
        letter_p += c;
      }
      console.log(letter_p);
    }
  }
}

module.exports = Square;
