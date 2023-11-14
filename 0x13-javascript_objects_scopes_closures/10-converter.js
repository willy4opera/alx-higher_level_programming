#!/usr/bin/node

exports.converter = function (base) {
  return function (num1) {
    return num1.toString(base);
  };
};
