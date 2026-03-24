# ============================================================
#  Football Club Management System — Database Layer (db.py)
# ============================================================

import mysql.connector
from mysql.connector import Error

# ------------------------------------------------------------
#  Connection
# ------------------------------------------------------------

def get_connection():
    """Return a fresh DB connection. Raises Error on failure."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="MySQL@DB1",
        database="football_db"
    )

# Use a single persistent connection for the session.
# Wrapped so import failures are descriptive.
try:
    db = get_connection()
    cursor = db.cursor()
except Error as e:
    raise RuntimeError(f"Could not connect to MySQL: {e}")


def _ensure_connection():
    """Reconnect if the connection was dropped."""
    global db, cursor
    if not db.is_connected():
        db = get_connection()
        cursor = db.cursor()


# ============================================================
#  CLUBS
# ============================================================

def get_clubs():
    """Return (club_id, club_name) for all clubs."""
    _ensure_connection()
    cursor.execute("SELECT club_id, club_name FROM clubs ORDER BY club_name")
    return cursor.fetchall()


def get_clubs_full():
    """Return full club details for display."""
    _ensure_connection()
    cursor.execute("""
        SELECT club_name, city, league_titles,
               stadium_capacity, head_coach
        FROM clubs
        ORDER BY club_name
    """)
    return cursor.fetchall()


def add_club(club_name, city, league_titles, stadium_capacity, head_coach):
    _ensure_connection()
    query = """
        INSERT INTO clubs (club_name, city, league_titles, stadium_capacity, head_coach)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (club_name, city, league_titles, stadium_capacity, head_coach))
    db.commit()


# ============================================================
#  PLAYERS
# ============================================================

def get_players():
    """Return all players with their club name."""
    _ensure_connection()
    query = """
        SELECT  p.player_name,
                p.position,
                p.age,
                p.nationality,
                c.club_name
        FROM players p
        JOIN clubs c ON p.club_id = c.club_id
        ORDER BY p.player_name
    """
    cursor.execute(query)
    return cursor.fetchall()


def add_player(name, position, age, nationality, club_id):
    """
    Insert a new player.
    Uses %s placeholders — mysql.connector's universal parameterised form.
    This prevents SQL injection.
    """
    _ensure_connection()
    query = """
        INSERT INTO players (player_name, position, age, nationality, club_id)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, position, age, nationality, club_id))
    db.commit()


def delete_player(player_id):
    _ensure_connection()
    cursor.execute("DELETE FROM players WHERE player_id = %s", (player_id,))
    db.commit()


def search_players(keyword):
    """Search players by name (case-insensitive partial match)."""
    _ensure_connection()
    query = """
        SELECT  p.player_name,
                p.position,
                p.age,
                p.nationality,
                c.club_name
        FROM players p
        JOIN clubs c ON p.club_id = c.club_id
        WHERE p.player_name LIKE %s
        ORDER BY p.player_name
    """
    cursor.execute(query, (f"%{keyword}%",))
    return cursor.fetchall()


# ============================================================
#  LEAGUE TABLE
# ============================================================

def get_league_table():
    """Return league standings sorted by points (desc), then GD."""
    _ensure_connection()
    cursor.execute("""
        SELECT team_name, matches_played, wins, draws, losses,
               goals_for, goals_against, goal_difference, points
        FROM league_table
        ORDER BY points DESC, goal_difference DESC
    """)
    return cursor.fetchall()


# ============================================================
#  TRANSFER MARKET
# ============================================================

def get_transfer_market():
    _ensure_connection()
    cursor.execute("""
        SELECT player_name, age, speciality,
               transfer_value, club_id
        FROM transfer_market
        ORDER BY transfer_value DESC
    """)
    return cursor.fetchall()


def add_transfer_listing(player_id, club_id, player_name, age, speciality, transfer_value):
    _ensure_connection()
    query = """
        INSERT INTO transfer_market
            (player_id, club_id, player_name, age, speciality, transfer_value)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (player_id, club_id, player_name, age, speciality, transfer_value))
    db.commit()
