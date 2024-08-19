#!/usr/bin/node
// function that increment
exports.addMeMaybe = function (number, theFunction) {
  number++;
  theFunction(number);
};
