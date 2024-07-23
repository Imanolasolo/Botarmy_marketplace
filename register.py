import streamlit as st
import sqlite3
from auth import hash_password

def register_user(username, email, password, role):
    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()
    hashed_password = hash_password(password)
    try:
        c.execute('INSERT INTO users (username, email, password, role) VALUES (?, ?, ?, ?)', 
                  (username, email, hashed_password, role))
        conn.commit()
        st.success("User registered successfully")
    except sqlite3.IntegrityError:
        st.error("Username or email already exists")
    conn.close()

def register_page():
    st.title("Register")

    reg_username = st.text_input("Username", key="reg_username")
    reg_email = st.text_input("Email", key="reg_email")
    reg_password = st.text_input("Password", type="password", key="reg_password")
    reg_role = st.selectbox("Role", ["publisher", "customer"], key="reg_role")

    if st.button("Register", key="register_button"):
        register_user(reg_username, reg_email, reg_password, reg_role)

