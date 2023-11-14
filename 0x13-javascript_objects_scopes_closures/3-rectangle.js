#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let num = 0; num < this.height; num++) {
      let sum = '';
      for (let numj = 0; numj < this.width; numj++) {
        sum += 'X';
      }
      console.log(sum);
    }
  }
}

module.exports = Rectangle;
