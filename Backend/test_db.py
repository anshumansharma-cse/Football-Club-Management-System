from db import get_players

players = get_players()

for p in players:
    print(p)