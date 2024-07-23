import streamlit as st
from login import login_page
from register import register_page
from admin_dashboard import admin_dashboard_page
from publisher_dashboard import publisher_dashboard_page
from customer_dashboard import customer_dashboard_page
from auth import get_user_role
from db import init_db

st.set_page_config(page_title="Botarmy Marketplace", page_icon=":dollar:")
st.title("Welcome to Botarmy marketplace")
st.success("Your place to publish and sell apps or tutorials to build a successful AI based business")

st.sidebar.warning("You can login and register as publisher or customer")
# Inicializar la base de datos
init_db()

# Navegación principal
if 'page' not in st.session_state:
    st.session_state['page'] = 'login'

def navigate_to(page):
    st.session_state['page'] = page

# Menu de navegación
if 'user' in st.session_state:
    st.sidebar.write(f"Logged in as {st.session_state['user'][1]} ({get_user_role()})")
    st.sidebar.button("Logout", on_click=lambda: st.session_state.pop('user'))

    role = get_user_role()

    if role == 'administrator':
        navigate_to('admin_dashboard')
    elif role == 'publisher':
        navigate_to('publisher_dashboard')
    elif role == 'customer':
        navigate_to('customer_dashboard')

else:
    st.sidebar.button("Login", on_click=lambda: navigate_to('login'))
    st.sidebar.button("Register", on_click=lambda: navigate_to('register'))

# Mostrar la página seleccionada
if st.session_state['page'] == 'login':
    login_page()
elif st.session_state['page'] == 'register':
    register_page()
elif st.session_state['page'] == 'admin_dashboard':
    admin_dashboard_page()
elif st.session_state['page'] == 'publisher_dashboard':
    publisher_dashboard_page()
elif st.session_state['page'] == 'customer_dashboard':
    customer_dashboard_page()
