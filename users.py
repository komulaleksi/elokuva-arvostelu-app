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
        else:
            print("Incorrect password")

def register(username, password):
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

def logout():
    del session["user_id"]
    del session["username"]