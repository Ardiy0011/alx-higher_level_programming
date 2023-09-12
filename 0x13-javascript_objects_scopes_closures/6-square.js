#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }


  CharPrint (c) {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      if (c === undefined) {
        c = 'X';
      }
      console.log(c.repeat(this.width));
    }
  }
};
