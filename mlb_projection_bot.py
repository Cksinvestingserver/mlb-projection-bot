import streamlit as st
import pandas as pd

st.title("⚾ MLB The Show 25 Projection Bot")

st.write("Project player ratings based on real performance stats!")

# User inputs
player_name = st.text_input("Enter player name:", "Shohei Ohtani")

col1, col2, col3 = st.columns(3)

with col1:
    batting_avg = st.number_input("Batting Average", min_value=0.0, max_value=1.0, value=0.280, step=0.001)

with col2:
    home_runs = st.number_input("Home Runs", min_value=0, max_value=80, value=25, step=1)

with col3:
    era = st.number_input("ERA (if pitcher)", min_value=0.0, max_value=10.0, value=3.50, step=0.01)

# Simple projection formula
# Weighted mix of stats → scale to 0-99
hitter_score = (batting_avg * 300) + (home_runs * 1.5)
pitcher_score = max(0, (50 - era * 8))

overall_projection = int(min(99, max(60, (hitter_score + pitcher_score) / 2)))

# Output
st.subheader(f"Projected Overall for {player_name}:")
st.metric(label="Rating", value=overall_projection)
