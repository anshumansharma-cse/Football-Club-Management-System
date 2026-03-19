# Backend for DBMS Project
import mysql.connector

# DB Connection

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="MySQL@DB1",
    database="football_db"
)

cursor=db.cursor()

# FETCH PLAYERS

def get_players():
    query= """
    SELECT  players.player_name,
            players.position,
            players.age,
            clubs.club_name
    FROM players
    JOIN clubs ON players.club_id=clubs.club_id
    """
    cursor.execute(query)
    return cursor.fetchall()

# ADD PLAYER

def add_player(name, position, age, club_id):
    query="""
    INSERT INTO players(player_name, position, age, club_id)
    VALUES (%s,%s,%s,%s)
    """
    cursor.execute(query,(name, position, age, club_id))
    db.commit()

#In mysql.connector, %s is the universal placeholder & parameteric queries prevent SQL Injections


# FETCH CLUBS

def get_clubs():
    cursor.execute("SELECT club_id, club_name FROM clubs")
    return cursor.fetchall()


