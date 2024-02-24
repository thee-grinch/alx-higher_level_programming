#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
  print () {
    let i;
    let j;
    let row = '';
    for (i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
}
module.exports = Rectangle;
