import streamlit as st

# ---------- Selection ---------- #
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")

with col1:
    st.image("assets/Linkedin_Photo.png", width=230)

with col2:
    st.title("Mochamad Fiqi Sabila", anchor=False)
    st.write(
        "Data Science Enthusiast"
    )

st.title("Description")
st.write("""
        With over 5 years of experience in the creative industry, I’m currently working as a Video Editor and Motion Graphics Designer at iShinora Pte Ltd, Singapore.
        Now, driven by deep curiosity and a commitment to continuous learning, I’m transitioning into the field of Data Science. As a current student in the Data Science Bootcamp at Dibimbing.id,
        I’m developing skills in Python, data analysis, and machine learning, with a focus on solving real-world problems through data-driven insights.""")