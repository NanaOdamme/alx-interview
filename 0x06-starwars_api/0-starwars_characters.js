#!/usr/bin/node

const request = require('request');

const MAX_RETRIES = 5;
const RETRY_DELAY = 2000; // 2 seconds

function fetchWithRetry(url, callback, retries = MAX_RETRIES) {
    request(url, (error, response, body) => {
        if (error) {
            if (retries > 0) {
                console.log(`Error fetching data. Retrying in ${RETRY_DELAY / 1000} seconds... (${MAX_RETRIES - retries + 1}/${MAX_RETRIES})`);
                setTimeout(() => fetchWithRetry(url, callback, retries - 1), RETRY_DELAY);
            } else {
                callback(error, null);
            }
        } else {
            callback(null, response, body);
        }
    });
}

function getMovieCharacters(movieId) {
    const baseUrl = 'https://swapi-api.alx-tools.com/api/films/';
    
    fetchWithRetry(`${baseUrl}${movieId}/`, (error, response, body) => {
        if (error) {
            console.error('Error fetching movie data:', error);
            return;
        }
        
        if (response.statusCode !== 200) {
            console.error('Error fetching movie data, status code:', response.statusCode);
            return;
        }
        
        const movieData = JSON.parse(body);
        const characters = movieData.characters;
        
        // Fetch and print each character's name
        characters.forEach((url) => {
            fetchWithRetry(url, (charError, charResponse, charBody) => {
                if (charError) {
                    console.error('Error fetching character data:', charError);
                    return;
                }
                
                if (charResponse.statusCode !== 200) {
                    console.error('Error fetching character data, status code:', charResponse.statusCode);
                    return;
                }
                
                const characterData = JSON.parse(charBody);
                console.log(characterData.name);
            });
        });
    });
}

// Get the movie ID from command-line arguments
const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a movie ID');
    process.exit(1);
}

// Fetch and print characters
getMovieCharacters(movieId);