import streamlit as st
from sqlalchemy import text
from db import engine

st.title("📝 Register")

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):

    with engine.connect() as conn:

        # Check if email already exists
        existing = conn.execute(
            text("SELECT * FROM users WHERE email=:email"),
            {"email": email}
        ).fetchone()

        if existing:
            st.error("Email already registered.")

        else:
            conn.execute(
                text("""
                INSERT INTO users(name,email,password)
                VALUES(:name,:email,:password)
                """),
                {
                    "name": name,
                    "email": email,
                    "password": password
                }
            )

            conn.commit()

            st.success("Registration Successful! Please Login.")