#!/usr/bin/node

const datafetch = require('request');
const EpisodNum = process.argv[2];
const Api_link = 'https://swapi-api.hbtn.io/api/films/';

datafetch(Api_link + EpisodNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
