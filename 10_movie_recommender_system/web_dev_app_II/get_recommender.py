"""Here we define functions to get movie recommendations"""

import random
import pandas as pd
import pickle 
# import the nmf pickled nmf model to implement the nmf_recommender function
with open('nmf_model1.pkl','rb') as file:
    loaded_model = pickle.load(file)

ratings_extended = pd.read_csv('ratings_extended.csv')

MOVIES = list(ratings_extended['title'].unique())
print(MOVIES)

# https://www.google.com/search?q=Import+%22pandas%22+could+not+be+resolved+from+sourcePylance&oq=Import+%22pandas%22+could+not+be+resolved+from+sourcePylance&aqs=chrome.0.69i59j0i10i512l2j0i10i22i30l6j0i22i30.957j0j7&sourceid=chrome&ie=UTF-8
# https://medium.com/@jwu2/improving-collaborative-filtering-with-clustering-88c63bdae7cc
'''
MOVIES = [
    "The Great Beauty",
    "The Big Lebowsky",
    "Don't Look UP",
    'In Bruges',
    "Toy Story",
    "Avatar"
]
'''

def nmf_recommender(user_query={"The Great Beauty":1}):
    """it returns movie recommendations based on NMF algorithm"""
    pass


def cosim_recommender(user_query={"The Great Beauty":1}):
    """it returns movie recommendations based on cosine similarities algorithm"""
    pass


def random_recommender(user_query={"The Great Beauty":1}):
    random.shuffle(MOVIES)
    top2 = MOVIES[:2]
    return top2


if __name__=='__main__':
    top2 = random_recommender()
    print(top2)