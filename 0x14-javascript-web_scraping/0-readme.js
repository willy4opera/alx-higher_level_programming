#!/usr/bin/node

const filesys = require('fs');
filesys.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
