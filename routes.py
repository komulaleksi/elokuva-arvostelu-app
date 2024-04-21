from app import app
import users, movies, reviews, base64
from flask import render_template, request, redirect, session

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
        review_list = reviews.get_reviews(movie_id)
        average_score = reviews.get_average_score(movie_id)
        data = bytes(movies.get_movie_image(movie_id))
        movie_image = base64.b64encode(data).decode('utf-8')    # Decode image
        if not average_score:
            average_score = "?"
        return render_template("movie.html", movie_id=movie_id, movie=movie, reviews=review_list, average_score=average_score, movie_image=movie_image)
    except:
        return redirect("/movies")
    
@app.route("/movies/<movie_id>/review")
def movie_review(movie_id):
    if session.get("user_id") is not None:  # Check if user is logged in
        try:    # Check that movie exists
            movie = movies.get_movie(movie_id)
            return render_template("review.html", movie=movie, movie_id=movie_id)
        except:
            return redirect("/movies")
    else:
        return redirect("/movies")

@app.route("/movies/add-review", methods=["POST"])
def add_review():
        movie_id = request.form["movie_id"]
        user_id = session["user_id"]
        username = session["username"]
        score = request.form["score"]
        comment = request.form["comment"]
        has_review = reviews.has_review(session["user_id"], movie_id)
        if has_review:  # Update review if review exists
            reviews.update_review(movie_id, user_id, score, comment)
        else:   # Create review if review doesn't exist
            reviews.add_review(movie_id, user_id, username, score, comment)
        return redirect("/movies/<movie_id>")

@app.route("/movies/add", methods=["GET", "POST"])
def add_movie():
    if users.is_admin(session["user_id"]):  # Check that user is admin
        if request.method == "GET":
            return render_template("add-movie.html")
        elif request.method == "POST":
            movie_name = request.form["movie_name"]
            release_year = request.form["release_year"]

            movie_image = request.files["movie_image"]
            if not movie_image:
                return redirect("/movies")
            image_name = movie_image.filename
            filetypes = (".jpg", ".jpeg")
            if not image_name.endswith(filetypes): # Check that file is jpeg
                print("Wrong filetype")
                return error("Väärä tiedostotyyppi. Vain jpeg tiedostot hyväksytään")
            data = movie_image.read()
            if len(data) > 100*1024:    # Check that file is not larger than 100KB
                print("Too big picture")
                return error("Liian suuri kuva. Max. koko 100kb")
            movie_id = movies.add_movie(movie_name, release_year)
            movies.add_movie_image(movie_id, data)
            return redirect("/movies")
    else:
        return redirect("/movies")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not users.login(username, password): # If password is incorrect
            return error("Väärä käyttäjätunnus tai salasana")
        return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        password2 = request.form["password2"]
        if password == password2:   # Check that passwords match
            try:
                users.register(username, password)
            except:
                return error("Käyttätunnus on jo käytössä")
        else:
            print("Passwords don't match")
            return error("Salasanat eivät täsmää")
        return redirect("/")

@app.route("/logout")
def logout():
    if not users.logout():  # If user is not logged in
        return error("Et ole kirjautunut sisään")
    return redirect("/")

@app.route("/movies/search")
def search():
    return render_template("search.html")

@app.route("/movies/search/result")
def search_result():
    query = request.args["query"]
    results = movies.get_movies_like(query)
    return render_template("movies.html", movies=results)

@app.route("/error")
def error(error_message):
    return render_template("error.html", error_message=error_message)