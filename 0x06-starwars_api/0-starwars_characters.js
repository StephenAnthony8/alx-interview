#!/usr/bin/node
/* logs all starwars characters as shown in the characters list */

const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const chArr = (JSON.parse(res.body).characters);
  for (const character of chArr) {
    await new Promise((resolve, reject) => {
      request(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
