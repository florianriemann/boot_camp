"""Here we define the flask application"""

from flask import Flask
from get_recommender import random_recommender

app = Flask(import_name=__name__)

@app.route('/') # A decorator is a function that takes in another function as a parameter and then returns a function.
def homepage():
    return """
    <h1> Garlic Boosting Recommender </h1>
    <p> Welcome to the amazing movie recommender </p>
    <p> Click <a href="/recommendations"></a> to get the recommendations </p>
    """
    

@app.route("/recommendations")
def recommendation():
    top2 = random_recommender()
    return f"""
    <h1> Movie Recommendations </h1>
    <> Hop on the couch and watch one of the following movies: </p>
    <p>
    <ul>
        <li>{top2[0]}</li>
        <li>{top2[1]}</li>   
    </ul>
    </p>
    </p> Click <a href="/">here
    """

if __name__ == "__main__":
    app.run(debug=True)

# run the application.py file in the terminal: python application.py 
# from the output you get the URL you can access












