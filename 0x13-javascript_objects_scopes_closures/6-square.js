#!/usr/bin/node

const Sqr = require('./5-square.js');

module.exports = class Square extends Sqr {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
}
