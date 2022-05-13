#app.py
import app1
import app2
import streamlit as st

st.set_page_config(layout="wide", page_icon="^_^", page_title="Potion Rarity and Ranking")
PAGES = {
    "Rank and Rarity": app1,
    "Find your potion match": app2
}
st.sidebar.title('Page Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()