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
    sql = text("SELECT name, genre, year FROM movies WHERE id=:movie_id")
    movie = db.session.execute(sql, {"movie_id":movie_id}).fetchall()[0]
    return movie

# Add movie to database
def add_movie(movie_name, genre, release_year):
    sql = text("INSERT INTO movies (name, genre, year) VALUES (:movie_name, :genre, :release_year) RETURNING id")
    movie_id = db.session.execute(sql, {"movie_name":movie_name, "genre":genre, "release_year":release_year}).fetchone()[0]
    db.session.commit()
    return movie_id

def add_movie_image(movie_id, data):
    sql = text("INSERT INTO images (movie_id, data) VALUES (:movie_id, :data)")
    db.session.execute(sql, {"movie_id":movie_id, "data":data})
    db.session.commit()

def get_movie_image(movie_id):
    sql = text("SELECT data FROM images WHERE movie_id=:movie_id")
    movie_image = db.session.execute(sql, {"movie_id":movie_id}).fetchone()[0]
    return movie_image

# Get movies that include keyword/query
def get_movies_like(query):
    sql = text("SELECT id, name, year FROM movies WHERE name LIKE :query")
    movies_like = db.session.execute(sql, {"query":"%"+query+"%"}).fetchall()
    return movies_like

def delete_movie(id):
    sql = text("DELETE FROM movies WHERE id=:id")
    db.session.execute(sql, {"id":id})
    db.session.commit()