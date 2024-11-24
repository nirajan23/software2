
document.getElementById('search').addEventListener('submit', function(event) {
    event.preventDefault();

    const searchTerm = document.getElementById('searchInput').value;


    fetch(`https://api.chucknorris.io/jokes/search?query=${searchTerm}`)
        .then(response => response.json())
        .then(data => {

            const jokesContainer = document.getElementById('jokesContainer');
            jokesContainer.innerHTML = ''; // Clear previous jokes

            data.result.forEach(joke => {
                const article = document.createElement('article');
                const p = document.createElement('p');
                p.textContent = joke.value;
                article.appendChild(p);
                jokesContainer.appendChild(article);
            });
        });
});
