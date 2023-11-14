#!/usr/bin/node

const arrg = process.argv.length <= 3;
if (arrg) {
  console.log('0');
} else {
  const arrgv = process.argv.slice(2).map(Number);
  const num2 = arrgv.sort(function (a, b) { return b - a; })[1];
  console.log(num2);
}
