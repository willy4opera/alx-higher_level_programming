#!/usr/bin/node

const datafetch = require('request');
datafetch.get(process.argv[2]).on('response', function (response) {
  console.log(`code: ${response.statusCode}`);
});
