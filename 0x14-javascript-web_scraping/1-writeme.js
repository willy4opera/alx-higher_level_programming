#!/usr/bin/node

"Create A new Files System Object filesys"

const filesys = require('fs');
filesys.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
