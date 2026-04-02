# ============================================================
#  Football Club Management System — Database Layer (db.py)
# ============================================================

import mysql.connector
from mysql.connector import Error

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MySQL@DB1",
        database="football_db"
    )

try:
    db = get_connection()
    cursor = db.cursor()
except Error as e:
    raise RuntimeError(f"Could not connect to MySQL: {e}")

def _ensure_connection():
    global db, cursor
    if not db.is_connected():
        db = get_connection()
        cursor = db.cursor()

# ── CLUBS ────────────────────────────────────────────────────

def get_clubs():
    _ensure_connection()
    cursor.execute("SELECT club_id, club_name FROM clubs ORDER BY club_name")
    return cursor.fetchall()

def get_clubs_full():
    _ensure_connection()
    cursor.execute("""
        SELECT club_name, city, league_titles, stadium_capacity, head_coach
        FROM clubs ORDER BY club_name
    """)
    return cursor.fetchall()

def add_club(club_name, city, league_titles, stadium_capacity, head_coach):
    _ensure_connection()
    cursor.execute("""
        INSERT INTO clubs (club_name, city, league_titles, stadium_capacity, head_coach)
        VALUES (%s, %s, %s, %s, %s)
    """, (club_name, city, league_titles, stadium_capacity, head_coach))
    db.commit()

# ── PLAYERS ──────────────────────────────────────────────────

def get_players():
    _ensure_connection()
    cursor.execute("""
        SELECT p.player_name, p.position, p.age, c.club_name
        FROM players p
        JOIN clubs c ON p.club_id = c.club_id
        ORDER BY p.player_name
    """)
    return cursor.fetchall()

def search_players(keyword):
    _ensure_connection()
    cursor.execute("""
        SELECT p.player_name, p.position, p.age, c.club_name
        FROM players p
        JOIN clubs c ON p.club_id = c.club_id
        WHERE p.player_name LIKE %s
        ORDER BY p.player_name
    """, (f"%{keyword}%",))
    return cursor.fetchall()

def add_player(name, position, age, club_id):
    _ensure_connection()
    cursor.execute("""
        INSERT INTO players (player_name, position, age, club_id)
        VALUES (%s, %s, %s, %s)
    """, (name, position, age, club_id))
    db.commit()

def delete_player(player_id):
    _ensure_connection()
    cursor.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
    db.commit()

# ── LEAGUE TABLE ─────────────────────────────────────────────

def get_league_table():
    _ensure_connection()
    cursor.execute("""
        SELECT team_name, matches_played, wins, draws, losses,
               goals_for, goals_against, goal_difference, points
        FROM league_table
        ORDER BY points DESC, goal_difference DESC
    """)
    return cursor.fetchall()

# ── TRANSFER MARKET ──────────────────────────────────────────

def get_transfer_market():
    _ensure_connection()
    cursor.execute("""
        SELECT player_name, age, speciality, transfer_value, club_id
        FROM transfer_market ORDER BY transfer_value DESC
    """)
    return cursor.fetchall()

def add_transfer_listing(player_id, club_id, player_name, age, speciality, transfer_value):
    _ensure_connection()
    cursor.execute("""
        INSERT INTO transfer_market
            (player_id, club_id, player_name, age, speciality, transfer_value)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (player_id, club_id, player_name, age, speciality, transfer_value))
    db.commit()