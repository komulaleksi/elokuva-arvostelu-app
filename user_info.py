from db import db
from flask import session
from sqlalchemy import text

def create_profile(user_id, username, fav_movie, fav_genre):
    sql = text("INSERT INTO user_info (user_id, username, fav_movie, fav_genre) VALUES (:user_id, :username, :fav_movie, :fav_genre)")
    db.session.execute(sql, {"user_id":user_id, "username":username, "fav_movie":fav_movie, "fav_genre":fav_genre})
    db.session.commit()

def edit_profile(user_id, fav_movie, fav_genre):
    sql = text("UPDATE user_info SET fav_movie=:fav_movie, fav_genre=:fav_genre WHERE user_id=:user_id")
    db.session.execute(sql, {"user_id":user_id, "fav_movie":fav_movie, "fav_genre":fav_genre})
    db.session.commit()

def get_profiles(user_id):
    sql = text("SELECT user_id, username, fav_movie, fav_genre FROM user_info WHERE user_id=:user_id")
    profiles = db.session.execute(sql, {"user_id":user_id}).fetchall()[0]
    return profiles

def add_fav_movie(fav_movie):
    return