#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let lack_of_Occurrences = 0;
  for (let i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      lack_of_Occurrences++;
    }
  }
  return lack_of_Occurrences;
};
