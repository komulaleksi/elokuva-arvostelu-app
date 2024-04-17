from db import db
from flask import session
from sqlalchemy import text

# Return list of movies
def get_movies():
    sql = text("SELECT id, name, year FROM movies")
    movies = db.session.execute(sql).fetchall()
    return movies

# Return movie name and release year by id
def get_movie(movie_id):
    sql = text("SELECT name, year FROM movies WHERE id=:movie_id")
    movie = db.session.execute(sql, {"movie_id":movie_id}).fetchall()[0]
    return movie

# Add movie to database
def add_movie(movie_name, release_year):
    sql = text("INSERT INTO movies (name, year) VALUES (:movie_name, :release_year) RETURNING id")
    movie_id = db.session.execute(sql, {"movie_name":movie_name, "release_year":release_year}).fetchone()[0]
    db.session.commit()
    return movie_id

def add_movie_image(movie_id, data):
    sql = text("INSERT INTO images (movie_id, data) VALUES (:movie_id, :data)")
    db.session.execute(sql, {"movie_id":movie_id, "data":data})
    db.session.commit()