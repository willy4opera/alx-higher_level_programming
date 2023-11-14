#!/usr/bin/node

const prc2 = process.argv[2];
const prc3 = isNaN(process.argv[2]);
if (prc2 === undefined || prc3) {
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  let i = 0;
  while (i < x) {
    console.log('X'.repeat(x));
    i++;
  }
}
