import pandas as pd
from surprise import Reader, Dataset, SVD, accuracy
from surprise.model_selection import train_test_split

# Load the MovieLens data into a pandas dataframe
ratings = pd.read_csv('ml-100k/u.data', delimiter='\t', header=None, names=['userId', 'movieId', 'rating', 'timestamp'])

# Load the movie information (you can use this to map movie IDs to movie names later)
movies = pd.read_csv('ml-100k/u.item', delimiter='|', header=None, encoding='latin-1', usecols=[0, 1], names=['movieId', 'title'])

# Merge ratings and movie dataframes to get movie titles
ratings = pd.merge(ratings, movies, on='movieId')

# Instantiate a reader with the rating scale and prepare data for Surprise
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

# Split the data into training and testing sets
trainset, testset = train_test_split(data, test_size=0.2)

# Instantiate and train the SVD model
model = SVD()
model.fit(trainset)

# Test the model and print the RMSE
predictions = model.test(testset)
print("RMSE: ", accuracy.rmse(predictions))

# Function to get the top N recommendations for each user
def get_top_n(predictions, n=10):
    top_n = {}
    for uid, iid, true_r, est, _ in predictions:
        if uid not in top_n:
            top_n[uid] = []
        top_n[uid].append((iid, est))
    
    # Sort and return the top N recommendations for each user
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    
    return top_n

# Example: Get top 10 recommendations for each user and print for user ID 1
top_n = get_top_n(predictions, n=10)
print("Recommendations for User 1:")
for movie_id, rating in top_n.get(1, []):
    movie_name = movies[movies['movieId'] == movie_id]['title'].values[0]
    print(f"{movie_name}: {rating}")

# Define train_model function outside of any loops
def train_model():
    # Load the MovieLens data
    ratings = pd.read_csv('ml-100k/u.data', delimiter='\t', header=None, names=['userId', 'movieId', 'rating', 'timestamp'])
    movies = pd.read_csv('ml-100k/u.item', delimiter='|', header=None, encoding='latin-1', usecols=[0, 1], names=['movieId', 'title'])

    # Merge ratings and movie data
    ratings = pd.merge(ratings, movies, on='movieId')

    # Setup for Surprise library
    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)

    # Split data and train the model
    trainset, testset = train_test_split(data, test_size=0.2)
    model = SVD()
    model.fit(trainset)

    # Test the model and get predictions
    predictions = model.test(testset)
    print("RMSE: ", accuracy.rmse(predictions))

    return predictions
