#!/usr/bin/node
// const Rectangle = require('./4-rectangle');
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
