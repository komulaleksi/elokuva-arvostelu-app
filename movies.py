from db import db
from flask import session
from sqlalchemy import text

def get_movies():
    sql = text("SELECT name, year FROM movies")
    movies = db.session.execute(sql).fetchall()
    return movies

def add_movie(movie_name, release_year):
    sql = text("INSERT INTO movies (name, year) VALUES (:movie_name, :release_year)")
    db.session.execute(sql, {"movie_name":movie_name, "release_year":release_year})
    db.session.commit()