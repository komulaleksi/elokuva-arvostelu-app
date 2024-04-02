CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT
);

CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    name TEXT,
    year TEXT
);