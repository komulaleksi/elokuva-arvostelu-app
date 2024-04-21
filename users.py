from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text

def login(username, password):
    sql = text("SELECT id, password FROM users WHERE username=:username")
    user = db.session.execute(sql, {"username":username}).fetchone()

    # Check if user exists
    if not user:
        print(f"User {username} not found")
    else:
        password_hash = user[1] # Hashed password from database
        if check_password_hash(password_hash, password):
            session["user_id"] = user[0]
            session["username"] = username
            print(f"Logged in as {username}")
            return True
        else:
            print("Incorrect password")
            return False
            

def register(username, password):
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

def logout():
    try:
        del session["user_id"]
        del session["username"]
        return True
    except:
        print("Not logged in")
        return False


def get_username(user_id):
    sql = text("SELECT username FROM users WHERE id=:user_id")
    username = db.session.execute(sql, {"user_id":user_id}).fetchone()[0]
    return username

def is_admin(user_id):
    if user_id != 1:
        return False
    return user_id