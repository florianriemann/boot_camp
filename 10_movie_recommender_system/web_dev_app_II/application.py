"""Here we define the flask application"""
from flask import Flask, render_template, request
from get_recommender import random_recommender


app = Flask(import_name=__name__)


@app.route("/")
#@app.route("/home")
def homepage():
    return render_template('home.html')



@app.route("/recommendations")
def recommendation():
    user_query =request.args.to_dict()
    #transform the values of the user query to integer
    user_query = {key:float(value) for key, value in user_query.items()}
    #print(user_query)
    top2 = random_recommender(user_query)

    return render_template(
        "recommendations.html",
        movies_list=top2
    )



if __name__ == "__main__":
    app.run(debug=True)

