#!/usr/bin/node

let lg = 0;

exports.logMe = function (item) {
  console.log(lg + ': ' + item);
  lg++;
};
