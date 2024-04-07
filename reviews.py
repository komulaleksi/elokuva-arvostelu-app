from db import db
from flask import session
from sqlalchemy import text

def get_reviews(movie_id):
    sql = text("SELECT user_id, username, score, comment FROM reviews WHERE movie_id=:movie_id")
    reviews = db.session.execute(sql, {"movie_id":movie_id}).fetchall()
    return reviews

def add_review(movie_id, user_id, username, score, comment):
    sql = text("""INSERT INTO reviews (movie_id, user_id, username, score, comment) 
                                VALUES (:movie_id, :user_id, :username, :score, :comment)""")
    db.session.execute(sql, {"movie_id":movie_id, "user_id":user_id, "username":username, "score":score, "comment":comment})
    db.session.commit()

def update_review(movie_id, user_id, score, comment):
    sql = text("UPDATE reviews SET score=:score, comment=:comment WHERE movie_id=:movie_id AND user_id=:user_id")
    db.session.execute(sql, {"movie_id":movie_id, "user_id":user_id, "score":score, "comment":comment})
    db.session.commit()

def get_average_score(movie_id):
    sql = text("SELECT AVG(score) FROM reviews WHERE movie_id=:movie_id")
    average_score = db.session.execute(sql, {"movie_id":movie_id}).fetchone()[0]
    return round(average_score, 2)

def has_review(user_id, movie_id):
    sql = text("SELECT id FROM reviews WHERE user_id=:user_id AND movie_id=:movie_id")
    review = db.session.execute(sql, {"user_id":user_id, "movie_id":movie_id}).fetchone()

    return review