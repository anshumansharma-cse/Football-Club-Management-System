DROP DATABASE IF EXISTS football_db;
CREATE DATABASE football_db;
USE football_db;

CREATE TABLE clubs (
    club_id           INT AUTO_INCREMENT PRIMARY KEY,
    club_name         VARCHAR(100) NOT NULL,
    city              VARCHAR(100),
    league_titles     INT DEFAULT 0,
    stadium_capacity  INT DEFAULT 0,
    head_coach        VARCHAR(100)
);

CREATE TABLE players (
    player_id    INT AUTO_INCREMENT PRIMARY KEY,
    player_name  VARCHAR(100) NOT NULL,
    position     VARCHAR(50),
    age          INT,
    club_id      INT DEFAULT NULL,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

CREATE TABLE league_table (
    entry_id        INT AUTO_INCREMENT PRIMARY KEY,
    team_name       VARCHAR(100) NOT NULL,
    matches_played  INT DEFAULT 0,
    wins            INT DEFAULT 0,
    draws           INT DEFAULT 0,
    losses          INT DEFAULT 0,
    goals_for       INT DEFAULT 0,
    goals_against   INT DEFAULT 0,
    goal_difference INT DEFAULT 0,
    points          INT DEFAULT 0
);

CREATE TABLE transfer_market (
    listing_id     INT AUTO_INCREMENT PRIMARY KEY,
    player_id      INT,
    club_id        INT DEFAULT NULL,
    player_name    VARCHAR(100) NOT NULL,
    age            INT,
    speciality     VARCHAR(200),
    transfer_value BIGINT DEFAULT 0,
    FOREIGN KEY (club_id) REFERENCES clubs(club_id)
        ON DELETE SET NULL ON UPDATE CASCADE
);

-- INSERT INTO clubs (club_name, city, league_titles, stadium_capacity, head_coach) VALUES
-- ('Mohun Bagan SG',  'Kolkata',   5, 60000, 'Jose Molina'),
-- ('East Bengal FC',  'Kolkata',   8, 60000, 'Carles Cuadrat'),
-- ('Mumbai City FC',  'Mumbai',    2,  8000, 'Petr Kratky'),
-- ('Bengaluru FC',    'Bengaluru', 3, 12000, 'Gerard Nus'),
-- ('Kerala Blasters', 'Kochi',     0, 50000, 'Mikael Stahre'),
-- ('Hyderabad FC',    'Hyderabad', 1, 15000, 'Thangboi Singto');

-- INSERT INTO players (player_name, position, age, club_id) VALUES
-- ('Sunil Chhetri',         'Forward',    39, 4),
-- ('Roy Krishna',           'Striker',    36, 1),
-- ('Brandon Fernandes',     'Midfielder', 30, 1),
-- ('Lallianzuala Chhangte', 'Winger',     27, 3),
-- ('Gurpreet Singh',        'Goalkeeper', 32, 4),
-- ('Sandesh Jhingan',       'Defender',   31, 5),
-- ('Bipin Singh',           'Winger',     29, 3),
-- ('Anirudh Thapa',         'Midfielder', 27, 4),
-- ('Manvir Singh',          'Forward',    27, 1),
-- ('Rahul Bheke',           'Defender',   33, 1);

-- INSERT INTO league_table
--     (team_name, matches_played, wins, draws, losses, goals_for, goals_against, goal_difference, points)
-- VALUES
-- ('Mohun Bagan SG',  20, 13, 4,  3, 38, 18,  20, 43),
-- ('Mumbai City FC',  20, 12, 3,  5, 35, 22,  13, 39),
-- ('Bengaluru FC',    20, 10, 5,  5, 30, 24,   6, 35),
-- ('Kerala Blasters', 20,  9, 4,  7, 28, 27,   1, 31),
-- ('East Bengal FC',  20,  7, 5,  8, 25, 30,  -5, 26),
-- ('Hyderabad FC',    20,  4, 3, 13, 18, 40, -22, 15);

-- INSERT INTO transfer_market (player_id, club_id, player_name, age, speciality, transfer_value) VALUES
-- (4, 3, 'Lallianzuala Chhangte', 27, 'Pace, Dribbling, Crossing',   8000000),
-- (6, 5, 'Sandesh Jhingan',       31, 'Aerial Duels, Leadership',    5000000),
-- (7, 3, 'Bipin Singh',           29, 'Pace, Left Wing, Set Pieces', 4500000),
-- (2, 1, 'Roy Krishna',           36, 'Finishing, Hold-up Play',     3000000);