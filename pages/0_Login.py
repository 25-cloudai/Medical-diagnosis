import streamlit as st
from sqlalchemy import text
from db import engine

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    with engine.connect() as conn:

        user = conn.execute(
            text("""
            SELECT *
            FROM users
            WHERE email=:email
            AND password=:password
            """),
            {
                "email": email,
                "password": password
            }
        ).fetchone()

    if user:

        st.session_state.logged_in = True
        st.session_state.user = user.name
        st.session_state.user_email = user.email

        st.success("Login Successful!")
        st.switch_page("app.py")

    else:
        st.error("Invalid Email or Password")