#!/usr/bin/node

const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let numi = 0; numi < this.height; numi++) {
      let sum = '';
      for (let numj = 0; numj < this.width; njumj++) {
        sum += c;
      }
      console.log(sum);
    }
  }
}

module.exports = Square;
