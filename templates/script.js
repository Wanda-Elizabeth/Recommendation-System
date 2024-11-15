// Fetch top movies and display them
async function fetchTopMovies() {
    try {
        const response = await fetch('http://127.0.0.1:5001/top-movies');
        const movies = await response.json();

        const moviesGrid = document.getElementById('movies-grid');
        moviesGrid.innerHTML = ''; // Clear any existing movies

        movies.forEach(movie => {
            const movieCard = document.createElement('div');
            movieCard.classList.add('movie-card');

            movieCard.innerHTML = `
                <div class="top-badge">Top ${movie.rank}</div>
                <img src="${movie.imageUrl}" alt="${movie.title}">
                <div class="movie-info">
                    <h3>${movie.title}</h3>
                    ${movie.recentlyAdded ? '<div class="recently-added">Recently Added</div>' : ''}
                </div>
            `;

            moviesGrid.appendChild(movieCard);
        });
    } catch (error) {
        console.error('Error fetching top movies:', error);
    }
}

// Fetch top movies when the page loads
window.onload = fetchTopMovies;
