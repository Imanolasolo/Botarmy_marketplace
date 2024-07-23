import streamlit as st
from auth import authenticate

def login_page():
    st.title("Login")

    username = st.text_input("Username", key="login_username")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_button"):
        user = authenticate(username, password)
        if user:
            st.session_state['user'] = user
            st.success(f"Logged in as {username}")
        else:
            st.error("Invalid username or password")

