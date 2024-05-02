from db import db
from flask import session
from sqlalchemy import text

def create_profile(user_id, username, fav_movie, fav_genre):
    sql = text("INSERT INTO user_info (user_id, username, fav_movie, fav_genre) VALUES (:user_id, :username, :fav_movie, :fav_genre)")
    db.session.execute(sql, {"user_id":user_id, "username":username, "fav_movie":fav_movie, "fav_genre":fav_genre})
    db.session.commit()

def add_fav_movie(fav_movie):
    return