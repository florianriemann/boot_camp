"""Here we define the flask application"""
from flask import Flask, render_template, request 
from get_recommender import random_recommender

app = Flask(import_name=__name__)

@app.route("/")
#@app.route("/home")
def homepage():
    #return "Welcome to the amazing 🧄 📈 movie recommender"
    # return """
    # <h1> 🧄 📈 Movie Recommender </h1>
    # <p> Welcome to the amazing movie recommender</p>
    # <p> Click <a href="/recommendations">here</a> to get recommendations</p>
    # """
    return render_template('home.html')


@app.route("/recommendations")
def recommendation():
    user_query = request.args.to_dict()
    user_query = {key:int(value) for key, value in user_query.items()}
    print(user_query)
    top2 = random_recommender(user_query)
    #return f"{top2}"
    # return f"""
    #  <h1> 🎥 Recommendations </h1>
    #  <p> Hop on the sofa and watch one the folling movie:</p>
    #  <p>
    #  <ul style="list-style-type:none">
    #     <li>{top2[0]}</li>
    #     <li>{top2[1]}</li>
    #  </ul>
    #  </p>
    #  <p> Click <a href="/">here</a> to go home</p>
    # """
    # return render_template(
    #     'recommendations.html', 
    #     movie1=top2[0],
    #     movie2=top2[1]
    #     )
    return render_template(
        'recommendations.py',
        movies_list=top2
    )

if __name__ == "__main__":
    app.run(debug=True)