#!/usr/bin/node

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';
const characterId = 18;

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(function (film) {
      const characters = film.characters;
      if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
        count++;
      }
    });

    console.log(count);
  }
});
