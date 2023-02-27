"""Here we define functions to get movie recommendations"""

import random
import pickle
import numpy as np
from sklearn.decomposition import NMF
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# import the nmf pickled nmf model to implement the nmf_recommender function

with open('nmf_model1.pkl','rb') as file:
    nmf_model = pickle.load(file)

Q_matrix = nmf_model.components_
ratings_pivot = pd.read_csv('ratings_pivot.csv')
movie_list_df = pd.read_csv('movie_list_df.csv')
MOVIES = list(movie_list_df['movies'])

user_item = pd.read_csv('user_item.csv')
user_user = pd.read_csv('user_user.csv')
user_user_sklearn = pd.read_csv('user_user_sklearn.csv')
initial = pd.read_csv('initial.csv')

items = []
pred_ratings = []

# MOVIES = ["The Great Beauty","The Big Lebowsky","Don't Look UP",'In Bruges',"Toy Story","Avatar"]

def nmf_recommender(user_query={"The Great Beauty":1}):
    """it returns movie recommendations based on NMF algorithm"""
    new_user_dataframe = pd.DataFrame(data=user_query,
                                      columns=MOVIES,
                                      index=['new_user']
                                      )
    new_user_dataframe_imputed = new_user_dataframe.fillna(ratings_pivot.mean())
    P_new_user_matrix = nmf_model.transform(new_user_dataframe_imputed)
    #P_new_user = pd.DataFrame(data=P_new_user_matrix,index=['new_user'])
    R_hat_new_user_matrix = np.dot(P_new_user_matrix, Q_matrix)

    prediction = pd.DataFrame(R_hat_new_user_matrix, columns=new_user_dataframe_imputed.columns)
    prediction = prediction.T
    prediction.rename(columns={0: "movies"}, inplace=True)
    prediction = prediction.sort_values(by='movies', ascending=False)
    top10 = list(prediction.head(10).index)
    print(top10)
    return top10


def cosim_recommender(user_query={"The Great Beauty":1}):
    """it returns movie recommendations based on cosine similarities algorithm"""
    pass

def random_recommender(user_query={"The Great Beauty":1}):
    random.shuffle(MOVIES)
    top2 = MOVIES[:2]
    return top2

if __name__=='__main__':
    #top2 = random_recommender()
    #print(top2)
    top10 = nmf_recommender()
    print(top10)
    #top10 = cosim_recommender()
    #print(top10)