/*creattion de la base de données*/
CREATE TABLE movies(
id INTEGER PRIMARY KEY,
movie_title TEXT NOT NULL,
rating REAL);

/* on remplit la base de données avec un élément*/
INSERT INTO movies (movie_title,rating) VALUES("mulan",4.0);