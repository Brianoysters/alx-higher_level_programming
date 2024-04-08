#!/usr/bin/node
/*increaments and call a function*/
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
