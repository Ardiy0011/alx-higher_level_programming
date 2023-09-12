#!/usr/bin/node
exports.converter = function (radix) {
    return (number) => {
      return number.toString(radix);
    };
  };
