#!/usr/bin/node

const request = require ('request');
const movieId = process.argv[2];

if (!movieId) {
    console.error('Please provide a Movie ID as the first argument.');
    process.exit(1);
}

const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

request(filmUrl, { json: true }, (err, res, body) => {
    if (err) {
        return console.error(err);
    }

    if (res.statusCode !== 200) {
        return console.error(`Failed to fetch film data: ${res.statusCode}`);
    }

    const characterUrls = body.characters;

    characterUrls.forEach((url) => {
        request(url, { json: true }, (err, res, body) => {
            if (err) {
                return console.error(err);
            }

            if (res.statusCode !== 200) {
                return console.error(`Failed to fetch character data: ${res.statusCode}`);
            }

            console.log(body.name);
        });
    });
});
