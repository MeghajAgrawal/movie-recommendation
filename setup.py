from setuptools import setup

AUTHOR_NAME = 'MEGHAJ AGRAWAL'
SRC_REPO = 'SRC'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name = SRC_REPO,
    version='0.0.1',
    author= AUTHOR_NAME,
    description= "Movie Recommender",
    package = [SRC_REPO],
    python_requirements = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS
)