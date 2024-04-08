#!/usr/bin/node
/*execute x times a function*/
exports.callMeMoby = function (x, theFunction) {
  for (let index = 0; index < x; index++) {
    theFunction();
  }
};
