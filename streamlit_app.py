import streamlit as st
import pandas as pd
import numpy as np

with st.sidebar :
    selected = option_menu(menu_title = "Tableau de bord", options = ["Home", "Données Financières", "Données Cliniques", "Contactez nous"], default_index = 0)

if selected == "Home":
    st.header("Dashboard")
    

st.title("Dashboard")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

