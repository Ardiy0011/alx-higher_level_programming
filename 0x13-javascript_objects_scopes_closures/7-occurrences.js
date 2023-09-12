#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
    let occurences = 0;

    for (let i = 0; i < list.length; i++) {
      if (list[i] === searchElement) {
        occurences++;// anytime the if statement is fulfilled increease the counter
      };
    };
    return occurences;
  };
