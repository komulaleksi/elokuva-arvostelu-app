from app import app
import users, movies
from flask import render_template, request, redirect

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/movies")
def get_movies():
    movie_list = movies.get_movies()
    return render_template("movies.html", movies=movie_list)

@app.route("/movies/<movie_id>")
def movie_page(movie_id):
    try:
        movie = movies.get_movie(movie_id)
        return render_template("movie.html", movie=movie)
    except:
        return redirect("/movies")

@app.route("/movies/add", methods=["GET", "POST"])
def add_movie():
    if request.method == "GET":
        return render_template("add-movie.html")
    elif request.method == "POST":
        movie_name = request.form["movie_name"]
        release_year = request.form["release_year"]
        movies.add_movie(movie_name, release_year)
        return redirect("/movies")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users.login(username, password)
        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        users.register(username, password)
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")