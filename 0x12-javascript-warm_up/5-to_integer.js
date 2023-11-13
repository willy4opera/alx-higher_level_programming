#!/usr/bin/node

const prc1 = isNaN(process.argv[2]);
const prc2 = process.argv[2];
if (prc1 || prc2 === undefined) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(prc2));
}
