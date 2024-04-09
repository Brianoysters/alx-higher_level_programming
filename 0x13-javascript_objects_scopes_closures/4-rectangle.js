#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let letter_p = '';
      for (let j = 0; j < this.width; j++) {
        letter_p += 'X';
      }
      console.log(letter_p);
    }
  }

  rotate () {
    const auxiliary = this.width;
    this.width = this.height;
    this.height = auxiliary;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
