/*nettoyage si une table du même nom avait déjà été créée*/
DROP TABLE IF EXISTS movies; 

/*creattion de la base de données*/
CREATE TABLE movies(
id INTEGER PRIMARY KEY,
movie_title TEXT NOT NULL,
author TEXT NOT NULL,
rating REAL);

/* on remplit la base de données avec un élément (test)*/
INSERT INTO movies (movie_title,author,rating) VALUES("mulan","user1",4.0);