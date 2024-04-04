from db import db
from flask import session
from sqlalchemy import text

def get_reviews(movie_id):
    sql = text("SELECT user_id, score, comment FROM reviews WHERE movie_id=:movie_id")
    reviews = db.session.execute(sql, {"movie_id":movie_id}).fetchall()
    return reviews

def add_review(movie_id, user_id, score, comment):
    sql = text("""INSERT INTO reviews (movie_id, user_id, score, comment) 
                                VALUES (:movie_id, :user_id, :score, :comment)""")
    db.session.execute(sql, {"movie_id":movie_id, "user_id":user_id, "score":score, "comment":comment})
    db.session.commit()