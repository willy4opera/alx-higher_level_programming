#!/usr/bin/node

const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    const dresult = JSON.parse(body).dresult;
    console.log(dresult.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1
        : count;
    }, 0));
  }
});
