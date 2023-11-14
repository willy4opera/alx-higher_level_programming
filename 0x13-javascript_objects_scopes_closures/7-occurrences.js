#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let numi = 0; numi < list.length; numi++) {
    if (searchElement === list[numi]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
