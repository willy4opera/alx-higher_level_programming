#!/usr/bin/node

const prc = process.argv[2];
const prcisn = isNaN(process.argv[2]);
if (prc === undefined || prcisn) {
  console.log('Missing number of occurrences');
} else {
  const x = Number(prc);
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
