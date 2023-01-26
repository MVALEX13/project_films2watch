
from flask import Flask, render_template, request

import sqlite3

connection = sqlite3.connect("movies.db")                                # we establish the connection to the database
cursor = connection.cursor()                                             # tool allowing us to interact with the database

app = Flask(__name__)

FILMS = {}

@app.route("/", methods = ["GET"])
def index():
    if not request.args.get("movie_name"):                              # only if the user filled the dorm
        return render_template("empty.html")
    else:
        movie_name = request.args.get("movie_name")
        movie_rating = request.args.get("movie_rating")
        FILMS[movie_name] = movie_rating
        #cursor.execute("INSERT INTO movies (movie,rating) VALUES(?,?)",movie_name,movie_rating)   # we insert the new data in the database
        return render_template("index.html", films = FILMS)


connection.close()                                                      # we close the connection to the database