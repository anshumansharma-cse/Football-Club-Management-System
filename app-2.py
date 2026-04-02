# ============================================================
#  Football Club Management System — Streamlit Frontend
# ============================================================

import streamlit as st
import pandas as pd
from db import (
    get_players, add_player, search_players,
    get_clubs, get_clubs_full, add_club,
    get_league_table,
    get_transfer_market, add_transfer_listing
)

st.set_page_config(
    page_title="Football Club Management",
    page_icon="⚽",
    layout="wide"
)

st.markdown("""
<style>
    .stApp { background-color: #0d1f0d; color: #e8f5e9; }
    h1, h2, h3 { color: #66bb6a !important; font-family: 'Georgia', serif; }
    .stDataFrame, .stTable { background: #1a2e1a !important; }
    .stButton > button {
        background-color: #2e7d32; color: white;
        border: none; border-radius: 8px; font-weight: bold;
    }
    .stButton > button:hover { background-color: #43a047; }
    section[data-testid="stSidebar"] { background-color: #0a1a0a; }
    .stTabs [data-baseweb="tab"] {
        background-color: #1a2e1a; color: #a5d6a7;
        border-radius: 6px 6px 0 0;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2e7d32 !important; color: white !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("⚽ Football Club Management System")
st.caption("DBMS Project — Powered by MySQL + Python + Streamlit")
st.divider()

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏃 Players", "🏟️ Clubs", "📊 League Table",
    "💸 Transfer Market", "➕ Add Data"
])

# ── TAB 1 — Players ─────────────────────────────────────────
with tab1:
    st.subheader("All Players")
    search_query = st.text_input("🔍 Search player by name", placeholder="e.g. Chhetri")

    try:
        players = search_players(search_query) if search_query else get_players()
        if players:
            df = pd.DataFrame(players, columns=["Name", "Position", "Age", "Club"])
            st.dataframe(df, use_container_width=True, hide_index=True)
            st.caption(f"Total: {len(players)} player(s)")
        else:
            st.info("No players found.")
    except Exception as e:
        st.error(f"Error: {e}")

# ── TAB 2 — Clubs ────────────────────────────────────────────
with tab2:
    st.subheader("All Clubs")
    try:
        clubs = get_clubs_full()
        if clubs:
            df_clubs = pd.DataFrame(
                clubs,
                columns=["Club", "City", "League Titles", "Stadium Capacity", "Head Coach"]
            )
            st.dataframe(df_clubs, use_container_width=True, hide_index=True)
        else:
            st.info("No clubs found.")
    except Exception as e:
        st.error(f"Error: {e}")

# ── TAB 3 — League Table ─────────────────────────────────────
with tab3:
    st.subheader("📋 League Standings")
    try:
        table = get_league_table()
        if table:
            df_lt = pd.DataFrame(
                table,
                columns=["Team", "MP", "W", "D", "L", "GF", "GA", "GD", "Pts"]
            )
            df_lt.insert(0, "Rank", range(1, len(df_lt) + 1))
            st.dataframe(df_lt, use_container_width=True, hide_index=True)
        else:
            st.info("League table is empty.")
    except Exception as e:
        st.error(f"Error: {e}")

# ── TAB 4 — Transfer Market ──────────────────────────────────
with tab4:
    st.subheader("💸 Players Available for Transfer")
    try:
        listings = get_transfer_market()
        if listings:
            df_tm = pd.DataFrame(
                listings,
                columns=["Player", "Age", "Speciality", "Transfer Value (€)", "Club ID"]
            )
            df_tm["Transfer Value (€)"] = df_tm["Transfer Value (€)"].apply(lambda x: f"€{int(x):,}")
            st.dataframe(df_tm, use_container_width=True, hide_index=True)
        else:
            st.info("No players listed on the transfer market.")
    except Exception as e:
        st.error(f"Error: {e}")

# ── TAB 5 — Add Data ─────────────────────────────────────────
with tab5:
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("➕ Add Player")
        with st.form("add_player_form"):
            p_name     = st.text_input("Player Name")
            p_position = st.selectbox("Position", [
                "Goalkeeper", "Defender", "Midfielder",
                "Winger", "Forward", "Striker"
            ])
            p_age      = st.number_input("Age", min_value=15, max_value=45, value=22)
            try:
                clubs_list  = get_clubs()
                club_dict   = {name: cid for cid, name in clubs_list}
                club_choice = st.selectbox("Club", list(club_dict.keys()))
            except:
                club_dict = {}
                st.warning("Could not load clubs.")

            if st.form_submit_button("Add Player"):
                if p_name.strip() and club_dict:
                    try:
                        add_player(p_name, p_position, p_age, club_dict[club_choice])
                        st.success(f"✅ {p_name} added to {club_choice}!")
                    except Exception as e:
                        st.error(f"Error: {e}")
                else:
                    st.error("Player name cannot be empty.")

    with col_right:
        st.subheader("🏟️ Add Club")
        with st.form("add_club_form"):
            c_name     = st.text_input("Club Name")
            c_city     = st.text_input("City")
            c_titles   = st.number_input("League Titles", min_value=0, value=0)
            c_capacity = st.number_input("Stadium Capacity", min_value=0, value=20000)
            c_coach    = st.text_input("Head Coach")

            if st.form_submit_button("Add Club"):
                if c_name.strip():
                    try:
                        add_club(c_name, c_city, c_titles, c_capacity, c_coach)
                        st.success(f"✅ {c_name} added!")
                    except Exception as e:
                        st.error(f"Error: {e}")
                else:
                    st.error("Club name cannot be empty.")

    st.divider()

    st.subheader("💸 List Player on Transfer Market")
    with st.form("add_transfer_form"):
        t_cols = st.columns(3)
        with t_cols[0]:
            t_player_id  = st.number_input("Player ID", min_value=1, value=1)
            t_name       = st.text_input("Player Name ")
        with t_cols[1]:
            t_age_t      = st.number_input("Age ", min_value=15, max_value=45, value=22)
            t_speciality = st.text_input("Speciality / Skills")
        with t_cols[2]:
            t_value      = st.number_input("Transfer Value (€)", min_value=0, value=1000000, step=500000)
            try:
                clubs_list2 = get_clubs()
                club_dict2  = {name: cid for cid, name in clubs_list2}
                t_club      = st.selectbox("Current Club ", list(club_dict2.keys()))
            except:
                club_dict2 = {}
                st.warning("Could not load clubs.")

        if st.form_submit_button("List on Transfer Market"):
            if t_name.strip() and club_dict2:
                try:
                    add_transfer_listing(
                        t_player_id, club_dict2[t_club],
                        t_name, t_age_t, t_speciality, t_value
                    )
                    st.success(f"✅ {t_name} listed for €{t_value:,}!")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.error("Player name cannot be empty.")