from setuptools import setup

AUTHOR_NAME = 'MEGHAJ AGRAWAL'
SRC_REPO = 'Movie_Recommendation'
LIST_OF_REQUIREMENTS = ['streamlit','pandas','numpy','pickle','requests','tmdbv3api','os','dotenv','ast','nltk','scikit-learn']

setup(
    name = SRC_REPO,
    version='0.0.1',
    author= AUTHOR_NAME,
    description= "Movie Recommender",
    packages= ['Data', 'Archive'],
    python_requirements = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS
)