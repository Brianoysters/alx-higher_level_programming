#!/usr/bin/node
//script prints the title of a Star Wars movie
const request = require('request');

if (process.argv.length !== 3) {
    console.error("Usage: node script.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
const mov_url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(mov_url, (error, response, body) => {
    if (error) {
        console.error(`An error occurred: ${error.message}`);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to fetch data: ${response.statusCode}`);
        process.exit(1);
    }

    const mov = JSON.parse(body);
    if (mov.title) {
        console.log(mov.title);
    } else {
        console.error("Movie not found");
    }
});

