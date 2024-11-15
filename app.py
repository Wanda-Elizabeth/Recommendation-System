from flask import Flask, render_template

app = Flask(__name__)

@app.route('/top-movies')
def top_movies():
    movies_data = [
        {
            "imageUrl": "https://via.placeholder.com/200x300.png?text=Meet+Me+Next+Christmas",
            "rank": 1,
            "rating": 4.5,
            "recentlyAdded": True,
            "title": "Meet Me Next Christmas"
        },
        {
            "imageUrl": "https://via.placeholder.com/200x300.png?text=Hidden+Figures",
            "rank": 2,
            "rating": 4.7,
            "recentlyAdded": True,
            "title": "Hidden Figures"
        },
        {
            "imageUrl": "https://via.placeholder.com/200x300.png?text=White+House+Down",
            "rank": 3,
            "rating": 4.6,
            "recentlyAdded": True,
            "title": "White House Down"
        },
        {
            "imageUrl": "https://via.placeholder.com/200x300.png?text=Time+Cut",
            "rank": 4,
            "rating": 4.3,
            "recentlyAdded": True,
            "title": "Time Cut"
        },
        {
            "imageUrl": "https://via.placeholder.com/200x300.png?text=Umjolo",
            "rank": 5,
            "rating": 4.4,
            "recentlyAdded": True,
            "title": "Umjolo: The Gone Girl"
        },
        {
            "imageUrl": "https://via.placeholder.com/200x300.png?text=Knights+of+the+Zodiac",
            "rank": 6,
            "rating": 4.1,
            "recentlyAdded": True,
            "title": "Knights of the Zodiac"
        }
    ]
    return render_template('top_movies.html', movies=movies_data)

if __name__ == '__main__':
    app.run(debug=True)
