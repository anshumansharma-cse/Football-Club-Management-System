# LEARNING WORK In Progress

import streamlit as st
from Backend.db import get_players, add_player, get_clubs

st.title("Football Club Management System [DBMS PROJECT]")

st.header("Players")
players=get_players()
for p in players:
    st.write(p)

st.header("ADD Player")

name=st.text_input("Player Name:")
position=st.text_input("Position:")
age=st.number_input("Age")

clubs=get_clubs()
club_dict={c[1]: c[0] for c in clubs}
club_name = st.selectbox("Club", club_dict.keys())

if st.button("ADD Player"):
    add_player(name, position, age, club_dict[club_name])
    st.success("Player Added")

