"""Here we define the flask application"""
from flask import Flask, render_template, request
from get_recommender import random_recommender, nmf_recommender, cosim_recommender

app = Flask(import_name=__name__)

@app.route("/")
def homepage(): 
    return render_template('home.html')

@app.route("/recommendations")
def recommendation():
    user_query =request.args.to_dict()
    user_query = {key:float(value) for key, value in user_query.items()}
    #top2 = random_recommender(user_query)
    top10 = nmf_recommender(user_query)
    #top10 = cosim_recommender(user_query)
    return render_template(
        "recommendations.html",
        #movies_list=top2
        movies_list=top10
    )

if __name__ == "__main__":
    app.run(debug=True)
