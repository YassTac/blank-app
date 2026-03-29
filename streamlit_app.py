import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import altair as alt

with st.sidebar :
    selected = option_menu(
    menu_title = "Tableau de bord", 
    options = ["Home", "Données Financières", "Données Cliniques", "Contactez nous"],
    default_index = 0
)

if selected == "Home":
    st.header("Dashboard")
    


if selected == "Données financières":
    st.header("")

if selected == "Données cliniques" :
    st.header("")

if selected == "Contactez nous" :
    st.header("")
    

st.title("Dashboard")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

