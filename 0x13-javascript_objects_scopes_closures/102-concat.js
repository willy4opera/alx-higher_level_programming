#!/usr/bin/node

const fils = require('fs');

const fArgs = fils.readFileSync(process.argv[2]).toString();
const sArgs = fils.readFileSync(process.argv[3]).toString();
fils.writeFileSync(process.argv[4], fArgs + sArgs);
