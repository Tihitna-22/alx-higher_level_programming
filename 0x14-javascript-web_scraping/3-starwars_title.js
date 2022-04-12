#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.
const request = require('request');
const id = process.argv[2];
const url = 'http://swapi.co/api/films/' + id;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const jsonDict = JSON.parse(body);
    console.log(jsonDict.title);
  }
});
