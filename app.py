
from flask import Flask,g, render_template, request, redirect

import sqlite3

app = Flask(__name__)


### FUNCTIONS ###

### return all the movies present in the database under the shape of a tab of dictionnary (1 row per movie) ###
def get_db_data():
    db = getattr(g,'_database', None)                               # we check if there is yet an established communication
    if db is None:
        conn = sqlite3.connect('movies.db')
        conn.row_factory = sqlite3.Row                              # instead of having tuples we get dictionnary (easier to use)
        cur = conn.cursor()                                         # cursor is the object allowing us to interact with the database
        cur.execute("SELECT * FROM movies;")                        # execute what's contained by the cursor
    return cur.fetchall()                                           # fetchall in order to get the output of the previous SQL command

### insert a new movie into the database (insert a new line) ###
def set_db_data(input_movie, input_rating):
    db = getattr(g,'_database', None)
    if db is None:
        conn = sqlite3.connect('movies.db')
        cur = conn.cursor()
    cur.execute("INSERT INTO movies (movie_title,rating) VALUES(?,?)",(input_movie,input_rating))
    conn.commit()

### delete all the row of the database table ###
def clean_db_data():
    db = getattr(g,'_database', None)
    if db is None:
        conn = sqlite3.connect('movies.db')
        cur = conn.cursor()
    cur.execute("DELETE FROM movies;")
    conn.commit()

### remove a movie from the database (remove a row of the database) ###
def remove_movie():
    id = request.args.get("id")
    db = getattr(g,'_database', None)
    if db is None:
        conn = sqlite3.connect('movies.db')
        cur = conn.cursor()
    cur.execute("DELETE FROM movies WHERE id = ?", id)
    conn.commit()



### VIEWS ###

### general view ###
@app.route("/", methods = ["GET"])
def index():
    if  request.args.get("movie_name"):                              # only if the user filled the dorm
        movie_name = request.args.get("movie_name")
        movie_rating = request.args.get("movie_rating")              # access the cursor in order to interact with the database
        set_db_data(movie_name,movie_rating)
    data = get_db_data()
    return render_template("index.html",films = data)

### deletion of the databas table ###
@app.route("/clean",methods = ["GET"])
def clean():
    clean_db_data()
    return redirect("/")

### removing of one movie of the list ###
@app.route("/delete_movie", methods=["GET"])
def delete():
    remove_movie()
    return redirect("/")

### interrup handler executed after each http request ###
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,'_database', None)
    if db is not None:
        db.close()


### DOCUMENTATION 📚📚📚 ###
"""
to access the request argument with GET method => request.args.get("argument_name")
to access the request argument with POST method => request.form.get("argument_name")
"""




