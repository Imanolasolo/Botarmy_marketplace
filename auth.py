import hashlib
import sqlite3
import streamlit as st

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hash_password(password)))
    user = c.fetchone()
    conn.close()
    return user

def get_user_role():
    if 'user' in st.session_state:
        return st.session_state['user'][3]  # El rol está en la columna 3
    return None
