import streamlit as st
import pandas as pd
import json
from pathlib import Path


# ---------- Sidebar ---------- #
with st.sidebar.expander("Contacts"):
    st.markdown("""
- 📧 [Gmail](mailto:fiqi.mochamad@email.com)
- 💼 [LinkedIn](https://linkedin.com/in/mochamadfiqi/)
""")


# ---------- Page ---------- #
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
)

data_analyst = st.Page(
    page="views/Data_Analyst_Project.py",
    title="Data Analyst Project",
    icon=":material/bar_chart:",
)


# ---------- Navigation Setup ---------- #
pg = st.navigation(pages=[about_page, data_analyst])

# ---------- Run Navigation ---------- #
pg.run()



