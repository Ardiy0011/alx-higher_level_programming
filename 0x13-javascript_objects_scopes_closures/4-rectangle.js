#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    };
  };
};


    print () {
      for (let i = 0; i < this.height; i++) {
        let msg = '';
        for (let j = 0; j < this.width; j++) {
          msg = msg + 'X';
        }
        console.log(msg);
      };
    };

    rotate () {
      const temp = this.width;
      this.width = this.height;
      this.height = temp;
    };

    double () {
      this.height *= 2;
      this.width *= 2;
    };
