#!/usr/bin/node

const filesys = require('fs');
filesys.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
