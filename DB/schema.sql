DROP DATABASE IF EXISTS football_db;
CREATE DATABASE football_db;
USE football_db;

CREATE TABLE clubs(
club_id INT AUTO_INCREMENT PRIMARY KEY,
club_name VARCHAR(100) NOT NULL,
city VARCHAR(100),
league_titles INT
);

CREATE TABLE players(
player_id INT AUTO_INCREMENT PRIMARY KEY,
player_name VARCHAR(100) NOT NULL,
position VARCHAR(50),
age INT,
club_id INT,

FOREIGN KEY (club_id) REFERENCES clubs(club_id)
);

INSERT INTO clubs (club_name, city, league_titles) VALUES
('Manchester City','Manchester',5),
('Liverpool','Liverpool',1);

INSERT INTO players(player_name,position,age,club_id) VALUES
('Kevin De Bruyne','Midfielder',33,1),
('Mohamed Salah','Forward',32,2);
