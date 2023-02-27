"""Here we define functions to get movie recommendations"""

import random
# import the nmf pickled nmf model to implement the nmf_recommender function
MOVIES = [
    "The Great Beauty",
    "The Big Lebowsky",
    "Don't Look UP",
    'In Bruges',
    "Toy Story",
    "Avatar"
]

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