CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    name TEXT,
    year TEXT
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
    user_id INTEGER REFERENCES users(id),
    username TEXT REFERENCES users(username),
    score INTEGER,
    comment TEXT
);

CREATE TABLE images (
    id SERIAL PRIMARY KEY,
    movie_id INTEGER REFERENCES movies(id) ON DELETE CASCADE,
    data BYTEA
);

CREATE TABLE user_info (
    user_id INTEGER REFERENCES users(id),
    fav_movie TEXT,
);