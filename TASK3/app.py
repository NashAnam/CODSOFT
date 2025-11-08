from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

app = Flask(__name__)

# Load dataset
df = pd.read_csv('movies.csv')

# TF-IDF setup for movie descriptions
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(df['description'])
similarity = cosine_similarity(tfidf_matrix)

@app.route('/')
def home():
    genres = sorted(df['genre'].unique())
    return render_template('index.html', genres=genres)

@app.route('/recommend', methods=['POST'])
def recommend():
    selected_genres = request.form.getlist('genres')
    if not selected_genres:
        return render_template('index.html', message="Please select at least one genre!")

    # Filter movies from selected genres
    genre_movies = df[df['genre'].isin(selected_genres)].sort_values(by='rating', ascending=False)
    recommended = genre_movies.head(10).to_dict(orient='records')

    # Surprise pick (from any genre)
    surprise = random.choice(df[df['rating'] > 8.0].to_dict(orient='records'))

    return render_template('index.html', genres=sorted(df['genre'].unique()),
                           recommended=recommended, surprise=surprise)

if __name__ == '__main__':
    app.run(debug=True)
