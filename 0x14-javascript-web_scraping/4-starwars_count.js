#!/usr/bin/node
//prints num of movies where char “Wedge Antilles” is present.
const request = require('request');

if (process.argv.length !== 3) {
    console.error("Usage: node script.js <API_URL>");
    process.exit(1);
}

const apiUrl = process.argv[2];
const wedgeAntillesId = "18";

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(`An error occurred: ${error.message}`);
        process.exit(1);
    }

    if (response.statusCode !== 200) {
        console.error(`Failed to fetch data: ${response.statusCode}`);
        process.exit(1);
    }

    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach(film => {
        if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeAntillesId}/`)) {
            count++;
        }
    });

    console.log(count);
});

