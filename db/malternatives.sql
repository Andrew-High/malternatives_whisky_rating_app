DROP TABLE IF EXISTS wishlists;
DROP TABLE IF EXISTS reviews;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS whiskies;
DROP TABLE IF EXISTS distilleries;

CREATE TABLE distilleries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    region VARCHAR (255),
    founded INT
);

CREATE TABLE whiskies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    flavour_profile TEXT,
    distillery_id INT REFERENCES distilleries(id)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255)
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    rating INT,
    description TEXT,
    date VARCHAR (255),
    whisky_id SERIAL REFERENCES whiskies(id),
    user_id SERIAL REFERENCES users(id)
);

CREATE TABLE wishlists (
    id SERIAL PRIMARY KEY,
    user_id SERIAL REFERENCES users(id),
    whisky_id SERIAL REFERENCES whiskies(id)
);