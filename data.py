import pandas as pd
import ast
import pickle
from nltk import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

movies = pd.read_csv('Archive/tmdb_5000_movies.csv')
credits = pd.read_csv('Archive/tmdb_5000_credits.csv')

movies = movies.merge(credits, on = 'title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

def convert(text):
    l = []
    for i in ast.literal_eval(text):
        l.append(i['name'].replace(" ",''))
    return l

def convert_cast(text):
    return convert(text)[:3]

def convert_crew(text):
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            return [i['name'].replace(" ",'')]
    return ['']

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert_cast)
movies['crew'] = movies['crew'].apply(convert_crew)

movies['overview'] = movies['overview'].apply(lambda x:x.split())

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

new_df = movies[['movie_id', 'title', 'tags']]

ps = PorterStemmer()
def stems(text):
    return " ".join([ps.stem(word) for word in text])
new_df['tags'] = new_df['tags'].apply(stems)

cv = CountVectorizer(max_features=5000, stop_words='english')

vector = cv.fit_transform(new_df['tags']).toarray()

similarity = cosine_similarity(vector)

pickle.dump(new_df, open('Data/movie_list.pkl', 'wb'))
pickle.dump(similarity, open('Data/similarity_list.pkl', 'wb'))

def recommend(movie):
    index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key= lambda x:x[1])
    for i in distances[1:6]:
        print(new_df.iloc[i[0]].title)

recommend("Avatar")