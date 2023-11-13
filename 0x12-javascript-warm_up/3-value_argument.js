#!/usr/bin/node

const k = process.argv[2] === undefined;
if (k) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
