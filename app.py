import pickle
import streamlit as st
import requests
from tmdbv3api import TMDb, Movie
import os
from dotenv import load_dotenv

load_dotenv()

st.header('Movies')
movies = pickle.load(open('Data/movie_list.pkl','rb'))
similarity = pickle.load(open('Data/similarity_list.pkl', 'rb'))

movie_list = movies['title'].values

selected_movie = st.selectbox('Type Movie', movie_list)
tmdb = TMDb()
tmdb.api_key = os.getenv('API_KEY')

def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb.api_key}'
    resp = requests.get(url)
    data = resp.json()
    poster_path = data['poster_path']
    if poster_path:
        full_path = f'https://image.tmdb.org/t/p/w500/{poster_path}'
    else:
        full_path = None
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x:x[1])
    recommended_movies = []
    recommended_movies_poster = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster


if st.button('Show Recommendation'):
    recommended_movies_list , movie_posters = recommend(selected_movie)
    columns = st.columns(5)
    for i, col in enumerate(columns):
        with col:
            st.text(recommended_movies_list[i])
            if movie_posters[i]:
                st.image(movie_posters[i])
            else:
                st.text("No image available")