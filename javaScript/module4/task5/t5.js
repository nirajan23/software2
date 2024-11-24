
fetch('https://api.chucknorris.io/jokes/random')
    .then(response => response.json())
    .then(data => {
        console.log("Chuck Norris Joke:", data.value);
    });
